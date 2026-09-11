"""Generate matching SVG/PNG editorial panels and responsive README files."""
from pathlib import Path
from html import escape
import base64
from PIL import Image, ImageDraw, ImageFont
from studio_motion import build_studio
from project_showcases import build_showcases

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'profile/assets'
BG, FG, MUTED, LIME, LINE = '#101416', '#F0F3ED', '#A1ADA8', '#B4E878', '#344039'

class Panel:
    def __init__(self, width, height):
        self.w, self.h = width, height
        self.image = Image.new('RGB', (width,height), BG)
        self.draw = ImageDraw.Draw(self.image)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="{BG}"/>']
    def text(self,x,y,text,size=24,color=FG,bold=False):
        font=ImageFont.truetype('C:/Windows/Fonts/'+('segoeuib.ttf' if bold else 'segoeui.ttf'),size)
        self.draw.text((x,y),text,font=font,fill=color,anchor='lt')
        self.svg.append(f'<text x="{x}" y="{y}" dominant-baseline="text-before-edge" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(text)}</text>')
    def line(self,x1,y1,x2,y2,color=LINE,width=1):
        self.draw.line((x1,y1,x2,y2),fill=color,width=width)
        self.svg.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}"/>')
    def logo(self, slug):
        """Place the transparent source logo directly on the panel, preserving its ratio."""
        source = OUT / 'logos' / (slug + '.png')
        x, y, width, height = 32, 68, self.w-64, 182
        logo = Image.open(source).convert('RGBA')
        logo.thumbnail((min(width-32,660),height-20),Image.Resampling.LANCZOS)
        left, top = x+16, y+(height-logo.height)//2
        self.image.paste(logo,(left,top),logo)
        data = base64.b64encode(source.read_bytes()).decode('ascii')
        self.svg.append(f'<image x="{left}" y="{top}" width="{logo.width}" height="{logo.height}" preserveAspectRatio="xMidYMid meet" href="data:image/png;base64,{data}"/>')
    def save(self,name):
        (OUT/f'{name}.svg').write_text(''.join(self.svg)+'</svg>',encoding='utf-8')
        self.image.save(OUT/f'{name}.png')

for mobile in (False,True):
    suffix='-mobile' if mobile else ''
    w=560 if mobile else 1080
    # A static editorial introduction lets the hero remain the motion focal point.
    p=Panel(w,270 if mobile else 220)
    p.text(32,24,'01 / SELECTED PROJECTS',17,LIME,True)
    p.text(32,72,'Distinct businesses.',38 if mobile else 48,bold=True)
    p.text(32,124,'Purpose-built software.',38 if mobile else 48,bold=True)
    if not mobile:
        p.text(888,45,'04',92,LIME,True)
    p.text(32,220 if mobile else 190,'CLINICAL SOFTWARE  /  BUSINESS WEBSITES',15,MUTED)
    p.save('mancar-work-intro'+suffix)
    p=Panel(w,530 if mobile else 390)
    p.text(32,28,'02 / WHAT WE BUILD',18,LIME,True)
    p.text(32,76,'Your business.',42 if mobile else 50,bold=True)
    p.text(32,132,'Better connected.',42 if mobile else 50,bold=True)
    services=[('Web experiences','Websites, landing pages & catalogs.'),('Business software','Desktop systems & local networks.'),('Custom applications','Interfaces, services & databases.')]
    for i,(title,body) in enumerate(services):
        x=32 if mobile else 32+i*350
        y=226+i*94 if mobile else 258
        p.line(x,y,x+(496 if mobile else 316),y)
        p.text(x,y+16,title,27 if mobile else 26,bold=True)
        p.text(x,y+53,body,22 if mobile else 18,MUTED)
    p.save('mancar-capabilities'+suffix)

    p=Panel(w,400 if mobile else 260)
    p.text(32,26,'03 / HOW WE BUILD',18,LIME,True)
    for i,(title,body) in enumerate([('Understand.','Begin with the real workflow.'),('Design.','Make everyday tasks intuitive.'),('Engineer.','Build a foundation that can evolve.')]):
        x=32 if mobile else 32+i*350
        y=86+i*101 if mobile else 105
        p.text(x,y,title,36,bold=True)
        p.text(x,y+49,body,23 if mobile else 21,MUTED)
    p.save('mancar-approach'+suffix)
    p=Panel(w,240)
    p.text(32,26,'LET’S TALK / MANCAR SOFTWARE',18,LIME,True)
    p.text(32,78,'What could work better?',37 if mobile else 52,bold=True)
    p.text(32,164,'Tell us about your project  →',25,LIME)
    p.save('mancar-contact'+suffix)

build_studio(OUT)
build_showcases(OUT)

def picture(name,alt):
    if name.startswith('project-') or name in ('mancar-studio-cover','mancar-capabilities','mancar-approach','mancar-contact'):
        return f'<picture>\n  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/{name}-mobile.png" />\n  <source media="(prefers-reduced-motion: reduce)" srcset="assets/{name}.png" />\n  <source media="(max-width: 600px)" srcset="assets/{name}-mobile.gif" />\n  <img src="assets/{name}.gif" width="100%" alt="{alt}" />\n</picture>'
    extension = 'png' if name == 'mancar-studio' else 'svg'
    return f'<picture>\n  <source media="(max-width: 600px)" srcset="assets/{name}-mobile.{extension}" />\n  <img src="assets/{name}.{extension}" width="100%" alt="{alt}" />\n</picture>'

hero=(ROOT/'profile/README.md').read_text(encoding='utf-8').split('</picture>',1)[0]+'</picture>'
parts=[hero,
    '**Every business works differently. Its software should, too.**',
    'Mancar Software designs and develops websites, applications, and business systems around real users and real workflows—from the first customer inquiry to the daily work behind the scenes.',
    '[Explore the projects ↓](#selected-work) &nbsp; / &nbsp; [Discuss your project ↗](https://www.instagram.com/mancarsoftware/)',
    '## Selected Work',
    picture('mancar-studio-cover','Mancar Software. Designed with purpose. Built to perform. An animated geometric composition representing digital product design.'),
    '[01 OdontoCare](#odontocare) &nbsp; / &nbsp; [02 VetCare Pro](#vetcare-pro) &nbsp; / &nbsp; [03 Alma Vet](#alma-vet) &nbsp; / &nbsp; [04 Casa Nativa](#casa-nativa)'
]
capabilities = [
    picture('mancar-capabilities','What we build: web experiences, including websites, landing pages, and catalogs; business software for desktop and local network environments; and custom applications spanning interfaces, services, and databases.'),
    '''## Capabilities

**Build a Clear Digital Presence.** Corporate websites, landing pages, and catalogs that explain your services, express your identity, and guide visitors toward an inquiry. Responsive layouts and focused content make essential information easy to find on any screen.

**Bring Your Operations Together.** Business applications for records, appointments, inventory, payments, and reporting. We shape each workflow around the people doing the work, with access aligned to their responsibilities.

**Create Software for a Specific Need.** Custom web applications and desktop software that connect interfaces, business logic, and data. The scope may include authentication, APIs, and integrations with existing tools.

<details>
<summary>Where the Software Runs</summary>

- **Web:** browser-based products and digital experiences.
- **Local desktop:** dedicated applications, including workflows that must remain available offline.
- **Local network:** shared systems for teams working across several computers at one location.

We select the deployment model according to connectivity, access, data handling, and maintenance requirements. The featured clinical applications illustrate both local and LAN-based approaches; the final deployment is defined for each project.

</details>'''
]
project_details = {
    'odontocare': '''**Designed For:** dental clinics managing clinical and administrative work in one place.

**Core Functionality:** patient histories, appointments, odontograms, treatments, payments, inventory, and reporting. The documented workflows also cover user roles, audit records, backups, and restoration.

**Built With:** Electron, React, TypeScript, NestJS, PostgreSQL, and Prisma.

<details>
<summary>Deployment and Engineering Details</summary>

Designed as an installable Windows application with local PostgreSQL storage. The production installer manages the required application services, allowing the clinic to work offline. The repository documents verification procedures for critical workflows, packaging, backup restoration, and installation.

</details>''',
    'vetcare': '''**Designed For:** veterinary teams working from a single computer or across several computers in the same clinic.

**Core Functionality:** patient records, clinical histories, appointments, vaccinations, treatments, images, and payments. Local network support allows reception, veterinary staff, and the payment desk to access the same system.

**Built With:** Electron, Node.js, and PostgreSQL.

<details>
<summary>Deployment and Engineering Details</summary>

Supports standalone, LAN server, and LAN client modes on Windows. One computer hosts the local services and data, while the others connect through the clinic's network. This local workflow does not require internet access. The repository includes guidance for installation, network configuration, and backups.

</details>''',
    'almavet': '''**Designed For:** the Alma Vet clinic and pet owners requesting care.

**Core Functionality:** service discovery and structured appointment requests, supported by server-side validation, bot protection, persistent request storage, and email notifications. Each request is submitted for review and does not automatically confirm an appointment.

**Built With:** React, Supabase, PostgreSQL, Cloudflare Turnstile, and Resend.''',
    'casanativa': '''**Designed For:** Casa Nativa and customers exploring furniture for their homes.

**Core Functionality:** a furniture catalog with product photography and color variants, an administration area for publishing products, and tools for space proposals and customer inquiries.

**Built With:** React, TypeScript, Vite, and Supabase.'''
}
project_evidence = {
    'odontocare': '[Read the user guide](https://github.com/MancarSoftware/odonto_care/blob/main/docs/USER_GUIDE.md) · [Review the release checklist](https://github.com/MancarSoftware/odonto_care/blob/main/docs/RELEASE_CHECKLIST.md)',
    'vetcare': '[Review the LAN test plan](https://github.com/MancarSoftware/vetCarePro/blob/main/docs/release-1.1-lan-test-plan.md) · [Read the setup guide](https://github.com/MancarSoftware/vetCarePro#readme)',
    'almavet': '[Read the architecture and setup guide](https://github.com/MancarSoftware/veterinaria#readme)',
    'casanativa': '[Read the catalog and administration guide](https://github.com/MancarSoftware/muebleria#readme)'
}
for slug,name,url,description in [
    ('odontocare','OdontoCare','odonto_care','An offline-ready Windows application for managing patient records, appointments, treatments, and payments.'),
    ('vetcare','VetCare Pro','vetCarePro','Veterinary practice software for standalone and local network environments, with clinical records, scheduling, and payments accessible across the clinic.'),
    ('almavet','Alma Vet','veterinaria','A veterinary clinic website that guides pet owners from service discovery to a structured appointment request.'),
    ('casanativa','Casa Nativa','muebleria','A furniture retail website with an editable catalog, color variants, and structured customer inquiry workflows.')]:
    parts += ['### '+name,'<a href="https://github.com/MancarSoftware/'+url+'">\n'+picture('project-'+slug,name+' interface tour: '+{'odontocare':'patient records, clinical history, and the daily agenda.','vetcare':'patients, clinical history, and the record entry form.','almavet':'the clinic homepage, service discovery, and appointment request form.','casanativa':'the storefront, furniture catalog, product details, and a saved selection.'}[slug])+'\n</a>']
    parts += [description,'<sub>Interface captured from the repository · '+('Fictional clinical data' if slug in ('odontocare','vetcare') else 'Repository demo content')+' · Original interface in Spanish</sub>',
        '[View the still-image tour](../docs/PROJECT-GALLERY.md#'+{'odontocare':'odontocare','vetcare':'vetcare-pro','almavet':'alma-vet','casanativa':'casa-nativa'}[slug]+') &nbsp; / &nbsp; [Explore the repository →](https://github.com/MancarSoftware/'+url+')',
        project_details[slug],project_evidence[slug]]
parts += capabilities
parts += [
    '''## Working Together

**01 / Define the Right Scope.** Begin with the business objective, the users, and the current workflow. Identify the essential features, constraints, integrations, and outcomes required for a successful first release.

**02 / Make the Experience Concrete.** Organize the information and map the critical user journeys. Establish a visual direction and review the key screens before expanding the implementation.

**03 / Build in Meaningful Increments.** Develop complete workflows with clear responsibilities in the code, gathering feedback as the product takes shape. Add complexity only when the requirements justify it.

**04 / Validate and Prepare for Delivery.** Verify critical paths, permissions, error handling, and the deployment setup. Prepare the installation and operational documentation required for the agreed environment.

<details>
<summary>What We Plan for Beyond the First Release</summary>

- **Maintainability:** readable code, clear boundaries, and documented setup.
- **Usability:** accessible interaction, useful feedback, and recovery from errors.
- **Data protection:** input validation, appropriate access controls, and backup planning where relevant.
- **Performance:** measured attention to loading time, rendering, and data access.
- **Handover:** installation, configuration, and operating instructions appropriate to the product.

Hosting, ongoing maintenance, future features, and support arrangements are defined in the project scope so expectations remain clear from the outset.

</details>''',
    '''## Decisions That Shape the Product

**Connectivity Is an Architectural Requirement.** A public website and a clinic's internal system have different needs. We consider where people work, how they connect, and which functions must remain available when the internet is down.

**Recovery Belongs in the Plan.** Installation, backups, updates, and operational guidance affect the reliability of a business system as much as its interface does. The clinical project guides above make these considerations concrete.

**Design Extends Beyond the First Screen.** Navigation, validation, empty states, and feedback deserve the same attention as the initial impression. The goal is a product people can understand, trust, and continue using.''',
    '## Meet Mancar',
    picture('mancar-studio','Meet Mancar Software. Close to the work. Clear about the craft. Websites, applications, and business systems.'),
    'Mancar Software connects two sides of a business: the experience customers see and the systems a team relies on behind the scenes. The four projects above reflect that focus—from a furniture catalog and a veterinary clinic website to applications that support daily clinical operations.',
    'Our approach begins with the people, the workflow, and the problem. We bring design and development into the same conversation, make the essential screens concrete, and build toward a focused first release.',
    '**To discuss a project:** describe the challenge you are facing. **To propose a collaboration:** share your work and explain where you would like to contribute.',
    '## Our Toolkit',
    'A focused technology ecosystem reflected in the projects above. We select tools according to product requirements, the deployment environment, and long-term maintenance needs.',
    '**Interface** &nbsp; React · TypeScript · JavaScript · Tailwind CSS<br>\n**Application** &nbsp; Node.js · NestJS · Electron<br>\n**Foundation** &nbsp; PostgreSQL · Prisma · Docker · Git',
    '''## Before We Start

<details>
<summary>Do I need a complete specification?</summary>

Begin with the problem, the people affected, and an example of how the work is handled today. Screenshots, spreadsheets, or a description of the current process can help define the initial scope.

</details>

<details>
<summary>Can the software work with our existing tools?</summary>

We first review the available APIs, data formats, access permissions, and workflows. Integration and data migration are then scoped according to what those systems support.

</details>

<details>
<summary>What determines the timeline and budget?</summary>

The timeline and budget depend on the critical workflows, design scope, integrations, data migration, and deployment environment. A target date and budget range help define a realistic first release and a practical roadmap for later phases.

</details>

<details>
<summary>What happens after delivery?</summary>

Maintenance, hosting, updates, and support responsibilities are defined in the project scope. These responsibilities, together with documentation and handover requirements, should be clear before development begins.

</details>''',
    '<a href="https://www.instagram.com/mancarsoftware/">\n'+picture('mancar-contact','What does your team still manage manually? Show us one task worth improving. Contact Mancar Software on Instagram.')+'\n</a>',
    '''## What Does Your Team Still Manage Manually?

An appointment schedule, a spreadsheet, a product inquiry, or any task that requires entering the same information more than once. Tell us where the process becomes difficult and who it affects.

**Start With One Message:** “We run a [type of business]. Today, we manage [task] with [current tool]. We want to make [desired outcome] easier.”

Helpful context includes the features you have in mind, existing tools or data, whether the product must work locally or online, and your target timeline and budget range.

**For Developers and Collaborators:** explore the repositories for technology choices, setup instructions, and implementation details. When proposing a collaboration, introduce your area of expertise and the project you would like to discuss.''',
    '[Discuss your project on Instagram →](https://www.instagram.com/mancarsoftware/) &nbsp; / &nbsp; [Browse our repositories](https://github.com/MancarSoftware?tab=repositories)',
    '<sub>MANCAR SOFTWARE · Designed for people. Engineered for business.</sub>'
]
content='\n\n'.join(parts)+'\n'
(ROOT/'profile/README.md').write_text(content,encoding='utf-8')
(ROOT/'README.md').write_text(content.replace('"assets/','"profile/assets/').replace('(../docs/','(docs/'),encoding='utf-8')

# Inspect the actual artwork together at desktop and phone widths.
names=['mancar-header-static','mancar-studio-cover','project-odontocare','project-vetcare','project-almavet','project-casanativa','mancar-capabilities','mancar-studio','mancar-contact']
for mobile in (False,True):
    width=375 if mobile else 900
    images=[]
    for name in names:
        suffix='-mobile' if mobile and name!='mancar-header-static' else ''
        im=Image.open(OUT/(name+suffix+'.png'))
        images.append(im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS))
    sheet=Image.new('RGB',(width,sum(im.height for im in images)+16*(len(images)-1)),'#0d1117')
    y=0
    for im in images: sheet.paste(im,(0,y)); y+=im.height+16
    preview=ROOT/'docs' / ('artwork-mobile.png' if mobile else 'artwork-desktop.png')
    sheet.save(preview)
print('Built responsive presentation, SVG panels, and artwork previews.')
