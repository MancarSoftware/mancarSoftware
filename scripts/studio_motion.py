"""GitHub-native studio motion: permanent copy, animated explanatory geometry."""
import math
from PIL import Image, ImageDraw
from project_motion import text, font, DARK, WHITE, MUTED

BLUE = '#284BE8'
CYAN = '#54DCEC'
LIME = '#B4E878'
CORAL = '#FF866E'
LINE = '#3B5355'
FRAMES = 64
DURATION = 120


def lines(draw, xy, copy, size, color=WHITE, bold=False, leading=None):
    for i, line in enumerate(copy):
        text(draw, (xy[0], xy[1] + i * (leading or size * 1.2)), line, size, color, bold)


def paragraph(draw, xy, copy, width, size=24, color=MUTED):
    """Wrap copy by measured glyph width; never crop responsive text."""
    row = ''
    y = xy[1]
    for word in copy.split():
        candidate = f'{row} {word}'.strip()
        if row and draw.textlength(candidate, font=font(size)) > width:
            text(draw, (xy[0], y), row, size, color)
            y += size * 1.4
            row = word
        else:
            row = candidate
    text(draw, (xy[0], y), row, size, color)


def route_point(points, progress):
    distances = [math.dist(a, b) for a, b in zip(points, points[1:])]
    remaining = progress * sum(distances)
    for a, b, distance in zip(points, points[1:], distances):
        if remaining <= distance:
            t = remaining / distance
            return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
        remaining -= distance
    return points[-1]


def cover(w, h, t, mobile):
    im = Image.new('RGB', (w, h), BLUE)
    d = ImageDraw.Draw(im)
    text(d, (32, 28), 'MANCAR SOFTWARE', 24, WHITE, True)
    text(d, (32, 67), 'INDEPENDENT STUDIO / ECUADOR', 17, '#D9E2FF')
    lines(d, (32, 126), ['Built around', 'people.', 'Made for', 'real work.'], 58 if mobile else 76, leading=65 if mobile else 80, bold=True)
    x, y, size = (330, 438, 185) if mobile else (665, 140, 330)
    # The same geometric M as the company mark, expressed as a working path.
    for gx in range(0, int(size) + 1, 22):
        for gy in range(0, int(size) + 1, 22):
            d.ellipse((x + gx, y + gy, x + gx + 2, y + gy + 2), fill='#4969F0')
    path = [(x, y + size), (x, y), (x + size / 2, y + size * .52), (x + size, y), (x + size, y + size)]
    d.line(path, fill='#6881F6', width=7, joint='curve')
    # Three moving signals share one path; the copy and composition stay still.
    for phase, color in ((0, LIME), (.33, CYAN), (.66, CORAL)):
        p = (t + phase) % 1
        px, py = route_point(path, (1 - math.cos(p * math.tau)) / 2)
        d.ellipse((px - 9, py - 9, px + 9, py + 9), fill=color)
    if mobile:
        lines(d, (32, 462), ['Strategy.', 'Design.', 'Development.', 'Support.'], 25, WHITE, leading=36)
    else:
        text(d, (32, 492), 'STRATEGY  /  DESIGN  /  DEVELOPMENT  /  SUPPORT', 22, WHITE)
    d.line((32, h - 71, w - 32, h - 71), fill='#6E88FF', width=1)
    text(d, (32, h - 47), 'YOUR BUSINESS SETS THE DIRECTION.', 19 if mobile else 22, WHITE, True)
    return im


OUTCOMES = [
    ('01', 'Earn Trust', 'Communicate your value. Make the next step clear.', CYAN),
    ('02', 'Simplify the Work', 'Connect information. Reduce repeated effort.', LIME),
    ('03', 'Move Forward', 'Set clear priorities. Build a foundation for change.', CORAL),
]


def outcome_symbol(d, x, y, index, t, color):
    motion = (1 - math.cos(t * math.tau)) / 2
    if index == 0:
        # A focal point becomes framed and recognizable.
        r = 28 + 8 * motion
        d.ellipse((x - 15, y - 15, x + 15, y + 15), fill=color)
        for sx, sy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
            xx, yy = x + sx * r, y + sy * r
            d.line((xx - sx * 14, yy, xx, yy, xx, yy - sy * 14), fill=color, width=3)
    elif index == 1:
        # Distributed tasks converge on one organized record.
        for j in range(3):
            yy = y - 26 + j * 26
            xx = x - 35 + (j % 2) * 16 * (1 - motion)
            d.line((xx, yy, x + 34, yy), fill=color, width=5)
            px = xx + (x + 34 - xx) * motion
            d.rectangle((px - 4, yy - 4, px + 4, yy + 4), fill=WHITE)
    else:
        # A signal follows a stepped route rather than suggesting measured growth.
        path = [(x - 35, y + 30), (x - 10, y + 30), (x - 10, y), (x + 14, y), (x + 14, y - 30), (x + 35, y - 30)]
        d.line(path, fill=color, width=3)
        px, py = route_point(path, motion)
        d.ellipse((px - 6, py - 6, px + 6, py + 6), fill=WHITE)


def outcomes(w, h, t, mobile):
    im = Image.new('RGB', (w, h), DARK)
    d = ImageDraw.Draw(im)
    text(d, (32, 28), '01 / WHAT THE WORK SHOULD CHANGE', 18, CYAN, True)
    lines(d, (32, 80), ['A stronger business.', 'One useful change at a time.'] if mobile else ['A stronger business starts', 'with a useful change.'], 34 if mobile else 56, bold=True)
    for index, (number, title, body, color) in enumerate(OUTCOMES):
        y = (206 if mobile else 252) + index * (150 if mobile else 126)
        d.line((32, y, w - 32, y), fill=LINE)
        outcome_symbol(d, 81, y + 64, index, t, color)
        text(d, (148, y + 23), title, 31 if mobile else 34, color, True)
        if mobile:
            paragraph(d, (148, y + 69), body, w - 180, 24)
        else:
            paragraph(d, (555, y + 33), body, 476, 26)
            text(d, (148, y + 76), f'{number} / BUSINESS OUTCOME', 15, MUTED)
    return im


STAGES = [
    ('Discover', 'Understand the business and its priorities.'),
    ('Define', 'Agree the scope, deliverables, and timing.'),
    ('Create', 'Design and build around the real workflow.'),
    ('Evolve', 'Launch, support, and refine the product.'),
]


def method(w, h, t, mobile):
    im = Image.new('RGB', (w, h), '#172D31')
    d = ImageDraw.Draw(im)
    text(d, (32, 28), '02 / HOW WE WORK TOGETHER', 18, CYAN, True)
    lines(d, (32, 83), ['Clear steps.', 'Direct collaboration.'], 43 if mobile else 57, bold=True)
    points = [(60, 250 + i * 114) for i in range(4)] if mobile else [(62 + i * 251, 291) for i in range(4)]
    d.line(points, fill='#557075', width=3)
    progress = (1 - math.cos(t * math.tau)) / 2
    active = min(int(progress * 4), 3)
    px, py = route_point(points, progress)
    d.ellipse((px - 5, py - 5, px + 5, py + 5), fill=WHITE)
    for index, ((x, y), (title, body)) in enumerate(zip(points, STAGES)):
        color = LIME if index == active else '#86A3A3'
        d.ellipse((x - 16, y - 16, x + 16, y + 16), fill=color)
        text(d, (x - 6, y - 11), str(index + 1), 16, DARK, True)
        tx, ty = (103, y - 16) if mobile else (x - 30, y + 40)
        text(d, (tx, ty), title, 29, WHITE, True)
        paragraph(d, (tx, ty + 44), body, w - 135 if mobile else 220, 24 if mobile else 22, '#C6D5D2')
    d.line((32, h - 70, w - 32, h - 70), fill='#557075')
    text(d, (32, h - 44), 'BUSINESS FIRST. TECHNOLOGY WITH PURPOSE.', 17 if mobile else 20, CYAN, True)
    return im


def contact(w, h, t, mobile):
    im = Image.new('RGB', (w, h), CORAL)
    d = ImageDraw.Draw(im)
    text(d, (32, 26), 'MANCAR SOFTWARE / YOUR NEXT CHAPTER', 17, DARK, True)
    lines(d, (32, 85), ['What could', 'work better?'], 61 if mobile else 76, DARK, True)
    x, y = (444, 327) if mobile else (921, 189)
    shift = 10 * math.sin(t * math.tau)
    for size in (50, 75, 100):
        d.arc((x - size, y - size, x + size, y + size), 30, 330, fill='#B44D3C', width=1)
    d.line((x - 31 - shift, y + 31 + shift, x + 31 - shift, y - 31 + shift), fill=DARK, width=8)
    d.line((x - 8 - shift, y - 31 + shift, x + 31 - shift, y - 31 + shift, x + 31 - shift, y + 8 + shift), fill=DARK, width=8)
    lines(d, (32, 286 if mobile else 295), ['Tell us about the work.', 'Let’s define the next step.'], 24 if mobile else 27, DARK, leading=35)
    return im


PANELS = [
    ('mancar-studio-cover', cover, 620, 750),
    ('mancar-capabilities', outcomes, 650, 710),
    ('mancar-approach', method, 560, 770),
    ('mancar-contact', contact, 410, 460),
]


def build_studio(out):
    for mobile in (False, True):
        for name, render, desktop_h, mobile_h in PANELS:
            width, height = (560, mobile_h) if mobile else (1080, desktop_h)
            frames = [render(width, height, i / FRAMES, mobile) for i in range(FRAMES)]
            stem = out / (name + ('-mobile' if mobile else ''))
            frames[0].save(stem.with_suffix('.png'))
            samples = Image.new('RGB', (256 * 8, 192))
            for i in range(8):
                samples.paste(frames[i * FRAMES // 8].resize((256, 192)), (256 * i, 0))
            palette = samples.quantize(colors=128)
            indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
            indexed[0].save(stem.with_suffix('.gif'), save_all=True, append_images=indexed[1:], duration=DURATION, loop=0, optimize=True, disposal=1)
