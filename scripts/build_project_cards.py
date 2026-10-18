#!/usr/bin/env python3
"""Build the project-specific SVG studies beside the approved Clibble card.

No network, third-party packages, raster assets, fonts, or animation required.
Source direction and visual ownership: assets/projects/DESIGN.md.
"""
from pathlib import Path
from html import escape
import argparse

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/projects"
CHECK = False

def text(x, y, value, size=10, fill="#eef3e8", font="monospace", extra=""):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{font}" font-size="{size}" {extra}>{escape(value)}</text>'

def card(slug, name, description, background, edge, art):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="132" height="132" viewBox="0 0 132 132" role="img" aria-labelledby="title desc">
  <title id="title">{escape(name)}</title>
  <desc id="desc">{escape(description)}</desc>
  <defs><clipPath id="frame"><rect x="1" y="1" width="130" height="130" rx="8"/></clipPath></defs>
  <rect x="1" y="1" width="130" height="130" rx="8" fill="{background}" stroke="{edge}"/>
  <g clip-path="url(#frame)">
{art}
  </g>
</svg>
'''
    path = OUT / f"{slug}.svg"
    if CHECK:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            raise SystemExit(f"Generated card is out of date: {path.relative_to(ROOT)}")
        return
    path.write_text(content, encoding="utf-8")


def readlane():
    violet, ivory = "#AEA5FF", "#F0EFFA"
    art = '''<g fill="none" stroke="#302B4D" stroke-width="1"><path d="M0 78 66 44l66 34-66 34ZM0 91l66-34 66 34-66 34"/></g>
<path d="m-8 98 47-25 34 17 36-19 35 17" fill="none" stroke="#6253D9" stroke-width="14"/>
<path d="m-8 98 47-25 34 17 36-19 35 17" fill="none" stroke="#AEA5FF" stroke-width="5"/>
<path d="m-8 98 47-25 34 17 36-19 35 17" fill="none" stroke="#F0EFFA" stroke-width=".8"/>
<g fill="#171525" stroke="#AEA5FF" stroke-width="1.2">
<path d="M19 44h18v27H19Z"/><path d="M55 52h19v30H55Z"/><path d="M95 35h20v29H95Z"/>
</g>
<g stroke="#F0EFFA" stroke-width="1.3"><path d="M23 51h10m-10 5h10m-10 5h6M59 59h11m-11 5h11m-11 5h8M99 43h12m-12 5h12m-12 5h8"/></g>
<g fill="#6253D9"><rect x="12" y="78" width="3" height="3"/><rect x="84" y="54" width="3" height="3"/><rect x="113" y="91" width="3" height="3"/></g>'''
    art += text(12, 24, "$", 17, violet, extra='font-weight="700"')
    art += text(26, 24, "Readlane", 15, ivory, extra='font-weight="700"')
    art += text(66, 121, "Feeds, at your pace.", 8, violet, extra='text-anchor="middle"')
    card("readlane-feed-reader", "Readlane — Feed reader", "Violet reading lanes carry article pages through a miniature terminal landscape. RSS and Atom, collected locally.", "#10111c", "#50457f", art)


def threadline():
    art = '''<g fill="none" stroke-linecap="round">
<path d="M-12 99C22 16 63 112 105 50s52 12 36 42" stroke="#134d56" stroke-width="17"/>
<path d="M-12 99C22 16 63 112 105 50s52 12 36 42" stroke="#39d6c0" stroke-width="5"/>
<path d="M-12 99C22 16 63 112 105 50s52 12 36 42" stroke="#b3f2e8" stroke-width=".8"/>
<path d="M-8 55c39 69 64-33 99 7s53-2 59-18" stroke="#34575b" stroke-width="12"/>
<path d="M-8 55c39 69 64-33 99 7s53-2 59-18" stroke="#f4f0e7" stroke-width="3"/>
</g>
<g fill="#142d38" stroke="#709d9e" stroke-width=".7">
<rect x="16" y="43" width="36" height="21" rx="3"/><rect x="73" y="83" width="39" height="20" rx="3"/>
</g>
<g fill="#39d6c0"><circle cx="23" cy="50" r="2"/><circle cx="80" cy="90" r="2"/></g>
<g stroke="#cbe2de"><path d="M29 49h16m-24 8h24M86 89h19m-26 7h26"/></g>'''
    art += text(66, 25, "Threadline", 16, "#f4f0e7", "sans-serif", 'text-anchor="middle" font-weight="700"')
    art += text(66, 121, "Social publishing API", 8, "#a6d8d2", extra='text-anchor="middle"')
    card("threadline-social-api", "Threadline — Social publishing API", "Ivory and turquoise threads weave between small post records, echoing Threadline's connected accounts and publishing cover.", "#101e29", "#33636b", art)


def portlight():
    art = '''<path d="M96 40 0 18v28Z" fill="#163a43"/>
<path d="M96 40 0 28v9Z" fill="#285960"/>
<g fill="none" stroke="#21505b" stroke-width=".7"><path d="m104 44 36 17m-36-11 38 27M2 76l35-10 34 6 22-13"/></g>
<path d="m0 108 22-12 19 7 17-11 22 8 13-14 22 11 21-7v26H0Z" fill="#17343e"/>
<path d="m57 105 18-8 13-11 19 5 15 13Z" fill="#08151e" stroke="#417780"/>
<g fill="#173640" stroke="#78bdc5" stroke-width=".8">
<path d="M85 90h25V74H85ZM87 73h21V59H87ZM90 58h15V46H90Z"/>
</g>
<g stroke="#427c87" stroke-width=".7"><path d="M89 76v12m5-12v12m5-12v12m5-12v12M91 61v10m5-10v10m5-10v10"/></g>
<path d="M91 45h13V34H91Z" fill="#376c75" stroke="#b8f2ee"/>
<path d="m89 33 9-7 8 7ZM97 21v5" fill="none" stroke="#8bd9dc"/>
<path d="M96 36h4v7h-4Z" fill="#e4ffed"/>
<g fill="none" stroke="#417780" stroke-width=".7"><path d="m-3 94 18-3 17 2m-22 13 15-3 15 2m-4 7 18-2 14 2m-51-12 13-2 12 2"/></g>'''
    art += text(11, 23, "Portlight", 15, "#f2f2e8", extra='font-weight="700"')
    art += text(66, 123, "Small service. Clear signals.", 6.7, "#b8d8dc", extra='text-anchor="middle"')
    card("portlight-http-server", "Portlight — HTTP server", "A lighthouse built from stacked containers sends a quiet teal beacon across the sea. Small service, clear signals.", "#0b1c28", "#38616b", art)


def workbench():
    art = '''<g stroke="#3e3425" stroke-width=".5"><path d="M8 41h116M8 53h116M8 65h116M8 77h116M8 89h116M20 35v68m18-68v68m18-68v68m18-68v68m18-68v68m18-68v68"/></g>
<path d="m9 95 54-22 62 24-54 21Z" fill="#342a20" stroke="#7e6541"/>
<path d="m9 95 62 23v6L9 101Z" fill="#201c17"/>
<g fill="#2d2921" stroke="#d4a45f" stroke-width="2.5" stroke-linejoin="round">
<path d="M91 89h22v6H91ZM98 88l1-22-19-19 4-7 24 22-4 26Z"/>
<path d="m82 42-29 13 2 7 30-13Z"/>
</g>
<g fill="#c29553" stroke="#f3d598"><circle cx="102" cy="65" r="4"/><circle cx="82" cy="45" r="4"/><circle cx="54" cy="58" r="3"/></g>
<path d="m53 61-4 8 5 3m-1-11 6 8-4 3" fill="none" stroke="#d4a45f" stroke-width="1.5"/>
<g fill="#73502c" stroke="#e3b86e" stroke-width=".8"><path d="m37 83 13-5 13 5-13 5Zm0 0v11l13 5V88m13-5v11l-13 5"/><path d="m57 92 12-5 12 5-12 5Zm0 0v8l12 5v-8m12-5v8l-12 5"/></g>
<path d="m42 88 4 2-4 2m12-6-4 9" fill="none" stroke="#fff0bf"/>'''
    art += text(66, 23, "Workbench", 14, "#f4e6c8", extra='text-anchor="middle"')
    art += text(66, 123, "Inspect / edit / execute", 7.2, "#d4a45f", extra='text-anchor="middle"')
    card("workbench-ai-agent", "Workbench — AI coding agent", "An amber mechanical drafting arm assembles code blocks on a measured engineering bench. Inspect, edit, execute.", "#191811", "#6c5635", art)


def cinesearch():
    art = '''<g fill="none" stroke="#713a2d" stroke-width=".7"><path d="M-9 86C35 9 144 33 130 94S29 150 8 77ZM-4 67l139 24M15 44l106 63"/></g>
<g fill="#e8af62"><circle cx="15" cy="39" r="1"/><circle cx="113" cy="37" r="1.4"/><circle cx="23" cy="96" r="1"/><circle cx="101" cy="102" r="1"/></g>
<path d="m63 72 63-23v49Z" fill="#613528"/>
<path d="M94 49h26v22H94Z" fill="#b15d39" stroke="#f0bc78"/>
<path d="m96 67 8-11 6 6 7-10v17H96Z" fill="#291b20"/>
<g fill="#43242a" stroke="#e8af62" stroke-width="1.2">
<rect x="36" y="65" width="35" height="24" rx="3"/><circle cx="37" cy="54" r="14"/><circle cx="64" cy="49" r="12"/>
</g>
<g fill="#d58d52"><circle cx="37" cy="54" r="3"/><circle cx="31" cy="47" r="3"/><circle cx="45" cy="51" r="3"/><circle cx="34" cy="62" r="3"/><circle cx="63" cy="49" r="2.5"/><circle cx="58" cy="43" r="2.5"/><circle cx="70" cy="47" r="2.5"/><circle cx="62" cy="57" r="2.5"/></g>
<path d="m71 69 8-4v23l-8-4ZM45 90l-7 13m25-13 7 13" fill="#a86436" stroke="#e8af62"/>
<path d="M-4 100c31-10 51 18 79 3s48-2 64 6" fill="none" stroke="#b86043" stroke-width="9"/>
<path d="M-4 100c31-10 51 18 79 3s48-2 64 6" fill="none" stroke="#f1bb73" stroke-width="1" stroke-dasharray="2 5"/>'''
    art += text(66, 26, "CineSearch", 19, "#ffd69a", "serif", 'font-weight="700" font-style="italic" text-anchor="middle"')
    art += text(66, 123, "Movie search & RAG", 8, "#f1bb73", extra='text-anchor="middle"')
    card("cinesearch-rag-engine", "CineSearch — Movie RAG engine", "A warm retro film projector illuminates a movie frame; reels and a winding filmstrip echo CineSearch's cinema cover.", "#2b181d", "#a06445", art)


def sitelens():
    art = '''<g fill="none" stroke="#21404f" stroke-width=".7"><path d="M-4 62C28 29 35 78 75 41s61 7 62 15M-4 74C29 41 35 90 75 53s61 7 62 15M-4 86c33-33 39 16 79-21s61 7 62 15M-4 98c33-33 39 16 79-21s61 7 62 15"/></g>
<g fill="none" stroke="#71b8c9" stroke-width=".9"><path d="m42 77 49-33 21 29-31 26-39-22 62-2M20 51l22 26"/></g>
<g fill="#e9d7b5" stroke="#b99566" stroke-width=".7"><path d="M83 35h17v20H83ZM103 64h17v20h-17ZM73 91h15v17H73ZM12 42h17v19H12Z"/></g>
<g stroke="#a47b4d" stroke-width=".8"><path d="M86 40h11m-11 4h11m-11 4h7M106 69h11m-11 4h11m-11 4h7M76 96h9m-9 4h6M15 47h11m-11 4h11m-11 4h7"/></g>
<path d="m28 103 14-23 13 23m-13-23v25" fill="none" stroke="#b99566" stroke-width="2"/>
<path d="m30 72 24-5 4 9-24 5Z" fill="#856341" stroke="#e5c08a"/>
<circle cx="54" cy="72" r="7" fill="#0d2e40" stroke="#e5c08a" stroke-width="2"/>
<circle cx="54" cy="72" r="3" fill="#73c6d9"/>
<circle cx="42" cy="83" r="4" fill="#b99566"/>'''
    art += text(66, 25, "SiteLens", 19, "#f3dfb9", "serif", 'text-anchor="middle"')
    art += text(66, 123, "Explore / extract / report", 6.8, "#b9d3d7", extra='text-anchor="middle"')
    card("sitelens-web-crawler", "SiteLens — Web crawler", "A brass surveying instrument traces linked paper webpages across a midnight topographic atlas, matching SiteLens's expedition artwork.", "#0c2030", "#4e6b74", art)


def orbit():
    art = '''<g fill="#a4adc5"><circle cx="18" cy="39" r=".8"/><circle cx="76" cy="40" r=".8"/><circle cx="117" cy="83" r=".8"/><circle cx="49" cy="97" r=".8"/><circle cx="9" cy="83" r=".8"/><circle cx="108" cy="44" r=".8"/></g>
<g fill="none" stroke="#364058" stroke-width=".6"><ellipse cx="65" cy="77" rx="73" ry="26" transform="rotate(-25 65 77)"/><ellipse cx="65" cy="77" rx="45" ry="45"/><path d="M0 77h132M65 33v77"/></g>
<path d="M-7 108c34-4 26-28 52-22S72 66 94 58" fill="none" stroke="#3c8e88" stroke-width="5"/>
<path d="M-7 108c34-4 26-28 52-22S72 66 94 58" fill="none" stroke="#83efd0" stroke-width="1.4"/>
<g fill="#2a233c" stroke="#f18c83" stroke-width="1.3" stroke-linejoin="round"><path d="m23 48 8-5 8 6-1 11-9 4-9-8Z"/><path d="m94 90 10-8 14 6 3 12-12 8-12-5Z"/><path d="m11 96 5-3 7 4-3 7-7-1Z"/></g>
<g stroke="#a95e68" fill="none"><path d="m23 48 7 8 9-7m-9 7-1 8M104 82l3 13 14 5m-14-5-10 8"/></g>
<path d="m91 47 9 21-12-4-7 6Z" fill="#101327" stroke="#83efd0" stroke-width="1.5"/>
<path d="m87 69-6 9" stroke="#eef3e8" stroke-width="1.2"/>'''
    art += text(66, 27, "ORBIT", 25, "#eef3e8", "sans-serif", 'text-anchor="middle" font-weight="800" font-style="italic"')
    art += text(66, 123, "Dodge / split / survive", 7.3, "#83efd0", extra='text-anchor="middle"')
    card("orbit-asteroids-game", "Orbit — Asteroids game", "A mint wireframe ship cuts through faceted coral asteroids on an indigo navigation chart, matching the game's runtime palette.", "#101327", "#53516e", art)


def textscope():
    art = '''<g fill="none" stroke="#55282c" stroke-width=".7"><path d="M6 38h120M6 107h120M10 38v69m112-69v69"/></g>
<path d="M15 81q24-11 51 4 27-15 51-4v23q-25-10-51 3-25-13-51-3Z" fill="#e8d7af" stroke="#bf955a" stroke-width="1.2"/>
<path d="M66 85v22" stroke="#8f6844" stroke-width="1.4"/>
<g fill="none" stroke="#aa8a61" stroke-width=".7"><path d="m22 86 34 3m-34 2 34 3m-34 2 34 3m-34 2 25 2m28-14 34-3m-34 8 34-3m-34 8 34-3m-34 8 25-2"/></g>
<g fill="#bd9456"><path d="M74 52h4v23h-4ZM83 43h4v32h-4ZM92 58h4v17h-4ZM101 64h4v11h-4Z"/></g>'''
    art += text(66, 25, "TextScope", 19, "#efdcb1", "serif", 'text-anchor="middle" font-weight="700"')
    art += text(25, 62, "a", 20, "#efdcb1", "serif")
    art += text(45, 51, "e", 16, "#bd9456", "serif")
    art += text(55, 72, "t", 15, "#e2c698", "serif")
    art += text(39, 76, "i", 11, "#bd9456", "serif")
    art += text(66, 123, "Read / count / discover", 7.1, "#d9b775", extra='text-anchor="middle"')
    card("textscope-text-analyzer", "TextScope — Text analyzer", "Letters rise from a parchment book into frequency bars in an oxblood and gold letterpress study, drawn from TextScope's printing-workshop cover.", "#35181e", "#84503b", art)


def folio():
    art = '''<path d="M12 36h108M12 105h108" stroke="#45474b" stroke-width=".8"/>
<path d="M15 73h54m-54 5h48m-48 5h53m-53 5h39" stroke="#77797b" stroke-width="1.3"/>
<rect x="15" y="94" width="32" height="6" rx="1" fill="#deddd9"/>
<path d="M84 46h24v12H84Z" fill="#27292c" stroke="#45474b"/>
<path d="M84 73h24v14H84Z" fill="#27292c" stroke="#45474b"/>
<path d="M96 61v8m-3-3 3 3 3-3" fill="none" stroke="#b0b2b6"/>'''
    art += text(12, 25, "Folio", 17, "#f2f1ed", "sans-serif", 'font-weight="700"')
    art += text(15, 62, "yaqyn.", 19, "#f2f1ed", "Trebuchet MS, sans-serif", 'font-weight="700"')
    art += text(96, 54, "# md", 5.8, "#b0b2b6", extra='text-anchor="middle"')
    art += text(96, 82, "html", 5.8, "#deddd9", extra='text-anchor="middle"')
    art += text(66, 123, "Site & generator", 8.5, "#b0b2b6", "sans-serif", 'text-anchor="middle"')
    card("folio-static-site", "Folio — Site and generator", "A miniature charcoal portfolio with the lowercase yaqyn wordmark, editorial rules, and a Markdown-to-HTML publishing diagram.", "#1c1d20", "#45474b", art)


def leafmark():
    art = '''<path d="M13 42h106v65H13Z" fill="#dce2ed"/>
<rect x="19" y="36" width="94" height="67" rx="4" fill="#ffffff" stroke="#365bc4"/>
<path d="M19 40v59q0 4 4 4h19V36H23q-4 0-4 4Z" fill="#365bc4"/>
<g stroke="#c1d0f4" stroke-width="2"><path d="M25 49h10m-10 9h10m-10 9h10"/></g>
<path d="M59 45h24l12 12v34H59Z" fill="#f5f7fb" stroke="#61708a"/>
<path d="M83 45v12h12" fill="#dce2ed" stroke="#61708a"/>
<g stroke="#61708a"><path d="M65 66h23m-23 7h23m-23 7h16"/></g>'''
    art += text(66, 25, "Leafmark", 19, "#202d45", "serif", 'text-anchor="middle"')
    art += text(66, 122, "A home for your notes", 8, "#365bc4", extra='text-anchor="middle"')
    card("leafmark-notebook", "Leafmark — Personal notebook", "A blue notebook rail and folded writing sheet echo Leafmark's private plain-text workspace.", "#f5f7fb", "#dce2ed", art)


def waymark():
    art = '''<g fill="none" stroke="#40556c"><path d="M0 102 48 83 76 90l56-25M0 114l48-19 28 7 56-25"/></g>
<path d="M65 39v67" stroke="#afc0d4" stroke-width="4"/>
<path d="M40 43h44l12 10-12 10H40Z" fill="#18283a" stroke="#a9d5ff" stroke-width="1.5"/>
<path d="M91 70H49L37 80l12 10h42Z" fill="#18283a" stroke="#a9d5ff" stroke-width="1.5"/>
<g stroke="#a9d5ff" stroke-width="2"><path d="M49 53h30m-24 27h26"/></g>'''
    art += text(66, 25, "Waymark", 19, "#f0f5fc", "serif", 'text-anchor="middle"')
    art += text(66, 122, "Links worth sharing", 8, "#a9d5ff", extra='text-anchor="middle"')
    card("waymark-link-shortener", "Waymark — Link shortener", "A pale blue route-marker post points toward editable destinations over ink-blue paths.", "#101b2a", "#40556c", art)


def counter():
    art = '''<rect x="17" y="38" width="98" height="43" rx="7" fill="#14222c" stroke="#263a46"/>
<path d="M66 82v8" stroke="#a8cbd7"/>
<rect x="47" y="91" width="38" height="20" rx="4" fill="#1e3440" stroke="#45616f"/>'''
    art += text(66, 25, "Counter", 17, "#edf3f7", "sans-serif", 'text-anchor="middle"')
    art += text(66, 69, "33", 29, "#edf3f7", extra='text-anchor="middle"')
    art += text(66, 105, "F1", 11, "#a8cbd7", extra='text-anchor="middle"')
    art += text(66, 124, "Keep your place", 8, "#a8cbd7", extra='text-anchor="middle"')
    card("omarchy-counter", "Counter — Omarchy tally counter", "A quiet numeric display connected to an F1 keycap, following Counter's documentation cover.", "#101922", "#263a46", art)


def modern():
    art = '''<g fill="#1e332d" stroke="#6ba38a" stroke-width=".8"><path d="M14 103V66l24-10v47ZM38 103V42l29-9v70ZM67 103V56l23 9v38ZM90 103V49l27 12v42Z"/></g>
<g stroke="#9bc2ae" stroke-width="1"><path d="M21 72h10m-10 9h10m-10 9h10M45 49h15m-15 10h15m-15 10h15m-15 10h15m-15 10h15M74 69h9m-9 10h9m-9 10h9M97 66h13m-13 11h13m-13 11h13"/></g>
<path d="M9 104h114" stroke="#9bc2ae"/>'''
    art += text(66, 24, "Modern", 19, "#eaf1eb", "sans-serif", 'text-anchor="middle" font-weight="700"')
    art += text(66, 122, "Construction & services", 7.3, "#9bc2ae", extra='text-anchor="middle"')
    card("modern", "Modern — Construction company website", "Green architectural silhouettes represent Modern's bilingual construction services showcase.", "#12231d", "#446d57", art)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify generated cards without rewriting them")
    args = parser.parse_args()
    CHECK = args.check
    for draw in [modern, counter, leafmark, waymark, readlane, threadline, portlight, workbench, cinesearch, sitelens, orbit, textscope, folio]:
        draw()
    action = "Verified" if CHECK else "Built"
    print(f"{action} 13 project-specific SVG cards; approved Clibble card preserved.")
