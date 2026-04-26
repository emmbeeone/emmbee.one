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
   - Standard anchor tags are used (`<a href="directory/">...</a>`). Subpages use their own directories with `index.html`.
4. **Form Logic & Leads:**
   - **Web3Forms:** Active lead capture (Key: `5b17f4f9-ab49-4755-9afa-2882fb0be379`).
5. **Analytics:**
   - **GA4:** `gtag` must be on all pages. Use descriptive labels (e.g., `'Lead Form FAQs'`).

## Previous Refactoring Notes
- **Lead Generation Deployment:** Standardized the "Stress Buster Kit" site-wide via exit-intent.
- **Conversion Tracking:** Live for `stress_buster_view`, `stress_buster_download`, `whatsapp_share_viral`, and `gap_checker_click`.
- **Stabilization:** Cleared deep structural duplicates in `faqs/index.html`.
- **Local SEO:** Deployed standardized JSON-LD schema for Dehradun tutoring/mentoring keywords.

## Handover State
- **Lead Magnet Hierarchy:** **Gap Checker** is the High-Value Primary Magnet. **Stress Buster Kit** is the Low-Friction Entry Point.
- **Critical Keys:** Web3Forms API Key is embedded and should not be modified.
- **Testing Mode:** Append `?test=1` to ignore session storage flags for modal testing.

## Agent Instructions:
- **Resumption:** Read `DEVELOPER_HANDBOOK.md` sections 8-11 immediately upon start.
- **Standardization:** Maintain the "Apple-style" aesthetics and relative pathing for all new sub-pages.
- **Analytics:** Ensure every new lead capture point includes a descriptive `event_label` for the source page.
