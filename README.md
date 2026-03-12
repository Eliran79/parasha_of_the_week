# פרשת השבוע — Parasha of the Week

🌐 **[blog.gibraltarcloud.dev](https://blog.gibraltarcloud.dev)**

An automated Hebrew website publishing weekly insights that connect Jewish Torah portions (Parashot) with mathematics, physics, data science, and AI. Each article analyzes ancient wisdom through a rigorous technical lens — from information theory in the Red Heifer ritual to Bell's theorem in Talmudic logic.

---

## What This Is

**53 Hebrew articles** and growing. One new article every Shabbat.

Each piece takes a Torah portion and finds the deep structural connection to a concept in modern science or technology — not metaphorically, but mathematically. The kind of analysis that makes you realize the Torah was encoding information-theoretic principles 3,300 years before Landauer.

**Language**: Hebrew (RTL) with LaTeX math, English technical sections, Python/code examples.

**Stack**: Markdown → Python build → GitHub Actions → GitHub Pages (custom domain).

---

## Repository Structure

```
parasha_of_the_week/
├── content/          # Source articles (.md with YAML frontmatter)
├── images/           # Article images (auto-matched by name + year)
├── assets/
│   ├── css/style.css # RTL Hebrew layout, LaTeX, mobile-responsive
│   └── js/main.js    # Search, PWA, WasmShield encryption
├── scripts/
│   └── build.py      # Full build system (HTML, feeds, sitemap, PWA)
├── .github/
│   └── workflows/    # Auto-deploy on push (~45 seconds)
└── docs/             # Generated site (gitignored, built by CI)
```

---

## Running Locally

```bash
git clone https://github.com/Eliran79/parasha_of_the_week.git
cd parasha_of_the_week
pip install -r requirements.txt
python scripts/build.py
cd docs && python -m http.server 8000
```

---

## Adding an Article

```bash
# 1. Create content file
vim content/parasha_[name]_[year].md

# 2. Add image (optional — auto-matched)
cp ~/image.jpg images/[name]_[year].jpg

# 3. Commit and push
git add .
git commit -m "פרשת [name]: [description]"
git push origin main
# Site rebuilds automatically in ~45 seconds
```

### Article Frontmatter

```yaml
---
title: "כותרת בעברית"
parasha: "שם הפרשה"
date: "2026-03-07"
tags: ["פיזיקה", "קוונטום", "ARC"]
emoji: "🔴"
excerpt: "תיאור קצר (עד 200 תווים)"
author: "אלירן סבג"
year: 2026
---
```

---

## Features

- **Hebrew RTL** — full right-to-left layout with proper bidi handling
- **LaTeX math** — MathJax 3, with RTL-aware rendering fixes
- **Syntax highlighting** — Prism.js for code blocks
- **PWA** — offline reading, installable
- **WasmShield** — articles index encrypted with Ring/WASM crypto
- **Feeds** — JSON Feed + RSS for syndication
- **SEO** — sitemap, Open Graph, structured metadata
- **Multi-year** — same parasha analyzed from different angles each year

---

## Author

**Eliran Sabag (אלירן סבג)**
[ARC.ceo](https://arc.ceo) · [LinkedIn](https://www.linkedin.com/in/eliran-sabag-51832651/)
