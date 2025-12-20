# Parasha of the Week 📚⚡

🌐 **[Live Site → eliran79.github.io/parasha_of_the_week](https://eliran79.github.io/parasha_of_the_week/)**

**Automated Hebrew website** connecting Jewish Torah portions (Parashot) with mathematics, data science, AI, and startup concepts. Each week features deep technical analysis of ancient wisdom through a modern lens.

## 🎯 **Project Overview**

- **Content**: 13+ Hebrew articles with mathematical and technical analysis
- **Technology**: Automated Python build system with GitHub Actions
- **Features**: RTL Hebrew layout, LaTeX math, year-based image matching
- **Deployment**: Auto-deploys to GitHub Pages from markdown files
- **Author**: Eliran Sabag (אלירן סבג) - Credits on every page

## ✨ **What Makes This Special**

- **Mathematical models** in biblical contexts
- **Statistical principles** in traditional texts  
- **Ethical frameworks** for modern technology
- **Data-driven insights** from ancient wisdom
- **Leadership lessons** through technical lens
- **Multi-year approach** - same parasha, different angles each year

## 🚀 **Current Status: PRODUCTION READY**

✅ **Complete build system** (1000+ lines)  
✅ **13 articles** ready to publish  
✅ **Year-based image matching**  
✅ **Full automation** via GitHub Actions  
✅ **Hebrew RTL support** with LaTeX math  
✅ **SEO optimized** with feeds and sitemap  
✅ **PWA features** for offline reading  
✅ **Test suite** for quality assurance

## 📁 **Repository Structure**

```
parasha_of_the_week/
├── content/                    # 📝 13 Hebrew articles ready to publish
├── images/                     # 🖼️ Year-based image matching (shalach_2025.jpg)
├── scripts/build.py            # ⚙️ Complete 1000+ line build system
├── assets/                     # 🎨 RTL Hebrew CSS + Interactive JS
├── .github/workflows/          # 🤖 Production GitHub Actions
├── tests/                      # 🧪 Build verification (local only)
└── docs/                       # 🏗️ Auto-generated website (15+ files)
```

## 🛠️ **Quick Start**

### **🔒 Contributing (Secure Workflow)**
**All content contributions must go through Pull Request review:**

```bash
# Fork the repository on GitHub first, then:
git clone https://github.com/Eliran79/parasha_of_the_week.git
cd parasha_of_the_week

# Create a branch for your article
git checkout -b parasha-[name]-[year]

# Add your content (see CONTRIBUTING.md for guidelines)
# content/parasha_[name]_[year].md
# images/[name]_[year].jpg (optional)

# Commit and push
git add .
git commit -m "Add פרשת [name]: [brief Hebrew description]"
git push origin parasha-[name]-[year]

# Create Pull Request on GitHub for review
```

### **🚀 For Repository Owners:**
```bash
# Clone and setup
git clone <your-repo>
cd parasha_of_the_week

# Enable branch protection (see .github/branch-protection.md)
# Settings → Branches → Add rule for 'main'

# Test locally (optional)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python tests/test_build.py

# Direct commits only for maintenance (content goes via PR)
git add .
git commit -m "Maintenance: [description]"
git push
```

### **📄 For GitHub Pages Setup:**
1. **Enable GitHub Pages** → Settings → Pages → Source: "GitHub Actions"
2. **Configure branch protection** → See `.github/branch-protection.md`
3. **Merge approved PRs** → Auto-deploys in ~2 minutes
4. **Visit the live site** → [eliran79.github.io/parasha_of_the_week](https://eliran79.github.io/parasha_of_the_week/)

## 🎨 **Sample Content**

The repository includes rich Hebrew content like:

- **Parasha Behar**: Jubilee system solving modern concurrency problems
- **Parasha Mishpatim**: 3 mathematical models in biblical law
- **Parasha Tetzave**: High Priest's breastplate as mathematical matrix
- **Parasha Beshalach**: Startup lessons from Moses vs. Amalek
- **And 9+ more** technical Torah analyses

## 🔗 **Key Features**

- **Automated deployment** - Write markdown, get website
- **Hebrew RTL layout** - Proper right-to-left text flow
- **LaTeX math support** - Render mathematical formulas
- **Year-based articles** - Multi-year perspectives on same topics
- **Smart image system** - Auto-matching and responsive resizing
- **GitHub Pages ready** - Proper URL paths and asset loading
- **SEO optimized** - Feeds, sitemap, meta tags
- **PWA ready** - Offline reading capability
- **Mobile responsive** - Perfect on all devices

## 👨‍💻 **Author**

**Eliran Sabag (אלירן סבג)**
- 📧 eliran.sbg@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/eliran-sabag-51832651/)

*Credits appear on every page of the generated website*

## 🔒 **Security & Quality Assurance**

This repository implements comprehensive security measures:

### **Branch Protection**
- ✅ **Main branch protected** - No direct commits allowed
- ✅ **Pull Request required** - All changes reviewed before merge
- ✅ **Status checks enforced** - Automated validation must pass
- ✅ **Review approval needed** - Human oversight for all content

### **Automated Validation**
- 🔍 **YAML frontmatter validation** - Ensures proper metadata
- 📝 **Hebrew text verification** - UTF-8 encoding and RTL formatting
- 🖼️ **Image optimization** - Size limits and format validation
- 🔧 **Build process testing** - Verifies site generation works
- 🛡️ **Security scanning** - Prevents malicious content

### **Content Quality Standards**
- 📚 **Hebrew language accuracy** - Grammar and spelling checked
- 🔬 **Technical correctness** - Mathematical and scientific validation
- 📖 **Torah scholarship** - Respectful and accurate religious content
- 🎯 **Project alignment** - Maintains mission and quality standards

### **Contributor Guidelines**
- 📋 **See CONTRIBUTING.md** - Complete submission guidelines
- 🚨 **See SECURITY.md** - Security policies and procedures
- 🔧 **Use PR templates** - Guided submission process
- 👥 **Community standards** - Respectful and collaborative environment

---

## 🚀 **Ready to Contribute?**

1. **Read [CONTRIBUTING.md](.github/CONTRIBUTING.md)** for detailed guidelines
2. **Fork the repository** and create a feature branch  
3. **Submit a Pull Request** with your Hebrew article
4. **Wait for review** and address feedback
5. **Celebrate** when your contribution goes live! 🎉

**Questions?** Create an issue or contact the maintainers.

---

*This project bridges ancient wisdom with modern technology while maintaining the highest standards of quality and security.* ✨
