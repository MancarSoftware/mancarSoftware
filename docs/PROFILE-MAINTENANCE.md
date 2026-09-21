# Profile Maintenance

The root `README.md` is the personal-profile version. `profile/README.md` is the organization-profile version. Both default to Spanish. English, Simplified Chinese, and Hindi editions use `.en.md`, `.zh.md`, and `.hi.md` suffixes in both locations. The language buttons link to complete editions, with paths adjusted for their respective directories.

## Localization

`scripts/build-presentation.py` holds the English source copy; `scripts/translations.py` contains the translations. `scripts/localize_presentation.py` generates the four editions and galleries. Translate prose, accessible labels, buttons, and graphic captions together. Original logos and captured project interfaces remain unchanged; captions explicitly identify the original Spanish interface. Linked external repositories and technical source documentation retain their original language.

English artwork stays in `profile/assets/`; Spanish, Chinese, and Hindi artwork lives in `es/`, `zh/`, and `hi/` subdirectories. Each edition includes desktop/mobile GIFs and reduced-motion PNGs. Language buttons are shared under `languages/`. `localized-labels.json` records the rendered captions for accessibility and validation.

Install the build dependencies with `python -m pip install -r scripts/requirements.txt`. Artwork generation uses Windows Segoe UI, Microsoft YaHei, and Nirmala UI fonts from `C:/Windows/Fonts`. HarfBuzz and FreeType shape Hindi conjuncts correctly even when Pillow lacks RAQM. Do not redistribute the font files.

Use `python -B scripts/build-presentation.py --locale es` to rebuild one edition, or omit the option for all four. Use `--content-only` only when no graphic captions changed and existing label manifests are present. Always regenerate previews and run validation afterwards.

## Public Scope

The public profile combines the Mancar company story with four verified projects: OdontoCare, VetCare Pro, Alma Vet, and Casa Nativa. Place selected projects immediately after the introduction. Preserve the cover, company artwork, delivery timeline, post-launch support, and contact invitation alongside project evidence. Outcomes and working principles are consolidated into the introduction and delivery copy. Company information remains visible, with native disclosures for extra detail. Do not add unsupported claims or reintroduce Beauty Business.

Every project entry must include a repository link, an accurate description, and only claims supported by the repository. Keep the labels in title case: **Designed For**, **Core Functionality**, and **Built With**.

## Assets

The starting-points and first-conversation panels explain when to contact Mancar and what follows. Keep their wording aligned with the actual company process. Each project also has an expandable “Feature in Focus” view that reuses an existing captured still; keep these closed by default to preserve the single changing image in the main tour. Both panels retain their desktop/mobile GIF animations, with PNG alternatives for reduced-motion preferences.

Public presentation links are rendered by `scripts/link_buttons.py` as reusable, high-resolution PNG buttons in `profile/assets/buttons/`. Coral identifies primary actions; deep teal and ivory identify navigation, reference, and contact links. Link destinations and accessible image labels remain in the README. Keep each button under 305 CSS pixels wide so groups wrap on mobile without custom CSS. Do not recolor links only in the local preview; the image treatment must also work on GitHub.

Keep studio panels, project tours, static reduced-motion alternatives, supplied logos, and captured stills in `profile/assets/`. The four supplied logos in `profile/assets/logos/` must remain byte-for-byte unchanged. Every displayed animation has a desktop/mobile PNG alternative and descriptive alt text. `scripts/studio_motion.py` builds eight animated company panels; `scripts/project_showcases.py` builds repository tours. `scripts/project_story.py` builds the Casa Nativa story from catalog, product-detail, and saved-selection captures, with 5.5-second reading holds and brief dissolves. Keep its three stages available as visible README text and through the still-image gallery.

Regenerate with `python -B scripts/build-presentation.py`, then run `node scripts/render-preview.mjs` sequentially. The generator rebuilds all README editions, studio and project GIF/PNG assets, buttons, and translated still-image galleries. The older artwork contact sheets are English reference overviews, not localized deliverables. Studio loops use 64 frames at 120 ms per frame.

## Publishing

- For a personal profile, keep the root README and `profile/assets/` together in this repository.
- For an organization profile, copy all of `profile/`, all four `docs/PROJECT-GALLERY*.md` editions, and `docs/PROJECT-EVIDENCE.md` into the public `.github` repository, preserving their directory structure.
- Review the published profile on GitHub in light and dark themes and on mobile.

## Verification

Run `python -B scripts/validate-presentation.py` after generation. It checks all four synchronized README editions, language switches, project entries, local paths and gallery anchors, accessible text, static alternatives, animation dimensions and timing, glyph coverage, and captured stills. Review desktop and mobile previews visually as well. The default preview is Spanish; other previews use `.en.html`, `.zh.html`, and `.hi.html` suffixes.

`docs/PROJECT-EVIDENCE.md` records capture sources and limitations. Add a project only after its description and public repository link have been verified.

## Suggested Commit Descriptions

- `commit(profile): restore expressive studio animations and visual storytelling`
- `commit(content): update project evidence and repository links`
- `commit(docs): document studio and project presentation maintenance`
