# Profile maintenance

The root README is the visitor-facing company presentation. `profile/README.md` carries the same presentation for installation in an organization's public `.github` repository. Their image and gallery paths differ because the files live at different levels.

## Assets

Keep all visual assets in `profile/assets/`. The public presentation uses an animated brand header, cobalt studio cover, capability illustrations, process sequence, and coral invitation. Every animated image has a static reduced-motion alternative selected through `picture` where supported. Essential information remains readable as Markdown. Regenerate the original brand header with `scripts/build-brand-assets.py`; regenerate the presentation with `python -B scripts/build-presentation.py`. Both use Pillow and Windows Segoe UI fonts. GIF playback and reduced-motion selection still require verification in the target GitHub client.

## Publishing

- This repository already uses the account's name, ignoring capitalization. Its root README is the personal-profile version; keep `profile/assets/` with it.
- For an organization, copy the complete `profile/` directory and `docs/PROJECT-GALLERY.md` and `docs/PROJECT-EVIDENCE.md` into its public `.github` repository, keeping the same directory structure.
- Review the rendered profile on GitHub in light and dark themes and on mobile after publishing.

## Editorial updates

The latest direction is an expressive software studio with more color and motion across the page. See `docs/ART-DIRECTION.md` for the concept, palette, and composition rules. The cobalt studio cover and four-project index precede the detailed project entries; illustrated capabilities and process follow. Preserve the original transparent logos without added backings. Native project headings provide readable names and anchors for direct navigation. The project logos are stationary; screen sequences demonstrate each product. `scripts/project_showcases.py` controls these tours and the studio introduction.

### Evidence and browser review

- Project tours now use real repository interface captures with fictional clinical data and repository website content. See `docs/PROJECT-EVIDENCE.md` for pinned source revisions, capture adapters, and validation limits. The public user guide, release checklist, and LAN test plan are linked from the respective entries; a test plan is not evidence that all tests have passed.
- `docs/presentation-preview.html` is a local HTML rendering of the complete README with approximate GitHub styling. It includes native copy, disclosure sections, and project images. Its CSS is only for local review and is not embedded in the README.
- Browser review at 390 px and 960 px confirmed that mobile/desktop image variants load, no image is broken, content has no horizontal overflow, and an expandable answer opens. `docs/presentation-mobile-check.png` records the mobile project layout. This is not a published GitHub verification.

The presentation includes custom service, project, process, and contact panels. Each has a mobile variant selected below 600 px through `picture` sources. Regenerate these panels and both README files with `scripts/build-presentation.py` (Python, Pillow, and Windows Segoe UI). Edit the copy in that generator before regenerating. The original animated hero is preserved.

The four supplied project logos are stored unchanged in `profile/assets/logos/`: `odontocare.png`, `vetcare.png`, `almavet.png`, and `casanativa.png`. The generator places each transparent logo proportionally directly on its project panel, without a separate background. Project panels use animated GIFs with static PNG alternatives. Earlier SVG layout drafts are retained as legacy assets and are not used by the presentation. No source logo is redrawn, recolored, or cropped. Alma Vet links to `MancarSoftware/veterinaria`; Casa Nativa links to `MancarSoftware/muebleria`. Their descriptions are based on the public repository documentation.

`scripts/studio_motion.py` draws the orbital studio composition, moving service symbols, connected process, and closing arrow. It is called by `scripts/build-presentation.py`; no extra dependency is needed beyond Pillow. The supporting loops run for approximately 7.9 seconds with eased motion. Project screens hold for four seconds and change through a 360 ms eased dissolve; the illustrated workflow uses a shorter three-second hold. Shared GIF palettes keep stationary artwork stable. `picture` selects desktop/mobile static PNGs when reduced motion is requested by supporting clients. These illustrations are conceptual, not screenshots or claims about a running application's state. Earlier SVG drafts remain available but are not the sources for the new colored motion panels.

`docs/artwork-desktop.png` and `docs/artwork-mobile.png` are static artwork contact sheets, not screenshots of GitHub rendering. The README embeds GIF project tours and studio, service, process, and contact panels with static PNG alternatives. The editorial studio introduction is static. `docs/PROJECT-GALLERY.md` contains reader-controlled stills from every project tour. Native project summaries, navigation, and toolkit text are not included in these contact sheets. Validate the final composition and responsive source selection on GitHub after publishing.

Keep both README files synchronized, preserving their respective image paths. Add projects only with verified descriptions and public repository or case-study links. The current project details come from their public repository READMEs; Instagram comes from the company's GitHub profile.

The following optional contact fields are intentionally confined to this maintenance document. Add them to the presentation only after receiving the real values:

- Website: `TODO_WEBSITE_URL`
- Email: `TODO_CONTACT_EMAIL`
- LinkedIn: `TODO_LINKEDIN_URL`
- WhatsApp: `TODO_WHATSAPP_URL`

GymCare remains excluded until its project details and public link are provided.

## Suggested commit descriptions

- `commit(profile): replace setup copy with the public Mancar Software presentation`
- `commit(content): feature verified projects and add the company contact link`
- `commit(docs): separate profile maintenance from visitor-facing content`

## Regenerating previews

Run `python -B scripts/build-presentation.py`, then `node scripts/render-preview.mjs`. Serve the repository locally and open `docs/presentation-preview.html`. Gallery links in that preview open `docs/project-gallery-preview.html`; GitHub links correctly target the Markdown gallery. The capture process and source revisions are documented in `docs/PROJECT-EVIDENCE.md`.
