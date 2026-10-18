# Project gallery artwork

The project cards are miniature studies of each project's own visual
language. They share a 132 × 132 viewport and a quiet 8px corner radius, while
composition, palette, type, and illustration follow the individual project.
The profile gallery stays left aligned and wraps naturally. Names remain visible;
the link's alt text supplies the project category. Course provenance belongs in
the profile's project context rather than repeated badges inside each image.

## Sources and direction

The project READMEs, current covers, and available DESIGN.md files were reviewed
on 2026-10-15. Modern, Counter, Leafmark, and Waymark were added on
2026-10-18 after reviewing their current public documentation. These illustrations are interpretations of the established artwork
and behavior, rather than screenshots or additional product features.

| Project | Reviewed source | Card direction |
| --- | --- | --- |
| Modern | Public showcase README and cover | Green architectural silhouettes; career showcase with private application source. |
| Counter | README, DESIGN.md and readme-assets/STYLE.md | Slate numeric display and pale-blue F1 keycap; documentation colors only. |
| Leafmark | README and DESIGN.md | Blue notebook rail, folded writing sheet and serif title on a pale desk. |
| Waymark | README and DESIGN.md | Pale-blue route-marker post over ink-blue paths. |
| Readlane | README cover and DESIGN.md | Violet terminal reading lanes, floating article pages, integrated dollar prompt; monospace type. |
| Clibble | Approved card and runtime forest palette | Pine trees, leaf-filled centered selection, rain and Mosskin. The existing card is preserved. |
| Threadline | README and social API cover | Turquoise and ivory threads weave between post records; compact sans-serif type. |
| Portlight | README and lighthouse cover | A teal container lighthouse sends a beacon over a dark sea; clear monospace title. |
| Workbench | README, cover and generation brief | An amber drafting arm assembles code blocks on an engineering bench; measured monospace type. |
| CineSearch | README and retro cinema cover | Warm projector reels, a movie frame and curling filmstrip; italic serif wordmark. |
| SiteLens | README, cover and generation brief | Brass survey instrument and linked paper pages over a midnight contour map; atlas-like serif title. |
| Orbit | README, cover and DESIGN.md | Mint wireframe ship, coral faceted rocks, indigo navigation chart; angled arcade title. |
| TextScope | README, cover and generation brief | Oxblood, parchment, open book, rising letters and frequency bars; letterpress-style serif title. |
| Folio | README, site preview and DESIGN.md | Charcoal editorial page, lowercase yaqyn wordmark and a small Markdown-to-HTML diagram. No recreation or alteration of the author's portrait. |

The canonical product palettes remain in their own repositories. Card colors
adapt the documented runtime tokens or the established cover where no runtime
visual system exists. No product has been rebranded by this gallery update.

## Build and review

From the profile repository root:

```bash
python3 scripts/build_project_cards.py
```

This standard-library script generates thirteen cards. Clibble remains
an independently authored SVG. Every card is self-contained: no scripts, linked
images, web fonts, filters, animation, or external network requests. System font
families provide fallbacks without downloading a custom font.

For a visual check with librsvg installed:

```bash
rsvg-convert assets/projects/readlane-feed-reader.svg -o /tmp/readlane-card.png
```

Review at 132px before publishing; enlarged previews can conceal cramped text.
Keep the SVGs as vector assets. Preserve the existing HyperQuote/qvOS animated
covers and unrelated section icons. The older wide SVG assets for those projects
are not used by the current Learning Journey gallery.
