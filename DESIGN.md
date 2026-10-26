# Profile design

## Identity and reader journey

The profile is an editorial introduction to Abdulrahman M. Yaqyn's software.
A reader should identify the focus, inspect representative projects, explore
supporting work, and find a useful contact route. Accounting connects to records
and operational handoffs; it is not presented as a software seniority claim.

The reading order is introduction → career work → personal work → learning
projects → skills and process → credentials → contact. Career showcases,
personal projects, and Boot.dev work remain distinct. Project status and source
availability stay beside the relevant description.

## Wordmark and composition

The lowercase `yaqyn` wordmark follows the existing Folio identity. A measured
red punctuation mark and fine rules establish a repeatable signature. The
masthead replaces generic connected-node decoration with deliberate typography.
The original banner remains linked and visible in an expandable artwork section.

Desktop assets use a 1120 × 300 viewBox; mobile assets use 600 × 390. `<picture>`
selects the compact composition at 600 CSS pixels and below, then the appropriate
light/dark theme. These are image-selection rules, not custom page CSS. The
README retains a text H1, positioning paragraph, headings, and links independently
of the artwork. GitHub controls body typography and available content width.

## Palette

| Role | Dark artwork | Light artwork |
| --- | --- | --- |
| Background | `#141416` | `#f3f0e9` |
| Foreground | `#f3f0e9` | `#18181b` |
| Supporting labels | `#b9b7b0` | `#585851` |
| Accent | `#ff6b70` | `#b92732` |

The established profile red `#ed424a` remains the source accent for existing
icons. Theme variants adjust its lightness for readability. Neutral colors carry
the prose. Project covers retain their own palettes and artistic identities.

## Type and image direction

Mastheads use Arial, Helvetica, and a generic sans-serif fallback. Large,
closely spaced wordmark lettering contrasts with a regular-weight positioning
statement and small tracked labels. No external web fonts are requested.
Typography is confined to SVG artwork; body text inherits GitHub's font.

HyperQuote and qvOS are the two prominent wide covers. Modern and Counter retain
expandable showcases. Existing SVGs, GIFs, and covers are preserved byte for byte.
The 132 × 132 learning cards stay left aligned in a naturally wrapping flow,
with no fixed-column gallery table. The full project index is available directly
below the cards. Real interface captures and canonical project artwork are
preferred to generic stock imagery. No portrait is fabricated or altered.

## Icons and interactions

Existing outline icons follow the canonical workspace meanings, 24 px at H2
and 20 px at H3. Decorative icons have empty alt text beside visible headings.
Image links, descriptive navigation, project tables, `<picture>`, `<details>`,
and a Mermaid development-process diagram serve specific reader tasks.

The diagram describes a working approach, not a deployed system architecture.
Its introductory prose supplies the meaning if diagram rendering is unavailable.
Existing generated project artwork and the Boot.dev progress image provide
maintained visual content. Additional counters, games, or decorative dashboards
would displace project evidence and are not part of this layout.

## Principles and expressions

- **Evidence before adjectives:** show purpose, implementation, status, and a source or showcase link.
- **Hierarchy before volume:** use two featured projects, then progressive disclosure for supporting detail.
- **One identity, distinct projects:** use a restrained profile palette around original project artwork.
- **Text remains usable:** keep essential claims and navigation outside image assets.

The masthead establishes the profile identity; featured covers present the work;
gallery cards support browsing; the closing contact action explains what context
to send. Portfolio, project gallery, and README styling should retain those roles.

## Verification

Use GitHub's Markdown API for rendering/sanitization checks, validate local paths
and SVG XML, and run `python3 scripts/build_project_cards.py --check`. Rasterize
all new artwork with `rsvg-convert` and inspect desktop/mobile compositions.
Compare tracked asset hashes against the starting revision to confirm preservation.
These checks do not replace a rendered GitHub viewport audit. Honor the owner's
terminal-only preference; report that limitation without claiming browser checks.
