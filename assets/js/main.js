// assets/js/main.js
// Interactive features for Parasha website

class ParashaWebsite {
    constructor() {
        this.articles = [];
        this.searchInput = null;
        this.init();
    }

    async init() {
        await this.loadArticles();
        this.setupEventListeners();
        this.setupSearch();
        this.setupLazyLoading();
        this.setupScrollEffects();
        this.setupAnalytics();
    }

    // Load articles data
    async loadArticles() {
        try {
            const response = await fetch('/articles.json');
            this.articles = await response.json();
        } catch (error) {
            console.warn('Could not load articles data:', error);
            this.articles = [];
        }
    }

    // Setup event listeners
    setupEventListeners() {
        // Mobile menu toggle
        this.setupMobileMenu();
        
        // Smooth scrolling for anchor links
        this.setupSmoothScrolling();
        
        // Back to top button
        this.setupBackToTop();
        
        // External link handling
        this.setupExternalLinks();
        
        // Keyboard navigation
        this.setupKeyboardNavigation();
    }

    // Setup search functionality
    setupSearch() {
        this.searchInput = document.getElementById('search-input');
        if (!this.searchInput) return;

        let searchTimeout;
        this.searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                this.performSearch(e.target.value);
            }, 300);
        });

        // Clear search on escape
        this.searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.clearSearch();
            }
        });
    }

    // Perform search
    performSearch(query) {
        if (!query.trim()) {
            this.showAllArticles();
            return;
        }

        const searchTerms = query.toLowerCase().trim().split(/\s+/);
        const filteredArticles = this.articles.filter(article => {
            const searchableText = [
                article.title,
                article.parasha,
                article.excerpt,
                ...(article.tags || [])
            ].join(' ').toLowerCase();

            return searchTerms.every(term => searchableText.includes(term));
        });

        this.displaySearchResults(filteredArticles, query);
    }

    // Display search results
    displaySearchResults(articles, query) {
        const articlesGrid = document.getElementById('articles-grid');
        if (!articlesGrid) return;

        if (articles.length === 0) {
            articlesGrid.innerHTML = `
                <div class="no-results">
                    <h3>לא נמצאו תוצאות עבור "${query}"</h3>
                    <p>נסה לחפש במילים אחרות או בדוק את האיות</p>
                    <button onclick="parashaWebsite.clearSearch()" class="btn-primary">נקה חיפוש</button>
                </div>
            `;
            return;
        }

        const articlesHtml = articles.map(article => this.createArticleCard(article)).join('');
        articlesGrid.innerHTML = articlesHtml;
        
        // Highlight search terms
        this.highlightSearchTerms(query);
    }

    // Create article card HTML
    createArticleCard(article) {
        return `
            <article class="article-card" data-article-id="${article.id}">
                <div class="article-image" style="background-image: url('${article.image || ''}')">
                    <span class="article-emoji">${article.emoji || '📖'}</span>
                </div>
                <div class="article-content">
                    <div class="article-meta">
                        <span class="parasha-tag">${article.parasha}</span>
                        <span>${this.formatDate(article.date)}</span>
                    </div>
                    <h2 class="article-title">
                        <a href="/articles/${article.slug}.html">${article.title}</a>
                    </h2>
                    <p class="article-excerpt">${article.excerpt}</p>
                    <a href="/articles/${article.slug}.html" class="read-more">
                        קרא עוד ←
                    </a>
                </div>
            </article>
        `;
    }

    // Highlight search terms
    highlightSearchTerms(query) {
        if (!query.trim()) return;

        const terms = query.toLowerCase().split(/\s+/);
        const textElements = document.querySelectorAll('.article-title, .article-excerpt');

        textElements.forEach(element => {
            let html = element.innerHTML;
            terms.forEach(term => {
                const regex = new RegExp(`(${this.escapeRegex(term)})`, 'gi');
                html = html.replace(regex, '<mark>$1</mark>');
            });
            element.innerHTML = html;
        });
    }

    // Escape regex special characters
    escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    // Clear search
    clearSearch() {
        if (this.searchInput) {
            this.searchInput.value = '';
        }
        this.showAllArticles();
    }

    // Show all articles
    showAllArticles() {
        const articlesGrid = document.getElementById('articles-grid');
        if (!articlesGrid || this.articles.length === 0) return;

        const articlesHtml = this.articles.map(article => this.createArticleCard(article)).join('');
        articlesGrid.innerHTML = articlesHtml;
    }

    // Setup lazy loading for images
    setupLazyLoading() {
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        imageObserver.unobserve(img);
                    }
                });
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }
    }

    // Setup scroll effects
    setupScrollEffects() {
        let lastScrollTop = 0;
        const nav = document.querySelector('.nav');
        
        window.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            // Hide/show navigation on scroll
            if (nav) {
                if (scrollTop > lastScrollTop && scrollTop > 100) {
                    nav.style.transform = 'translateY(-100%)';
                } else {
                    nav.style.transform = 'translateY(0)';
                }
            }
            
            lastScrollTop = scrollTop;
        }, { passive: true });

        // Parallax effect for hero images
        const heroImages = document.querySelectorAll('.article-hero-image');
        heroImages.forEach(img => {
            window.addEventListener('scroll', () => {
                const scrolled = window.pageYOffset;
                const parallax = scrolled * 0.5;
                img.style.transform = `translateY(${parallax}px)`;
            }, { passive: true });
        });
    }

    // Setup mobile menu
    setupMobileMenu() {
        // Add mobile menu button if needed
        const nav = document.querySelector('.nav-content');
        if (window.innerWidth <= 768 && nav) {
            const menuButton = document.createElement('button');
            menuButton.className = 'mobile-menu-button';
            menuButton.innerHTML = '☰';
            menuButton.addEventListener('click', () => {
                nav.classList.toggle('mobile-menu-open');
            });
            nav.prepend(menuButton);
        }
    }

    // Setup smooth scrolling
    setupSmoothScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // Setup back to top button
    setupBackToTop() {
        const backToTop = document.createElement('button');
        backToTop.className = 'back-to-top';
        backToTop.innerHTML = '↑';
        backToTop.title = 'חזרה למעלה';
        backToTop.style.cssText = `
            position: fixed;
            bottom: 20px;
            left: 20px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: var(--primary-color);
            color: white;
            border: none;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 1000;
            font-size: 20px;
        `;

        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        document.body.appendChild(backToTop);

        // Show/hide back to top button
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTop.style.opacity = '1';
            } else {
                backToTop.style.opacity = '0';
            }
        });
    }

    // Setup external links
    setupExternalLinks() {
        document.querySelectorAll('a[href^="http"]').forEach(link => {
            if (!link.href.includes(window.location.hostname)) {
                link.target = '_blank';
                link.rel = 'noopener noreferrer';
                link.title = link.title || 'קישור חיצוני (נפתח בחלון חדש)';
            }
        });
    }

    // Setup keyboard navigation
    setupKeyboardNavigation() {
        document.addEventListener('keydown', (e) => {
            // ESC to close search
            if (e.key === 'Escape' && this.searchInput) {
                this.clearSearch();
                this.searchInput.blur();
            }
            
            // Ctrl/Cmd + K to focus search
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                if (this.searchInput) {
                    this.searchInput.focus();
                }
            }
        });
    }

    // Setup analytics (privacy-friendly)
    setupAnalytics() {
        // Track page views without personal data
        if (window.location.hostname !== 'localhost') {
            this.trackPageView();
        }
        
        // Track search queries (without personal info)
        if (this.searchInput) {
            this.searchInput.addEventListener('input', 
                this.debounce((e) => {
                    if (e.target.value.length > 2) {
                        this.trackSearch(e.target.value.length);
                    }
                }, 1000)
            );
        }
    }

    // Track page view
    trackPageView() {
        // Simple analytics without cookies or personal data
        const data = {
            page: window.location.pathname,
            timestamp: new Date().toISOString(),
            language: document.documentElement.lang
        };
        
        // Send to your analytics endpoint
        // fetch('/analytics/pageview', { method: 'POST', body: JSON.stringify(data) });
    }

    // Track search (only query length for privacy)
    trackSearch(queryLength) {
        const data = {
            event: 'search',
            queryLength: queryLength,
            timestamp: new Date().toISOString()
        };
        
        // Send to your analytics endpoint
        // fetch('/analytics/search', { method: 'POST', body: JSON.stringify(data) });
    }

    // Utility functions
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    formatDate(dateStr) {
        try {
            const date = new Date(dateStr);
            return date.toLocaleDateString('he-IL', { 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
            });
        } catch {
            return dateStr;
        }
    }

    // Share functionality
    shareArticle(title, url) {
        if (navigator.share) {
            navigator.share({
                title: title,
                url: url
            });
        } else {
            // Fallback to copy URL
            navigator.clipboard.writeText(url).then(() => {
                this.showNotification('הקישור הועתק ללוח');
            });
        }
    }

    // Show notification
    showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--primary-color);
            color: white;
            padding: 1rem 2rem;
            border-radius: 8px;
            z-index: 1000;
            opacity: 0;
            transition: opacity 0.3s;
        `;
        
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => notification.style.opacity = '1', 100);
        
        // Remove after 3 seconds
        setTimeout(() => {
            notification.style.opacity = '0';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }

    // Print article functionality
    printArticle() {
        window.print();
    }

    // Toggle dark mode
    toggleDarkMode() {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('darkMode', 
            document.body.classList.contains('dark-mode') ? 'enabled' : 'disabled'
        );
    }

    // Initialize dark mode from user preference
    initDarkMode() {
        const darkMode = localStorage.getItem('darkMode');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        
        if (darkMode === 'enabled' || (darkMode === null && prefersDark)) {
            document.body.classList.add('dark-mode');
        }
    }
}

// Initialize website when DOM is loaded
let parashaWebsite;

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        parashaWebsite = new ParashaWebsite();
    });
} else {
    parashaWebsite = new ParashaWebsite();
}

// Service Worker registration for offline support
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then((registration) => {
                console.log('SW registered: ', registration);
            })
            .catch((registrationError) => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Make functions available globally for inline event handlers
window.parashaWebsite = parashaWebsite;
window.shareArticle = (title, url) => parashaWebsite?.shareArticle(title, url);
window.printArticle = () => parashaWebsite?.printArticle();
window.toggleDarkMode = () => parashaWebsite?.toggleDarkMode();

// Performance monitoring
window.addEventListener('load', () => {
    if (window.performance && window.performance.timing) {
        const loadTime = window.performance.timing.loadEventEnd - 
                        window.performance.timing.navigationStart;
        console.log(`Page loaded in ${loadTime}ms`);
    }
});
