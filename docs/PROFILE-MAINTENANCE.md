# Profile Maintenance

The root `README.md` is the personal-profile version. `profile/README.md` is the organization-profile version. They contain the same project catalogue, with paths adjusted for their respective directories.

## Public Scope

The public profile contains only the Mancar header, the project index, and four verified project entries: OdontoCare, VetCare Pro, Alma Vet, and Casa Nativa. Keep service descriptions, generic studio claims, process explanations, FAQs, contact prompts, and unverified projects out of the profile.

Every project entry must include a repository link, an accurate description, and only claims supported by the repository. Keep the labels in title case: **Designed For**, **Core Functionality**, and **Built With**.

## Assets

Keep project tours, static reduced-motion alternatives, supplied logos, and captured stills in `profile/assets/`. The four supplied logos in `profile/assets/logos/` must remain byte-for-byte unchanged. The public project panels use animated GIFs with PNG alternatives; the header has its own static alternative.

Regenerate the presentation with `python -B scripts/build-presentation.py`, then render the local review with `node scripts/render-preview.mjs`. The generator rebuilds both README variants, the project GIFs and PNGs, the still-image gallery, and project-only contact sheets.

## Publishing

- For a personal profile, keep the root README and `profile/assets/` together in this repository.
- For an organization profile, copy `profile/` and the two project documentation files into the public `.github` repository, preserving their directory structure.
- Review the published profile on GitHub in light and dark themes and on mobile.

## Verification

Run `python -B scripts/validate-presentation.py` after generation. It checks that README variants stay synchronized, only the approved project headings remain, all local paths and gallery anchors resolve, alternatives include accessible text, the eight project tours animate, and all thirteen stills decode.

`docs/PROJECT-EVIDENCE.md` records capture sources and limitations. Add a project only after its description and public repository link have been verified.

## Suggested Commit Descriptions

- `commit(profile): focus the company profile on verified projects`
- `commit(content): update project evidence and repository links`
- `commit(docs): document project-only profile maintenance`
