# Project Profile Verification — September 2026

September 18 additions: “When to Bring Us In,” four expandable project feature views, and the first-contact sequence. Reviewed desktop/mobile artwork for both new panels. The validator passes with twenty studio animations (1.32 MiB combined), static alternatives, existing project media, and the new branded contact link. Browser checks confirmed loaded images, no horizontal overflow at 390 and 840 CSS pixels, and successful expansion/collapse of the clinical-history feature. Feature screenshots reuse existing repository captures and remain collapsed by default.

Branded link update: all 32 presentation text links now use coral or deep-teal image buttons with accessible labels. Verified unchanged destinations, no remaining text-only links in the rendered presentation, all 45 images loaded, keyboard focus on the support/contact actions, and no horizontal overflow at 390 or 1200 CSS pixels. The generator validator checks button dimensions, paths, and unused button assets. These checks cover the local preview; publication on GitHub remains a separate review.

The profile combines eight animated company panels, a featured Casa Nativa story, and the four established project tours. Company content covers purpose, the public team, connected disciplines, outcomes, delivery, working principles, post-launch support, and contact. New company information remains visible, with disclosures for additional detail.

The connected-disciplines and Casa Nativa additions passed the asset validator: sixteen studio animations, two featured-story variants, eight project tours, thirteen captured stills, synchronized README variants, and static alternatives. Studio animations total 0.96 MiB. Inspected both new desktop/mobile compositions, checked all thirteen image sources on mobile, and found no horizontal overflow at 390 or 1200 CSS pixels. No browser console errors were reported. The story preserves a single changing screenshot on mobile and provides its complete narrative as visible text. No studio note or photograph was added.

- Passed `python -B scripts/validate-presentation.py`: matching README variants, paths and gallery anchors, accessible image alternatives, fourteen studio animations, eight project animations, static PNG alternatives, studio media budget, and thirteen captured stills. Studio GIFs total 0.84 MiB across desktop and mobile.
- Verified that the four supplied logos match their original user-provided PNG files by SHA-256.
- Mobile project tours show one complete changing interface per scene. Company panels use separately composed desktop/mobile artwork; their text stays fixed while explanatory geometry moves.
- Checked the local presentation for image loading and console errors.
- Reviewed browser layouts at 1440, 768, and 390 CSS pixels, with no horizontal overflow. Confirmed desktop/mobile source selection and native company-detail expansion. Inspected static artwork for typography and spacing; fixed the timeline marker so it cannot obscure stage numbers.
- Reviewed the added team, principles, and support artwork, then checked the expanded preview at 1200 and 390 CSS pixels. All eleven displayed images load, internal navigation targets resolve, and no console errors or horizontal overflow were found. Team roles and support content were checked against the company About and Support pages.
- Ran `git diff --check`: no whitespace errors.

The local preview verifies presentation assets and links. It does not verify final GitHub rendering, other browsers, production deployments, backend persistence, LAN connectivity, appointment submissions, or external messaging. Capture sources and limitations are documented in [PROJECT-EVIDENCE.md](PROJECT-EVIDENCE.md).
