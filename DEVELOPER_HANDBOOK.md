# EmmBee.One - Developer Handbook

Welcome to the EmmBee.One repository! This document is created to help the next developer (or AI agent) onboard quickly and understand the current state, architecture, and design principles of the project.

## 1. Project Overview
EmmBee.One is a static website (HTML/CSS) for a boutique academic mentoring studio in Dehradun. The project was recently migrated from a single-page site to a multi-page site structure. It is currently hosted on GitHub Pages.

## 2. Tech Stack & Architecture
- **Core Strategy:** Static HTML files with shared CSS. No complex build tools (Webpack/Vite) are used to keep it simple and hostable directly.
- **Styling:** 
  - Tailwind CSS via CDN (referenced in `<head>`).
  - Vanilla CSS in `css/styles.css` for custom animations, glassmorphism, glowing effects, and shared styles across pages.
- **Fonts:** Google Fonts (Inter for sans-serif, Playfair Display for serif).
- **Analytics & Booking:** Google Analytics (gtag) and Calendly widget integration.

## 3. Directory Structure
```
emmbee.one/
├── css/
│   └── styles.css                 # Main stylesheet loaded by all pages
├── images/                        # Optimised WebP images and logos
├── competency-based-education/    # Subpage (Blog/Article)
├── faqs/                          # FAQs Subpage
├── mentor/                        # Meet the Mentor Subpage
├── studio/                        # Learning Studio Subpage
├── success-stories/               # Success Stories Subpage
├── tools/                         # Helper tools or assets
├── raw-data/                      # Original uncompressed assets / scripts
├── index.html                     # Main Landing Page
├── sitemap.xml                    # SEO Sitemap
├── robots.txt                     # SEO Robots config
├── build_assets.py                # Optional python script for asset generation
└── compress.py                    # Script to compress images to WebP
```

## 4. Key Design Principles (Aesthetics)
- **Theme:** "Apple-like" minimal and premium design, heavily utilizing a "Persian Blue" (`#1C3F60`, `#0a192f`) and "Gold" (`#D4AF37`) color palette.
- **UI Elements:** Glassmorphism (`.glass-card`), gold glowing text (`.gold-gradient-text`, `.sanskrit-glow`), drop shadows, and subtle background blurs.
- **Responsiveness:** Ensure consistent spacing and logic on mobile vs desktop. Navigation uses a hamburger menu on mobile.

## 5. Development Workflow
- When adding a new page, create a new directory (e.g., `new-page/`) and add `index.html` inside it so the URL pathway remains clean (`emmbee.one/new-page/`).
- Make sure to add `../css/styles.css` for shared styling in subpages.
- Python scripts (`compress.py`) can be used to process images if you add new visual assets. All images should ideally be WebP for modern performance.
- Any new interactive scripts should ideally rely on vanilla JavaScript within or referenced by the HTML files.
- Google Analytics is required on every page.

## 6. Current Status & Next Steps
- Development is currently paused. 
- The site successfully transitioned to multiple pages. Common elements like navigation, footers, and the Contact Hub are standardized.
- **Future Actions:** If resuming, check on adding dynamic/CMS content if limits of static HTML are reached, or continue expanding individual articles under `competency-based-education`.
