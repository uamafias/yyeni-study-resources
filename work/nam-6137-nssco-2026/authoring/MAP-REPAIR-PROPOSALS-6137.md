# 6137 Geography: proposed repairs for two map-stimulus gaps

Prepared by Claude (visual author), 30 Oct 2026. **For planner and Vitalis approval. Nothing here is approved.**

- No resource ID has been assigned. The proposed resources are called P-A and P-B below only so they can be referred to.
- The approved plan (`planning/visual-resource-plan-6137.json`), the recorded approval hashes and the 54-resource count are unchanged.
- The five affected cards still carry their VISUAL PENDING situation. They are not counted as delivered and have no bindings in `assets/asset-manifest-6137.json`.
- The preflight therefore still reports:
  - "Unapproved map-plan concern: 2.2 / 2.6";
  - "Map-stimulus binding absent" for these five cards.

## Gap 1: topic 2.2, cards 013–016 (Namibia farming distribution)

**What the cards need.** One map of Namibia showing:
- household (communal) crop farming in the north-central regions, labelled Omusati, Oshana, Ohangwena and Oshikoto, with further crop sites farther east (014);
- commercial cattle in central areas and sheep/goats farther south (013, 016);
- the Otavi–Grootfontein–Tsumeb crop area, the "Maize Triangle", inland (016);
- local irrigated crop sites (013);
- a small plot keyed "vegetables for sale" near a northern town, beside unlabelled cultivated plots (015);
- a full key.

**Proposed resource P-A.** An original thematic map; to be named by the planner, e.g. as a second 2.2 resource.

**Base layers.**

| Layer | Source | Licence |
|---|---|---|
| Regions | geoBoundaries NAM ADM1 (the 14 current regions, including Kavango East and West) | CC BY 4.0 per the global dataset. **The Namibia file's own `boundaryLicense` metadata must be checked before use.** |
| Coastline and neighbours | Natural Earth | public domain, already in `assets/sources/ne_110m_land.geojson` |
| Towns: Otavi, Grootfontein, Tsumeb, Oshakati, Ruacana, Rundu, Katima Mulilo, Windhoek, Mariental, Keetmanshoop, Aussenkehr | GeoNames | CC BY 4.0 |

**Thematic overlays.** These are generalised at region scale and drawn from cited statistics, not traced from any atlas or examination insert.
- **Communal crop (mahangu) zone:** the north-central regions, plus Kavango East and West and Zambezi as "crop sites farther east".
  - Source: Namibia Statistics Agency and Ministry of Agriculture, Water and Forestry, *Namibia Census of Agriculture 2013/2014: Communal Sector Report* (Nov 2015). Its regional crop tables are disaggregated by region; a copy is on FAO Open Knowledge.
- **Commercial cattle (central) and small stock (south, Hardap and //Karas):**
  - Sources: the census's commercial-sector report and the Meat Board of Namibia livestock statistics.
  - Shading must follow the regional figures, not a remembered pattern.
- **Maize Triangle:** a hatched inland area joining the three GeoNames town points.
- **Irrigated sites:** point symbols at the Green Scheme project locations:
  - Etunda (Ruacana);
  - Hardap (Mariental);
  - Orange River (Aussenkehr);
  - the Kavango schemes: Shadikongoro, Ndonga-Linena, Musese, Sikondo, Uvungu-Vungu, Mashare and Shitemo;
  - Kalimbeza (Zambezi).

  Source: Agribank's Green Scheme page and ministry statements. The key must say "irrigation scheme location", not "currently producing", because recent reporting describes several schemes as idle (e.g. Kalimbeza).
- **Card 015's small plot:** a separate inset at a larger scale beside a northern town, explicitly titled "schematic example, not a surveyed farm". It shows one plot keyed "vegetables for sale" and neighbouring plots keyed only "cultivated".
  - The card's answer already limits the claim to this keyed site.
  - The inset must not be presented as a real farm.

**Keyed classes.**
- communal crop farming;
- commercial cattle;
- sheep/goats (small stock);
- crop area (Maize Triangle);
- irrigation scheme;
- town;
- region boundary;
- an inset key for "vegetables for sale" and "cultivated (purpose not shown)".

Furniture: north arrow, scale bar, title, source line and date.

**Bindings if approved.** Cards 013–016 to P-A, each with its own answer side, because the four answers differ:
- **013:** north and centre/south and local exceptions;
- **014:** the north-central cluster, with eastern sites qualified;
- **015:** the inset plot and its limit;
- **016:** livestock contrast and inland crop area.

**Card text check before authoring.**
- Card 014 asks for the "Omusati–Oshana–Ohangwena–Oshikoto labels"; the map must label these four regions.
- Card 016's "Maize Triangle … inland around its three labelled towns" requires the three towns to be labelled.
- No answer needs changing if the map follows the census figures. If the regional figures put cattle or small stock somewhere other than the cards state, the cards will be revised, not the data.

## Gap 2: topic 2.6, card 002 (Namibia conservation locations)

**What the card needs.** A map distinguishing:
- Etosha National Park, an area in the north;
- the Cheetah Conservation Fund, a point (specialist centre) near Otjiwarongo;
- two conservancy examples as areas: Torra (north-west, Kunene) and Salambala (north-east, Zambezi).

The key must separate area categories from the centre point.

**Proposed resource P-B.**

**Base.** The same geoBoundaries ADM1 and Natural Earth base as P-A.
- Alternatively, it could reuse the Natural Earth outline already used in VIS-6137-1.7-01, as an explicit reuse approved by the planner.

**Areas.**
- **Etosha National Park:** the OpenStreetMap park boundary (ODbL; credit "© OpenStreetMap contributors"), generalised.
  - WDPA/Protected Planet is not proposed, because its terms restrict redistribution and commercial use.
- **Torra and Salambala conservancies:** generalised outlines digitised from the coordinate schedules in the conservancies' Government Gazette declarations. NACSO hosts gazette PDFs for conservancies.
  - If a usable schedule cannot be found, use NACSO's published profile maps only as a location reference, and show the conservancies as approximate generalised areas labelled "approximate".
  - NACSO maps are images, not open vector data, so they must not be traced.

**Point.** The Cheetah Conservation Fund centre, located from CCF's published address relative to Otjiwarongo (town point from GeoNames).

**Key and furniture.**
- national park (area);
- communal conservancy (area);
- conservation centre (point);
- town;
- region boundary;
- north arrow, scale bar, sources and date.

**Binding if approved.** Card 002 to P-B. The current answer needs no change if the map places the four features as described.

## What approval would need to state

1. Whether P-A and P-B are added as new planned resources, with planner-assigned IDs and paths, or as explicit reuses.
2. The approved sources above, or substitutes.
3. Whether the schematic inset for card 015 is acceptable or the card should be rewritten.
4. The approver and the evidence. The preflight requires `scope_concerns[].resolution.approved_by = "Vitalis P Haupindi"` and `approval_evidence`.

Once approved, each map would be authored like the other 54 resources: one resource at a time, with code, spec, checklist, hashes, manifest entry and bindings, and then Codex review.

## Sources consulted for this proposal

- geoBoundaries ADM1 (CC BY 4.0, per-country licence in metadata): https://developers.google.com/earth-engine/datasets/catalog/WM_geoLab_geoBoundaries_600_ADM1
- Namibia Census of Agriculture 2013/2014, Communal Sector Report (NSA/MAWF, 2015): https://the-eis.com/elibrary/search/21497 and https://openknowledge.fao.org/server/api/core/bitstreams/7814fed5-7b8d-4673-9be3-299da500e994/content
- Green Scheme projects (list and status): https://agribank.com.na/page/green-scheme/ and https://www.republikein.com.na/mw-b7-main/re-evaluating-green-scheme-projects-in-namibia2023-08-1679233
- Conservancy maps and gazettes: https://www.ccf-namibia.org/resources/conservancy-maps/ and https://nacso.org.na/ (gazette PDFs, e.g. https://nacso.org.na/wp-content/uploads/2025/06/Kapinga-Kamwalye.pdf)

These sources were located on 30 Oct 2026 but not yet downloaded or checked line by line. That check is part of authoring once the proposal is approved.
