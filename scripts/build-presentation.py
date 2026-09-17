"""Generate the project-led Mancar Software profile and its visual previews."""
from pathlib import Path

from PIL import Image

from project_showcases import build_showcases


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'profile' / 'assets'


def project_picture(slug, alt):
    return f'''<a href="https://github.com/MancarSoftware/{PROJECTS[slug]["repository"]}">
<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/project-{slug}-mobile.png" />
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/project-{slug}.png" />
  <source media="(max-width: 600px)" srcset="assets/project-{slug}-mobile.gif" />
  <img src="assets/project-{slug}.gif" width="100%" alt="{alt}" />
</picture>
</a>'''


PROJECTS = {
    'odontocare': {
        'number': '01', 'name': 'OdontoCare', 'repository': 'odonto_care', 'gallery_anchor': 'odontocare',
        'alt': 'OdontoCare interface tour: patient records, clinical history, and the daily agenda.',
        'summary': 'An offline-ready Windows application for managing patient records, appointments, treatments, and payments.',
        'evidence': 'Interface captured from the repository · Fictional clinical data · Original interface in Spanish',
        'facts': '''**Designed For:** dental clinics managing clinical and administrative work in one place.

**Core Functionality:** patient histories, appointments, odontograms, treatments, payments, inventory, and reporting. The documented workflows also cover user roles, audit records, backups, and restoration.

**Built With:** Electron, React, TypeScript, NestJS, PostgreSQL, and Prisma.

<details>
<summary>Deployment and Engineering Details</summary>

Designed as an installable Windows application with local PostgreSQL storage. The production installer manages the required application services, allowing the clinic to work offline. The repository documents verification procedures for critical workflows, packaging, backup restoration, and installation.

</details>

[Read the User Guide](https://github.com/MancarSoftware/odonto_care/blob/main/docs/USER_GUIDE.md) · [Review the Release Checklist](https://github.com/MancarSoftware/odonto_care/blob/main/docs/RELEASE_CHECKLIST.md)''',
    },
    'vetcare': {
        'number': '02', 'name': 'VetCare Pro', 'repository': 'vetCarePro', 'gallery_anchor': 'vetcare-pro',
        'alt': 'VetCare Pro interface tour: patients, clinical history, and the record entry form.',
        'summary': 'Veterinary practice software for standalone and local network environments, with clinical records, scheduling, and payments accessible across the clinic.',
        'evidence': 'Interface captured from the repository · Fictional clinical data · Original interface in Spanish',
        'facts': '''**Designed For:** veterinary teams working from a single computer or across several computers in the same clinic.

**Core Functionality:** patient records, clinical histories, appointments, vaccinations, treatments, images, and payments. Local network support allows reception, veterinary staff, and the payment desk to access the same system.

**Built With:** Electron, Node.js, and PostgreSQL.

<details>
<summary>Deployment and Engineering Details</summary>

Supports standalone, LAN server, and LAN client modes on Windows. One computer hosts the local services and data, while the others connect through the clinic's network. This local workflow does not require internet access. The repository includes guidance for installation, network configuration, and backups.

</details>

[Review the LAN Test Plan](https://github.com/MancarSoftware/vetCarePro/blob/main/docs/release-1.1-lan-test-plan.md) · [Read the Setup Guide](https://github.com/MancarSoftware/vetCarePro#readme)''',
    },
    'almavet': {
        'number': '03', 'name': 'Alma Vet', 'repository': 'veterinaria', 'gallery_anchor': 'alma-vet',
        'alt': 'Alma Vet interface tour: the clinic homepage, service discovery, and appointment request form.',
        'summary': 'A veterinary clinic website that guides pet owners from service discovery to a structured appointment request.',
        'evidence': 'Interface captured from the repository · Repository demo content · Original interface in Spanish',
        'facts': '''**Designed For:** the Alma Vet clinic and pet owners requesting care.

**Core Functionality:** service discovery and structured appointment requests, supported by server-side validation, bot protection, persistent request storage, and email notifications. Each request is submitted for review and does not automatically confirm an appointment.

**Built With:** React, Supabase, PostgreSQL, Cloudflare Turnstile, and Resend.

[Read the Architecture and Setup Guide](https://github.com/MancarSoftware/veterinaria#readme)''',
    },
    'casanativa': {
        'number': '04', 'name': 'Casa Nativa', 'repository': 'muebleria', 'gallery_anchor': 'casa-nativa',
        'alt': 'Casa Nativa interface tour: the storefront, furniture catalog, product details, and a saved selection.',
        'summary': 'A furniture retail website with an editable catalog, color variants, and structured customer inquiry workflows.',
        'evidence': 'Interface captured from the repository · Repository demo content · Original interface in Spanish',
        'facts': '''**Designed For:** Casa Nativa and customers exploring furniture for their homes.

**Core Functionality:** a furniture catalog with product photography and color variants, an administration area for publishing products, and tools for space proposals and customer inquiries.

**Built With:** React, TypeScript, Vite, and Supabase.

[Read the Catalog and Administration Guide](https://github.com/MancarSoftware/muebleria#readme)''',
    },
}


def project_block(slug):
    project = PROJECTS[slug]
    return '\n\n'.join((
        f'## <a id="{slug}"></a>{project["number"]} / {project["name"]}',
        project_picture(slug, project['alt']),
        project['summary'],
        f'<sub>{project["evidence"]}</sub>',
        f'[View the Still-Image Tour](../docs/PROJECT-GALLERY.md#{project["gallery_anchor"]}) &nbsp; / &nbsp; [Explore the Repository →](https://github.com/MancarSoftware/{project["repository"]})',
        project['facts'],
    ))


def make_contact_sheet(mobile):
    width = 375 if mobile else 900
    suffix = '-mobile' if mobile else ''
    images = []
    for slug in PROJECTS:
        source = Image.open(OUT / f'project-{slug}{suffix}.png')
        images.append(source.resize((width, round(source.height * width / source.width)), Image.Resampling.LANCZOS))
    sheet = Image.new('RGB', (width, sum(image.height for image in images) + 16 * (len(images) - 1)), '#0d1117')
    y = 0
    for image in images:
        sheet.paste(image, (0, y))
        y += image.height + 16
    destination = ROOT / 'docs' / ('artwork-mobile.png' if mobile else 'artwork-desktop.png')
    sheet.save(destination)


build_showcases(OUT)

content = '\n\n'.join((
    '''<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/mancar-header-static.png" />
  <img src="assets/mancar-header.gif" width="100%" alt="Mancar Software. Designed for people. Engineered for business. Animated geometric M." />
</picture>''',
    '# Selected Projects',
    '[01 / OdontoCare](#odontocare) &nbsp; / &nbsp; [02 / VetCare Pro](#vetcare) &nbsp; / &nbsp; [03 / Alma Vet](#almavet) &nbsp; / &nbsp; [04 / Casa Nativa](#casanativa)',
    *(project_block(slug) for slug in PROJECTS),
    '<sub>MANCAR SOFTWARE</sub>',
)) + '\n'

(ROOT / 'profile' / 'README.md').write_text(content, encoding='utf-8')
(ROOT / 'README.md').write_text(content.replace('"assets/', '"profile/assets/').replace('(../docs/', '(docs/'), encoding='utf-8')

for mobile in (False, True):
    make_contact_sheet(mobile)

print('Built project-led presentation and project artwork previews.')
