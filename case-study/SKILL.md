---
name: case-study
description: "Generate professional Case Study PDF documents as portrait A4 slide decks for any business. Use this skill whenever the user wants to create a case study, client success story, project results document, campaign performance report, or any results-focused PDF showcasing work done for a client. Also trigger when the user provides stats, metrics, campaign results, or a content document and asks for a case study, success story, results deck, or client showcase. Handles the full pipeline: brand extraction from client website, content sourcing, stock image sourcing, HTML slide build, and Puppeteer PDF export."
---

# Case Study Skill — Client Success Story PDF Generator v2

> This skill generates a premium, data-dense Case Study PDF in portrait A4 format.
> Design reference: the Andersen IT case study — rich stat layouts, multi-colored feature badges,
> script accent typography, industry breakdown tables, gradient banners, and two-logo cover treatment.
> Branding is ALWAYS from Automate Accelerator (the presenting company).
> Client brand colors are used only for accent variety within the AA design system.

---

## INPUTS REQUIRED

| Input | Source | Required? |
|-------|--------|-----------|
| Client Website URL | User-provided | Strongly recommended |
| Content Document | PDF, doc, markdown, or inline text | Primary content source |
| Client Name | Extracted from sources | Required |
| Key Stats/Metrics | From content document | Required (at least 6-10 stats) |

---

## BRANDING RULES (CRITICAL)

**The case study is ALWAYS branded as Automate Accelerator.**

1. **Run `/brand-guide-extractor` on automateaccelerator.com FIRST** to get AA's brand assets (logo SVG, colors, fonts)
2. AA brand tokens are the PRIMARY design system — dark navy bg, orange accent, Roboto/Rubik fonts
3. Client brand is used ONLY for: client logo on cover, accent variety in feature badges
4. AA logo appears on: cover (top-left), every page footer, and closing page (centered)
5. AA contact details on closing page
6. "Presented by Automate Accelerator" on cover

### Automate Accelerator Brand Tokens (Default)

```
AA BRAND TOKENS
──────────────────────────────
DARK_BG:        #1a1a2e (dark navy/charcoal)
ACCENT:         #F97910 (orange — primary CTA)
ACCENT_2:       #3B1F95 (deep purple — secondary)
BADGE_BLUE:     #0066FF (feature badge)
BADGE_MAGENTA:  #D946EF (feature badge)
BADGE_GREEN:    #10B981 (feature badge)
BADGE_ORANGE:   #F97910 (feature badge)
LIGHT_BG:       #FFFFFF
BODY_DARK:      rgba(255,255,255,0.88)
BODY_LIGHT:     #4a4a4a
CARD_DARK:      rgba(255,255,255,0.07)
CARD_LIGHT:     #f7f7f7
FONT_HEADLINE:  'Rubik', system-ui, sans-serif
FONT_BODY:      'Roboto', system-ui, sans-serif
FONT_SCRIPT:    'Playfair Display', Georgia, serif (italic — for accent words in titles)
Logo:           [downloaded via brand-guide-extractor]
```

**Always re-extract via `/brand-guide-extractor automateaccelerator.com` to get the latest logo SVG and verify colors.**

---

## STEP 0 — BRAND & ASSET EXTRACTION (MANDATORY)

1. Run `/brand-guide-extractor automateaccelerator.com` — download AA logo, colors, fonts
2. Run `/brand-guide-extractor [client-website]` — download client logo for cover placement
3. Search and download relevant stock images from Unsplash for:
   - `cover_photo` — professional office/team photo matching client industry
   - Additional industry-relevant images as needed
4. Save all assets to `output/case-study-work/images/` and `brand-assets/`

**Do not proceed until AA logo SVG and client logo are downloaded.**

---

## INFORMATION SOURCES

### Primary Source
Use the **content document** as the primary source of all copy, claims, metrics, and results data.

### Secondary Source
Research the **client website URL** for gaps. Never contradict the content document.

### Do NOT
- Invent statistics, metrics, or claims not found in the sources
- Apply client brand colors as the primary design — AA brand is always primary
- Skip the brand extraction step

---

## OUTPUT FORMAT

**PDF — Portrait A4** (794 x 1123px per page)
**Pipeline**: HTML → Puppeteer → PDF

### File Naming
`[client-name]-case-study-v1.pdf`

### Output Directory
`output/[client-name]-case-study-v1.pdf`

---

## PAGE STRUCTURE — 7 Pages

The case study follows this exact page sequence with alternating backgrounds:

| Page | Section | Background | Content Focus |
|------|---------|------------|---------------|
| 1 | Cover | DARK | Hero headline, cover photo, two logos, 3 hero stats |
| 2 | Business Overview | LIGHT | Client intro, 3 stat badges, "Who They Are", "The Challenge" card |
| 3 | The Solution | DARK | Solution ecosystem, 3-4 numbered feature cards with colored badges |
| 4 | Campaign Performance | LIGHT | Hero metrics row, industry breakdown table, follow-up callout |
| 5 | Voice/Secondary Metrics | DARK→LIGHT | Additional metrics, gradient highlight banner, two-column details |
| 6 | What Made This Work | LIGHT | 3 pillars of success, scalable framework, direct impact stats |
| 7 | CTA / Closing | DARK (orange gradient) | CTA headline, two logos bottom |

---

### Page 1: Cover (DARK)

**Layout**: Dark charcoal/navy background. AA logo top-left (small, ~20px height). Professional photo top-right with white border frame (3px, rounded 12px). Large headline center-left. Body paragraph below. Two logo badges side-by-side (AA + client) with pill-shaped containers. Bottom: 3 hero stats in a row with large orange numbers and small labels.

**Content**:
- AA logo (top-left, small)
- Cover photo (top-right, ~45% width, white border frame, rounded corners)
- Headline: e.g. "Building a Predictable **Revenue Ecosystem** for [Client]"
  - Regular words in white, key phrase in `ACCENT` (orange), bold
  - Size: 42-46px, font-weight: 800
- Body paragraph (16px, light gray, 60% width)
- Two logo pills: `[AA Logo] ←→ [Client Logo]` with subtle connector line
- 3 hero stats row (bottom):
  - Large number (40px, ACCENT, 900 weight)
  - Small label below (12px, muted gray)
  - Separated by generous spacing

---

### Page 2: Business Overview (LIGHT)

**Layout**: White background. "Business **Overview**" title (regular + script italic accent). 3 stat badge cards in a row (icon + number + label). Two-column layout below: left = "Who They Are" text, right = dark "The Challenge" callout card.

**Content**:
- Title: "Business" (dark, sans-serif) + "Overview" (ACCENT, script italic font)
  - Size: 40px
- 3 stat badge cards (horizontal row):
  - Each: colored icon badge (44px square, rounded 8px, ACCENT bg) + large stat (28px, bold) + label (13px, gray)
  - Examples: "24+ Years of Experience", "Mid-Large Enterprise Size", "Australia Market"
- "Who They Are" section (left column, ~55%):
  - Subheading (18px, bold, dark)
  - 2-3 paragraphs (16px, body color)
- "The Challenge" dark card (right column, ~42%):
  - Dark background (`DARK_BG`), rounded 12px
  - "The Challenge" label (ACCENT, 14px, uppercase)
  - 3-5 bullet points (14px, white, with orange bullet markers)

---

### Page 3: The Solution (DARK)

**Layout**: Dark background. "The Solution" title (white) + "An End-to-End Growth Ecosystem" subtitle (ACCENT). 3-4 numbered feature cards stacked vertically. Each card has a colored left-border accent and icon badge.

**Content**:
- Title: "The Solution" (40px, white, bold)
- Subtitle: "An End-to-End [Outcome] Ecosystem" (ACCENT, 32px)
- 3-4 solution feature cards, each containing:
  - **Colored circle badge** (44px) with number — each card uses a DIFFERENT badge color:
    1. `BADGE_BLUE` (#0066FF)
    2. `BADGE_MAGENTA` (#D946EF)
    3. `BADGE_GREEN` (#10B981)
    4. `BADGE_ORANGE` (#F97910)
  - **Card title** (20px, white, bold)
  - **Card description** (14px, light gray)
  - **Sub-tags row**: 3-4 small pill tags below each card showing specific tactics/tools
    - Light dark bg, rounded 20px, 12px font, muted text
  - Card background: `rgba(255,255,255,0.05)`, border: `1px solid rgba(255,255,255,0.1)`, rounded 12px
  - Left color border: 4px solid in the badge's color

---

### Page 4: Campaign Performance (LIGHT)

**Layout**: White background. Title with script accent word. 3 hero metric cards in a row. "Industry-Specific Breakdown" section with data table rows. Dark callout at bottom.

This is the DATA-DENSE page — make numbers the hero.

**Content**:
- Title: "Email Campaign" (dark) + "Performance" (ACCENT, script italic)
  - Size: 38px
- Intro paragraph (14px, gray, 70% width)
- 3 hero metric cards (horizontal, equal width):
  - Each: large number (44px, ACCENT, 900 weight) + label (13px, gray)
  - White card bg, subtle border, rounded 10px, shadow
  - Examples: "20,000+ Emails Sent", "46-75% Open Rate", "2-7% Reply Rate"
- "Industry-Specific Breakdown" label (18px, bold)
- Data table rows (one per industry):
  - Each row: colored icon badge (28px, rounded 6px) + industry name (16px, bold) + 3 stat columns (14px)
  - Light border between rows
  - 4-6 industry rows
- "Follow-Up Success" dark callout card (bottom):
  - Dark bg, rounded 12px
  - Key insight text (14px, white)

---

### Page 5: Secondary Metrics (DARK top → LIGHT bottom, or full DARK)

**Layout**: Dark background. Title with script accent. 4 metric cards in a row. Large orange gradient banner with key highlight stat. Two-column detail section below.

**Content**:
- Title: "Voice Outreach &" (white) + "Appointment Metrics" (ACCENT, script italic)
  - Size: 36px
- Intro paragraph (14px, light gray)
- 4 metric cards (horizontal row):
  - Each: small colored icon badge (28px) + large number (32px, white, bold) + label (12px, gray)
  - Dark card bg, rounded 10px
  - Each badge uses a different color (blue, teal, magenta, orange)
- **Orange Gradient Highlight Banner** (full width):
  - Background: `linear-gradient(135deg, #F97910, #FF9A3E)`
  - Large stat number (44px, white, bold) + label
  - Rounded 12px, padding 32px
  - This is the signature visual element — always include one
- Two-column detail section:
  - Left: "Campaign Period" card (details about timeline)
  - Right: "Connection Quality" card (details about quality metrics)

---

### Page 6: What Made This Work (LIGHT)

**Layout**: White background. "What Made **This** Work" title (script accent on "This"). "The 3 Pillars of Success" subtitle. 3 pillar cards in a row. "Scalable Outbound Framework" section with numbered steps. "Direct Impact" dark callout with stat highlights.

**Content**:
- Title: "What Made" (dark) + "This" (ACCENT, script italic) + "Work" (dark)
  - Size: 40px
- Subtitle: "The [N] Pillars of Success" (16px, gray)
- 3 pillar cards (horizontal, equal width):
  - Each: colored icon badge (36px, rounded 8px) + title (18px, bold) + description (14px, gray)
  - White card bg, subtle border, rounded 10px
  - Badge colors: BADGE_BLUE, BADGE_MAGENTA, BADGE_ORANGE
- "Scalable [Framework Name]" section:
  - Numbered list with checkmark-style items
  - 4-5 steps, each with bold title + brief description
- "Direct Impact" dark callout card (right side or full width):
  - Dark bg, rounded 12px
  - 2-3 large stat numbers (32px, ACCENT)
  - Supporting labels

---

### Page 7: CTA / Closing (ORANGE GRADIENT)

**Layout**: Full orange gradient background (`linear-gradient(135deg, #F97910, #E86800)`). Large CTA headline in white. Supporting text. Two logos at bottom (AA + client) on semi-transparent white pills.

**Content**:
- CTA headline: "Ready to Build Your Own Growth System?" (36px, white, bold)
- Supporting text (16px, white, 80% opacity)
- Two logo pills at bottom:
  - AA logo (left) + Client logo (right)
  - Semi-transparent white backgrounds, rounded, side by side

---

## TYPOGRAPHY SYSTEM

### Font Stack
```
Headline:  'Rubik', 'Roboto', system-ui, sans-serif (800-900 weight)
Body:      'Roboto', system-ui, sans-serif (400-500 weight)
Script:    'Playfair Display', Georgia, serif (italic only — for accent words in titles)
```

### Mixed Title Pattern (CRITICAL)
Titles use TWO fonts in one line:
- Regular words → `FONT_HEADLINE` (Rubik), dark or white, bold
- Accent keyword → `FONT_SCRIPT` (Playfair Display italic), `ACCENT` color

Examples:
- "Business **_Overview_**" → "Business" in Rubik dark + "Overview" in Playfair italic orange
- "Email Campaign **_Performance_**" → same pattern
- "What Made **_This_** Work" → "This" in Playfair italic orange

### Size Scale
| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| Cover headline | 42-46px | 800 | Mixed fonts |
| Page title | 36-40px | 800 | Mixed fonts with script accent |
| Section subtitle | 28-32px | 700 | ACCENT color |
| Card title | 18-22px | 700 | Sans-serif only |
| Body text | 15-17px | 400 | Line-height 1.6 |
| Stat number (hero) | 40-48px | 900 | ACCENT color |
| Stat number (card) | 28-36px | 800 | ACCENT or white |
| Stat label | 12-14px | 400-500 | Muted gray |
| Tag/pill text | 12px | 500 | Inside rounded pills |
| Table row text | 14-15px | 400-600 | Industry data |

---

## COLOR SYSTEM

### Primary Palette (AA Brand)
| Role | Hex | Usage |
|------|-----|-------|
| Dark Background | `#1a1a2e` | Dark pages, callout cards |
| Orange Accent | `#F97910` | Primary accent, stats, CTAs, gradient banners |
| Purple Secondary | `#3B1F95` | Secondary buttons, accents |
| White | `#FFFFFF` | Light page bg, text on dark |
| Light Gray BG | `#f7f7f7` | Cards on light pages |
| Body Dark | `rgba(255,255,255,0.88)` | Text on dark pages |
| Body Light | `#4a4a4a` | Text on light pages |

### Multi-Color Badge System (CRITICAL)
Feature cards use DIFFERENT colored badges — never all the same color:

| Badge | Hex | Used For |
|-------|-----|----------|
| Blue | `#0066FF` | Strategy/CRM/Data features |
| Magenta | `#D946EF` | Content/Creative features |
| Green | `#10B981` | Outreach/LinkedIn features |
| Orange | `#F97910` | Multi-channel/Voice features |

Industry breakdown rows also use varied icon colors.

---

## CARD & COMPONENT SYSTEM

### Feature Cards (Page 3)
```css
.feature-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  border-left: 4px solid var(--badge-color); /* varies per card */
  border-radius: 12px;
  padding: 24px 28px;
  margin-bottom: 16px;
}
```

### Stat Cards (Page 4-5)
```css
.stat-card {
  background: #fff;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 10px;
  padding: 24px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
```

### Industry Data Rows (Page 4)
```css
.industry-row {
  display: flex;
  align-items: center;
  padding: 16px 0;
  border-bottom: 1px solid rgba(0,0,0,0.06);
  gap: 16px;
}
.industry-badge {
  width: 28px; height: 28px;
  border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-size: 12px; font-weight: 700;
}
```

### Orange Gradient Banner (Page 5)
```css
.gradient-banner {
  background: linear-gradient(135deg, #F97910, #FF9A3E);
  border-radius: 12px;
  padding: 32px 40px;
  color: #fff;
  text-align: center;
}
```

### Pill Tags (Page 3)
```css
.tag-pill {
  display: inline-block;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 20px;
  padding: 6px 16px;
  font-size: 12px;
  color: rgba(255,255,255,0.7);
  margin-right: 8px;
  margin-top: 10px;
}
```

### Dark Callout Card (on light pages)
```css
.callout-dark {
  background: #1a1a2e;
  color: #fff;
  border-radius: 12px;
  padding: 28px 32px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}
```

### Two-Logo Cover Treatment
```css
.logo-pills {
  display: flex;
  align-items: center;
  gap: 16px;
}
.logo-pill {
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 8px;
  padding: 10px 20px;
  height: 44px;
  display: flex;
  align-items: center;
}
.logo-connector {
  width: 24px;
  height: 2px;
  background: rgba(255,255,255,0.3);
}
```

---

## LAYOUT

- **Page dimensions**: 794 x 1123px (A4 portrait)
- **Padding**: 50px all sides (tighter than v1 — more content density)
- **Content area**: ~694 x 1023px usable
- **Card gaps**: 16px standard
- **Section gaps**: 28-36px between major sections
- **No page numbers** — clean, modern feel
- **AA logo footer**: Bottom-left of every content page, 16px height, subtle opacity

---

## PRODUCTION STEPS

1. **Run `/brand-guide-extractor automateaccelerator.com`** — download AA logo + brand tokens
2. **Run `/brand-guide-extractor [client-website]`** — download client logo
3. **Extract content** from the content document
4. **Research client website** for any gaps
5. **Search and download stock images** from Unsplash matching client industry
6. **Write** all page content following the 7-page structure
7. **Apply** writing guidelines
8. **Generate** HTML file with all 7 pages using AA brand tokens + stock images
9. **Export** to PDF using Puppeteer
10. **Open** the PDF for the user

---

## TECHNICAL PIPELINE

### Setup
```bash
cd output/case-study-work
npm install puppeteer
```

### Image Sourcing (Stock Photos)

Since we use Unsplash stock photos (not FLUX), search and download relevant images:

```bash
# Cover photo — professional office/team matching client industry
curl -L -o images/cover_photo.jpg "https://images.unsplash.com/photo-[ID]?w=1200&q=85&auto=format"

# Additional images as needed for dark page backgrounds
curl -L -o images/solution_bg.jpg "https://images.unsplash.com/photo-[ID]?w=1200&q=85&auto=format"
```

Use `WebSearch` to find relevant Unsplash photo URLs matching the client's industry.

### CSS Base

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700;800;900&family=Rubik:wght@400;500;600;700;800;900&family=Playfair+Display:ital,wght@1,400;1,500;1,600;1,700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }
@page { size: 794px 1123px; margin: 0; }

body {
  font-family: 'Roboto', system-ui, sans-serif;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}

:root {
  --dark-bg: #1a1a2e;
  --accent: #F97910;
  --accent-2: #3B1F95;
  --badge-blue: #0066FF;
  --badge-magenta: #D946EF;
  --badge-green: #10B981;
  --badge-orange: #F97910;
  --light-bg: #FFFFFF;
  --body-dark: rgba(255,255,255,0.88);
  --body-light: #4a4a4a;
  --card-dark: rgba(255,255,255,0.07);
  --card-light: #f7f7f7;
  --border-dark: rgba(255,255,255,0.12);
  --border-light: rgba(0,0,0,0.08);
  --font-headline: 'Rubik', system-ui, sans-serif;
  --font-body: 'Roboto', system-ui, sans-serif;
  --font-script: 'Playfair Display', Georgia, serif;
}

.page {
  width: 794px; height: 1123px;
  position: relative; overflow: hidden;
  page-break-after: always;
  padding: 50px;
}
.page-dark { background: var(--dark-bg); color: #fff; }
.page-light { background: var(--light-bg); color: #1a1a1a; }
.page-content { position: relative; z-index: 1; height: 100%; }

/* Accent word in titles — ALWAYS italic Playfair Display */
.accent-script {
  font-family: var(--font-script);
  font-style: italic;
  color: var(--accent);
}
```

### Puppeteer Export

```javascript
const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 794, height: 1123 });
  await page.goto('file://' + path.join(__dirname, 'case-study.html'), {
    waitUntil: 'networkidle0',
    timeout: 30000
  });
  await page.pdf({
    path: path.join(__dirname, '..', '[client-name]-case-study-v1.pdf'),
    width: '794px',
    height: '1123px',
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 }
  });
  await browser.close();
  console.log('SUCCESS');
})();
```

---

## WRITING GUIDELINES

- Australian English spelling throughout
- Active voice, results-focused, data-dense
- Specific numbers over vague claims — numbers are the hero
- Body copy: professional, confident, warm — not stiff
- Forbidden words: "unlock", "revolutionise", "seamless", "game-changing", "synergy", "leverage" (as verb)
- Connect every result to a tangible business outcome
- Only include content from source documents — never invent stats
- Use placeholders for missing data: `[METRIC]`, `[CLIENT TESTIMONIAL NEEDED]`
- Industry breakdown tables should use REAL data from source — never fabricate rows

---

## COMPLIANCE RULES

- **Branding is ALWAYS Automate Accelerator** — never brand as the client
- **Run `/brand-guide-extractor` for both AA and client** before starting
- **Stock images from Unsplash are mandatory** — never ship without real photography
- ONLY include the 7 pages defined in this skill
- ALWAYS follow the page order as defined
- ALWAYS source content from the provided document first
- NEVER invent metrics, testimonials, or contact details
- Output MUST be PDF in A4 portrait format (794 x 1123px)
- Feature cards MUST use different badge colors (blue, magenta, green, orange)
- Titles MUST use the mixed-font pattern (sans-serif + script italic accent word)
- Orange gradient banner on Page 5 is REQUIRED — signature visual element
- Two-logo treatment on cover and closing is REQUIRED
- AA logo footer on every content page

---

*Case Study Skill | v2.0 | Andersen IT Reference Design — AA-Branded, Data-Dense, Multi-Color Badges, Script Typography*
