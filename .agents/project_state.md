---
description: EmmBee.One Agent Memory and Context State
---

# Project Context for AI Agents

## Overview
This file contains the persistent context and instruction memory for AI Agents (such as Antigravity/Cursor) working on the `emmbee.one` project. Read this to understand the project rapidly when resuming development.

## Project Details
- **Name:** EmmBee.One
- **Type:** Multi-page Static HTML/CSS Website
- **Hosting:** GitHub Pages
- **Target Audience:** Parents and students of CBSE classes 8-10 seeking high-end academic mentoring in Dehradun.

## Technical Rules & Conventions
1. **No Frontend Frameworks:** Do NOT introduce React, Vue, Next.js, or Webpack unless explicitly instructed by the USER. Keep it static HTML, Vanilla Javascript, and Tailwind (via CDN).
2. **Styling Approach:**
   - Tailwind is used for layout and typography.
   - Complex effects (glassmorphism, gradient shadows, fixed backgrounds) must be defined in `css/styles.css`.
   - Never use ad-hoc inline styles unless absolutely necessary.
3. **Routing:**
   - Standard anchor tags are used (`<a href="directory/">...</a>`).
   - GitHub pages requires relative pathing for local dev to match production. Subpages are housed in their own directories containing an `index.html` file (e.g., `success-stories/index.html`).
4. **Third-Party Integrations:**
   - **Google Analytics:** `gtag` must be strictly present in the `<head>` of all `index.html` pages.
   - **Calendly:** The booking widget script and CSS are globally linked.

## Previous Refactoring Notes
- Converted a single tall index.html into a multi-page site.
- Handled Apple-like minimalistic visual tweaks, fixing zoom bugs, and resolving 404 paths for static publishing.
- Applied "Phoenix" watermarking graphics and specific QR code designs.

## Where We Left Off
- Development paused by the USER. The website is in a stable, multi-page format. All UX/UI refinements and Contact Hub standardization have been completed.
- To continue, monitor if adding new pages like "About" or additional blog posts requires CMS architecture, though currently static is preferred.

## Agent Instructions:
- Always read the `DEVELOPER_HANDBOOK.md` in the root folder alongside this.
- If requested to add a new page, duplicate an existing sub-page directory (like `faqs/`), clear the content, and use the existing header/footer elements. Ensure paths to `../css/styles.css` and `../images/` remain valid.
