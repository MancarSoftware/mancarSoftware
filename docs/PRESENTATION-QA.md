# Project Profile Verification — September 2026

The public profile is intentionally limited to a Mancar brand marker and four project entries. Non-project studio panels, capability claims, process explanations, toolkits, FAQs, and contact calls to action are excluded.

- Ran `python -B scripts/validate-presentation.py`: the README variants match, the public heading structure is project-only, local paths and gallery anchors resolve, image alternatives are present, eight project tours animate, and all thirteen stills decode.
- Verified that the four supplied logos match their original user-provided PNG files by SHA-256.
- Reviewed project artwork at desktop and mobile widths. Mobile tours show one complete changing interface per project scene.
- Checked the local presentation for image loading and console errors.
- Ran `git diff --check`: no whitespace errors.

The local preview verifies presentation assets and links. It does not verify final GitHub rendering, other browsers, production deployments, backend persistence, LAN connectivity, appointment submissions, or external messaging. Capture sources and limitations are documented in [PROJECT-EVIDENCE.md](PROJECT-EVIDENCE.md).
