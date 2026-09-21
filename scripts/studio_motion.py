"""GitHub-native studio motion: permanent copy, animated explanatory geometry."""
import math
from PIL import Image, ImageDraw
from project_motion import text, font, DARK, WHITE, MUTED
import locale_runtime as locale

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
    locale.draw_paragraph(draw, xy, copy, width, size, color)


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


def team(w, h, t, mobile):
    paper = '#EAE7DF'
    ink = '#173936'
    im = Image.new('RGB', (w, h), paper)
    d = ImageDraw.Draw(im)
    text(d, (32, 28), 'INSIDE MANCAR / THE PEOPLE', 18, ink, True)
    lines(d, (32, 79), ['Different strengths.', 'A shared standard.'], 44 if mobile else 60, ink, True)
    people = [
        ('AM', 'Alejandro Mantilla', 'Full Stack Development', 'Architecture, development, and the experience that connects them.', 'REACT / NEXT.JS / NODE.JS / UI/UX'),
        ('JM', 'Jeremy Macias', 'Frontend Development', 'Clear, accessible interfaces shaped around real business workflows.', 'REACT / TAILWIND CSS / ACCESSIBILITY'),
    ]
    for i, (initials, name, role, description, skills) in enumerate(people):
        x, y = (32, 230 + i * 264) if mobile else (32 + i * 536, 258)
        width = w - 64 if mobile else 472
        d.line((x, y, x + width, y), fill='#A4B4AA')
        text(d, (x, y + 20), initials, 51 if mobile else 67, ink, True)
        start = x + 119
        text(d, (start, y + 25), name, 28 if mobile else 31, ink, True)
        text(d, (start, y + 65), role, 23, ink)
        paragraph(d, (x, y + 116), description, width, 24, ink)
        text(d, (x, y + 202), skills, 17 if mobile else 18, ink)
        # A short moving rule links each person's monogram to their work.
        travel = (1 - math.cos((t + i * .25) * math.tau)) / 2
        px = x + 20 + travel * (width - 76)
        d.line((px, y, px + 56, y), fill=BLUE, width=4)
    y = h - (160 if mobile else 140)
    d.rectangle((0, y, w, h), fill=ink)
    text(d, (32, y + 22), 'BACKEND & AUTOMATION', 19, LIME, True)
    paragraph(d, (32, y + 59), 'Our backend team connects APIs, databases, security, and automation to keep the product maintainable.', w - 64, 24, WHITE)
    return im


PRINCIPLES = [
    ('Listen First.', 'Understand the people and the work before proposing a solution.'),
    ('Be Clear.', 'Explain scope, timing, and priorities in straightforward language.'),
    ('Stay Involved.', 'Work as a partner, with visible progress and decisions made together.'),
    ('Build Responsibly.', 'Consider design, performance, security, and long-term maintenance.'),
]


def principles(w, h, t, mobile):
    im = Image.new('RGB', (w, h), LIME)
    d = ImageDraw.Draw(im)
    text(d, (32, 27), 'THE MANCAR STANDARD / FOUR COMMITMENTS', 17, DARK, True)
    lines(d, (32, 78), ['The way we work', 'is part of the product.'], 39 if mobile else 56, DARK, True)
    for i, (title, description) in enumerate(PRINCIPLES):
        y = (216 if mobile else 240) + i * (151 if mobile else 118)
        d.line((32, y, w - 32, y), fill='#70934D')
        text(d, (32, y + 24), f'0{i+1}', 20, DARK)
        text(d, (89, y + 19), title, 33 if mobile else 40, DARK, True)
        paragraph(d, (89, y + 65) if mobile else (565, y + 26), description, w - 121 if mobile else 475, 24, DARK)
        # A small marginal indicator moves through the commitments without hiding copy.
        phase = (1 - math.cos(t * math.tau)) / 2
        if min(int(phase * 4), 3) == i:
            d.rectangle((0, y + 19, 8, y + 68), fill=DARK)
    return im


def support(w, h, t, mobile):
    im = Image.new('RGB', (w, h), '#142322')
    d = ImageDraw.Draw(im)
    text(d, (32, 28), 'AFTER LAUNCH / SUPPORT & MAINTENANCE', 17, CYAN, True)
    lines(d, (32, 81), ['Launch is a milestone.', 'The work continues.'], 38 if mobile else 57, bold=True)
    x, y, radius = (280, 335, 93) if mobile else (219, 379, 121)
    for r in (radius, radius - 18):
        d.ellipse((x-r, y-r, x+r, y+r), outline=LINE, width=2)
    d.arc((x-radius,y-radius,x+radius,y+radius), t*360-90, t*360+35, fill=CYAN, width=5)
    angle = t * math.tau - math.pi / 2
    px, py = x + radius * math.cos(angle), y + radius * math.sin(angle)
    d.ellipse((px-6,py-6,px+6,py+6), fill=LIME)
    text(d, (x-54, y-22), 'CARE', 35, WHITE, True)
    text(d, (x-58, y+24), 'FOR THE PRODUCT', 12, CYAN)
    items = [('Diagnose', 'Availability, performance, and visible errors.'),
             ('Maintain', 'Updates, security improvements, and backups.'),
             ('Refine', 'Forms, content, and focused feature improvements.')]
    for i, (title, description) in enumerate(items):
        tx, ty = (32, 481 + i * 122) if mobile else (475, 257 + i * 110)
        d.line((tx, ty, w-32, ty), fill=LINE)
        text(d, (tx, ty+15), title, 28, LIME, True)
        paragraph(d, (tx, ty+55), description, w-tx-32, 23, '#C6D5D2')
    text(d, (32, h-39), 'DIAGNOSE THE ISSUE. AGREE THE NEXT STEP.', 17 if mobile else 20, CYAN, True)
    return im


def disciplines(w, h, t, mobile):
    im = Image.new('RGB', (w, h), '#182B47')
    d = ImageDraw.Draw(im)
    text(d, (32, 28), 'MANCAR / CONNECTED DISCIPLINES', 17, CYAN, True)
    lines(d, (32, 78), ['Different skills.', 'One considered product.'], 37 if mobile else 57, bold=True)
    items = [('UX/UI Design', 'Make the next step clear.', CYAN),
             ('Frontend', 'Bring the experience to life.', CORAL),
             ('Backend', 'Connect data and business rules.', LIME),
             ('Automation', 'Reduce repetitive work.', CYAN),
             ('Support', 'Keep the product moving forward.', CORAL)]
    for i, (title, description, accent) in enumerate(items):
        y = (223 if mobile else 245) + i * (110 if mobile else 81)
        x = 65 if mobile else 90
        d.line((32, y + 13, 32, min(y + 123 if mobile else y + 94, h - 60)), fill=LINE, width=2)
        d.ellipse((25, y + 6, 39, y + 20), fill=accent)
        text(d, (x, y), title, 28, accent, True)
        paragraph(d, (x, y + 40) if mobile else (345, y + 4), description, w - x - 32 if mobile else 405, 22, WHITE)
        if not mobile:
            route = [(770, y + 16), (805, y + 16), (858, 425)]
            d.line(route, fill=LINE, width=2)
            px, py = route_point(route, (t + i / 5) % 1)
            d.ellipse((px-4, py-4, px+4, py+4), fill=accent)
    if not mobile:
        d.ellipse((853, 351, 1023, 521), outline=CYAN, width=2)
        text(d, (887, 393), 'YOUR', 24, WHITE, True)
        text(d, (871, 431), 'PRODUCT', 24, WHITE, True)
    else:
        py = 236 + ((t * 540) % 540)
        d.ellipse((27, py-5, 37, py+5), fill=WHITE)
    return im


def starting_points(w, h, t, mobile):
    im = Image.new('RGB', (w, h), '#EAE6DB')
    d = ImageDraw.Draw(im)
    ink, muted = '#172D28', '#52635B'
    text(d, (32, 28), 'WHEN TO BRING US IN / YOUR STARTING POINT', 16, ink, True)
    lines(d, (32, 78), ['What needs', 'to work better?'], 46 if mobile else 60, ink, True)
    items = [('A new beginning', 'You are launching a business or introducing a new offer.', 'Clarify the experience.'),
             ('Too much manual work', 'Your team repeats tasks or moves information between tools.', 'Connect the workflow.'),
             ('A product with potential', 'An existing product needs a clearer, more useful experience.', 'Improve what matters.'),
             ('The next stage', 'Your product needs care as the business changes.', 'Keep it moving forward.')]
    for i, (title, copy, outcome) in enumerate(items):
        x = 32 if mobile else 32 + (i % 2) * 524
        y = (235 + i * 176) if mobile else (260 + (i // 2) * 211)
        width = 496 if mobile else 492
        d.line((x, y, x + width, y), fill='#A4B3A6', width=2)
        text(d, (x, y + 18), f'0{i+1}', 20, '#A54834', True)
        text(d, (x + 48, y + 14), title, 27, ink, True)
        paragraph(d, (x + 48, y + 57), copy, width - 55, 23, muted)
        text(d, (x + 48, y + 131), outcome, 22, ink, True)
        phase = (t + i / 4) % 1
        px = x + width * phase
        d.line((px, y, min(px + 27, x + width), y), fill='#BD553D', width=4)
    return im


def first_conversation(w, h, t, mobile):
    im = Image.new('RGB', (w, h), '#193B38')
    d = ImageDraw.Draw(im)
    text(d, (32, 28), 'GETTING STARTED / THREE CLEAR STEPS', 17, LIME, True)
    lines(d, (32, 80), ['Bring the context.', 'We will shape the next step.'], 34 if mobile else 53, bold=True)
    items = [('Tell us about the work', 'Share your business, the challenge, and what you want to improve.'),
             ('Review the priorities', 'We discuss the people, existing tools, constraints, and scope.'),
             ('Define a proposal', 'Agree the deliverables, timing, and a practical approach.')]
    for i, (title, copy) in enumerate(items):
        x, y = (32, 228 + i * 161) if mobile else (32 + i * 345, 264)
        width = 496 if mobile else 310
        d.ellipse((x, y, x+42, y+42), outline=LIME, width=2)
        text(d, (x+13, y+10), str(i+1), 22, LIME, True)
        d.line((x+54, y+21, x+width, y+21), fill='#61847B', width=2)
        px = x + 54 + (width - 54) * ((t + i / 3) % 1)
        d.ellipse((px-4,y+17,px+4,y+25), fill=CORAL)
        text(d, (x, y+58), title, 27 if mobile else 25, WHITE, True)
        paragraph(d, (x, y+100), copy, width, 22, '#CFDDD5')
    return im


PANELS = [
    ('mancar-starting-points', starting_points, 720, 970),
    ('mancar-first-conversation', first_conversation, 530, 745),
    ('mancar-disciplines', disciplines, 690, 815),
    ('mancar-studio-cover', cover, 620, 750),
    ('mancar-approach', method, 560, 770),
    ('mancar-contact', contact, 410, 460),
    ('mancar-team', team, 670, 950),
    ('mancar-support', support, 650, 910),
]


def build_studio(out):
    for mobile in (False, True):
        for name, render, desktop_h, mobile_h in PANELS:
            locale.PANEL = name
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
