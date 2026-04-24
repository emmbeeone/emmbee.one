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
- Converted to multi-page site; fixed Apple-like aesthetics and 404 paths.
- **Lead Gen Site-Wide:** Deployed "Stress Buster Kit" exit-intent modal globally.
- **Stabilization:** Cleaned structural corruption in `faqs/index.html`.
- **Local SEO:** Standardized `LocalBusiness` JSON-LD schema for Dehradun keywords.

## Where We Left Off
- The site is live with an active lead funnel.
- **Lead Asset Hierarchy:** **Gap Checker** (Primary Lead Magnet) vs. **Stress Buster Kit** (Value-Add Gift).
- **Current Goal:** Monitor GA4 events (`stress_buster_view`, `stress_buster_download`) and verify the latest CBSE 2026 pattern alignment in lead assets.

## Agent Instructions:
- Read `DEVELOPER_HANDBOOK.md` and this state file before any changes.
- Form event capture MUST use GA4 names as documented in the handbook.
