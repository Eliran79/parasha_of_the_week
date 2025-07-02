# Security Policy

## 🔒 Repository Security for פרשת השבוע

This document outlines security policies and procedures for the Parasha of the Week project.

## 🛡️ Security Measures

### Branch Protection
- **Main branch is protected** - no direct commits allowed
- **Pull Request reviews required** - minimum 1 approval needed
- **Status checks enforced** - automated validation must pass
- **Up-to-date branches required** - must be current with main

### Content Security
- **YAML validation** - frontmatter must be valid and complete
- **File naming enforcement** - strict naming conventions required
- **Image size limits** - maximum 5MB per image file
- **Content scanning** - automated security scans for all submissions

### Access Control
- **Contributor workflow** - all content changes via Pull Requests
- **Review requirements** - content and technical validation
- **Code owners** - automatic review assignment
- **Admin oversight** - repository owners have final approval

## 📝 Supported Content Types

### Secure Content
- ✅ **Markdown articles** with Hebrew text and technical analysis
- ✅ **Images** (JPG, PNG, WebP) under 5MB
- ✅ **LaTeX mathematical expressions** using MathJax
- ✅ **Code examples** in common programming languages
- ✅ **YAML frontmatter** with project metadata

### Restricted Content
- ❌ **External scripts** or JavaScript execution
- ❌ **HTML with embedded scripts** 
- ❌ **External file includes** or remote resources
- ❌ **Binary files** other than approved image formats
- ❌ **Sensitive information** (passwords, keys, personal data)

## 🚨 Reporting Security Vulnerabilities

### What to Report
Please report any of the following:
- **Code injection** vulnerabilities in build process
- **Content security** issues (XSS, malicious content)
- **Access control** bypasses or unauthorized changes
- **Data exposure** of sensitive information
- **Infrastructure** vulnerabilities in GitHub Actions

### How to Report
**For security vulnerabilities, please do NOT create public issues.**

Instead, contact us privately:
- **Email**: eliran.sbg@gmail.com
- **Subject**: `[SECURITY] פרשת השבוע - Brief Description`
- **GitHub Security Advisories**: Use the "Security" tab > "Report a vulnerability"

### Response Timeline
- **Acknowledgment**: Within 24 hours
- **Initial assessment**: Within 72 hours  
- **Resolution plan**: Within 1 week
- **Public disclosure**: After fix is deployed (if applicable)

## 🔍 Security Validation Process

### Automated Checks
Every Pull Request automatically runs:

1. **Content Validation**
   - YAML frontmatter syntax validation
   - File naming convention enforcement
   - Image size and format validation
   - Hebrew text encoding verification

2. **Security Scanning**
   - Malicious content detection
   - External link validation
   - Script injection prevention
   - Credential exposure checks

3. **Build Validation**
   - Safe build process execution
   - Output validation and sanitization
   - HTML security verification

### Manual Review Process
Human reviewers verify:

1. **Content Safety**
   - No malicious or inappropriate content
   - Proper attribution and licensing
   - Respectful treatment of religious content
   - Technical accuracy and safety

2. **Security Compliance**
   - No embedded scripts or dangerous HTML
   - Safe external references
   - Proper file structure and permissions
   - Compliance with project guidelines

## 🚀 Deployment Security

### Production Deployment
- **Automated builds only** - no manual file uploads
- **GitHub Pages hosting** - secure, managed infrastructure
- **HTTPS enforcement** - all traffic encrypted
- **Content Security Policy** - XSS and injection protection

### Build Process Security
- **Isolated environments** - GitHub Actions containers
- **Dependency validation** - known, verified packages only
- **Output sanitization** - safe HTML generation
- **Artifact signing** - build integrity verification

## 📋 Security Compliance

### Data Protection
- **No personal data collection** - privacy-focused design
- **No tracking cookies** - respects user privacy
- **Minimal analytics** - page views only, no user tracking
- **GDPR compliance** - European privacy standards

### Content Licensing
- **Open source project** - transparent and auditable
- **Clear attribution** - proper credit for all contributors
- **Respectful usage** - appropriate handling of religious content
- **Copyright compliance** - original content or proper licensing

## ⚠️ Security Guidelines for Contributors

### Safe Content Creation
- ✅ Use only plain text and Markdown formatting
- ✅ Include properly formatted YAML frontmatter
- ✅ Verify all mathematical expressions render safely
- ✅ Test content in local environment before submission
- ✅ Follow Hebrew text encoding standards (UTF-8)

### Avoid Security Risks
- ❌ Never include executable scripts or HTML
- ❌ Don't embed external content or iframes
- ❌ Avoid exposing personal information
- ❌ Don't use deprecated or unsafe LaTeX commands
- ❌ Never commit sensitive data or credentials

### Best Practices
- 🔍 **Review your own content** before submitting
- 🔒 **Use secure connections** for all development
- 📝 **Document any external references** in your PR
- 🚀 **Test the build process** locally when possible
- 👥 **Collaborate transparently** through public channels

## 🆘 Incident Response

### Security Incident Types
1. **Critical**: Active exploitation or data breach
2. **High**: Vulnerability with high impact potential
3. **Medium**: Security weakness requiring attention
4. **Low**: Minor security improvement opportunity

### Response Procedures
1. **Immediate containment** - disable affected functionality
2. **Impact assessment** - determine scope and severity
3. **Communication** - notify stakeholders appropriately
4. **Remediation** - implement fix and validate solution
5. **Post-incident review** - improve processes and prevention

### Recovery Process
- **Service restoration** - return to normal operations
- **Monitoring** - enhanced surveillance post-incident
- **Documentation** - record lessons learned
- **Process improvement** - update security measures

## 📞 Contact Information

### Security Team
- **Primary Contact**: Eliran Sabag (eliran.sbg@gmail.com)
- **GitHub**: @eliran-sabag
- **Response Time**: Within 24 hours for security issues

### Repository Maintainers
- **Technical Issues**: Create GitHub issue with `security` label
- **Content Concerns**: Create GitHub issue with `content-security` label
- **Infrastructure**: Contact via GitHub Security Advisories

## 📚 Security Resources

### Documentation
- [GitHub Security Documentation](https://docs.github.com/en/code-security)
- [Markdown Security Guide](https://github.com/github/markup/tree/master#security)
- [GitHub Actions Security](https://docs.github.com/en/actions/security-guides)

### Tools and Validation
- [YAML Validator](https://yamlchecker.com/)
- [Hebrew Text Encoding Verification](https://validator.w3.org/i18n-checker/)
- [LaTeX Security Guidelines](https://www.latex-project.org/help/security/)

---

## 🛡️ Security Summary

This project maintains security through:
- **Automated validation** of all content submissions
- **Human review process** for quality and safety
- **Secure deployment pipeline** with isolated builds
- **Clear guidelines** for safe content creation
- **Rapid response** to security concerns

**Your security is our priority. When in doubt, ask questions before submitting.** 🔒

---

*Last updated: July 2025*