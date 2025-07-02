# Branch Protection Setup Guide

## 🔒 Repository Security Configuration

To properly secure the repository and enforce Pull Request workflows, the repository owner must configure the following settings through GitHub's web interface:

### 1. Branch Protection Rules

Navigate to: **Settings > Branches > Add rule**

#### Main Branch Protection (Required)
Configure the following settings for the `main` branch:

**Branch name pattern:** `main`

✅ **Require a pull request before merging**
- ✅ Require approvals: **1**
- ✅ Dismiss stale PR approvals when new commits are pushed
- ✅ Require review from code owners (if CODEOWNERS file exists)

✅ **Require status checks to pass before merging**
- ✅ Require branches to be up to date before merging
- Required status checks:
  - `validate-content`
  - `check-pr-requirements` 
  - `validation-summary`

✅ **Require conversation resolution before merging**

✅ **Require signed commits** (recommended)

✅ **Require linear history** (optional, for clean history)

✅ **Include administrators** (applies rules to repo admins too)

❌ Allow force pushes (disabled for security)

❌ Allow deletions (disabled for security)

### 2. Repository Settings

Navigate to: **Settings > General**

#### Merge Settings
- ✅ Allow merge commits
- ✅ Allow squash merging (recommended for clean history)
- ❌ Allow rebase merging (optional)
- ✅ Always suggest updating pull request branches
- ✅ Automatically delete head branches

#### Pull Request Settings
- ✅ Allow auto-merge
- ✅ Require approval of the most recent reviewable push

### 3. Code Owners (Optional)

Create `.github/CODEOWNERS` file to assign automatic reviewers:

```
# Global owners for all files
* @repository-owner

# Content-specific owners
content/ @content-reviewers @hebrew-reviewers
images/ @content-reviewers

# Technical files
scripts/ @technical-reviewers
.github/ @repository-owner
```

### 4. Required Status Checks

The following GitHub Actions workflows must pass before merging:

1. **PR Validation** (`.github/workflows/pr-validation.yml`)
   - YAML frontmatter validation
   - File naming convention checks
   - Image validation
   - Build process testing
   - Security scanning

2. **Content Quality Checks**
   - Hebrew text validation
   - Technical accuracy review
   - Torah scholarship verification

### 5. Webhook Configuration (Optional)

For additional notifications:

Navigate to: **Settings > Webhooks > Add webhook**

- **Payload URL**: Your notification endpoint
- **Content type**: `application/json`
- **Events**: 
  - Pull requests
  - Pull request reviews
  - Pushes to main

## 🚀 Enforcement Timeline

### Phase 1: Soft Enforcement (First 2 weeks)
- Branch protection enabled with warnings
- PR reviews encouraged but not strictly required
- Focus on education and process adoption

### Phase 2: Full Enforcement (After 2 weeks)
- All protection rules fully enforced
- No direct commits to main branch allowed
- Mandatory PR reviews for all content

## 👥 Reviewer Guidelines

### Content Reviewers Responsibilities
1. **Hebrew Language Review**
   - Grammar and spelling accuracy
   - Proper RTL formatting
   - Cultural and religious sensitivity

2. **Content Quality Review**
   - Technical accuracy verification
   - Torah scholarship validation
   - Logical flow and clarity
   - Appropriate depth and complexity

3. **Project Alignment Review**
   - Fits project mission and scope
   - Maintains quality standards
   - Adds value to existing collection

### Technical Reviewers Responsibilities
1. **Code Quality Review**
   - YAML frontmatter validation
   - File structure and naming
   - Build process compatibility
   - Performance considerations

2. **Security Review**
   - No sensitive data exposure
   - Safe external link usage
   - Proper attribution and licensing
   - Malicious content detection

## 🔧 Setup Commands

Repository owners can use these GitHub CLI commands to configure protection:

```bash
# Enable branch protection with required reviews
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["validate-content","check-pr-requirements"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null

# Alternatively, use the web interface for easier configuration
```

## 📋 Compliance Checklist

Before going live with protection:

- [ ] Branch protection rules configured
- [ ] PR validation workflow tested
- [ ] Code owners file created (optional)
- [ ] Reviewer team established
- [ ] Contributor guidelines published
- [ ] Emergency access procedures documented
- [ ] Backup procedures in place

## 🆘 Emergency Procedures

In case of urgent hotfixes:

1. **Option 1**: Temporary protection bypass
   - Disable protection temporarily
   - Make urgent commit
   - Re-enable protection immediately
   - Create follow-up PR for documentation

2. **Option 2**: Emergency PR process
   - Create urgent PR with `[URGENT]` prefix
   - Request immediate review
   - Use admin override if necessary
   - Document reason in PR description

## 📞 Support

For questions about repository security:
- Create an issue with `security` label
- Contact repository maintainers
- Review GitHub documentation on branch protection

---

**Implementation of these security measures ensures content quality while maintaining collaborative workflows.** 🔒✨