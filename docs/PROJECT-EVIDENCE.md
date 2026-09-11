# Project capture sources

The presentation uses actual interfaces rendered locally from the four repositories supplied by Mancar Software. Screens retain their original Spanish text; editorial captions are in English. The animation is an edited tour of captured interface states, not a continuous screen recording.

## Source revisions

| Project | Repository revision | Captured views |
| --- | --- | --- |
| OdontoCare | [b570cbf](https://github.com/MancarSoftware/odonto_care/tree/b570cbf13eac29a1e37802d304b02990d203bd35) | Patient list, clinical history, daily appointments |
| VetCare Pro | [f4f04b8](https://github.com/MancarSoftware/vetCarePro/tree/f4f04b80a930000d81ffb841d8a803cfd0e24caa) | Pet list, clinical history, new clinical entry form |
| Alma Vet | [f7a6f27](https://github.com/MancarSoftware/veterinaria/tree/f7a6f2751468346f44cc79ea5fc0eac019578812) | Homepage, services, appointment request form |
| Casa Nativa | [c7be0ee](https://github.com/MancarSoftware/muebleria/tree/c7be0eee173c308882c256ea29a93826e929d95b) | Homepage, catalog, furniture detail, saved selection |

## What the captures demonstrate

- OdontoCare and VetCare Pro use their original React interface components with capture-only authentication and data adapters. All displayed patient names, clinical entries, appointments, and users are fictional. The adapters reject writes. A fixture health response supplies VetCare Pro's local runtime indicator; this is not a LAN connectivity test.
- Alma Vet uses repository content. The request form was populated with fictional names but was not submitted. The local preview has no production Turnstile or Supabase credentials. The request requires subsequent clinic confirmation; no booking success is implied.
- Casa Nativa uses its built-in fallback catalog and bundled product images. Saving Sofá Olmo to “Mi espacio” was exercised locally. No inquiry was sent and no purchase was made. Prices and availability shown belong to the repository's demonstration content.
- No clinic database, customer records, production API, email service, or external messaging account was connected.
- Existing website photography was rendered as used by the source website. The capture process does not assert that stock photography depicts real staff or premises. The Mancar studio introduction uses editorial artwork, not an invented portrait, staff identity, or location.
- The workflow and wireframe in the “From workflow to working interface” panel are explanatory illustrations inspired by Alma Vet's request form. They are not claimed to be historical project design artifacts.

## Reproduce the source previews

1. Clone each repository at the revision above into a disposable directory named `mancar-project-evidence`. Keep the original repository directory names.
2. Install dependencies inside each clone with `npm install --ignore-scripts --no-audit --no-fund`.
3. Run `python scripts/prepare-capture.py PATH_TO/mancar-project-evidence` once against those disposable clones. The script changes only capture adapters, initial sections, and the capture host; it does not change interface components. Use fresh clones for a rerun.
4. Serve OdontoCare from `apps/desktop` with `node ../../node_modules/vite/bin/vite.js --host 127.0.0.1 --port 4191`.
5. Serve VetCare Pro from `apps/desktop` with `node ../../node_modules/vite/bin/vite.js --config capture.vite.config.mjs` (port 4192).
6. Serve Alma Vet and Casa Nativa with `npm run dev -- --host 127.0.0.1 --port 4193` and port `4194`, respectively.
7. Open each server's `/capture.html`. This host scales an unchanged 1440 × 960 interface into a single browser capture to avoid display-scaling stitching artifacts. Navigate the views listed above and save PNG screenshots into `profile/assets/captures/`, using the existing filenames. Wait for data and entrance animations to settle. Do not submit external forms.
8. Run `python -B scripts/build-presentation.py` to regenerate showcase GIFs, static alternatives, the still-image gallery, artwork contact sheets, and both README files. Run `node scripts/render-preview.mjs` for the local presentation and gallery previews. The renderer uses the bundled Marked module; another installation can be supplied through `MARKED_MODULE` as a module URL.

## Asset handling

Raw captures are retained beside clean stills. Composition removes only the capture-host margin. Mobile showcase panels present one complete interface at a time, matching the desktop tour without implying that the desktop products have a mobile interface. Supplied project logos remain byte-for-byte unchanged, with their transparency and original colors preserved.

Project scenes hold for 4.2 seconds, followed by a 360 ms crossfade. Full-resolution stills provide a reader-controlled alternative. Reduced-motion picture sources select PNGs in supporting clients. Backend correctness, production deployment, and final GitHub rendering are outside these local capture checks.
