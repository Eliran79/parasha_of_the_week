// Native mobile initialisation — runs only inside the Capacitor shell.
// Handles StatusBar styling and safe-area CSS variables.

async function initMobile() {
    if (!window.Capacitor?.isNativePlatform()) return;

    const { StatusBar, Style } = await import('@capacitor/status-bar');

    // Match the site's dark header (#0a1628)
    await StatusBar.setStyle({ style: Style.Dark });
    await StatusBar.setBackgroundColor({ color: '#0a1628' });

    // Expose safe-area insets as CSS custom properties so the stylesheet
    // can push content below the status bar and above the home indicator.
    // On Android the WebView already insets; on iOS we do it manually.
    if (window.Capacitor.getPlatform() === 'ios') {
        document.documentElement.classList.add('capacitor-ios');
    } else {
        document.documentElement.classList.add('capacitor-android');
    }
}

initMobile();
