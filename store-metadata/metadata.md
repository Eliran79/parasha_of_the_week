# App Store & Google Play Metadata

## App identity

| Field | Value |
|---|---|
| App name (Hebrew) | פרשת השבוע |
| App name (English) | Parasha of the Week |
| Bundle ID (iOS) | dev.gibraltarcloud.parasha |
| Package name (Android) | dev.gibraltarcloud.parasha |
| Category | Books / Education |
| Age rating | 4+ |
| Privacy Policy URL | https://blog.gibraltarcloud.dev/privacy.html |
| Support URL | https://blog.gibraltarcloud.dev |
| Marketing URL | https://blog.gibraltarcloud.dev |

---

## Short description (max 80 chars — both stores)

```
פרשת השבוע — מאמרים על התורה, מדע ובינה מלאכותית
```

English fallback:
```
Weekly Torah portion — articles connecting Torah, science & AI
```

---

## Full description (Google Play, up to 4000 chars)

```
פרשת השבוע היא אפליקציה עברית המחברת בין פרשות התורה לעולמות המדע, המתמטיקה והבינה המלאכותית.

✡ 62+ מאמרים על כל פרשות השנה
📐 נוסחאות מתמטיות ותובנות מדעיות לכל פרשה
🤖 זווית של בינה מלאכותית לרעיונות עתיקים
🔔 התראה שבועית בכל ערב שבת עם שם הפרשה
📵 גישה מלאה ללא חיבור לאינטרנט (מצב לא מקוון)
🔐 אינדקס מאמרים מוצפן בטכנולוגיית WasmShield

האפליקציה כתובה בעברית עם תמיכה מלאה בכיוון טקסט מימין לשמאל.
אין צורך בהרשמה. אין פרסומות. אין איסוף מידע אישי.

מאת: אלירן סבג | ARC.ceo
```

---

## iOS App Store description (up to 4000 chars)

Same as Google Play description above.

---

## Keywords

### iOS (max 100 chars total, comma-separated)
```
פרשה,תורה,שבת,מדע,מתמטיקה,בינה מלאכותית,יהדות,דת,קבלה,פרשת שבוע
```

### Google Play (tags)
פרשה, תורה, שבת, מדע, מתמטיקה, בינה מלאכותית, יהדות

---

## Screenshots required

### iOS (App Store Connect)
- **6.7" — iPhone 16 Pro Max** (1320×2868 px) — min 3, max 10
- **5.5" — iPhone 8 Plus** (1242×2208 px) — min 3, max 10
- **12.9" iPad Pro** (2048×2732 px) — optional but recommended

Suggested shots:
1. Home / article list — showing Hebrew RTL layout
2. Article page — showing LaTeX formula rendering
3. Dark mode article — showing night theme
4. Push notification banner — showing weekly parasha alert

### Google Play
- **Phone** (1080×1920 px minimum) — 2–8 screenshots
- **Feature graphic** (1024×500 px) — required
- Store icon (512×512 px) — `images/icon-512.png` ✓

---

## What's new (first release)

```
גרסה ראשונה של אפליקציית פרשת השבוע.
First release of Parasha of the Week.
```

---

## Checklist before submission

- [ ] Add `google-services.json` to `android/app/` (from Firebase Console)
- [ ] Add `GoogleService-Info.plist` to `ios/App/App/` (from Firebase Console)
- [ ] Set `aps-environment` in `App.entitlements` to `production` before release build
- [ ] Generate screenshots on a real device or Simulator
- [ ] Upload `images/icon-512.png` as the Play Store feature icon
- [ ] Set Privacy Policy URL in both stores: `https://blog.gibraltarcloud.dev/privacy.html`
- [ ] Run `npm run build:sync` for the final release build
- [ ] Archive in Xcode → upload to App Store Connect
- [ ] Build signed APK/AAB in Android Studio → upload to Play Console
