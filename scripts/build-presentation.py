"""Generate matching SVG/PNG editorial panels and responsive README files."""
from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont

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
    def save(self,name):
        (OUT/f'{name}.svg').write_text(''.join(self.svg)+'</svg>',encoding='utf-8')
        self.image.save(OUT/f'{name}.png')

for mobile in (False,True):
    suffix='-mobile' if mobile else ''
    w=560 if mobile else 1080
    p=Panel(w,530 if mobile else 390)
    p.text(32,28,'01 / WHAT WE BUILD',18,LIME,True)
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

    projects=[('odontocare','01','OdontoCare','DENTAL PRACTICE SOFTWARE','Local-first. Practice-focused.','PATIENTS / APPOINTMENTS / TREATMENTS'),('vetcare','02','VetCare Pro','VETERINARY SOFTWARE','One clinic. Connected teams.','DESKTOP / LOCAL NETWORK / OFFLINE'),('beauty','03','Beauty Business','WEBSITES FOR SERVICE BUSINESSES','Make the first impression count.','BARBERSHOPS / SALONS / SPAS')]
    for slug,num,name,category,tag,meta in projects:
        p=Panel(w,280 if mobile else 270)
        p.line(0,0,0,p.h,LIME,5)
        p.text(32,28,category,17,LIME,True)
        p.text(30,76,name,48 if mobile else 58,bold=True)
        p.text(32,150,tag,25 if mobile else 28,MUTED)
        p.line(32,208,w-32,208)
        p.text(32,230,meta,14 if mobile else 17,MUTED)
        if not mobile:
            p.text(900,34,num,88,LINE,True)
            # Abstract structural motif, deliberately not a product screenshot.
            for j in range(3):
                p.line(770+j*35,174-j*30,875+j*35,174-j*30,LIME if j==1 else LINE,3)
        p.save('project-'+slug+suffix)

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

def picture(name,alt):
    return f'<picture>\n  <source media="(max-width: 600px)" srcset="assets/{name}-mobile.svg" />\n  <img src="assets/{name}.svg" width="100%" alt="{alt}" />\n</picture>'

hero=(ROOT/'profile/README.md').read_text(encoding='utf-8').split('</picture>',1)[0]+'</picture>'
parts=[hero,'<p><strong>Websites, applications, and business systems for the way you work.</strong><br>We bring product design and software engineering together for businesses and SMEs.</p>', '[Selected work](#selected-work) &nbsp; / &nbsp; [Our toolkit](#our-toolkit) &nbsp; / &nbsp; [Let’s talk](https://www.instagram.com/mancarsoftware/)',picture('mancar-capabilities','What we build: web experiences — websites, landing pages and catalogs; business software — desktop systems and local networks; custom applications — interfaces, services and databases.'),'## Selected work']
for slug,name,url,description in [
    ('odontocare','OdontoCare','odonto_care','Patient records, appointments, treatments, and payments in a Windows application that works offline.'),
    ('vetcare','VetCare Pro','vetCarePro','Veterinary software for a single PC or a connected clinic, with records and payments available over the local network.'),
    ('beauty','Beauty Business','beauty-business-template','Adaptable websites for barbershops, salons, and spas, with service listings, galleries, and contact sections.')]:
    parts += ['<a href="https://github.com/MancarSoftware/'+url+'">\n'+picture('project-'+slug,name+' — explore the repository.')+'\n</a>',description+'\n\n[Explore '+name+' →](https://github.com/MancarSoftware/'+url+')']
parts += [picture('mancar-approach','How we build: understand the real workflow; design for clear everyday use; engineer foundations that evolve.'),'## Our toolkit','**Interface** &nbsp; React · TypeScript · Tailwind CSS<br>\n**Application** &nbsp; Node.js · NestJS · Electron<br>\n**Foundation** &nbsp; PostgreSQL · Prisma · Docker · Git','<a href="https://www.instagram.com/mancarsoftware/">\n'+picture('mancar-contact','What could work better? Talk to Mancar Software about your next project on Instagram.')+'\n</a>','[Start a conversation →](https://www.instagram.com/mancarsoftware/) &nbsp; / &nbsp; [Browse our repositories](https://github.com/MancarSoftware?tab=repositories)','<sub>MANCAR SOFTWARE · Designed for people. Engineered for business.</sub>']
content='\n\n'.join(parts)+'\n'
(ROOT/'profile/README.md').write_text(content,encoding='utf-8')
(ROOT/'README.md').write_text(content.replace('"assets/','"profile/assets/'),encoding='utf-8')

# Inspect the actual artwork together at desktop and phone widths.
names=['mancar-header-static','mancar-capabilities','project-odontocare','project-vetcare','project-beauty','mancar-approach','mancar-contact']
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
