#!/usr/bin/env python3
"""Generate article image for Acharei Mot-Kedoshim 2026 via Vertex AI Imagen 3."""

from google import genai
from google.genai import types

PROJECT = "arc-project-487920"
LOCATION = "us-central1"
OUTPUT_PNG = "/data/git/parasha_of_the_week/images/acharei_mot_kedoshim_2026_raw.png"

PROMPT = (
    "A richly detailed digital painting in Israeli illuminated-manuscript style. "
    "An ancient Jerusalem courtyard bathed in golden afternoon light, honey-colored stone walls "
    "and ornate arched doorways. In the center: a glowing golden balance scale — one pan holds "
    "a radiant, luminous heart (representing happiness of the soul), the other holds golden coins "
    "(wealth); the heart side floats higher, gently tipping the scale. "
    "Behind the scale, a majestic white doorway radiates soft white light — "
    "the entrance to the Holy of Holies, symbolizing inner purity. "
    "Around the courtyard, olive branches and pomegranates in bloom frame the scene. "
    "Mood: serene, sacred, hopeful. Warm amber, ivory and gold tones. Cinematic lighting. "
    "No text, no letters in the image."
)

def main():
    client = genai.Client(
        vertexai=True,
        project=PROJECT,
        location=LOCATION,
    )

    print(f"Generating image with Imagen 3 (project={PROJECT})...")
    response = client.models.generate_images(
        model="imagen-3.0-generate-001",
        prompt=PROMPT,
        config=types.GenerateImagesConfig(
            number_of_images=1,
            aspect_ratio="1:1",
            output_mime_type="image/png",
        ),
    )

    if not response.generated_images:
        print("ERROR: No images returned (safety filter may have blocked the prompt).")
        return

    img = response.generated_images[0].image
    with open(OUTPUT_PNG, "wb") as f:
        f.write(img.image_bytes)
    print(f"Saved: {OUTPUT_PNG}")

if __name__ == "__main__":
    main()
