# Contributing to פרשת השבוע (Parasha of the Week)

Thank you for your interest in contributing to this unique project that bridges ancient Torah wisdom with modern technology! 🙏

## 🎯 Contribution Guidelines

### Who Can Contribute?
We welcome contributions from:
- Torah scholars with technical backgrounds
- Technology professionals interested in Jewish wisdom
- Hebrew writers with mathematical/scientific knowledge
- Data scientists exploring ancient texts
- Anyone combining tradition with innovation

### What We're Looking For
**High-quality Hebrew articles that connect weekly Torah portions with:**
- Mathematics and algorithms
- Data science and statistics
- Software engineering principles
- AI and machine learning
- Startup and business insights
- Scientific methodologies

## 📝 How to Contribute

### 1. Fork and Clone
```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/Eliran79/parasha_of_the_week.git
cd parasha_of_the_week
```

### 2. Create Your Article
**File Structure:**
```
content/parasha_[name]_[year].md    # Your article
images/[name]_[year].jpg            # Optional image
```

**Article Template:**
```yaml
---
title: "כותרת המאמר בעברית"
parasha: "שם הפרשה"
date: "2025-01-15"
tags: ["מתמטיקה", "תכנות", "בינה_מלאכותית"]
emoji: "🔢"
excerpt: "תיאור קצר של המאמר (מקסימום 200 תווים)"
author: "שם המחבר"
year: 2025
---

# כותרת ראשית

תוכן המאמר בעברית עם תמיכה מלאה ב:

## עברית ו-RTL
זה טקסט עברי שיוצג נכון עם כיוון RTL.

## LaTeX ומתמטיקה
$$P(X|Y) = \frac{P(Y|X) \cdot P(X)}{P(Y)}$$

## קוד עם הדגשת תחביר
```python
def parasha_algorithm():
    return "אלגוריתם מהפרשה"
```

## אנגלית (LTR)
<div class="english">
This text will be displayed LTR with English fonts.
</div>
```

### 3. Submission Process

**⚠️ IMPORTANT: All contributions must go through Pull Request review process.**

```bash
# Create a new branch for your article
git checkout -b parasha-[name]-[year]

# Add your files
git add content/parasha_[name]_[year].md
git add images/[name]_[year].jpg  # if applicable

# Commit with descriptive message
git commit -m "Add פרשת [name]: [brief description in Hebrew]"

# Push to your fork
git push origin parasha-[name]-[year]

# Create Pull Request on GitHub
```

### 4. Pull Request Requirements

Your PR must include:

#### Content Quality
- [ ] **Hebrew proficiency**: Correct grammar and spelling
- [ ] **Technical accuracy**: Verified mathematical/scientific content
- [ ] **Original insights**: Fresh perspective connecting Torah with technology
- [ ] **Appropriate length**: 800-2000 words for substantial analysis
- [ ] **Respectful tone**: Maintains reverence for religious content

#### Technical Requirements
- [ ] **Valid YAML frontmatter**: All required fields completed
- [ ] **Proper file naming**: Follows established conventions
- [ ] **UTF-8 encoding**: Hebrew text properly encoded
- [ ] **Working LaTeX**: Math expressions render correctly
- [ ] **Optimized images**: If included, < 2MB and properly named

#### Metadata Requirements
- [ ] **Relevant tags**: Minimum 3, maximum 8 tags
- [ ] **Accurate excerpt**: Compelling 200-character summary
- [ ] **Proper dating**: Reflects actual publication timeline
- [ ] **Author attribution**: Your name and credentials (optional)

## 🔒 Security and Review Process

### Branch Protection Rules
- **Main branch is protected** - no direct commits allowed
- **Requires Pull Request reviews** - minimum 1 reviewer approval
- **Status checks required** - automated build must pass
- **Up-to-date branches** - must be current with main before merge

### Review Criteria
Reviewers will evaluate:

1. **Content Quality** (40%)
   - Hebrew language accuracy
   - Technical correctness
   - Original insights and analysis
   - Connection to Torah portion

2. **Technical Implementation** (30%)
   - File structure and naming
   - YAML frontmatter validity
   - Markdown formatting
   - Build compatibility

3. **Project Fit** (20%)
   - Aligns with project mission
   - Appropriate topic and approach
   - Maintains quality standards
   - Adds value to collection

4. **Code of Conduct** (10%)
   - Respectful content
   - Proper attribution
   - No plagiarism
   - Community guidelines

### Reviewer Responsibilities
- Review within 48-72 hours
- Provide constructive feedback
- Ensure technical accuracy
- Verify Hebrew correctness
- Test build process

## 🚫 What We Don't Accept

- **Poor Hebrew**: Grammatical errors, improper RTL formatting
- **Plagiarized content**: Must be original work
- **Off-topic articles**: Must connect Torah portion with technology
- **Disrespectful content**: Maintains reverence for religious texts
- **Technical errors**: Broken LaTeX, invalid YAML, incorrect file structure
- **Short articles**: Less than 800 words (except special circumstances)

## 🎯 Content Guidelines

### Writing Style
- **Hebrew-first**: Primary language with English technical terms as needed
- **Technical depth**: Include mathematical formulas, code examples, or data analysis
- **Accessible**: Explain complex concepts clearly
- **Engaging**: Use modern examples and analogies

### Technical Integration
- **Mathematics**: Use LaTeX for equations and formulas
- **Code**: Include relevant programming examples
- **Data**: Provide statistical analysis where appropriate
- **Visuals**: Charts, diagrams, or relevant images

### Religious Sensitivity
- **Respectful approach**: Treat Torah text with reverence
- **Accurate citations**: Proper Hebrew references
- **Balanced perspective**: Technical analysis without diminishing spiritual meaning
- **Cultural awareness**: Understand Orthodox, Conservative, and Reform perspectives

## 🛠️ Development Setup

### Local Testing
```bash
# Install dependencies
pip install -r requirements.txt

# Build locally
python scripts/build.py

# Serve locally
cd docs && python -m http.server 8000
```

### Validation Tools
- **YAML validation**: Use yamllint or online validators
- **Hebrew spell check**: Use appropriate tools for Hebrew text
- **LaTeX testing**: Verify math rendering with MathJax
- **Build testing**: Ensure your article builds without errors

## 📞 Getting Help

### Questions About Contributing?
- **Content questions**: Create an issue with `question` label
- **Technical issues**: Create an issue with `technical` label
- **Hebrew language help**: Reach out to maintainers
- **Torah scholarship**: Connect with our review team

### Contact
- **GitHub Issues**: Primary communication method
- **Email**: eliran.sbg@gmail.com (project maintainer)
- **Discussions**: Use GitHub Discussions for broader topics

## 🏆 Recognition

Contributors will be:
- **Credited** in article bylines
- **Listed** in project contributors
- **Highlighted** in project documentation
- **Invited** to become regular contributors

## 📋 Review Timeline

1. **Submission**: Submit PR with complete article
2. **Initial Review** (24-48 hours): Technical validation and basic quality check
3. **Content Review** (48-72 hours): Hebrew language and Torah scholarship review
4. **Feedback** (if needed): Reviewers provide constructive feedback
5. **Revision** (author): Address feedback and update PR
6. **Final Approval**: Merge into main branch
7. **Deployment**: Automatic publication within 2 minutes

## 🙏 Thank You

Your contributions help bridge ancient wisdom with modern technology, creating meaningful connections for our community. Every article adds value to this unique collection of Torah-technology insights.

**Welcome to the פרשת השבוע contributor community!** 🎉

---

*"In every generation, wisdom must be renewed and applied to contemporary challenges."*