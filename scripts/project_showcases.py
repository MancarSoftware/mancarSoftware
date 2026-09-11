"""Compose repository interface captures into readable, GitHub-native visual tours."""
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageOps
from studio_motion import text, DARK, WHITE, MUTED, CYAN, LIME, CORAL

PROJECTS = {
 'odontocare': dict(name='OdontoCare', number='01', color='#54DCEC', category='DENTAL PRACTICE SOFTWARE',
  headline=['The patient.', 'The whole picture.'],
  steps=['Meet the patient','Review the history','Plan the next visit'],
  captions=['Records and clinical context, together.', 'A history that stays with the patient.', 'Appointments in a clear daily view.'],
  crops=[(580,210,910,585),(580,300,910,610),(185,205,900,560)]),
 'vetcare': dict(name='VetCare Pro', number='02', color='#57D7BC', category='VETERINARY DESKTOP SOFTWARE',
  headline=['Every patient.', 'A connected story.'],
  steps=['Find the patient','Follow the history','Prepare an entry'],
  captions=['Patients and their owners, connected.', 'Clinical context across each visit.', 'A structured place for the next entry.'],
  crops=[(185,225,675,545),(375,210,905,610),(230,60,720,540)]),
 'almavet': dict(name='Alma Vet', number='03', color='#7DAEFF', category='VETERINARY CLINIC WEBSITE',
  headline=['From a first visit', 'to a request for care.'],
  steps=['Meet the clinic','Explore services','Prepare a request'],
  captions=['A clear introduction to the clinic.', 'Find the right starting point for care.', 'Request a visit; the clinic confirms it.'],
  crops=[(45,85,500,495),(45,85,870,525),(450,125,895,595)]),
 'casanativa': dict(name='Casa Nativa', number='04', color='#ECAA8C', category='FURNITURE STORE & DIGITAL CATALOG',
  headline=['Find your piece.', 'Make room for it.'],
  steps=['Feel the space','Explore the catalog','Inspect a piece','Save a selection'],
  captions=['An editorial introduction to the store.', 'Browse pieces, categories, and prices.', 'Materials, dimensions, and color choices.', 'Build a selection before an inquiry.'],
  crops=[(90,145,850,540),(45,190,890,610),(465,135,875,590),(50,300,905,610)]),
}

def capture(path):
    """Remove only the outer capture-host margin, never alter interface content."""
    image = Image.open(path).convert('RGB')
    # The browser may color-manage the host background by a channel value.
    background = image.getpixel((image.width-1,image.height-1))
    diff = ImageChops.difference(image, Image.new('RGB', image.size, background))
    bbox = diff.getbbox()
    return image.crop(bbox) if bbox else image

def logo(im, path, xy, maxsize):
    source=Image.open(path).convert('RGBA')
    source.thumbnail(maxsize,Image.Resampling.LANCZOS)
    im.paste(source,xy,source)

def tour_scene(out,slug,project,index,mobile):
    w,h=(560,850) if mobile else (1080,950)
    im=Image.new('RGB',(w,h),DARK); d=ImageDraw.Draw(im); c=project['color']
    d.rectangle((0,0,w,5),fill=c)
    text(d,(32,28),project['number']+' / '+project['category'],14 if mobile else 17,c,True)
    logo(im,out/'logos'/f'{slug}.png',(32,70),(330 if mobile else 410,92))
    if mobile:
        for j,line in enumerate(project['headline']): text(d,(32,179+j*43),line,37,WHITE,True)
    else:
        for j,line in enumerate(project['headline']): text(d,(515,74+j*49),line,40,WHITE,True)
    screen=capture(out/'captures'/f'{slug}-{index+1:02}.png')
    if mobile:
        # A complete overview and a separate detail crop; no fake mobile product UI.
        overview=ImageOps.contain(screen,(496,327),Image.Resampling.LANCZOS)
        im.paste(overview,((w-overview.width)//2,275))
        crop=project['crops'][index]
        focus=screen.crop(crop)
        focus=ImageOps.fit(focus,(496,130),Image.Resampling.LANCZOS,centering=(.5,.35))
        im.paste(focus,(32,643))
        text(d,(32,618),'DETAIL / '+project['steps'][index].upper(),13,c,True)
        text(d,(32,794),f'{index+1:02} / '+project['steps'][index],23,WHITE,True)
        text(d,(32,831),'REPOSITORY INTERFACE / DEMO CONTENT',12,MUTED)
    else:
        stepwidth=1016/len(project['steps'])
        for n,step in enumerate(project['steps']):
            x=32+round(n*stepwidth)
            d.line((x,204,x+stepwidth-18,204),fill=c if n==index else '#344039',width=3)
            text(d,(x,224),f'{n+1:02}  {step}',20,c if n==index else MUTED,n==index)
        screenshot=ImageOps.contain(screen,(1016,616),Image.Resampling.LANCZOS)
        im.paste(screenshot,((w-screenshot.width)//2,268))
        # Footer lives on the screenshot-free strip.
        d.rectangle((0,899,w,h),fill=DARK)
        text(d,(32,913),project['captions'][index],22,WHITE,True)
        text(d,(805,921),'REPOSITORY PREVIEW / DEMO',12,MUTED)
    return im

def save_tour(scenes,stem):
    # Long holds make screen details legible. Only transitions add extra frames.
    scenes[0].save(stem.with_suffix('.png'))
    frames=[];durations=[]
    for i,current in enumerate(scenes):
        frames.append(current);durations.append(4200)
        following=scenes[(i+1)%len(scenes)]
        for j in range(1,3):
            frames.append(Image.blend(current,following,j/3));durations.append(180)
    strip=Image.new('RGB',(256*len(scenes),192))
    for i,scene in enumerate(scenes): strip.paste(scene.resize((256,192)),(256*i,0))
    palette=strip.quantize(colors=256)
    indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
    indexed[0].save(stem.with_suffix('.gif'),save_all=True,append_images=indexed[1:],
                    duration=durations,loop=0,optimize=True,disposal=1)

def method_scene(out,stage,mobile):
    w,h=(560,1070) if mobile else (1080,550)
    im=Image.new('RGB',(w,h),DARK);d=ImageDraw.Draw(im)
    text(d,(32,27),'INSIDE THE STUDIO / FROM WORKFLOW TO SCREEN',14,CYAN,True)
    text(d,(32,72),'Clarity takes shape.',42 if mobile else 58,WHITE,True)
    labels=['01 / THE WORKFLOW','02 / THE EXPERIENCE','03 / THE INTERFACE']
    for i,label in enumerate(labels):
        x=32 if mobile else 32+i*350; y=166+i*290 if mobile else 176
        text(d,(x,y),label,18,[CYAN,LIME,CORAL][i] if i==stage else MUTED,True)
        width=496 if mobile else 316
        d.rectangle((x,y+36,x+width,y+245),outline=[CYAN,LIME,CORAL][i] if i==stage else '#344039',width=2)
        if i==0:
            for k,line in enumerate(['Choose a service','Request a visit','Clinic reviews']):
                dy=y+61+k*57
                d.ellipse((x+20,dy,x+29,dy+9),fill=CYAN)
                text(d,(x+44,dy-4),line,24 if mobile else 21,WHITE)
                if k<2:d.line((x+24,dy+15,x+24,dy+46),fill='#344039',width=2)
        elif i==1:
            text(d,(x+20,y+56),'Appointment request',22,WHITE,True)
            for k in range(3):
                yy=y+101+k*38
                d.line((x+20,yy-8,x+95,yy-8),fill=MUTED,width=2)
                d.rectangle((x+20,yy,x+width-20,yy+23),outline=LIME,width=1)
        else:
            actual=capture(out/'captures/almavet-03.png').crop((455,123,895,570))
            actual=ImageOps.fit(actual,(width-4,205),Image.Resampling.LANCZOS,centering=(.5,.1))
            im.paste(actual,(x+2,y+38))
    text(d,(32,h-48),'ALMA VET / AN ILLUSTRATED PROCESS',16,MUTED)
    return im

def about(out,mobile):
    w,h=(560,470) if mobile else (1080,360)
    im=Image.new('RGB',(w,h),'#1B2C2B');d=ImageDraw.Draw(im)
    text(d,(32,30),'MEET MANCAR / DESIGN & DEVELOPMENT',16,LIME,True)
    lines=['Close to the work.', 'Clear about the craft.']
    for i,line in enumerate(lines):text(d,(32,90+i*61),line,42 if mobile else 58,WHITE,True)
    text(d,(32,264 if mobile else 259),'Websites. Applications. Business systems.',21 if mobile else 25,MUTED)
    text(d,(32,316 if mobile else 307),'Thoughtful design. Practical software.',22,LIME)
    if mobile:text(d,(32,403),'MANCAR SOFTWARE',22,WHITE,True)
    else:
        # Two precise paths form the M; no portrait or staff claims are invented.
        d.line((825,205,825,92,890,157,955,92,955,205),fill=LIME,width=10)
        d.line((847,205,847,145,890,190,933,145,933,205),fill=CYAN,width=3)
    im.save(out/('mancar-studio'+('-mobile' if mobile else '')+'.png'))

def build_showcases(out):
    for mobile in (False,True):
        suffix='-mobile' if mobile else ''
        for slug,project in PROJECTS.items():
            scenes=[tour_scene(out,slug,project,i,mobile) for i in range(len(project['steps']))]
            save_tour(scenes,out/('project-'+slug+suffix))
        save_tour([method_scene(out,i,mobile) for i in range(3)],out/('mancar-making'+suffix))
        about(out,mobile)
    gallery=['# A closer look at the work','Still frames from the project interface tours. Clinical names and records are fictional demonstration data. Website content comes from the repositories. These previews show interfaces; they are not evidence of a production deployment or an end-to-end backend test.']
    for slug,p in PROJECTS.items():
        gallery += ['## '+p['name']]
        for i,caption in enumerate(p['captions']):
            clean=capture(out/'captures'/f'{slug}-{i+1:02}.png')
            clean.save(out/'captures'/f'{slug}-still-{i+1:02}.png',optimize=True)
            gallery += [f'### {i+1:02} / {p["steps"][i]}',caption,
               f'![{p["name"]}: {caption}](../profile/assets/captures/{slug}-still-{i+1:02}.png)']
    gallery += ['[Capture sources and reproduction notes](PROJECT-EVIDENCE.md)']
    (out.parents[1]/'docs/PROJECT-GALLERY.md').write_text('\n\n'.join(gallery)+'\n',encoding='utf-8')
