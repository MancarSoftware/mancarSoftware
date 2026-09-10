"""Build self-contained GitHub brand animations. Requires Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'profile' / 'assets'
FONT = Path('C:/Windows/Fonts')
def font(size, bold=False):
    return ImageFont.truetype(str(FONT / ('segoeuib.ttf' if bold else 'segoeui.ttf')), size)

BG = '#101416'
WHITE = '#F0F3ED'
GRAY = '#A1ADA8'
ACCENT = '#B4E878'
W, H = 1080, 420
frames = []
points = [(775, 268), (775, 113), (857, 203), (939, 113), (939, 268)]
lengths = [math.dist(a,b) for a,b in zip(points, points[1:])]
total = sum(lengths)
def point_at(distance):
    for a,b,length in zip(points, points[1:], lengths):
        if distance <= length:
            t = distance / length
            return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
        distance -= length
    return points[-1]

for i in range(90):
    phase = i / 90
    im = Image.new('RGB', (W,H), BG)
    d = ImageDraw.Draw(im)
    d.text((48,34), 'MANCAR / SOFTWARE STUDIO', font=font(16,True), fill=GRAY)
    d.text((43,91), 'MANCAR', font=font(91,True), fill=WHITE)
    d.text((48,202), 'SOFTWARE', font=font(37), fill=WHITE)
    d.text((48,278), 'Designed for people.', font=font(23), fill=GRAY)
    d.text((48,311), 'Engineered for business.', font=font(23), fill=GRAY)
    for x in range(711,1001,24):
        for y in range(64,330,24):
            d.ellipse((x,y,x+1,y+1), fill='#303A34')
    d.rectangle((720,72,994,311), outline='#344039', width=1)
    d.line(points, fill='#35463B', width=14)
    # A bright segment travels continuously along the structural monogram.
    for j in range(55):
        offset = (phase*total-j*2.5) % total
        x,y = point_at(offset)
        blend = 1-j/55
        color = tuple(round(a+(b-a)*blend) for a,b in zip((53,70,59),(180,232,120)))
        d.ellipse((x-6,y-6,x+6,y+6), fill=color)
    d.text((755,337), 'DESIGN / BUILD / EVOLVE', font=font(14,True), fill=GRAY)
    d.line((48,385,1032,385), fill='#344039', width=1)
    x=48+int(phase*984)
    d.line((x,385,min(x+72,1032),385), fill=ACCENT, width=3)
    frames.append(im)

# One shared palette keeps flat brand colors stable between frames.
palette = frames[0].quantize(colors=64)
indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
indexed[0].save(ASSETS/'mancar-header.gif', save_all=True, append_images=indexed[1:], duration=70, loop=0, optimize=True, disposal=1)
frames[0].save(ASSETS/'mancar-header-static.png')

dividers=[]
for i in range(60):
    im=Image.new('RGB',(1080,36), BG)
    d=ImageDraw.Draw(im)
    d.line((0,18,1080,18),fill='#344039')
    x=int(i/60*1080)
    d.line((x,18,min(x+100,1080),18),fill=ACCENT,width=2)
    dividers.append(im)
dividers[0].save(ASSETS/'mancar-divider.gif',save_all=True,append_images=dividers[1:],duration=80,loop=0,optimize=True)
print('Generated hero, static fallback, and animated divider.')
