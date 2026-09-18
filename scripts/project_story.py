"""An evidence-led Casa Nativa walkthrough using original repository captures."""
from PIL import Image, ImageDraw, ImageOps
from project_showcases import capture, save_tour
from studio_motion import text, lines, paragraph


STEPS = [
    ('Explore', 'Find a starting point.',
     'Category and price filters help customers narrow the catalog around what they need.', 2),
    ('Evaluate', 'See how a piece fits.',
     'Photography, dimensions, materials, and color options sit together on the product page.', 3),
    ('Collect', 'Keep the possibilities.',
     'A saved selection lets customers bring chosen pieces together before an inquiry.', 4),
]


def scene(out, index, mobile):
    w, h = (560, 850) if mobile else (1080, 700)
    im = Image.new('RGB', (w, h), '#EAE6DB')
    d = ImageDraw.Draw(im)
    ink, muted, accent = '#172D28', '#52635B', '#BD553D'
    text(d, (32, 28), 'PROJECT IN FOCUS / CASA NATIVA', 17, accent, True)
    lines(d, (32, 77), ['From discovery', 'to a considered choice.'], 38 if mobile else 51, ink, True)
    for i, (label, _, _, _) in enumerate(STEPS):
        x = 32 + i * (170 if mobile else 345)
        d.line((x, 205, x + (148 if mobile else 315), 205), fill=accent if i == index else '#B7BDB2', width=4)
        text(d, (x, 223), f'0{i+1} / {label}', 19, accent if i == index else muted, True)
    _, title, copy, number = STEPS[index]
    if mobile:
        text(d, (32, 280), title, 30, ink, True)
        paragraph(d, (32, 325), copy, 496, 23, ink)
        box, origin = (496, 350), (32, 444)
    else:
        paragraph(d, (32, 310), title, 285, 36, ink)
        paragraph(d, (32, 422), copy, 285, 24, muted)
        box, origin = (680, 385), (368, 280)
    screenshot = ImageOps.contain(capture(out / 'captures' / f'casanativa-{number:02}.png'), box, Image.Resampling.LANCZOS)
    im.paste(screenshot, (origin[0] + (box[0] - screenshot.width)//2, origin[1] + (box[1] - screenshot.height)//2))
    text(d, (32, h - 32), 'REAL INTERFACE / REPOSITORY DEMO CONTENT', 15, muted)
    return im


def build_story(out):
    for mobile in (False, True):
        stem = out / ('mancar-casa-story' + ('-mobile' if mobile else ''))
        save_tour([scene(out, i, mobile) for i in range(3)], stem, hold_ms=5500)
