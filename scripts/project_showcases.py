"""Compose repository interface captures into readable, GitHub-native visual tours."""
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageOps
from studio_motion import text, DARK, WHITE, MUTED, CYAN, LIME

PROJECTS = {
 'odontocare': dict(name='OdontoCare', number='01', color='#54DCEC', category='DENTAL PRACTICE SOFTWARE',
  headline=['Every patient.', 'The complete picture.'],
  steps=['Open record','Review history','Plan next visit'],
  captions=['Clinical and administrative context in one record.', 'A complete history across visits.', 'Appointments organized in a clear daily view.']),
 'vetcare': dict(name='VetCare Pro', number='02', color='#57D7BC', category='VETERINARY DESKTOP SOFTWARE',
  headline=['Connected care.', 'Complete records.'],
  steps=['View records','Follow history','Document visit'],
  captions=['Patients and their owners connected in one record.', 'Clinical context preserved across visits.', 'A structured workflow for documenting care.']),
 'almavet': dict(name='Alma Vet', number='03', color='#7DAEFF', category='VETERINARY CLINIC WEBSITE',
  headline=['From discovery', 'to a request for care.'],
  steps=['Meet the clinic','Review services','Request a visit'],
  captions=['A clear introduction to the clinic and its approach.', 'Services organized around common care needs.', 'A structured request for the clinic to review.']),
 'casanativa': dict(name='Casa Nativa', number='04', color='#ECAA8C', category='FURNITURE STORE & DIGITAL CATALOG',
  headline=['Find your piece.', 'Make room for it.'],
  steps=['Discover','Browse catalog','Review details','Save selection'],
  captions=['An editorial introduction to the collection.', 'Furniture organized by category and price.', 'Materials, dimensions, and color options in context.', 'A saved selection ready for an inquiry.']),
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
    w,h=(560,740) if mobile else (1080,950)
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
        # Match the desktop tour: one complete interface changes per scene.
        stepwidth=496/len(project['steps'])
        for n,step in enumerate(project['steps']):
            x=32+round(n*stepwidth)
            d.line((x,270,x+stepwidth-12,270),fill=c if n==index else '#344039',width=3)
        text(d,(32,283),f'{index+1:02} / '+project['steps'][index],18,c,True)
        screenshot=ImageOps.contain(screen,(496,334),Image.Resampling.LANCZOS)
        im.paste(screenshot,((w-screenshot.width)//2,320))
        d.rectangle((0,667,w,h),fill=DARK)
        text(d,(32,681),project['captions'][index],20,WHITE,True)
        text(d,(32,719),'REPOSITORY INTERFACE / DEMO CONTENT',12,MUTED)
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

def save_tour(scenes,stem,hold_ms=4000,transition_ms=120):
    # Long holds keep the evidence readable; eased dissolves make scene changes deliberate.
    scenes[0].save(stem.with_suffix('.png'))
    frames=[];durations=[]
    for i,current in enumerate(scenes):
        frames.append(current);durations.append(hold_ms)
        following=scenes[(i+1)%len(scenes)]
        for j in range(1,4):
            progress=j/4
            eased=progress*progress*(3-2*progress)
            frames.append(Image.blend(current,following,eased));durations.append(transition_ms)
    strip=Image.new('RGB',(256*len(scenes),192))
    for i,scene in enumerate(scenes): strip.paste(scene.resize((256,192)),(256*i,0))
    palette=strip.quantize(colors=256)
    indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
    indexed[0].save(stem.with_suffix('.gif'),save_all=True,append_images=indexed[1:],
                    duration=durations,loop=0,optimize=True,disposal=1)

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
        about(out,mobile)
    gallery=['# A closer look at the work','Still frames from the project interface tours. All clinical names and records are fictional demonstration data; website content comes from the repositories. These previews document interface design and do not constitute evidence of a production deployment or end-to-end backend testing.']
    for slug,p in PROJECTS.items():
        gallery += ['## '+p['name']]
        for i,caption in enumerate(p['captions']):
            clean=capture(out/'captures'/f'{slug}-{i+1:02}.png')
            clean.save(out/'captures'/f'{slug}-still-{i+1:02}.png',optimize=True)
            gallery += [f'### {i+1:02} / {p["steps"][i]}',caption,
               f'![{p["name"]}: {caption}](../profile/assets/captures/{slug}-still-{i+1:02}.png)']
    gallery += ['[Capture sources and reproduction notes](PROJECT-EVIDENCE.md)']
    (out.parents[1]/'docs/PROJECT-GALLERY.md').write_text('\n\n'.join(gallery)+'\n',encoding='utf-8')
