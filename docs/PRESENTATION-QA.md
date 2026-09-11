# Presentation verification — September 2026

The expanded presentation includes four animated project tours, an editorial studio introduction, a concise delivery process, and a task-focused contact invitation. Thirteen source interface states are available as still images.

- Ran `python -B scripts/validate-presentation.py`: README variants match, local images and gallery targets exist, gallery anchors resolve, image alternatives and reduced-motion PNG sources are present, eight project tours and eight supporting motion loops have the expected dimensions and timing, and all 13 stills decode.
- Compared all four stored logos against the original user-supplied PNGs by SHA-256: unchanged.
- Reviewed captured interfaces and generated desktop/mobile artwork. Corrected capture-host margins and replaced the repeated mobile detail crop with one complete changing interface. Native Spanish product interfaces remain intact.
- Completed an editorial English review across the public README, project descriptions, calls to action, accessibility text, gallery captions, and text embedded in generated artwork. Terminology now follows consistent American English and parallel project structure.
- Checked local presentation DOM at 1080 px: all ten images loaded, desktop variants selected, no horizontal overflow.
- Checked the local presentation at 390 px: nine mobile sources selected, no broken images, no horizontal overflow. Saved the rendered mobile screenshot as `presentation-mobile-check.png`.
- Followed the presentation's still-image tour link to its correct gallery anchor. All 13 gallery images loaded, with no overflow or captured console errors.
- Opened a FAQ disclosure using Enter and verified its open state.
- Checked `git diff --check`: no whitespace errors.
- Project screens hold for four seconds and change through three eased transition frames over 360 ms. Supporting studio artwork uses approximately 7.9-second loops with eased movement. This is timing validation, not a network or Core Web Vitals benchmark.

Static source selection is encoded in `picture`; the operating system's reduced-motion preference was not changed during this review. The original dark logo colors remain as supplied, so some marks have low contrast on graphite; each project also has a native text heading. Desktop products are shown through complete desktop captures in both responsive compositions, not claimed mobile product implementations.

These are local interface and presentation checks. Final GitHub light/dark rendering, other browsers, screen-reader operation, production deployments, backend persistence, LAN connectivity, appointment submission, and external messaging were not tested. Capture adapters and source revisions are documented in [PROJECT-EVIDENCE.md](PROJECT-EVIDENCE.md).
