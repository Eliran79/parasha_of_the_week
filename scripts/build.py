# Updated build.py with complete template system
#!/usr/bin/env python3

import os
import json
import re
import yaml
from pathlib import Path
from datetime import datetime
import markdown
from markdown.extensions import codehilite, tables, toc
import shutil

class ParashaWebsiteBuilder:
    def __init__(self, content_dir="content", output_dir="docs", images_dir="images"):
        self.content_dir = Path(content_dir)
        self.output_dir = Path(output_dir)
        self.images_dir = Path(images_dir)
        self.articles = []
        
        # Base path for GitHub Pages - change to empty string for root domain
        self.base_path = "/parasha_of_the_week"
        
        # Load all templates
        self.templates = {
            'base': self.load_base_template(),
            'index': self.load_index_template(),
            'article': self.load_article_template(),
            'archive': self.load_archive_template()
        }
    
    def apply_base_path(self, html_content):
        """Replace {{base_path}} and {base_path} placeholders with actual base path"""
        html_content = html_content.replace('{{base_path}}', self.base_path)
        html_content = html_content.replace('{base_path}', self.base_path)
        return html_content

    def load_base_template(self):
        """Base HTML template for all pages"""
        return '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{page_title}}</title>
    
    <!-- SEO Meta Tags -->
    <meta name="description" content="{{description}}">
    <meta name="keywords" content="{{keywords}}">
    <meta name="author" content="{{author}}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{{page_title}}">
    <meta property="og:description" content="{{description}}">
    <meta property="og:image" content="{{image_url}}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="{{page_title}}">
    <meta property="og:type" content="{{og_type}}">
    <meta property="og:locale" content="he_IL">
    <meta property="og:url" content="{{canonical_url}}">
    <meta property="og:site_name" content="פרשת השבוע">
    {{article_meta}}
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{{page_title}}">
    <meta name="twitter:description" content="{{description}}">
    <meta name="twitter:image" content="{{image_url}}">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="{{canonical_url}}">
    
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- MathJax for LaTeX support -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                processEscapes: true,
                processEnvironments: true
            },
            options: {
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
            }
        };
    </script>
    
    <!-- Syntax highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
    
    <!-- Styles -->
    <link rel="stylesheet" href="{{base_path}}/assets/css/style.css">
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="{{base_path}}/manifest.json">
    <meta name="theme-color" content="#2563eb">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="{{base_path}}/favicon.ico">
    <link rel="apple-touch-icon" href="{{base_path}}/apple-touch-icon.png">
    
    <!-- RSS Feed -->
    <link rel="alternate" type="application/rss+xml" title="פרשת השבוע" href="{{base_path}}/feed.xml">
    <link rel="alternate" type="application/json" title="פרשת השבוע" href="{{base_path}}/feed.json">
    
    {{extra_head}}
</head>
<body>
    {{content}}
    
    <!-- Scripts -->
    <script src="{{base_path}}/assets/js/main.js"></script>
    
    <!-- Re-render MathJax and Prism -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Re-render MathJax
            if (window.MathJax && window.MathJax.typesetPromise) {
                MathJax.typesetPromise();
            }
            
            // Re-highlight code
            if (window.Prism) {
                Prism.highlightAll();
            }
        });
    </script>
    
    {{extra_scripts}}
</body>
</html>'''

    def load_index_template(self):
        """Homepage template"""
        return '''
    <header class="header">
        <div class="header-content">
            <h1 class="site-title">פרשת השבוע</h1>
            <p class="site-subtitle">חיבור בין חכמת התורה למתמטיקה, מדע הנתונים ובינה מלאכותית</p>
        </div>
    </header>

    <nav class="nav">
        <div class="nav-content">
            <ul class="nav-links">
                <li><a href="{{base_path}}/" class="nav-link active">בית</a></li>
                <li><a href="{{base_path}}/archive.html" class="nav-link">ארכיון</a></li>
                <li><a href="{{base_path}}/tags.html" class="nav-link">תגיות</a></li>
                <li><a href="{{base_path}}/about.html" class="nav-link">אודות</a></li>
            </ul>
        </div>
    </nav>

    <main class="main">
        <div class="content">
            <div class="search-container">
                <input type="text" class="search-input" placeholder="חפש פרשה, נושא או תגית..." id="search-input">
                <div class="search-stats" id="search-stats"></div>
            </div>
            
            <div class="featured-section">
                <h2 class="section-title">פרשיות אחרונות</h2>
                <div class="articles-grid" id="articles-grid">
                    {{articles_html}}
                </div>
            </div>
            
            <div class="cta-section">
                <h3>רוצה לקבל עדכונים?</h3>
                <p>עקוב אחרי הפרויקט ב-GitHub לעדכונים על פרשיות חדשות</p>
                <a href="https://github.com/Eliran79/parasha_of_the_week" class="btn-primary">GitHub →</a>
            </div>
        </div>
        
        {{sidebar_html}}
    </main>
    
    {{footer_html}}
'''

    def load_article_template(self):
        """Individual article page template"""
        return '''
    <header class="header">
        <div class="header-content">
            <h1 class="site-title">פרשת השבוע</h1>
            <p class="site-subtitle">חיבור בין חכמת התורה למתמטיקה, מדע הנתונים ובינה מלאכותית</p>
        </div>
    </header>

    <nav class="nav">
        <div class="nav-content">
            <ul class="nav-links">
                <li><a href="{{base_path}}/" class="nav-link">בית</a></li>
                <li><a href="{{base_path}}/archive.html" class="nav-link">ארכיון</a></li>
                <li><a href="{{base_path}}/tags.html" class="nav-link">תגיות</a></li>
                <li><a href="{{base_path}}/about.html" class="nav-link">אודות</a></li>
            </ul>
        </div>
    </nav>

    <main class="main single-article">
        <article class="article-page">
            <div class="article-header">
                <div class="article-hero">
                    <img src="{{article.image}}" alt="{{article.title}}" class="article-hero-image" loading="lazy">
                </div>
                <div class="article-meta-wrapper">
                    <div class="article-meta">
                        <span class="parasha-tag">{{article.parasha}}</span>
                        <time datetime="{{article.date}}" class="article-date">{{formatted_date}}</time>
                        <span class="reading-time">{{article.reading_time}} דקות קריאה</span>
                    </div>
                    <h1 class="article-title">{{article.title}}</h1>
                    {{article.excerpt}}
                </div>
            </div>
            
            <div class="article-content">
                {{article_content}}
            </div>
            
            <div class="article-footer">
                <div class="article-tags">
                    {{tags_html}}
                </div>
                
                <div class="article-actions">
                    <button onclick="shareArticle('{{article.title}}', window.location.href)" class="btn-secondary">
                        שתף מאמר
                    </button>
                    <button onclick="printArticle()" class="btn-secondary">
                        הדפס
                    </button>
                </div>
                
                <div class="article-navigation">
                    {{prev_next_html}}
                </div>
            </div>
        </article>
        
        <aside class="article-sidebar">
            <div class="sidebar-section">
                <h3 class="sidebar-title">תוכן עניינים</h3>
                <div class="toc" id="article-toc">
                    {{toc_html}}
                </div>
            </div>
            
            <div class="sidebar-section">
                <h3 class="sidebar-title">פרשיות קשורות</h3>
                <div class="related-articles">
                    {{related_articles_html}}
                </div>
            </div>
        </aside>
    </main>
    
    {{footer_html}}
'''

    def load_archive_template(self):
        """Archive page template"""
        return '''
    <header class="header">
        <div class="header-content">
            <h1 class="site-title">ארכיון פרשיות</h1>
            <p class="site-subtitle">כל הפרשיות שפורסמו עד כה</p>
        </div>
    </header>

    <nav class="nav">
        <div class="nav-content">
            <ul class="nav-links">
                <li><a href="{{base_path}}/" class="nav-link">בית</a></li>
                <li><a href="{{base_path}}/archive.html" class="nav-link active">ארכיון</a></li>
                <li><a href="{{base_path}}/tags.html" class="nav-link">תגיות</a></li>
                <li><a href="{{base_path}}/about.html" class="nav-link">אודות</a></li>
            </ul>
        </div>
    </nav>

    <main class="main">
        <div class="content">
            <div class="archive-filters">
                <div class="filter-group">
                    <label for="year-filter">שנה:</label>
                    <select id="year-filter">
                        <option value="">כל השנים</option>
                        {{year_options}}
                    </select>
                </div>
                
                <div class="filter-group">
                    <label for="parasha-filter">פרשה:</label>
                    <select id="parasha-filter">
                        <option value="">כל הפרשיות</option>
                        {{parasha_options}}
                    </select>
                </div>
                
                <div class="filter-group">
                    <label for="tag-filter">תגית:</label>
                    <select id="tag-filter">
                        <option value="">כל התגיות</option>
                        {{tag_options}}
                    </select>
                </div>
            </div>
            
            <div class="archive-stats">
                <div class="stat">
                    <span class="stat-number">{{total_articles}}</span>
                    <span class="stat-label">מאמרים</span>
                </div>
                <div class="stat">
                    <span class="stat-number">{{total_parashot}}</span>
                    <span class="stat-label">פרשיות</span>
                </div>
                <div class="stat">
                    <span class="stat-number">{{total_tags}}</span>
                    <span class="stat-label">תגיות</span>
                </div>
            </div>
            
            <div class="articles-list" id="archive-articles">
                {{archive_articles_html}}
            </div>
        </div>
    </main>
    
    {{footer_html}}
'''

    def generate_sidebar_html(self):
        """Generate sidebar HTML"""
        return f'''
        <aside class="sidebar">
            <div class="sidebar-section">
                <h3 class="sidebar-title">תגיות פופולריות</h3>
                <div class="tag-cloud">
                    {self.generate_tag_cloud()}
                </div>
            </div>

            <div class="sidebar-section">
                <h3 class="sidebar-title">פרשיות אחרונות</h3>
                <ul class="recent-list">
                    {self.generate_recent_articles()}
                </ul>
            </div>
            
            <div class="sidebar-section">
                <h3 class="sidebar-title">סטטיסטיקות</h3>
                <div class="stats">
                    <div class="stat-item">
                        <span class="stat-number">{len(self.articles)}</span>
                        <span class="stat-label">מאמרים</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number">{len(set(a['parasha'] for a in self.articles))}</span>
                        <span class="stat-label">פרשיות</span>
                    </div>
                </div>
            </div>

            <div class="sidebar-section">
                <h3 class="sidebar-title">הסבר על הפרויקט</h3>
                <p style="font-size: 0.875rem; color: var(--text-secondary); line-height: 1.6;">
                    כל שבוע אנחנו חוקרים את פרשת השבוע מזווית מדעית וטכנולוגית מודרנית, 
                    וחושפים קשרים מפתיעים בין חכמת התורה לעולם המתמטיקה והטכנולוגיה.
                </p>
                <a href="{{base_path}}/about.html" class="read-more">קרא עוד על הפרויקט →</a>
            </div>
        </aside>
        '''

    def generate_footer_html(self):
        """Generate footer HTML"""
        current_year = datetime.now().year
        return f'''
        <footer class="footer">
            <div class="footer-content">
                <div class="footer-links">
                    <a href="https://github.com/Eliran79/parasha_of_the_week" class="footer-link">GitHub</a>
                    <a href="{{base_path}}/feed.xml" class="footer-link">RSS</a>
                    <a href="{{base_path}}/feed.json" class="footer-link">JSON Feed</a>
                    <a href="{{base_path}}/about.html" class="footer-link">אודות</a>
                    <a href="{{base_path}}/contact.html" class="footer-link">צור קשר</a>
                </div>
                <p>&copy; {current_year} פרשת השבוע. בנוי עם ❤️ ו-GitHub Pages</p>
                <p class="footer-tech">
                    <span>נבנה עם Python, GitHub Actions, ומתמטיקה יהודית עתיקה</span>
                </p>
                <div class="footer-author">
                    <p class="author-credit">
                        <strong>מאת: אלירן סבג (Eliran Sabag)</strong>
                    </p>
                    <div class="author-links">
                        <a href="mailto:eliran.sbg@gmail.com" class="author-link">📧 eliran.sbg@gmail.com</a>
                        <a href="https://www.linkedin.com/in/eliran-sabag-51832651/" class="author-link" target="_blank" rel="noopener">💼 LinkedIn</a>
                    </div>
                </div>
            </div>
        </footer>
        '''

    def render_index_page(self):
        """Render the main index.html page"""
        # Sort articles by date (newest first)
        sorted_articles = sorted(self.articles, key=lambda x: x['date'], reverse=True)
        
        # Generate articles HTML
        articles_html = ""
        for i, article in enumerate(sorted_articles[:9]):  # Show 9 most recent
            featured_class = "featured" if i < 3 else ""
            articles_html += f'''
            <article class="article-card {featured_class}" data-article-id="{article['id']}">
                <div class="article-image" style="background-image: url('{article['image']}')">
                    <span class="article-emoji">{article['emoji']}</span>
                </div>
                <div class="article-content">
                    <div class="article-meta">
                        <span class="parasha-tag">{article['parasha']}</span>
                        <time datetime="{article['date']}">{self.format_date(article['date'])}</time>
                    </div>
                    <h2 class="article-title">
                        <a href="{{base_path}}/articles/{article['slug']}.html">{article['title']}</a>
                    </h2>
                    <p class="article-excerpt">{article['excerpt']}</p>
                    <div class="article-footer">
                        <a href="{{base_path}}/articles/{article['slug']}.html" class="read-more">
                            קרא עוד ←
                        </a>
                        <span class="reading-time">{article['reading_time']} דק׳</span>
                    </div>
                </div>
            </article>
            '''

        # Fill template
        content = self.templates['index'].replace('{{articles_html}}', articles_html)
        content = content.replace('{{sidebar_html}}', self.generate_sidebar_html())
        content = content.replace('{{footer_html}}', self.generate_footer_html())

        # Fill base template
        page_html = self.templates['base'].replace('{{content}}', content)
        page_html = page_html.replace('{{page_title}}', 'פרשת השבוע | מתמטיקה, מדע ונתונים')
        page_html = page_html.replace('{{description}}', 'חיבור בין פרשיות התורה למתמטיקה, מדע הנתונים, בינה מלאכותית ועולם הסטארטאפים')
        page_html = page_html.replace('{{keywords}}', 'פרשת השבוע, מתמטיקה, מדע נתונים, בינה מלאכותית, יהדות, טכנולוגיה')
        page_html = page_html.replace('{{author}}', 'אלירן סבג')
        page_html = page_html.replace('{{image_url}}', f'https://Eliran79.github.io{self.base_path}/images/logo.png')
        page_html = page_html.replace('{{og_type}}', 'website')
        page_html = page_html.replace('{{canonical_url}}', 'https://Eliran79.github.io/parasha_of_the_week/')
        page_html = page_html.replace('{{article_meta}}', '')
        page_html = page_html.replace('{{extra_head}}', '')
        page_html = page_html.replace('{{extra_scripts}}', '')

        # Apply base path to all links
        page_html = self.apply_base_path(page_html)
        
        return page_html

    def render_article_page(self, article):
        """Render individual article page"""
        # Convert markdown to HTML
        md = markdown.Markdown(extensions=[
            'codehilite',
            'tables', 
            'toc',
            'fenced_code',
            'nl2br'
        ])
        
        content_html = md.convert(article['content'])
        
        # Generate tags HTML
        tags_html = ''.join([f'<a href="{{base_path}}/tags.html#tag-{tag}" class="tag">#{tag}</a>' 
                            for tag in article['tags']])
        
        # Generate TOC
        toc_html = md.toc if hasattr(md, 'toc') else ''
        
        # Generate related articles
        related_articles_html = self.generate_related_articles(article)
        
        # Generate prev/next navigation
        prev_next_html = self.generate_prev_next_navigation(article)
        
        # Fill article template
        content = self.templates['article']
        replacements = {
            '{{article.image}}': article['image'],
            '{{article.title}}': article['title'],
            '{{article.parasha}}': article['parasha'],
            '{{article.date}}': article['date'],
            '{{formatted_date}}': self.format_date(article['date']),
            '{{article.reading_time}}': str(article['reading_time']),
            '{{article.excerpt}}': f'<p class="article-lead">{article["excerpt"]}</p>',
            '{{article_content}}': content_html,
            '{{tags_html}}': tags_html,
            '{{toc_html}}': toc_html,
            '{{related_articles_html}}': related_articles_html,
            '{{prev_next_html}}': prev_next_html,
            '{{footer_html}}': self.generate_footer_html()
        }
        
        for placeholder, replacement in replacements.items():
            content = content.replace(placeholder, replacement)
        
        # Fill base template
        page_html = self.templates['base'].replace('{{content}}', content)
        page_html = page_html.replace('{{page_title}}', f"{article['title']} | פרשת השבוע")
        page_html = page_html.replace('{{description}}', article['excerpt'])
        page_html = page_html.replace('{{keywords}}', ', '.join(article['tags']))
        page_html = page_html.replace('{{author}}', article.get('author', 'אלירן סבג'))
        # Convert relative image path to absolute URL for Open Graph
        if article['image'].startswith('/parasha_of_the_week/'):
            absolute_image_url = f"https://Eliran79.github.io{article['image']}"
        elif article['image'].startswith('/'):
            absolute_image_url = f"https://Eliran79.github.io/parasha_of_the_week{article['image']}"
        else:
            absolute_image_url = f"https://Eliran79.github.io/parasha_of_the_week/{article['image']}"
        page_html = page_html.replace('{{image_url}}', absolute_image_url)
        page_html = page_html.replace('{{og_type}}', 'article')
        page_html = page_html.replace('{{canonical_url}}', f"https://Eliran79.github.io/parasha_of_the_week/articles/{article['slug']}.html")
        article_meta_tags = f'''<meta property="article:published_time" content="{article['date']}T00:00:00Z">
    <meta property="article:author" content="{article.get('author', 'אלירן סבג')}">
    <meta property="article:section" content="{article['parasha']}">'''
        for tag in article['tags']:
            article_meta_tags += f'\n    <meta property="article:tag" content="{tag}">'
        
        page_html = page_html.replace('{{article_meta}}', article_meta_tags)
        page_html = page_html.replace('{{extra_head}}', '')
        page_html = page_html.replace('{{extra_scripts}}', '')

        # Apply base path to all links
        page_html = self.apply_base_path(page_html)
        
        return page_html

    def generate_related_articles(self, current_article):
        """Generate related articles HTML"""
        # Find articles with similar tags
        related = []
        for article in self.articles:
            if article['id'] != current_article['id']:
                common_tags = set(article['tags']) & set(current_article['tags'])
                if common_tags:
                    related.append((article, len(common_tags)))
        
        # Sort by number of common tags and take top 3
        related = sorted(related, key=lambda x: x[1], reverse=True)[:3]
        
        html = ""
        for article, _ in related:
            html += f'''
            <div class="related-article">
                <a href="{{base_path}}/articles/{article['slug']}.html" class="related-link">
                    <img src="{article['image']}" alt="{article['title']}" class="related-image">
                    <div class="related-content">
                        <span class="related-parasha">{article['parasha']}</span>
                        <h4 class="related-title">{article['title']}</h4>
                    </div>
                </a>
            </div>
            '''
        
        return html

    def generate_prev_next_navigation(self, current_article):
        """Generate previous/next article navigation"""
        sorted_articles = sorted(self.articles, key=lambda x: x['date'], reverse=True)
        current_index = next((i for i, a in enumerate(sorted_articles) if a['id'] == current_article['id']), None)
        
        if current_index is None:
            return ""
        
        html = '<div class="article-nav">'
        
        # Previous article
        if current_index > 0:
            prev_article = sorted_articles[current_index - 1]
            html += f'''
            <a href="{{base_path}}/articles/{prev_article['slug']}.html" class="nav-prev">
                <span class="nav-label">← הקודם</span>
                <span class="nav-title">{prev_article['title']}</span>
            </a>
            '''
        
        # Next article
        if current_index < len(sorted_articles) - 1:
            next_article = sorted_articles[current_index + 1]
            html += f'''
            <a href="{{base_path}}/articles/{next_article['slug']}.html" class="nav-next">
                <span class="nav-label">הבא →</span>
                <span class="nav-title">{next_article['title']}</span>
            </a>
            '''
        
        html += '</div>'
        return html

    def create_additional_pages(self):
        """Create additional pages like about, contact, etc."""
        
        # About page with full page structure
        about_page_content = '''
    <header class="header">
        <div class="header-content">
            <h1 class="site-title">פרשת השבוע</h1>
            <p class="site-subtitle">חיבור בין חכמת התורה למתמטיקה, מדע הנתונים ובינה מלאכותית</p>
        </div>
    </header>

    <nav class="nav">
        <div class="nav-content">
            <ul class="nav-links">
                <li><a href="{{base_path}}/" class="nav-link">בית</a></li>
                <li><a href="{{base_path}}/archive.html" class="nav-link">ארכיון</a></li>
                <li><a href="{{base_path}}/tags.html" class="nav-link">תגיות</a></li>
                <li><a href="{{base_path}}/about.html" class="nav-link active">אודות</a></li>
            </ul>
        </div>
    </nav>

    <main class="main">
        <div class="content">
            <div class="page-header">
                <h1>אודות הפרויקט</h1>
                <p class="page-subtitle">המטרה והגישה של פרשת השבוע</p>
            </div>
            
            <div class="page-content">
                <section class="content-section">
                    <h2>המטרה</h2>
                    <p>הפרויקט שואף לגלות קשרים מעמיקים ומפתיעים בין הפרשיות השבועיות לבין עקרונות מתמטיים, אלגוריתמים, מודלים סטטיסטיים ותובנות מעולם הבינה המלאכותית.</p>
                    
                    <p>כל שבוע אנחנו חוקרים את פרשת השבוע מזווית מדעית וטכנולוגית מודרנית, וחושפים קשרים מפתיעים בין חכמת התורה לעולם המתמטיקה והטכנולוגיה.</p>
                </section>
                
                <section class="content-section">
                    <h2>הגישה</h2>
                    <p>כל פרשה נבחנת דרך עדשה טכנולוגית ומדעית, תוך חיפוש אחר דפוסים, מבנים לוגיים ועקרונות שיכולים לשמש השראה לפתרונות מודרניים בעולם הטכנולוגיה והחדשנות.</p>
                    
                    <p>המאמרים מתמקדים בנושאים כמו:</p>
                    <ul>
                        <li>מודלים מתמטיים בטקסטים מקראיים</li>
                        <li>עקרונות סטטיסטיים בחכמת המסורת</li>
                        <li>מסגרות אתיות לטכנולוגיה מודרנית</li>
                        <li>תובנות מבוססות נתונים מחכמה עתיקה</li>
                        <li>לקחי מנהיגות דרך עדשה טכנית</li>
                        <li>חשיבה אלגוריתמית בהלכה יהודית</li>
                    </ul>
                </section>
                
                <section class="content-section">
                    <h2>הקהל היעד</h2>
                    <ul>
                        <li>אנשי טכנולוגיה המתעניינים בחכמה יהודית</li>
                        <li>מדעני נתונים ומתמטיקאים</li>
                        <li>מייסדי סטארטאפים ויזמים</li>
                        <li>תלמידי תורה וטכנולוגיה כאחד</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>
    
    ''' + self.generate_footer_html()
        
        about_html = self.templates['base'].replace('{{content}}', about_page_content)
        about_html = about_html.replace('{{page_title}}', 'אודות | פרשת השבוע')
        about_html = about_html.replace('{{description}}', 'אודות פרויקט פרשת השבוע - חיבור בין חכמת התורה למתמטיקה ומדע הנתונים')
        about_html = about_html.replace('{{keywords}}', 'אודות, פרשת השבוע, מתמטיקה, מדע נתונים')
        about_html = about_html.replace('{{author}}', 'אלירן סבג')
        about_html = about_html.replace('{{image_url}}', f'https://Eliran79.github.io{self.base_path}/images/about.png')
        about_html = about_html.replace('{{og_type}}', 'website')
        about_html = about_html.replace('{{canonical_url}}', 'https://Eliran79.github.io/parasha_of_the_week/about.html')
        about_html = about_html.replace('{{article_meta}}', '')
        about_html = about_html.replace('{{extra_head}}', '')
        about_html = about_html.replace('{{extra_scripts}}', '')
        
        # Apply base path to all links
        about_html = self.apply_base_path(about_html)
        
        with open(self.output_dir / "about.html", 'w', encoding='utf-8') as f:
            f.write(about_html)
        
        # Contact page with full page structure
        contact_page_content = '''
    <header class="header">
        <div class="header-content">
            <h1 class="site-title">פרשת השבוע</h1>
            <p class="site-subtitle">חיבור בין חכמת התורה למתמטיקה, מדע הנתונים ובינה מלאכותית</p>
        </div>
    </header>

    <nav class="nav">
        <div class="nav-content">
            <ul class="nav-links">
                <li><a href="{{base_path}}/" class="nav-link">בית</a></li>
                <li><a href="{{base_path}}/archive.html" class="nav-link">ארכיון</a></li>
                <li><a href="{{base_path}}/tags.html" class="nav-link">תגיות</a></li>
                <li><a href="{{base_path}}/about.html" class="nav-link">אודות</a></li>
            </ul>
        </div>
    </nav>

    <main class="main">
        <div class="content">
            <div class="page-header">
                <h1>צור קשר</h1>
                <p class="page-subtitle">יש לך רעיון למאמר? שאלה? הערה? נשמח לשמוע!</p>
            </div>
            
            <div class="page-content">
                <section class="content-section">
                    <h2>אלירן סבג (Eliran Sabag)</h2>
                    <p>מחבר ויוצר פרויקט פרשת השבוע</p>
                    
                    <div class="contact-info">
                        <div class="contact-item">
                            <strong>📧 אימייל:</strong>
                            <a href="mailto:eliran.sbg@gmail.com">eliran.sbg@gmail.com</a>
                        </div>
                        
                        <div class="contact-item">
                            <strong>💼 LinkedIn:</strong>
                            <a href="https://www.linkedin.com/in/eliran-sabag-51832651/" target="_blank" rel="noopener">Eliran Sabag</a>
                        </div>
                        
                        <div class="contact-item">
                            <strong>📂 GitHub:</strong>
                            <a href="https://github.com/Eliran79/parasha_of_the_week" target="_blank" rel="noopener">parasha-week</a>
                        </div>
                    </div>
                </section>
                
                <section class="content-section">
                    <h2>תרומות וחיבור</h2>
                    <p>הפרויקט מקבל בברכה:</p>
                    <ul>
                        <li>רעיונות למאמרים חדשים</li>
                        <li>הצעות לשיפור טכני</li>
                        <li>משוב על התוכן הקיים</li>
                        <li>תרומות קוד ב-GitHub</li>
                        <li>שיתופי הפוסטים ברשתות החברתיות</li>
                    </ul>
                </section>
                
                <section class="content-section">
                    <h2>הזמנה לשיתוף</h2>
                    <p>מוזמנים לשתף את המאמרים, לתת כוכבית ב-GitHub, ולהמליץ לחברים שאוהבים חיבורים מעניינים בין עולמות!</p>
                </section>
            </div>
        </div>
    </main>
    
    ''' + self.generate_footer_html()
        
        contact_html = self.templates['base'].replace('{{content}}', contact_page_content)
        contact_html = contact_html.replace('{{page_title}}', 'צור קשר | פרשת השבוע')
        contact_html = contact_html.replace('{{description}}', 'יצירת קשר עם אלירן סבג, יוצר פרויקט פרשת השבוע')
        contact_html = contact_html.replace('{{keywords}}', 'צור קשר, אלירן סבג, פרשת השבוע')
        contact_html = contact_html.replace('{{author}}', 'אלירן סבג')
        contact_html = contact_html.replace('{{image_url}}', f'https://Eliran79.github.io{self.base_path}/images/contact.png')
        contact_html = contact_html.replace('{{og_type}}', 'website')
        contact_html = contact_html.replace('{{canonical_url}}', 'https://Eliran79.github.io/parasha_of_the_week/contact.html')
        contact_html = contact_html.replace('{{article_meta}}', '')
        contact_html = contact_html.replace('{{extra_head}}', '')
        contact_html = contact_html.replace('{{extra_scripts}}', '')
        
        # Apply base path to all links
        contact_html = self.apply_base_path(contact_html)
        
        with open(self.output_dir / "contact.html", 'w', encoding='utf-8') as f:
            f.write(contact_html)
        
        # Generate archive page
        self.render_archive_page()
        
        # Generate tags page
        self.render_tags_page()

    def render_archive_page(self):
        """Generate the archive page with all articles organized by year"""
        # Group articles by year
        articles_by_year = {}
        for article in self.articles:
            year = article.get('year', 2025)
            if year not in articles_by_year:
                articles_by_year[year] = []
            articles_by_year[year].append(article)
        
        # Sort years in descending order
        sorted_years = sorted(articles_by_year.keys(), reverse=True)
        
        # Generate archive articles HTML
        archive_articles_html = ''
        
        for year in sorted_years:
            year_articles = sorted(articles_by_year[year], key=lambda x: x.get('date', ''), reverse=True)
            archive_articles_html += f'''
            <div class="year-section">
                <h2 class="year-header">{year}</h2>
                <div class="year-articles">
            '''
            
            for article in year_articles:
                archive_articles_html += f'''
                <div class="archive-article">
                    <div class="archive-article-content">
                        <h3><a href="{{{{base_path}}}}/articles/{article['slug']}.html">{article['title']}</a></h3>
                        <p class="archive-excerpt">{article['excerpt'][:100]}...</p>
                        <div class="archive-meta">
                            <span class="archive-date">{self.format_date(article.get('date', ''))}</span>
                            <span class="archive-parasha">פרשת {article.get('parasha', '')}</span>
                        </div>
                    </div>
                </div>
                '''
            
            archive_articles_html += '</div></div>'
        
        # Generate archive page content with full structure including header and footer
        archive_page_content = '''
    <header class="header">
        <div class="header-content">
            <h1 class="site-title">פרשת השבוע</h1>
            <p class="site-subtitle">חיבור בין חכמת התורה למתמטיקה, מדע הנתונים ובינה מלאכותית</p>
        </div>
    </header>

    <nav class="nav">
        <div class="nav-content">
            <ul class="nav-links">
                <li><a href="{{base_path}}/" class="nav-link">בית</a></li>
                <li><a href="{{base_path}}/archive.html" class="nav-link active">ארכיון</a></li>
                <li><a href="{{base_path}}/tags.html" class="nav-link">תגיות</a></li>
                <li><a href="{{base_path}}/about.html" class="nav-link">אודות</a></li>
            </ul>
        </div>
    </nav>

    <main class="main">
        <div class="content">
            <div class="archive-container">
                <h1>ארכיון מאמרים</h1>
                <p class="archive-intro">כל המאמרים מאורגנים לפי שנים</p>
                
                ''' + archive_articles_html + '''
            </div>
        </div>
    </main>
    
    ''' + self.generate_footer_html()
        
        # Apply to base template
        archive_html = self.templates['base'].replace('{{content}}', archive_page_content)
        archive_html = archive_html.replace('{{page_title}}', 'ארכיון | פרשת השבוע')
        archive_html = archive_html.replace('{{description}}', 'ארכיון כל המאמרים בפרשת השבוע')
        archive_html = archive_html.replace('{{keywords}}', 'ארכיון, פרשות, מאמרים')
        archive_html = archive_html.replace('{{author}}', 'אלירן סבג')
        archive_html = archive_html.replace('{{image_url}}', f'https://Eliran79.github.io{self.base_path}/images/archive.png')
        archive_html = archive_html.replace('{{og_type}}', 'website')
        archive_html = archive_html.replace('{{canonical_url}}', 'https://Eliran79.github.io/parasha_of_the_week/archive.html')
        archive_html = archive_html.replace('{{article_meta}}', '')
        archive_html = archive_html.replace('{{extra_head}}', '')
        archive_html = archive_html.replace('{{extra_scripts}}', '')
        
        # Apply base path to all links
        archive_html = self.apply_base_path(archive_html)
        
        with open(self.output_dir / "archive.html", 'w', encoding='utf-8') as f:
            f.write(archive_html)

    def render_tags_page(self):
        """Generate the tags page with tag cloud and articles by tag"""
        # Collect all tags
        all_tags = {}
        for article in self.articles:
            for tag in article.get('tags', []):
                if tag not in all_tags:
                    all_tags[tag] = []
                all_tags[tag].append(article)
        
        # Sort tags by frequency
        sorted_tags = sorted(all_tags.items(), key=lambda x: len(x[1]), reverse=True)
        
        # Generate tags page content with full structure
        tags_content = '''
    <header class="header">
        <div class="header-content">
            <h1 class="site-title">פרשת השבוע</h1>
            <p class="site-subtitle">חיבור בין חכמת התורה למתמטיקה, מדע הנתונים ובינה מלאכותית</p>
        </div>
    </header>

    <nav class="nav">
        <div class="nav-content">
            <ul class="nav-links">
                <li><a href="{{base_path}}/" class="nav-link">בית</a></li>
                <li><a href="{{base_path}}/archive.html" class="nav-link">ארכיון</a></li>
                <li><a href="{{base_path}}/tags.html" class="nav-link active">תגיות</a></li>
                <li><a href="{{base_path}}/about.html" class="nav-link">אודות</a></li>
            </ul>
        </div>
    </nav>

    <main class="main">
        <div class="content">
            <div class="tags-container">
                <h1>תגיות</h1>
                <p class="tags-intro">מאמרים מאורגנים לפי נושאים</p>
                
                <div class="tag-cloud">
        '''
        
        # Generate tag cloud
        for tag, articles in sorted_tags:
            size_class = 'large' if len(articles) > 3 else 'medium' if len(articles) > 1 else 'small'
            tags_content += f'''
                <a href="#tag-{tag}" class="tag-item {size_class}" data-count="{len(articles)}">
                    {tag} ({len(articles)})
                </a>
            '''
        
        tags_content += '</div>'
        
        # Generate articles by tag
        for tag, articles in sorted_tags:
            tags_content += f'''
            <div class="tag-section" id="tag-{tag}">
                <h2 class="tag-header">{tag} ({len(articles)} מאמרים)</h2>
                <div class="tag-articles">
            '''
            
            for article in articles:
                tags_content += f'''
                <div class="tag-article">
                    <h3><a href="articles/{article['slug']}.html">{article['title']}</a></h3>
                    <p class="tag-excerpt">{article['excerpt'][:120]}...</p>
                    <div class="tag-meta">
                        <span class="tag-date">{self.format_date(article.get('date', ''))}</span>
                        <span class="tag-parasha">פרשת {article.get('parasha', '')}</span>
                    </div>
                </div>
                '''
            
            tags_content += '</div></div>'
        
        tags_content += '''
            </div>
        </div>
    </main>
    
    ''' + self.generate_footer_html()
        
        # Apply to base template
        tags_html = self.templates['base'].replace('{{content}}', tags_content)
        tags_html = tags_html.replace('{{page_title}}', 'תגיות | פרשת השבוע')
        tags_html = tags_html.replace('{{description}}', 'מאמרים מאורגנים לפי תגיות ונושאים')
        tags_html = tags_html.replace('{{keywords}}', 'תגיות, נושאים, פרשות')
        tags_html = tags_html.replace('{{author}}', 'אלירן סבג')
        tags_html = tags_html.replace('{{image_url}}', f'https://Eliran79.github.io{self.base_path}/images/tags.png')
        tags_html = tags_html.replace('{{og_type}}', 'website')
        tags_html = tags_html.replace('{{canonical_url}}', 'https://Eliran79.github.io/parasha_of_the_week/tags.html')
        tags_html = tags_html.replace('{{article_meta}}', '')
        tags_html = tags_html.replace('{{extra_head}}', '')
        tags_html = tags_html.replace('{{extra_scripts}}', '')
        
        # Apply base path to all links
        tags_html = self.apply_base_path(tags_html)
        
        with open(self.output_dir / "tags.html", 'w', encoding='utf-8') as f:
            f.write(tags_html)

    def create_manifest_and_service_worker(self):
        """Create PWA manifest and service worker"""
        
        # PWA Manifest
        manifest = {
            "name": "פרשת השבוע",
            "short_name": "פרשת השבוע", 
            "description": "חיבור בין חכמת התורה למתמטיקה ומדע הנתונים",
            "start_url": "/",
            "display": "standalone",
            "background_color": "#ffffff",
            "theme_color": "#2563eb",
            "lang": "he",
            "dir": "rtl",
            "icons": [
                {
                    "src": "/images/icon-192.png",
                    "sizes": "192x192", 
                    "type": "image/png"
                },
                {
                    "src": "/images/icon-512.png",
                    "sizes": "512x512",
                    "type": "image/png"
                }
            ]
        }
        
        with open(self.output_dir / "manifest.json", 'w', encoding='utf-8') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
        
        # Service Worker
        sw_content = f'''
const CACHE_NAME = 'parasha_of_the_week-v1';
const urlsToCache = [
  '{self.base_path}/',
  '{self.base_path}/assets/css/style.css',
  '{self.base_path}/assets/js/main.js',
  '{self.base_path}/manifest.json'
];

self.addEventListener('install', function(event) {{
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {{
        return cache.addAll(urlsToCache);
      }})
  );
}});

self.addEventListener('fetch', function(event) {{
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {{
        if (response) {{
          return response;
        }}
        return fetch(event.request);
      }})
  );
}});
        '''
        
        with open(self.output_dir / "sw.js", 'w', encoding='utf-8') as f:
            f.write(sw_content)

    def build(self):
        """Enhanced build process"""
        print("🚀 Building Parasha website...")
        
        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Process all markdown files
        print("📝 Processing markdown files...")
        for md_file in self.content_dir.glob("*.md"):
            if md_file.name != "README.md":
                article = self.process_markdown_file(md_file)
                self.articles.append(article)
                print(f"   ✓ {article['title']}")
        
        # Generate individual article pages
        print("📄 Generating article pages...")
        articles_dir = self.output_dir / "articles"
        articles_dir.mkdir(exist_ok=True)
        
        for article in self.articles:
            article_html = self.render_article_page(article)
            with open(articles_dir / f"{article['slug']}.html", 'w', encoding='utf-8') as f:
                f.write(article_html)
            print(f"   ✓ {article['slug']}.html")
        
        # Generate index page
        print("🏠 Generating index page...")
        index_html = self.render_index_page()
        with open(self.output_dir / "index.html", 'w', encoding='utf-8') as f:
            f.write(index_html)
        
        # Create additional pages
        print("📑 Creating additional pages...")
        self.create_additional_pages()
        
        # Copy assets
        print("📁 Copying assets...")
        self.copy_assets()
        
        # Generate feeds
        print("📡 Generating feeds...")
        self.generate_json_feed()
        self.generate_rss_feed()
        
        # Create PWA files
        print("📱 Creating PWA files...")
        self.create_manifest_and_service_worker()
        
        # Generate sitemap
        print("🗺️ Generating sitemap...")
        self.generate_sitemap()
        
        # Generate articles metadata
        with open(self.output_dir / "articles.json", 'w', encoding='utf-8') as f:
            json.dump([{k: v for k, v in article.items() if k != 'content'} 
                      for article in self.articles], f, ensure_ascii=False, indent=2)
        
        print(f"✅ Website built successfully!")
        print(f"📊 Statistics:")
        print(f"   - Articles: {len(self.articles)}")
        print(f"   - Parashot: {len(set(a['parasha'] for a in self.articles))}")
        print(f"   - Tags: {len(set(tag for a in self.articles for tag in a['tags']))}")
        print(f"📂 Output directory: {self.output_dir}")

    def parse_frontmatter(self, content):
        """Parse YAML frontmatter from markdown content"""
        if content.startswith('---'):
            try:
                end_pos = content.find('---', 3)
                if end_pos != -1:
                    frontmatter = yaml.safe_load(content[3:end_pos])
                    body = content[end_pos + 3:].strip()
                    return frontmatter, body
            except yaml.YAMLError as e:
                print(f"Error parsing YAML frontmatter: {e}")
        return {}, content
    
    def find_matching_image(self, filename):
        """Find matching image for article with year-based naming"""
        # Extract parasha name and year from filename
        # Expected: parasha_behar_2025.md or parashat_shalach_2025.md
        stem = Path(filename).stem
        
        # Try different patterns to extract parasha name and year
        patterns = [
            r'parasha_(\w+)_(\d{4})',    # parasha_behar_2025
            r'parashat_(\w+)_(\d{4})',   # parashat_shalach_2025
            r'parasha_(\w+)',            # parasha_behar (no year)
            r'parashat_(\w+)'            # parashat_shalach (no year)
        ]
        
        parasha_name = None
        year = None
        
        for pattern in patterns:
            match = re.match(pattern, stem)
            if match:
                parasha_name = match.group(1)
                if len(match.groups()) > 1:
                    year = match.group(2)
                break
        
        if not parasha_name:
            print(f"Warning: Could not extract parasha name from {filename}")
            return "/images/default.jpg"
        
        # Look for matching images with different naming patterns
        image_patterns = []
        
        if year:
            # Priority patterns with year
            image_patterns.extend([
                f"{parasha_name}_{year}.*",      # behar_2025.jpg
                f"parasha_{parasha_name}_{year}.*",  # parasha_behar_2025.jpg
                f"parashat_{parasha_name}_{year}.*", # parashat_shalach_2025.jpg
            ])
        
        # Fallback patterns without year
        image_patterns.extend([
            f"{parasha_name}.*",             # behar.jpg
            f"parasha_{parasha_name}.*",     # parasha_behar.jpg
            f"parashat_{parasha_name}.*",    # parashat_shalach.jpg
        ])
        
        # Search for matching images
        for pattern in image_patterns:
            matches = list(self.images_dir.glob(f"**/{pattern}"))
            if matches:
                # Return the first match, relative to images directory
                relative_path = matches[0].relative_to(self.images_dir)
                return f"{self.base_path}/images/{relative_path}"
        
        # Default fallback - check if default exists, otherwise use a safe fallback
        if (self.images_dir / "default.jpg").exists():
            print(f"Warning: No matching image found for {filename}, using default")
            return f"{self.base_path}/images/default.jpg"
        else:
            print(f"Warning: No matching image found for {filename}, no default available")
            return "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'%3E%3Crect width='100%25' height='100%25' fill='%23f3f4f6'/%3E%3Ctext x='50%25' y='50%25' font-family='Arial' font-size='16' fill='%23666' text-anchor='middle' dy='.3em'%3ENo Image%3C/text%3E%3C/svg%3E"
    
    def calculate_reading_time(self, content):
        """Calculate estimated reading time in minutes"""
        # Average reading speed: 200 Hebrew words per minute
        word_count = len(content.split())
        return max(1, round(word_count / 200))
    
    def generate_excerpt(self, content, max_length=200):
        """Generate excerpt from content if not provided"""
        # Remove markdown formatting
        text = re.sub(r'[#*`\[\]()]', '', content)
        # Remove Hebrew vowels/diacritics if any
        text = re.sub(r'[\u0591-\u05C7]', '', text)
        
        if len(text) <= max_length:
            return text.strip()
        
        # Find good break point
        truncated = text[:max_length]
        last_space = truncated.rfind(' ')
        if last_space > max_length * 0.8:  # If we found a space in the last 20%
            truncated = truncated[:last_space]
        
        return truncated.strip() + "..."
    
    def process_markdown_file(self, md_file):
        """Process a markdown file and return article data"""
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse frontmatter
        frontmatter, body = self.parse_frontmatter(content)
        
        # Extract filename info
        filename = md_file.name
        slug = md_file.stem
        
        # Find matching image
        image = self.find_matching_image(filename)
        
        # Calculate reading time
        reading_time = self.calculate_reading_time(body)
        
        # Generate excerpt if not provided
        excerpt = frontmatter.get('excerpt')
        if not excerpt:
            excerpt = self.generate_excerpt(body)
        
        # Create article data
        article = {
            'id': slug,
            'slug': slug,
            'title': frontmatter.get('title', 'ללא כותרת'),
            'parasha': frontmatter.get('parasha', 'לא צוין'),
            'date': frontmatter.get('date', datetime.now().strftime('%Y-%m-%d')),
            'tags': frontmatter.get('tags', []),
            'emoji': frontmatter.get('emoji', '📜'),
            'excerpt': excerpt,
            'author': frontmatter.get('author', 'אלירן סבג'),
            'year': frontmatter.get('year', datetime.now().year),
            'image': image,
            'content': body,
            'reading_time': reading_time,
            'filename': filename
        }
        
        return article
    
    def format_date(self, date_str):
        """Format date for display"""
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            # Hebrew months
            months = ['ינואר', 'פברואר', 'מרץ', 'אפריל', 'מאי', 'יוני',
                     'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר']
            return f"{date_obj.day} {months[date_obj.month-1]} {date_obj.year}"
        except:
            return date_str
    
    def generate_tag_cloud(self):
        """Generate HTML for tag cloud"""
        all_tags = {}
        for article in self.articles:
            for tag in article['tags']:
                all_tags[tag] = all_tags.get(tag, 0) + 1
        
        if not all_tags:
            return '<p>אין תגיות זמינות</p>'
        
        # Sort by frequency
        sorted_tags = sorted(all_tags.items(), key=lambda x: x[1], reverse=True)[:15]
        
        tag_html = '<div class="tag-cloud">'
        for tag, count in sorted_tags:
            size_class = 'tag-large' if count > 3 else 'tag-medium' if count > 1 else 'tag-small'
            tag_html += f'<a href="{{base_path}}/tags.html#tag-{tag}" class="tag {size_class}">#{tag} ({count})</a>'
        tag_html += '</div>'
        
        return tag_html
    
    def generate_recent_articles(self):
        """Generate HTML for recent articles"""
        recent = sorted(self.articles, key=lambda x: x['date'], reverse=True)[:5]
        
        html = '<ul class="recent-articles">'
        for article in recent:
            html += f'''
            <li class="recent-article">
                <a href="{{base_path}}/articles/{article['slug']}.html" class="recent-article-link">
                    <span class="recent-article-emoji">{article['emoji']}</span>
                    <div class="recent-article-content">
                        <span class="recent-article-title">{article['title']}</span>
                        <span class="recent-article-date">{self.format_date(article['date'])}</span>
                    </div>
                </a>
            </li>'''
        html += '</ul>'
        
        return html
    
    def copy_assets(self):
        """Copy assets to output directory"""
        # Create assets directories
        (self.output_dir / "assets" / "css").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "assets" / "js").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "images").mkdir(parents=True, exist_ok=True)
        
        # Copy CSS
        css_source = Path("assets/css/style.css")
        if css_source.exists():
            shutil.copy2(css_source, self.output_dir / "assets" / "css" / "style.css")
        
        # Copy and process JS (replace hardcoded paths with base_path)
        js_source = Path("assets/js/main.js")
        if js_source.exists():
            with open(js_source, 'r', encoding='utf-8') as f:
                js_content = f.read()
            
            # Replace hardcoded paths with base_path
            js_content = js_content.replace("'/articles.json'", f"'{self.base_path}/articles.json'")
            js_content = js_content.replace('"/articles/', f'"{self.base_path}/articles/')
            js_content = js_content.replace("'/sw.js'", f"'{self.base_path}/sw.js'")
            
            with open(self.output_dir / "assets" / "js" / "main.js", 'w', encoding='utf-8') as f:
                f.write(js_content)
        
        # Copy images
        if self.images_dir.exists():
            for img_file in self.images_dir.iterdir():
                if img_file.is_file():
                    shutil.copy2(img_file, self.output_dir / "images" / img_file.name)
    
    def generate_json_feed(self):
        """Generate JSON feed"""
        feed = {
            "version": "https://jsonfeed.org/version/1.1",
            "title": "פרשת השבוע",
            "description": "חיבור בין פרשיות התורה למתמטיקה, מדע הנתונים ובינה מלאכותית",
            "home_page_url": "https://Eliran79.github.io/parasha_of_the_week/",
            "feed_url": "https://Eliran79.github.io/parasha_of_the_week/feed.json",
            "language": "he",
            "items": []
        }
        
        # Add articles to feed (latest 20)
        latest_articles = sorted(self.articles, key=lambda x: x['date'], reverse=True)[:20]
        for article in latest_articles:
            feed["items"].append({
                "id": f"https://Eliran79.github.io/parasha_of_the_week{{base_path}}/articles/{article['slug']}.html",
                "url": f"https://Eliran79.github.io/parasha_of_the_week{{base_path}}/articles/{article['slug']}.html",
                "title": article['title'],
                "content_html": markdown.markdown(article['content'], extensions=['codehilite', 'tables', 'toc', 'fenced_code']),
                "summary": article['excerpt'],
                "date_published": f"{article['date']}T00:00:00Z",
                "tags": article['tags'],
                "author": {
                    "name": article['author']
                }
            })
        
        with open(self.output_dir / "feed.json", 'w', encoding='utf-8') as f:
            json.dump(feed, f, ensure_ascii=False, indent=2)
    
    def generate_rss_feed(self):
        """Generate RSS XML feed"""
        latest_articles = sorted(self.articles, key=lambda x: x['date'], reverse=True)[:20]
        
        rss_content = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>פרשת השבוע</title>
    <description>חיבור בין פרשיות התורה למתמטיקה, מדע הנתונים ובינה מלאכותית</description>
    <link>https://Eliran79.github.io/parasha_of_the_week/</link>
    <language>he</language>
    <atom:link href="https://Eliran79.github.io/parasha_of_the_week/feed.xml" rel="self" type="application/rss+xml"/>
'''
        
        for article in latest_articles:
            rss_content += f'''
    <item>
        <title>{article['title']}</title>
        <description>{article['excerpt']}</description>
        <link>https://Eliran79.github.io/parasha_of_the_week{{base_path}}/articles/{article['slug']}.html</link>
        <guid>https://Eliran79.github.io/parasha_of_the_week{{base_path}}/articles/{article['slug']}.html</guid>
        <pubDate>{article['date']}</pubDate>
        <author>{article['author']}</author>
    </item>'''
        
        rss_content += '''
</channel>
</rss>'''
        
        with open(self.output_dir / "feed.xml", 'w', encoding='utf-8') as f:
            f.write(rss_content)
    
    def generate_sitemap(self):
        """Generate XML sitemap"""
        sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://Eliran79.github.io/parasha_of_the_week/</loc>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://Eliran79.github.io/parasha_of_the_week/archive.html</loc>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://Eliran79.github.io/parasha_of_the_week/about.html</loc>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>
'''
        
        for article in self.articles:
            sitemap_content += f'''
    <url>
        <loc>https://Eliran79.github.io/parasha_of_the_week{{base_path}}/articles/{article['slug']}.html</loc>
        <lastmod>{article['date']}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>'''
        
        sitemap_content += '''
</urlset>'''
        
        with open(self.output_dir / "sitemap.xml", 'w', encoding='utf-8') as f:
            f.write(sitemap_content)

if __name__ == "__main__":
    builder = ParashaWebsiteBuilder()
    builder.build()
