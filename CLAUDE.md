# CLAUDE.md - Parasha of the Week Project Guide

## 📚 Project Overview

**Parasha of the Week** is an automated Hebrew website that publishes weekly insights connecting Jewish Torah portions (Parashot) with mathematics, data science, AI, and startup concepts. The site features RTL Hebrew layout, LaTeX math support, and full automation via GitHub Actions.

## 🏗️ Architecture

### **Core Concept**
- **Input**: Markdown files + Images → **Output**: Complete Hebrew website
- **Automation**: Commit to GitHub → Auto-build → Live site in ~2 minutes
- **Content Focus**: Torah portions analyzed through technical/mathematical lens

### **Technology Stack**
- **Content**: Markdown with YAML frontmatter
- **Build**: Python with Markdown, PyYAML, Pillow
- **Styling**: Custom CSS with RTL Hebrew support
- **Features**: MathJax (LaTeX), Prism (syntax highlighting), PWA
- **Deployment**: GitHub Actions → GitHub Pages
- **Languages**: Hebrew (RTL primary), English (LTR secondary), LaTeX math

## 📁 Repository Structure

```
parasha-week/
├── content/                    # 📝 Source content (YOU CREATE)
│   ├── parasha_behar_2025.md
│   ├── parasha_bereshit_2024.md
│   ├── parashat_shalach_2025.md
│   └── ... (13 articles total)
├── images/                     # 🖼️ Article images (YOU CREATE)
│   ├── shalach_2025.jpg       # Matches parashat_shalach_2025.md
│   ├── korach_2025.jpg        # Example year-based naming
│   ├── README.md              # Image naming guide
│   └── [need: logo.png, default.jpg]
├── scripts/                    # ⚙️ Build system
│   └── build.py               # Complete build script (1000+ lines)
├── assets/                     # 🎨 Static assets
│   ├── css/style.css          # Complete RTL Hebrew styling
│   └── js/main.js             # Full interactive features
├── .github/workflows/          # 🤖 Automation
│   └── deploy.yml             # Production-ready GitHub Actions
├── tests/                      # 🧪 Testing (LOCAL ONLY)
│   └── test_build.py          # Build verification script
├── docs/                       # 🏗️ Generated website (AUTO-CREATED)
│   ├── index.html             # Generated homepage
│   ├── articles/              # Generated article pages (13+)
│   ├── images/                # Optimized images
│   ├── feed.json/feed.xml     # RSS feeds
│   ├── sitemap.xml            # SEO sitemap
│   ├── manifest.json          # PWA manifest
│   └── ... (15+ files total)
├── requirements.txt            # Python dependencies (verified)
├── .gitignore                 # Excludes venv/, docs/, etc.
└── README.md
```

## 📝 Content Format

### **Article Template**
```yaml
---
title: "כותרת המאמר בעברית"
parasha: "שם הפרשה"
date: "2025-01-15"
tags: ["מתמטיקה", "תכנות", "בינה_מלאכותית"]
emoji: "🔢"
excerpt: "תיאור קצר של המאמר (מקסימום 200 תווים)"
author: "שם המחבר"
year: 2025                     # For multi-year articles
---

# כותרת ראשית

תוכן המאמר בעברית עם תמיכה מלאה ב:

## עברית ו-RTL
זה טקסט עברי שיוצג נכון עם כיוון RTL.

## LaTeX ומתמטיקה
$$P(X|Y) = \frac{P(Y|X) \cdot P(X)}{P(Y)}$$

או בתוך הטקסט: $E = mc^2$

## קוד עם הדגשת תחביר
```python
def parasha_algorithm():
    return "אלגוריתם מהפרשה"
```

## אנגלית (LTR)
<div class="english">
This text will be displayed LTR with English fonts.
</div>

## ציטוטים
> "וְקִדַּשְׁתֶּ֗ם אֵ֣ת שְׁנַ֤ת הַֽחֲמִשִּׁים֙ שָׁנָ֔ה" (ויקרא כה:י)
```

### **Naming Convention (UPDATED)**
- **Articles**: `parasha_[name]_[year].md` or `parashat_[name]_[year].md`
  - Examples: `parasha_behar_2025.md`, `parashat_shalach_2025.md`
- **Images**: Match with year-based naming:
  - `[name]_[year].jpg/png` → `behar_2025.jpg`
  - `parasha_[name]_[year].jpg/png` → `parasha_behar_2025.jpg`
  - `parashat_[name]_[year].jpg/png` → `parashat_shalach_2025.jpg`
- **Auto-matching**: Build script automatically matches images to articles

## 🔧 Build System Details

### **Core Build Script**: `scripts/build.py` (COMPLETE - 1000+ lines)
```python
class ParashaWebsiteBuilder:
    # Contains complete HTML templates for:
    # - Base template (RTL layout, head, scripts)
    # - Index page template (homepage)
    # - Article page template (individual posts)
    # - Archive page template
    
    # Complete methods (ALL IMPLEMENTED):
    # - parse_frontmatter() → Extract YAML metadata
    # - process_markdown_file() → Convert MD to article data
    # - find_matching_image() → Year-based image matching
    # - render_article_page() → Generate article pages
    # - render_index_page() → Generate homepage
    # - generate_footer_html() → Eliran Sabag credits
    # - copy_assets() → Copy CSS/JS/images
    # - generate_json_feed() → JSON feed for syndication
    # - generate_rss_feed() → RSS XML feed
    # - generate_sitemap() → SEO sitemap
    # - create_manifest_and_service_worker() → PWA files
    # - format_date() → Hebrew date formatting
    # - generate_tag_cloud() → Tag cloud for sidebar
    # - build() → Main orchestration (TESTED ✅)
```

### **Generated Files**
- **index.html**: Homepage with article grid
- **articles/[slug].html**: Individual article pages
- **feed.json/feed.xml**: RSS feeds
- **sitemap.xml**: SEO sitemap
- **manifest.json**: PWA manifest
- **articles.json**: Metadata for search/API

### **Automatic Features (ALL IMPLEMENTED)**
- **Year-based image matching**: `behar_2025.jpg` → `parasha_behar_2025.md`
- **Reading time**: Auto-calculated from Hebrew content (200 words/min)
- **Excerpt generation**: Auto-generated if not provided (200 chars)
- **Tag cloud**: Auto-generated from all tags with frequency
- **Related articles**: Auto-linked by tags and parasha
- **Search index**: Auto-generated for client-side search
- **Author credits**: Eliran Sabag in footer of every page
- **SVG fallback**: For articles without matching images
- **Hebrew date formatting**: Months in Hebrew

## 🎨 Styling & Features

### **RTL Hebrew Support**
- **Default direction**: RTL for Hebrew content
- **LTR exceptions**: English content, code blocks, math
- **Typography**: Heebo font for Hebrew, Inter for English
- **Layout**: Right-to-left navigation, text alignment

### **Interactive Features**
- **Search**: Real-time article search
- **Dark mode**: Auto-detection + manual toggle
- **Mobile responsive**: Full mobile optimization
- **PWA**: Offline support, installable
- **Accessibility**: Screen reader compatible

### **Math & Code**
- **MathJax**: Full LaTeX support with proper RTL handling
- **Prism**: Syntax highlighting for 100+ languages
- **Code blocks**: LTR direction with proper styling

## 🚀 Deployment Workflow

### **GitHub Actions Pipeline**
```yaml
# Triggers: Push to main, content/ or images/ changes
# Process:
1. Checkout repository
2. Setup Python + dependencies
3. Optimize images (WebP conversion)
4. Run build.py (generate all HTML)
5. Validate build output
6. Deploy to GitHub Pages
7. Notify success/failure
```

### **Local Development**
```bash
# Setup
git clone <repo>
cd parasha-week
pip install -r requirements.txt

# Build locally
python scripts/build.py

# View output
cd docs && python -m http.server 8000
open http://localhost:8000
```

## 📊 Content Strategy

### **Topics & Themes**
- **Mathematical models** in biblical contexts
- **Statistical principles** in traditional texts
- **Ethical frameworks** for modern technology
- **Data-driven insights** from ancient wisdom
- **Leadership lessons** through technical lens
- **Algorithmic thinking** in Jewish law

### **Target Audience**
- Technology professionals interested in Jewish wisdom
- Data scientists and mathematicians
- Startup founders and entrepreneurs
- Students of both Torah and tech

### **Multi-Year Approach**
- Same parasha, different technical angles each year
- Evolution of understanding over time
- Cross-references between years
- Thematic development across cycles

## 🔍 Common Tasks

### **Adding New Article**
```bash
# 1. Create content file
vim content/parasha_vayera_2025.md

# 2. Add image (optional)
cp ~/vayera-image.jpg images/vayera.jpg

# 3. Commit and deploy
git add .
git commit -m "פרשת וירא: אלגוריתמי אירוח"
git push origin main

# 4. Wait ~2 minutes for auto-deployment
```

### **Testing Changes (UPDATED)**
```bash
# IMPORTANT: Always use the virtual environment for local testing
# Virtual environment already exists in repo (DO NOT commit venv/ folder)

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Dependencies already installed in venv, but if needed:
# pip install -r requirements.txt

# Run comprehensive test (includes full build)
source venv/bin/activate && python tests/test_build.py

# Manual build test
source venv/bin/activate && python scripts/build.py

# Check generated files
ls docs/                    # 17+ files (includes archive.html, tags.html)
ls docs/articles/          # 13+ article pages

# Local preview
cd docs && python -m http.server 8000
open http://localhost:8000

# REMEMBER: Always use virtual environment for any Python operations
```

### **Troubleshooting**
```bash
# Check GitHub Actions logs
# GitHub → Actions tab → View failed workflow

# Common issues:
# - Invalid YAML frontmatter
# - Missing dependencies in requirements.txt
# - Image optimization failures
# - Markdown syntax errors
```

## 🎯 Development Guidelines

### **Code Style**
- **Python**: Follow PEP 8, use type hints where helpful
- **HTML**: Semantic structure, accessibility-first
- **CSS**: RTL-first design, mobile-first responsive
- **JavaScript**: ES6+, progressive enhancement

### **Content Guidelines**
- **Hebrew**: Primary language, proper RTL formatting
- **English**: Technical terms, code comments, LTR sections
- **Math**: LaTeX syntax, proper display vs inline
- **Code**: Clear examples, Hebrew comments when appropriate

### **Performance**
- **Images**: Auto-optimized to WebP, lazy loading
- **CSS/JS**: Minified in production, critical path optimized
- **HTML**: Semantic structure, proper caching headers
- **Fonts**: Subset for Hebrew/English, display swap

## 🔒 Security & Privacy

### **GitHub Tokens**
- Uses `GITHUB_TOKEN` automatically provided by Actions
- No custom tokens or external API keys required
- All builds run in GitHub's secure environment

### **Privacy**
- No tracking cookies or user data collection
- No external analytics or advertising
- Optional privacy-friendly analytics (page views only)
- RSS/JSON feeds for syndication

## 🆘 Getting Help

### **Build Issues**
- Check GitHub Actions logs first
- Validate YAML frontmatter syntax
- Ensure all dependencies in requirements.txt
- Test locally with `python scripts/build.py`

### **Content Issues**
- Verify Hebrew UTF-8 encoding
- Check markdown syntax
- Ensure proper image file paths
- Test LaTeX expressions with MathJax

### **Styling Issues**
- RTL/LTR direction conflicts
- Mobile responsive breakpoints
- Font loading and display
- Cross-browser compatibility

---

## 💡 Project Philosophy

This project demonstrates that ancient wisdom and modern technology can illuminate each other. Each week's Torah portion is examined through a contemporary technical lens, revealing timeless patterns that apply to algorithms, data science, and innovation.

**Goal**: Create meaningful connections between Jewish tradition and technological advancement while maintaining the highest standards of both scholarly accuracy and technical excellence.

**Automation Philosophy**: Writing should be pure focus - everything else should be automated. Commit content, get beautiful website.

---

## 🎉 PROJECT STATUS: READY FOR PRODUCTION

### ✅ **COMPLETED FEATURES**
- **Complete build system** with all methods implemented
- **Year-based image matching** system
- **Author credits** (Eliran Sabag) on every page
- **13 existing articles** ready to publish
- **Full GitHub Actions** workflow tested
- **CSS/JS assets** complete with RTL Hebrew support
- **Test suite** for local verification
- **Production-ready** repository structure

### 📝 **CONTENT READY**
- 13 Parasha articles with technical analysis
- Mathematical models and programming concepts
- Hebrew content with LaTeX math support
- Multi-year approach for different perspectives

### 🚀 **DEPLOYMENT READY**
- Automated GitHub Pages deployment
- SEO optimization (sitemap, meta tags)
- PWA features (offline support)
- RSS/JSON feeds for syndication
- Performance optimized assets

**Next Step**: Commit to GitHub → Automatic deployment → Live website!
