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

## 6. Lead Generation & Analytics
- **Primary Lead Magnet:** [CBSE Foundation Gap Checker](https://www.emmbee.one/gap-checker/) — A high-intent diagnostic tool (interactive test) that captures student data and delivers reports.
- **Value-Add (Gift):** [Stress Buster Kit](https://www.emmbee.one/downloads/Stress_Buster_Kit.pdf) — A low-friction PDF magnet triggered via site-wide **Exit Intent**.
- **Exit Intent Logic:**
  - Desktop: Triggers when mouse leaves the top of the viewport.
  - Mobile: Triggers at 75% scroll depth.
  - Persistence: Managed via `sessionStorage` (flag: `emmbee_kit_seen`) to show only once per session.
- **Form Automation:** Uses **Web3Forms** (Production Key: `5b17f4f9-ab49-4755-9afa-2882fb0be379`).
- **Event Tracking (GA4):**
  - `stress_buster_view`: Modal displayed.
  - `stress_buster_download`: Successful form submission.
  - `whatsapp_share_viral`: Clicks on the viral sharing features in the modal.
  - `gap_checker_click`: Clicks on the diagnostic tool.

## 8. Maintenance & Testing
- **Bypassing Persistence:** To test the exit-intent modal without clearing `sessionStorage`, append `?test=1` to any URL. This ignores the `emmbee_kit_seen` flag.
- **Form Verification:** Forms are linked to Web3Forms. Test submissions will consume credits on the production key (`5b17f4f9-ab49-4755-9afa-2882fb0be379`). Use the browser console to verify 200 OK responses from `https://api.web3forms.com/submit`.
- **Structural Integrity:** If editing sub-pages, ensure the `</body>` tag is preceded by the singular modal and script blocks. Avoid duplicating the "Stress Buster Kit" code; refer to `faqs/index.html` for the "Definitive Implementation" structure.

## 9. Localhost vs. Production
- **Pathing:** All assets (CSS, Images) must use **relative paths** (e.g., `../css/styles.css`). Absolute paths (e.g., `/css/styles.css`) will break on GitHub Pages due to the sub-directory hosting structure.
- **CNAME:** The site uses a custom domain `www.emmbee.one`. Ensure the `CNAME` file in the root is never deleted.

## 10. Asset Workflow
- **Images:** All new images should be processed via `compress.py` to convert to WebP at 80% quality. 
- **SEO Schema:** Each `index.html` contains `LocalBusiness` and `BreadcrumbList` (where applicable) schema. Standardize any new page by copying the `<script type="application/ld+json">` block from `index.html`.

## 11. Handover Checklist
- [ ] Verify `gtag` is receiving events from the new sub-page.
- [ ] Check mobile responsiveness of the exit intent modal (75% scroll).
- [ ] Ensure all internal links use the trailing slash (e.g., `href="mentor/"`) for GitHub Pages compatibility.
- [ ] Validate that the Lead Form is sending data to the unified `Web3Forms` key.
