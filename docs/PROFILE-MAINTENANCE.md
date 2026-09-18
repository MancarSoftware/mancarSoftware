# Profile Maintenance

The root `README.md` is the personal-profile version. `profile/README.md` is the organization-profile version. They contain the same project catalogue, with paths adjusted for their respective directories.

## Public Scope

The public profile combines the Mancar company story with four verified projects: OdontoCare, VetCare Pro, Alma Vet, and Casa Nativa. Preserve the animated cover, team spread, business outcomes, delivery timeline, working principles, post-launch support, and contact invitation alongside project evidence. Company information remains visible, with native disclosures for extra detail. Do not add unsupported claims or reintroduce Beauty Business.

Every project entry must include a repository link, an accurate description, and only claims supported by the repository. Keep the labels in title case: **Designed For**, **Core Functionality**, and **Built With**.

## Assets

Keep studio panels, project tours, static reduced-motion alternatives, supplied logos, and captured stills in `profile/assets/`. The four supplied logos in `profile/assets/logos/` must remain byte-for-byte unchanged. Every displayed animation has a desktop/mobile PNG alternative and descriptive alt text. `scripts/studio_motion.py` builds the seven company panels; `scripts/project_showcases.py` builds repository tours.

Regenerate with `python -B scripts/build-presentation.py`, then run `node scripts/render-preview.mjs` sequentially. The generator rebuilds both README variants, studio and project GIF/PNG assets, the still-image gallery, and combined artwork contact sheets. Studio loops use 64 frames at 120 ms per frame. Keep their combined desktop/mobile GIF weight below 4 MiB.

## Publishing

- For a personal profile, keep the root README and `profile/assets/` together in this repository.
- For an organization profile, copy `profile/` and the two project documentation files into the public `.github` repository, preserving their directory structure.
- Review the published profile on GitHub in light and dark themes and on mobile.

## Verification

Run `python -B scripts/validate-presentation.py` after generation. It checks synchronized README variants, four project entries, paths and gallery anchors, accessible text, static alternatives, animation dimensions and timing, the studio weight budget, and all thirteen captured stills. Review desktop, tablet, and mobile previews visually as well.

`docs/PROJECT-EVIDENCE.md` records capture sources and limitations. Add a project only after its description and public repository link have been verified.

## Suggested Commit Descriptions

- `commit(profile): restore expressive studio animations and visual storytelling`
- `commit(content): update project evidence and repository links`
- `commit(docs): document studio and project presentation maintenance`
