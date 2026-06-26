# Handoff: עכבר ההר — מדריך קהילתי לאזור מרום גולן

## Overview
"עכבר ההר" is a community guide (ידיעון קהילתי) for Kibbutz Merom Golan and the
surrounding Golan Heights. It lists places residents recommend — food, hikes,
health/wellness practitioners, local businesses, and useful contacts — as an
illustrated, filterable directory with an interactive map. Hebrew, RTL.

The design line is **rural / natural / volcanic Golan**: dry-grass paper
backgrounds, basalt near-black, grazing-green moss, a single volcanic-orange
accent, plus a hand-built illustrated banner (Mt. Hermon, Mt. Bental, springs,
hexagonal basalt columns, and a little mouse — a pun on the name).

## About the Design Files
The files in this bundle are **design references created in HTML** — a working
prototype that shows the intended look, copy, and behavior. They are **not
production code to copy verbatim**. The task is to **recreate this design in the
target codebase's environment** (React/Vue/Next/native/etc.) using that project's
established patterns, and to wire the data to a real source (see Data Model). If
no codebase exists yet, React + a mapping library (Leaflet or MapLibre) is a good
fit and mirrors the prototype.

The prototype is authored as a single self-contained component; the standalone
HTML build (`עכבר ההר - לשיתוף.html`) runs offline-ish in any browser (needs the
network only for map tiles + Google Fonts).

## Fidelity
**High-fidelity (hifi).** Final colors, typography, spacing, illustration, and
interactions. Recreate the UI pixel-close using the codebase's libraries. All exact
values are below.

---

## Design Tokens

### Colors
| Token        | Hex        | Use |
|--------------|------------|-----|
| basalt       | `#20302E`  | Header, footer, active chip, dark text-on-light anchors |
| basalt-card  | `#2C3A39`  | Logo fills, illustration columns |
| paper        | `#F3EEE2`  | Page background, light text on basalt |
| card         | `#FBF8F0`  | Card background, inactive chip background |
| ink          | `#21282A`  | Primary text |
| ink-soft     | `#5A6562`  | Secondary text, meta |
| moss         | `#4A7A3A`  | Category "טיולים"; phone/call button |
| moss-deep    | `#3A5F2E`  | Illustration foreground hills |
| ember        | `#C9572E`  | Single accent: brand border, "הוספת מקום", category "אוכל", "תושבים ממליצים" pill, notes pill |
| teal         | `#3F8E8C`  | Category "בריאות"; spring water in illustration |
| ochre        | `#B0822A`  | Category "עסקים" |
| slate        | `#5C6E6C`  | Category "אנשי קשר" |
| line         | `rgba(31,42,42,.12)` | Hairline borders |

### Category color map (drives chips, section headers, card accent bar, map pins)
- אוכל → `#C9572E` (ember), icon: coffee cup
- טיולים → `#4A7A3A` (moss), icon: mountain
- בריאות → `#3F8E8C` (teal), icon: leaf
- עסקים → `#B0822A` (ochre), icon: briefcase
- אנשי קשר → `#5C6E6C` (slate), icon: person

Section-header icon tint = same color at ~12–15% alpha behind the colored icon.

### Typography
- **Display / UI labels:** `Rubik` (weights 500/600/700/800), `letter-spacing:-.01em` on headings.
- **Body:** `Assistant` (400/500/600/700).
- Scale: H1 brand `clamp(19px,2.4vw,24px)/800`; hero tagline `clamp(15px,1.8vw,20px)/700`;
  section header `21px/700`; card title `19px/700`; meta `14.5px`; chips `14.5px/600`;
  small pills/tags `11.5–13px/600-700`.

### Radius & shadow
- Radius: chips `999px`; cards & map `16px`; buttons/inputs `10–12px`; section icon tile `13px`.
- Card shadow (rest): `0 1px 2px rgba(31,42,42,.05), 0 6px 18px rgba(31,42,42,.06)`.
- Card shadow (selected): `0 0 0 2px <catColor> inset, 0 8px 24px rgba(31,42,42,.1)`.
- Map shadow: `0 1px 2px rgba(31,42,42,.06), 0 10px 30px rgba(31,42,42,.09)`.

### Spacing
- Content max-width `1240px`, page padding `clamp(14px,3vw,26px)`.
- Desktop grid gap `24px`; card list gap `12px` (comfortable) / `9px` (compact).
- Card padding `16px 18px 16px 20px` (comfortable) / `13px 15px 13px 17px` (compact).

---

## Screens / Views
Single responsive screen with three regions; the map can be toggled off and on mobile
swaps to a list/map tab switch.

### 1. Sticky header (basalt, 3px ember bottom border)
- Left cluster: mouse-in-mountain SVG logo (46px) + "עכבר ההר" (Rubik 800) and
  subtitle "כל מה שיש באזור מרום גולן" (12.5px, `#AFB6AE`).
- Center: search input — translucent on basalt, search glyph at inset-start,
  placeholder "חיפוש: שם, יישוב, סוג…". Filters across name/sub/settlement/notes/category.
- Right: "הוספת מקום" button — ember fill, white text, plus icon. Opens the
  community Google Sheet in a new tab.

### 2. Illustrated hero banner (`height: clamp(216px,29vw,332px)`, 3px ember bottom border)
Hand-built flat SVG landscape, back→front: warm sky gradient → soft sun →
snow-capped Hermon range → layered moss hills → **Mt. Bental cone** (crater rim,
two antenna masts, winding ochre path) → near foreground hill → **teal spring pool**
with ripples → **cluster of hexagonal basalt columns** (bottom-start) → small **mouse**
silhouette perched on a column → a couple of pine trees.
Overlay card (bottom-start, translucent basalt, blur): an ember **"תושבים ממליצים"**
pill (heart icon), then "המדריך הקהילתי לכל מה שיש לטעום, לטייל ולגלות באזור" and
"בין הבזלת והמעיינות · מרום גולן ורמת הגולן".

### 3. Sticky category nav (paper, blurred, hairline bottom)
Horizontally scrollable row of pill chips: "הכל" + one per category. Each chip =
icon + label + count. **Active** chip: basalt fill, paper text, category-colored icon.
**Inactive**: card-bg fill, ink text, hairline border that turns the category color on hover.
Counts respect the current search.

### 4. Content grid (`max-width 1240px`)
Desktop: two columns `minmax(0,1.04fr) minmax(0,0.96fr)` — list left (RTL: start),
sticky map right. Above it a count line e.g. "27 מקומות".

**Editorial category sections** (shown when "הכל" is active; a single section when a
category is selected): header row = colored rounded icon tile + category name (Rubik 700)
+ "<desc> · <n> מקומות" + a dashed rule filling the remaining width. Section descriptions:
- אוכל — "בתי קפה, מסעדות ומאפיות"
- טיולים — "שבילים, מעיינות ותצפיות"
- בריאות — "מטפלים ובעלי מקצוע"
- עסקים — "שירותים ועסקים מקומיים"
- אנשי קשר — "מספרים שטוב להכיר"

**Cards:** card-bg, hairline border, 16px radius, 5px category-colored accent bar at
inset-start. Title (Rubik 700) + small category tag in the category color. Meta line
"<sub> · <settlement>" in ink-soft. Optional ember **notes pill** (e.g. "פתוח רק בשישי").
Action row: green **call** button (`tel:`) when a phone exists; white **"במפות גוגל"**
button (except for "אנשי קשר"). Hover lifts the card 2px and borders it in the category color.
Clicking a card selects it (ring + map focus); clicking an action link does not select.

### 5. Interactive map (Leaflet, CARTO "voyager" tiles, `dir=ltr`)
Teardrop pins in the category color, 2.5px white border. Click pin → select + popup
(name + sub · settlement). Selected pin scales up with a basalt border. Map fits bounds
to the visible, geolocated items. Caption notes locations are approximate at
settlement level and exact lat/lng can be added per place. Height `clamp(400px,72vh,760px)`.

### 6. Footer (basalt, 3px ember top border)
"עכבר ההר · מדריך קהילתי לאזור מרום גולן…" + an ember "+ הוספת מקום" link.

---

## Interactions & Behavior
- **Search:** live filter on name/sub/settlement/notes/category; resets selection.
- **Category filter:** chip click sets active category; "הכל" shows all sections.
- **Card ↔ map sync:** selecting either highlights the other; geolocated selection
  pans/zooms the map (`max(zoom,13)`) and opens the popup.
- **Maps link:** opens Google Maps to exact coordinates when present —
  `https://www.google.com/maps/search/?api=1&query=<lat>,<lng>` — else a text search of
  `name + settlement + "רמת הגולן"`. Use `target="_blank" rel="noopener"`.
  (Note: new-tab links are blocked inside sandboxed editor previews; they work in a
  normally hosted page.)
- **Add place:** header + footer links open the community Google Sheet.
- **Transitions:** card transform/border/shadow `.1–.15s`; chip `all .15s`; respect
  reduced-motion.

## Responsive behavior
- Breakpoint at **≤860px** → single column. A sticky "רשימה / מפה" segmented toggle
  appears; list and map are display-swapped (map stays mounted; call `invalidateSize()`
  when it becomes visible). Sticky offsets (nav top, map/toggle top) are computed from
  the measured header/nav heights, recalculated on resize. Hit targets ≥44px.

## State Management
- `data` — array of places (see model). `activeCat` ("all" | category). `query` (search).
- `selected` — index of focused place. `isNarrow`, `mobileView` ("list" | "map").
- Derived: filtered list, per-category counts (search-aware), grouped sections.
- Map objects (map instance + marker map by index) live outside render state.

## Data Model
Each place:
```
{ name, cat, sub, settlement, phone, notes, lat, lng }
```
- `cat` ∈ { אוכל, טיולים, בריאות, עסקים, אנשי קשר } (rows with other cats are dropped).
- `lat`/`lng` optional ("" when unknown → no pin, no maps-by-coords).
The prototype ships seed data inline and also supports a **live Google Sheet** (CSV via
PapaParse): header row `name,cat,sub,settlement,phone,notes,lat,lng,status`; a row shows
only if `status` is empty or `approved`. Set the CSV URL to switch from seed to live.
In a real codebase, back this with the sheet (or a small DB/CMS) behind an API.

## Assets
- **No external image assets.** The logo, hero landscape, category icons, and map pins
  are all inline SVG (documented above) — reproduce as components/SVG in the target app.
- **Fonts:** Google Fonts — Rubik + Assistant.
- **Map:** Leaflet 1.9.4 + CARTO voyager raster tiles (swap for MapLibre/your tile
  provider as needed). **CSV parsing:** PapaParse (only if keeping the live-sheet source).

## Files
- `עכבר ההר.dc.html` — the source prototype (template + logic; full styling and SVGs).
- `עכבר ההר - לשיתוף.html` — self-contained build, open in any browser to view/share.
