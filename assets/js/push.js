// Capacitor push notification registration and deep-link handler.
// Loaded only when running inside the native app (Capacitor).

async function initPushNotifications() {
    if (!window.Capacitor?.isNativePlatform()) return;

    const { PushNotifications } = await import('@capacitor/push-notifications');

    // Request permission on first launch
    const status = await PushNotifications.requestPermissions();
    if (status.receive !== 'granted') return;

    await PushNotifications.register();

    // Send the device token to your backend / Firebase topic
    PushNotifications.addListener('registration', (token) => {
        console.log('[Push] Device token:', token.value);
        // TODO: POST token.value to your backend to subscribe to weekly parasha topic
        // fetch('/api/push/register', { method: 'POST', body: JSON.stringify({ token: token.value }) });
    });

    PushNotifications.addListener('registrationError', (err) => {
        console.error('[Push] Registration error:', err.error);
    });

    // Handle notification tap — navigate to the article
    PushNotifications.addListener('pushNotificationActionPerformed', (action) => {
        const slug = action.notification.data?.slug;
        if (slug) {
            window.location.href = `/parasha/${slug}.html`;
        }
    });

    // Show in-app notifications as a banner (foreground)
    PushNotifications.addListener('pushNotificationReceived', (notification) => {
        console.log('[Push] Received in foreground:', notification.title);
    });
}

initPushNotifications();
