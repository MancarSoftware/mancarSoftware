# Profile maintenance

The root README is the visitor-facing company presentation. `profile/README.md` carries the same presentation for installation in an organization's public `.github` repository. Their image paths differ because the files live at different levels.

## Assets

Keep the two SVG files in `profile/assets/`. Both include subtle animation and a reduced-motion alternative. Essential information remains readable as Markdown without the images.

## Publishing

- This repository already uses the account's name, ignoring capitalization. Its root README is the personal-profile version; keep `profile/assets/` with it.
- For an organization, copy the complete `profile/` directory into its public `.github` repository.
- Review the rendered profile on GitHub in light and dark themes and on mobile after publishing.

## Editorial updates

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
