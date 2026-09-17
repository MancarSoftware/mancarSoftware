# Project Profile Verification — September 2026

The profile combines four animated company panels with the four established project tours. Company content explains Mancar's purpose, business outcomes, delivery method, and contact route. Full supporting prose remains available through native disclosures.

- Passed `python -B scripts/validate-presentation.py`: matching README variants, paths and gallery anchors, accessible image alternatives, eight studio animations, eight project animations, static PNG alternatives, studio media budget, and thirteen captured stills. The new studio GIFs total approximately 0.50 MiB across both sizes.
- Verified that the four supplied logos match their original user-provided PNG files by SHA-256.
- Mobile project tours show one complete changing interface per scene. Company panels use separately composed desktop/mobile artwork; their text stays fixed while explanatory geometry moves.
- Checked the local presentation for image loading and console errors.
- Reviewed browser layouts at 1440, 768, and 390 CSS pixels, with no horizontal overflow. Confirmed desktop/mobile source selection and native company-detail expansion. Inspected static artwork for typography and spacing; fixed the timeline marker so it cannot obscure stage numbers.
- Ran `git diff --check`: no whitespace errors.

The local preview verifies presentation assets and links. It does not verify final GitHub rendering, other browsers, production deployments, backend persistence, LAN connectivity, appointment submissions, or external messaging. Capture sources and limitations are documented in [PROJECT-EVIDENCE.md](PROJECT-EVIDENCE.md).
