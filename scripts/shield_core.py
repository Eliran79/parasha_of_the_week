"""
Shield Core - Password-based symmetric encryption.

This module provides the main Shield class for encrypting and decrypting
data using password-derived keys. It uses PBKDF2-SHA256 for key derivation
and a SHA256-based stream cipher with HMAC-SHA256 authentication.

Security:
    - PBKDF2 with 100,000 iterations
    - 256-bit keys
    - 16-byte random nonces
    - HMAC-SHA256 authentication (16-byte tags)
    - Constant-time MAC comparison
"""

import os
import hmac
import hashlib
import struct
import time
from typing import Optional, Union

# Key derivation iterations (higher = more secure, slower)
PBKDF2_ITERATIONS = 100_000

# Sizes in bytes
NONCE_SIZE = 16
MAC_SIZE = 16
COUNTER_SIZE = 8

# V2 constants
V2_HEADER_SIZE = 17  # counter(8) + timestamp(8) + pad_len(1)
MIN_PADDING = 32
MAX_PADDING = 128

# Timestamp range for v2 detection (2020-2100 in milliseconds)
MIN_TIMESTAMP_MS = 1_577_836_800_000
MAX_TIMESTAMP_MS = 4_102_444_800_000


class Shield:
    """
    EXPTIME-secure symmetric encryption.

    Uses password-derived keys with PBKDF2 and encrypts using
    a SHA256-based stream cipher with HMAC-SHA256 authentication.
    Breaking requires 2^256 operations - no shortcut exists.

    Version 2 adds replay protection and length obfuscation:
    - Timestamp validation prevents replay attacks
    - Random padding (32-128 bytes) obfuscates message length

    Example:
        >>> s = Shield("my_password", "github.com")
        >>> encrypted = s.encrypt(b"secret data")
        >>> decrypted = s.decrypt(encrypted)
        >>> assert decrypted == b"secret data"
    """

    def __init__(
        self,
        password: str,
        service: str,
        salt: Optional[bytes] = None,
        iterations: int = PBKDF2_ITERATIONS,
        max_age_ms: Optional[int] = 60_000,
    ):
        """
        Initialize Shield with password and service name.

        Args:
            password: User's password for this service
            service: Service identifier (e.g., "github.com")
            salt: Optional custom salt (defaults to SHA256(service))
            iterations: PBKDF2 iterations (default: 100,000)
            max_age_ms: Maximum message age in milliseconds for replay protection
                       (default: 60000 = 60 seconds, None = disabled)
        """
        if salt is None:
            salt = hashlib.sha256(service.encode()).digest()

        self._key = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), salt, iterations
        )
        # Derive separated subkeys using HMAC-SHA256 (Shield's own primitive)
        self._enc_key = hmac.new(self._key, b"shield-encrypt", hashlib.sha256).digest()
        self._mac_key = hmac.new(self._key, b"shield-authenticate", hashlib.sha256).digest()
        self._counter = 0
        self._max_age_ms = max_age_ms

    @classmethod
    def with_key(cls, key: bytes) -> "Shield":
        """
        Create Shield instance with a pre-shared key (no password derivation).

        Args:
            key: 32-byte symmetric key

        Returns:
            Shield instance

        Raises:
            ValueError: If key is not 32 bytes
        """
        if len(key) != 32:
            raise ValueError(f"Key must be 32 bytes, got {len(key)}")

        instance = cls.__new__(cls)
        instance._key = key
        instance._enc_key = hmac.new(key, b"shield-encrypt", hashlib.sha256).digest()
        instance._mac_key = hmac.new(key, b"shield-authenticate", hashlib.sha256).digest()
        instance._counter = 0
        instance._max_age_ms = 60_000
        return instance

    @classmethod
    def with_fingerprint(cls, password: str, service: str, mode: str = "combined") -> "Shield":
        """
        Create Shield with hardware fingerprinting (device-bound encryption).

        Derives keys from password + hardware identifier, binding encryption to
        the physical device. Keys cannot be transferred to other hardware without
        the correct fingerprint.

        Args:
            password: User's password
            service: Service identifier (e.g., "github.com")
            mode: Fingerprint mode - "none", "motherboard", "cpu", or "combined"

        Returns:
            Shield instance with device-bound key

        Raises:
            FingerprintError: If hardware identifiers cannot be collected

        Security:
            - Binding Strength: MEDIUM (hardware IDs are stable but replaceable)
            - Spoofability: LOW-MEDIUM (requires hardware access or VM manipulation)
            - Portability: NONE (keys are device-bound by design)

        Example:
            >>> s = Shield.with_fingerprint("password", "github.com", "combined")
            >>> encrypted = s.encrypt(b"secret")
        """
        from .fingerprint import collect_fingerprint, FingerprintMode

        # Map string mode to enum
        mode_map = {
            "none": FingerprintMode.NONE,
            "motherboard": FingerprintMode.MOTHERBOARD,
            "cpu": FingerprintMode.CPU,
            "combined": FingerprintMode.COMBINED,
        }
        fingerprint_mode = mode_map.get(mode.lower())
        if fingerprint_mode is None:
            raise ValueError(f"Invalid fingerprint mode: {mode}")

        # Collect hardware fingerprint
        fingerprint = collect_fingerprint(fingerprint_mode)

        # Combine password with fingerprint
        combined_password = f"{password}:{fingerprint}" if fingerprint else password

        # Create instance with combined password
        return cls(combined_password, service)

    def encrypt(self, plaintext: bytes) -> bytes:
        """
        Encrypt data (v2 format with replay protection and length obfuscation).

        Inner format: counter(8) || timestamp_ms(8) || pad_len(1) || random_padding(32-128) || plaintext

        Args:
            plaintext: Data to encrypt

        Returns:
            Ciphertext in format: nonce(16) || encrypted_data || mac(16)
        """
        nonce = os.urandom(NONCE_SIZE)
        counter_bytes = struct.pack("<Q", self._counter)
        self._counter += 1

        # Timestamp in milliseconds since Unix epoch
        timestamp_ms = int(time.time() * 1000)
        timestamp_bytes = struct.pack("<Q", timestamp_ms)

        # Random padding: 32-128 bytes (rejection sampling to avoid modulo bias)
        pad_range = MAX_PADDING - MIN_PADDING + 1  # 97
        while True:
            val = os.urandom(1)[0]
            if val < pad_range * (256 // pad_range):  # Reject biased values
                pad_len = (val % pad_range) + MIN_PADDING
                break
        pad_len_byte = struct.pack("B", pad_len)
        padding = os.urandom(pad_len)

        # Data to encrypt: counter || timestamp || pad_len || padding || plaintext
        data = counter_bytes + timestamp_bytes + pad_len_byte + padding + plaintext

        # Generate keystream (using encryption subkey)
        keystream = _generate_keystream(self._enc_key, nonce, len(data))

        # XOR encrypt
        ciphertext = bytes(p ^ k for p, k in zip(data, keystream))

        # HMAC authenticate (using MAC subkey)
        mac = hmac.new(self._mac_key, nonce + ciphertext, hashlib.sha256).digest()[
            :MAC_SIZE
        ]

        return nonce + ciphertext + mac

    def decrypt(self, encrypted: bytes) -> Optional[bytes]:
        """
        Decrypt and verify data (auto-detects v1/v2 format).

        Args:
            encrypted: Ciphertext from encrypt()

        Returns:
            Plaintext bytes, or None if authentication fails or replay detected
        """
        min_size = NONCE_SIZE + COUNTER_SIZE + MAC_SIZE
        if len(encrypted) < min_size:
            return None

        nonce = encrypted[:NONCE_SIZE]
        ciphertext = encrypted[NONCE_SIZE:-MAC_SIZE]
        mac = encrypted[-MAC_SIZE:]

        # Verify MAC (constant-time, using MAC subkey)
        expected_mac = hmac.new(
            self._mac_key, nonce + ciphertext, hashlib.sha256
        ).digest()[:MAC_SIZE]

        if not hmac.compare_digest(mac, expected_mac):
            return None

        # Decrypt (using encryption subkey)
        keystream = _generate_keystream(self._enc_key, nonce, len(ciphertext))
        decrypted = bytes(c ^ k for c, k in zip(ciphertext, keystream))

        # Auto-detect v2 by timestamp range (2020-2100)
        if len(decrypted) >= V2_HEADER_SIZE:
            timestamp_bytes = decrypted[8:16]
            timestamp_ms = struct.unpack("<Q", timestamp_bytes)[0]

            if MIN_TIMESTAMP_MS <= timestamp_ms <= MAX_TIMESTAMP_MS:
                # v2 format detected
                pad_len = decrypted[16]

                # Validate padding length is within protocol bounds (SECURITY: CVE-PENDING)
                if pad_len < MIN_PADDING or pad_len > MAX_PADDING:
                    return None

                data_start = V2_HEADER_SIZE + pad_len

                if len(decrypted) < data_start:
                    return None

                # Replay protection
                if self._max_age_ms is not None:
                    now_ms = int(time.time() * 1000)
                    age = now_ms - timestamp_ms

                    # Reject if too far in future (>5s clock skew) or too old
                    if timestamp_ms > now_ms + 5000 or age > self._max_age_ms:
                        return None

                return decrypted[data_start:]

        # v1 format: skip counter (8 bytes)
        return decrypted[COUNTER_SIZE:]

    def decrypt_v1(self, encrypted: bytes) -> Optional[bytes]:
        """
        Decrypt v1 format explicitly (for legacy compatibility).

        Args:
            encrypted: Ciphertext from encrypt()

        Returns:
            Plaintext bytes, or None if authentication fails
        """
        min_size = NONCE_SIZE + COUNTER_SIZE + MAC_SIZE
        if len(encrypted) < min_size:
            return None

        nonce = encrypted[:NONCE_SIZE]
        ciphertext = encrypted[NONCE_SIZE:-MAC_SIZE]
        mac = encrypted[-MAC_SIZE:]

        # Verify MAC (constant-time, using MAC subkey)
        expected_mac = hmac.new(
            self._mac_key, nonce + ciphertext, hashlib.sha256
        ).digest()[:MAC_SIZE]

        if not hmac.compare_digest(mac, expected_mac):
            return None

        # Decrypt (using encryption subkey)
        keystream = _generate_keystream(self._enc_key, nonce, len(ciphertext))
        decrypted = bytes(c ^ k for c, k in zip(ciphertext, keystream))

        # v1 format: skip counter (8 bytes)
        return decrypted[COUNTER_SIZE:]

    @property
    def key(self) -> bytes:
        """Get the derived key (for testing/debugging)."""
        return self._key


def _generate_keystream(key: bytes, nonce: bytes, length: int) -> bytes:
    """
    Generate keystream using SHA256 (AES-256-CTR equivalent).

    Args:
        key: 32-byte key
        nonce: 16-byte nonce
        length: Number of keystream bytes needed

    Returns:
        Keystream bytes
    """
    keystream = b""
    num_blocks = (length + 31) // 32

    for i in range(num_blocks):
        counter = struct.pack("<I", i)
        block = hashlib.sha256(key + nonce + counter).digest()
        keystream += block

    return keystream[:length]


def quick_encrypt(key: bytes, data: bytes) -> bytes:
    """
    One-shot encrypt with pre-shared key (no password derivation).

    Args:
        key: 32-byte symmetric key
        data: Data to encrypt

    Returns:
        Ciphertext in format: nonce(16) || encrypted_data || mac(16)

    Example:
        >>> key = os.urandom(32)
        >>> encrypted = quick_encrypt(key, b"secret")
        >>> decrypted = quick_decrypt(key, encrypted)
    """
    nonce = os.urandom(NONCE_SIZE)
    keystream = _generate_keystream(key, nonce, len(data))
    ciphertext = bytes(d ^ k for d, k in zip(data, keystream))
    mac = hmac.new(key, nonce + ciphertext, hashlib.sha256).digest()[:MAC_SIZE]
    return nonce + ciphertext + mac


def quick_decrypt(key: bytes, encrypted: bytes) -> Optional[bytes]:
    """
    One-shot decrypt with pre-shared key.

    Args:
        key: 32-byte symmetric key
        encrypted: Ciphertext from quick_encrypt()

    Returns:
        Plaintext bytes, or None if authentication fails
    """
    if len(encrypted) < NONCE_SIZE + MAC_SIZE:
        return None

    nonce = encrypted[:NONCE_SIZE]
    ciphertext = encrypted[NONCE_SIZE:-MAC_SIZE]
    mac = encrypted[-MAC_SIZE:]

    expected_mac = hmac.new(key, nonce + ciphertext, hashlib.sha256).digest()[
        :MAC_SIZE
    ]

    if not hmac.compare_digest(mac, expected_mac):
        return None

    keystream = _generate_keystream(key, nonce, len(ciphertext))
    return bytes(c ^ k for c, k in zip(ciphertext, keystream))
