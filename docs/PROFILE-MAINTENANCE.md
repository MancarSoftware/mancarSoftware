# Profile maintenance

The root README is the visitor-facing company presentation. `profile/README.md` carries the same presentation for installation in an organization's public `.github` repository. Their image paths differ because the files live at different levels.

## Assets

Keep all visual assets in `profile/assets/`. The public presentation uses an animated GIF hero and divider for image-viewer compatibility, with reduced-motion alternatives selected through picture elements where supported. Essential information remains readable as Markdown. The original SVG hero is retained as an earlier vector concept; it is no longer embedded in the presentation. Regenerate the current artwork with `scripts/build-brand-assets.py` using Python and Pillow on Windows (Segoe UI fonts). GIF playback and reduced-motion selection still require verification in the target GitHub client.

## Publishing

- This repository already uses the account's name, ignoring capitalization. Its root README is the personal-profile version; keep `profile/assets/` with it.
- For an organization, copy the complete `profile/` directory into its public `.github` repository.
- Review the rendered profile on GitHub in light and dark themes and on mobile after publishing.

## Editorial updates

### Evidence and browser review

- The Beauty Business screenshots were captured from the actual public repository at commit `5ae0e3bd3186fa6aee8a703a0cd4b6e359537018`, running locally. The source checkout was kept outside this repository. Its lockfile needed resolution in that temporary checkout before the preview could run; application source was unchanged.
- The screenshots show the template's BarberPro example, including sample ratings, prices, and other business content. The public caption identifies it as a demonstration, not a customer endorsement or a verified business result.
- Clinical project artwork describes workflows documented in the public repositories. It is not an application screenshot. The public user guide, release checklist, and LAN test plan are linked from the respective entries; a test plan is not evidence that all tests have passed.
- `docs/presentation-preview.html` is a local HTML rendering of the complete README with approximate GitHub styling. It includes native copy, disclosure sections, and project images. Its CSS is only for local review and is not embedded in the README.
- Browser review at 390 px and 960 px confirmed that mobile/desktop image variants load, no image is broken, content has no horizontal overflow, and an expandable answer opens. `docs/presentation-mobile-check.png` records the mobile project layout. This is not a published GitHub verification.

The presentation now includes custom SVG service, project, process, and contact panels. Each has a mobile variant selected below 600 px through `picture` sources. Regenerate these panels and both README files with `scripts/build-presentation.py` (Python, Pillow, and Windows Segoe UI). Edit the copy in that generator before regenerating. The original animated hero is preserved.

`docs/artwork-desktop.png` and `docs/artwork-mobile.png` are artwork contact sheets, not screenshots of GitHub rendering. PNG copies are inspection artifacts; the README embeds the SVG versions. Native project summaries, navigation, and toolkit text are not included in these contact sheets. Validate the final composition and responsive source selection on GitHub after publishing.

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
