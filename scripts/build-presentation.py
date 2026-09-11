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
    p.text(32,72,'Different businesses.',38 if mobile else 48,bold=True)
    p.text(32,124,'Specific solutions.',38 if mobile else 48,bold=True)
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
    for i,(title,body) in enumerate([('Understand.','Start with the real workflow.'),('Design.','Make everyday use feel clear.'),('Engineer.','Build foundations that evolve.')]):
        x=32 if mobile else 32+i*350
        y=86+i*101 if mobile else 105
        p.text(x,y,title,36,bold=True)
        p.text(x,y+49,body,23 if mobile else 21,MUTED)
    p.save('mancar-approach'+suffix)
    p=Panel(w,240)
    p.text(32,26,'LET’S TALK / MANCAR SOFTWARE',18,LIME,True)
    p.text(32,78,'What could work better?',37 if mobile else 52,bold=True)
    p.text(32,164,'Tell us about your next project  →',25,LIME)
    p.save('mancar-contact'+suffix)

build_studio(OUT)
build_showcases(OUT)

def picture(name,alt):
    if name.startswith('project-') or name in ('mancar-studio-cover','mancar-capabilities','mancar-approach','mancar-contact','mancar-making'):
        return f'<picture>\n  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/{name}-mobile.png" />\n  <source media="(prefers-reduced-motion: reduce)" srcset="assets/{name}.png" />\n  <source media="(max-width: 600px)" srcset="assets/{name}-mobile.gif" />\n  <img src="assets/{name}.gif" width="100%" alt="{alt}" />\n</picture>'
    extension = 'png' if name == 'mancar-studio' else 'svg'
    return f'<picture>\n  <source media="(max-width: 600px)" srcset="assets/{name}-mobile.{extension}" />\n  <img src="assets/{name}.{extension}" width="100%" alt="{alt}" />\n</picture>'

hero=(ROOT/'profile/README.md').read_text(encoding='utf-8').split('</picture>',1)[0]+'</picture>'
parts=[hero,
    '**Your business has its own way of working. Your software should reflect it.**',
    'Mancar Software designs websites, applications, and business systems around the people who use them—from the first customer inquiry to the work behind the scenes.',
    '[Explore the projects ↓](#selected-work) &nbsp; / &nbsp; [Discuss your project ↗](https://www.instagram.com/mancarsoftware/)',
    '## Selected work',
    picture('mancar-studio-cover','Mancar Software. Made to look good. Built to work. Animated geometric composition representing digital product design.'),
    '[01 OdontoCare](#odontocare) &nbsp; / &nbsp; [02 VetCare Pro](#vetcare-pro) &nbsp; / &nbsp; [03 Alma Vet](#alma-vet) &nbsp; / &nbsp; [04 Casa Nativa](#casa-nativa)'
]
capabilities = [
    picture('mancar-capabilities','What we build: web experiences — websites, landing pages and catalogs; business software — desktop systems and local networks; custom applications — interfaces, services and databases.'),
    '''## Capabilities

**Build your digital presence.** Corporate websites, landing pages, and catalogs that explain your services, express your identity, and guide visitors toward an inquiry. Responsive layouts and clear content help people find what matters on any screen.

**Bring your operations together.** Business applications for records, appointments, inventory, payments, and reporting. We shape the workflow around the people doing the work, with roles and access appropriate to each responsibility.

**Create a product around a specific need.** Custom web applications and desktop software that connect interfaces, business logic, and data. The scope can include authentication, APIs, and integrations with existing tools.

<details>
<summary>Where the software runs</summary>

- **Web:** for products and experiences accessed through a browser.
- **Local desktop:** for work on a dedicated computer, including workflows that need to operate offline.
- **Local network:** for teams sharing a system across computers at the same location.

We choose the setup around connectivity, access, data handling, and maintenance needs. Our featured clinical products demonstrate local and LAN approaches; deployment requirements are defined for each project.

</details>'''
]
project_details = {
    'odontocare': '''**For:** dental clinics managing clinical and administrative work in one place.

**Inside the product:** patient histories, appointments, odontograms, treatments, payments, inventory, and reporting. Its documented workflows also cover roles, audit records, backups, and restoration.

**Built with:** Electron, React, TypeScript, NestJS, PostgreSQL, and Prisma.

<details>
<summary>Deployment and engineering details</summary>

Designed as an installable Windows application with local PostgreSQL storage. The production installer manages the application services so the clinic can work offline. The repository documents verification for critical workflows, packaging, backup restoration, and installation.

</details>''',
    'vetcare': '''**For:** veterinary teams working from one computer or several computers in the same clinic.

**Inside the product:** pet records, clinical histories, appointments, vaccines, treatments, images, and payments. Local network operation lets reception, veterinary staff, and the payment desk work with the shared system.

**Built with:** Electron, Node.js, and PostgreSQL.

<details>
<summary>Deployment and engineering details</summary>

Supports standalone, LAN server, and LAN client modes on Windows. One computer hosts the local services and data; the others connect over the clinic's network. Internet access is not required for this local workflow. The repository includes installation, network configuration, and backup guidance.

</details>''',
    'almavet': '''**For:** Alma Vet veterinary clinic and pet owners requesting care.

**Inside the project:** a React website with an appointment-request flow, server-side validation, bot protection, request storage, and email notifications. Requests are submitted for review; they do not automatically confirm an appointment.

**Built with:** React, Supabase, PostgreSQL, Cloudflare Turnstile, and Resend.''',
    'casanativa': '''**For:** Casa Nativa furniture store and customers exploring pieces for their homes.

**Inside the project:** a furniture catalog with product images and color variants, an administration area for publishing products, and tools for space proposals and customer inquiries.

**Built with:** React, TypeScript, Vite, and Supabase.'''
}
project_evidence = {
    'odontocare': '[Read the user guide](https://github.com/MancarSoftware/odonto_care/blob/main/docs/USER_GUIDE.md) · [Review the release checklist](https://github.com/MancarSoftware/odonto_care/blob/main/docs/RELEASE_CHECKLIST.md)',
    'vetcare': '[Review the LAN test plan](https://github.com/MancarSoftware/vetCarePro/blob/main/docs/release-1.1-lan-test-plan.md) · [Read the setup guide](https://github.com/MancarSoftware/vetCarePro#readme)',
    'almavet': '[Read the architecture and setup guide](https://github.com/MancarSoftware/veterinaria#readme)',
    'casanativa': '[Read the catalog and administration guide](https://github.com/MancarSoftware/muebleria#readme)'
}
for slug,name,url,description in [
    ('odontocare','OdontoCare','odonto_care','Patient records, appointments, treatments, and payments in a Windows application that works offline.'),
    ('vetcare','VetCare Pro','vetCarePro','Veterinary software for a single PC or a connected clinic, with records and payments available over the local network.'),
    ('almavet','Alma Vet','veterinaria','A veterinary clinic website that connects pet owners with the clinic through a structured appointment-request process.'),
    ('casanativa','Casa Nativa','muebleria','A furniture store website with an editable catalog, color variants, and customer inquiry workflows.')]:
    parts += ['### '+name,'<a href="https://github.com/MancarSoftware/'+url+'">\n'+picture('project-'+slug,name+' interface tour: '+{'odontocare':'patient records, clinical history, and the daily agenda.','vetcare':'patients, clinical history, and the record entry form.','almavet':'the clinic homepage, service discovery, and appointment request form.','casanativa':'the storefront, furniture catalog, product details, and a saved selection.'}[slug])+'\n</a>']
    parts += [description,'<sub>Actual repository interface · '+('Fictional clinical data' if slug in ('odontocare','vetcare') else 'Repository demo content')+' · Original Spanish interface</sub>',
        '[View the still-image tour](../docs/PROJECT-GALLERY.md#'+{'odontocare':'odontocare','vetcare':'vetcare-pro','almavet':'alma-vet','casanativa':'casa-nativa'}[slug]+') &nbsp; / &nbsp; [Explore the repository →](https://github.com/MancarSoftware/'+url+')',
        project_details[slug],project_evidence[slug]]
parts += capabilities
parts += [
    '## From workflow to working interface',
    picture('mancar-making','An illustrated Alma Vet design process: define the request workflow, organize the form, and connect it to the real appointment request interface.'),
    'A service inquiry becomes a clear path: choose the service, provide the details, and send a request for the clinic to review. The workflow and wireframe above are explanatory reconstructions; the final screen is captured from Alma Vet’s repository.',
    '''## Working together

**01 / Define the right scope.** Start with the business goal, the users, and the current workflow. Identify the essential features, constraints, integrations, and what a successful first release needs to achieve.

**02 / Make the experience concrete.** Organize the information and map the important user journeys. Establish a visual direction and review the key screens before expanding the implementation.

**03 / Build in useful increments.** Develop around complete workflows, with clear responsibilities in the code and feedback as the product takes shape. Add complexity when the requirements justify it.

**04 / Validate and prepare delivery.** Check the critical paths, permissions, error handling, and deployment setup. Define the installation and operating documentation needed for the agreed environment.

<details>
<summary>What we plan for beyond the first release</summary>

- **Maintainability:** readable code, clear boundaries, and documented setup.
- **Usability:** accessible interaction, useful feedback, and recovery from errors.
- **Data protection:** input validation, appropriate access controls, and backup planning where relevant.
- **Performance:** attention to real loading, rendering, and data-access bottlenecks.
- **Handover:** installation, configuration, and operating instructions appropriate to the product.

Hosting, ongoing maintenance, future features, and support arrangements belong in the project scope so expectations are clear from the beginning.

</details>''',
    '''## Decisions that shape the product

**Connectivity is a requirement.** A public website and a clinic's internal system have different needs. We consider where people work, how they connect, and what must remain available when the internet is down.

**Recovery belongs in the plan.** Installation, backups, updates, and operating instructions affect the usefulness of a business system as much as its screens. The clinical project guides above make these concerns concrete.

**Design continues after the first screen.** Navigation, validation, empty states, and feedback deserve the same attention as the opening impression. The aim is a product people can understand and keep using.''',
    '## Meet Mancar',
    picture('mancar-studio','Meet Mancar Software. Close to the work. Clear about the craft. Websites, applications, and business systems.'),
    'We are Mancar Software. Our work connects two sides of a business: the experience customers see and the software a team uses behind the scenes. The four projects above reflect that focus—from a furniture catalog and a clinic website to tools for managing daily clinical work.',
    'Our approach starts with a conversation about the people, the workflow, and the problem. We bring design and development into that same conversation, make the key screens concrete, and build around a useful first release.',
    '**For a project conversation:** tell us what is difficult today. **For a collaboration:** show us what you build and where you would like to contribute.',
    '## Our toolkit',
    'A focused ecosystem reflected in the projects above. We choose tools around the product’s needs, deployment environment, and long-term maintenance.',
    '**Interface** &nbsp; React · TypeScript · JavaScript · Tailwind CSS<br>\n**Application** &nbsp; Node.js · NestJS · Electron<br>\n**Foundation** &nbsp; PostgreSQL · Prisma · Docker · Git',
    '''## Before we start

<details>
<summary>Do I need a complete specification?</summary>

Start with the problem, the people affected, and an example of how the work happens today. Screenshots, spreadsheets, or a description of your existing process can help shape the first scope.

</details>

<details>
<summary>Can the software work with our existing tools?</summary>

We first review the available APIs, data formats, access permissions, and workflow. Integration and data migration need to be scoped around what those systems actually support.

</details>

<details>
<summary>What determines the timeline and budget?</summary>

The critical workflows, design scope, integrations, data migration, and deployment environment. Sharing a target date and budget range helps define a realistic first release and what can follow later.

</details>

<details>
<summary>What happens after delivery?</summary>

Maintenance, hosting, updates, and support responsibilities are defined in the project scope. They should be clear before development starts, alongside the documentation and handover requirements.

</details>''',
    '<a href="https://www.instagram.com/mancarsoftware/">\n'+picture('mancar-contact','What does your team still manage manually? Show us one task you would like to improve. Contact Mancar Software on Instagram.')+'\n</a>',
    '''## What does your team still manage manually?

An appointment book, a spreadsheet, a product inquiry, or a task that depends on copying the same information twice. Tell us where the work gets difficult and who it affects.

**Start with one message:** “We run a [business]. Today we manage [task] using [current tool]. We would like to make [outcome] easier.”

Helpful details include the features you have in mind, existing tools or data, whether the product needs to work locally or online, and your target timeline and budget range.

**For developers and collaborators:** explore the repositories for stack choices, setup instructions, and implementation details. For a collaboration proposal, introduce your area of expertise and the project you would like to discuss.''',
    '[Discuss a project on Instagram →](https://www.instagram.com/mancarsoftware/) &nbsp; / &nbsp; [Browse our repositories](https://github.com/MancarSoftware?tab=repositories)',
    '<sub>MANCAR SOFTWARE · Designed for people. Engineered for business.</sub>'
]
content='\n\n'.join(parts)+'\n'
(ROOT/'profile/README.md').write_text(content,encoding='utf-8')
(ROOT/'README.md').write_text(content.replace('"assets/','"profile/assets/').replace('(../docs/','(docs/'),encoding='utf-8')

# Inspect the actual artwork together at desktop and phone widths.
names=['mancar-header-static','mancar-studio-cover','project-odontocare','project-vetcare','project-almavet','project-casanativa','mancar-capabilities','mancar-making','mancar-studio','mancar-contact']
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
