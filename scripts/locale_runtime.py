"""Translation, Unicode wrapping, and Hindi glyph shaping for generated artwork."""
from functools import lru_cache
from pathlib import Path
import re
import math
from PIL import Image, ImageDraw, ImageFont
from translations import TRANSLATIONS

LANG = 'en'
PANEL = ''
LABELS = {}
FITS = []
PATTERN = re.compile('|'.join(re.escape(s) for s in sorted(TRANSLATIONS, key=len, reverse=True)))
FONT_ROOT = Path('C:/Windows/Fonts')


def translate(value):
    if LANG == 'en':
        return value
    return PATTERN.sub(lambda m: TRANSLATIONS[m[0]][LANG], value)


def set_locale(lang):
    global LANG
    LANG = lang
    LABELS.clear()
    FITS.clear()


def font_path(bold=False, lang=None):
    lang = lang or LANG
    if lang == 'zh':
        return FONT_ROOT / ('msyhbd.ttc' if bold else 'msyh.ttc')
    if lang == 'hi':
        return FONT_ROOT / 'Nirmala.ttc'
    return FONT_ROOT / ('segoeuib.ttf' if bold else 'segoeui.ttf')


@lru_cache(maxsize=512)
def face(size, bold=False, lang='en'):
    return ImageFont.truetype(str(font_path(bold, lang)), size)


@lru_cache(maxsize=4096)
def hindi_mask(value, size, bold=False):
    # Pillow's Windows build lacks RAQM. Shape conjuncts with HarfBuzz, then
    # rasterize its positioned glyphs with FreeType; never draw isolated letters.
    import uharfbuzz as hb
    import freetype
    path = font_path(bold, 'hi')
    hb_face = hb.Face(path.read_bytes())
    hb_font = hb.Font(hb_face)
    hb_font.scale = (size * 64, size * 64)
    hb.ot_font_set_funcs(hb_font)
    buffer = hb.Buffer()
    buffer.add_str(value)
    buffer.guess_segment_properties()
    hb.shape(hb_font, buffer)
    ft = freetype.Face(str(path))
    ft.set_pixel_sizes(0, size)
    glyphs, cursor = [], 0.0
    for info, position in zip(buffer.glyph_infos, buffer.glyph_positions):
        if info.codepoint == 0:
            raise ValueError(f'Font lacks a glyph in {value!r}')
        ft.load_glyph(info.codepoint, freetype.FT_LOAD_RENDER)
        bitmap = ft.glyph.bitmap
        x = round(cursor + position.x_offset / 64 + ft.glyph.bitmap_left)
        y = round(-position.y_offset / 64 - ft.glyph.bitmap_top)
        if bitmap.width and bitmap.rows:
            mask = Image.frombytes('L', (bitmap.width, bitmap.rows), bytes(bitmap.buffer), 'raw', 'L', bitmap.pitch)
            glyphs.append((x, y, mask))
        cursor += position.x_advance / 64
    if not glyphs:
        return Image.new('L', (max(1, math.ceil(cursor)), 1)), cursor
    left = min(0, min(x for x, _, _ in glyphs))
    top = min(y for _, y, _ in glyphs)
    right = max(math.ceil(cursor), max(x + m.width for x, _, m in glyphs))
    bottom = max(y + m.height for _, y, m in glyphs)
    canvas = Image.new('L', (right-left, bottom-top))
    from PIL import ImageChops
    for x, y, mask in glyphs:
        layer = Image.new('L', canvas.size)
        layer.paste(mask, (x-left, y-top))
        canvas = ImageChops.lighter(canvas, layer)
    return canvas, cursor


def measure(value, size, bold=False):
    if LANG == 'hi':
        mask, advance = hindi_mask(value, size, bold)
        return max(advance, mask.width)
    return face(size, bold, LANG).getlength(value)


def wrap(value, size, width, bold=False):
    # Chinese has no word spaces; wrap at characters while retaining punctuation.
    tokens = list(value) if LANG == 'zh' else value.split()
    join = '' if LANG == 'zh' else ' '
    rows, row = [], ''
    for token in tokens:
        candidate = row + (join if row else '') + token
        if row and measure(candidate, size, bold) > width:
            if LANG == 'zh' and token in '，。；：！？、）”：':
                row += token
                rows.append(row)
                row = ''
            else:
                rows.append(row)
                row = token
        else:
            row = candidate
    if row:
        rows.append(row)
    return rows or ['']


def record(value):
    if PANEL:
        LABELS.setdefault(PANEL, [])
        if value not in LABELS[PANEL]:
            LABELS[PANEL].append(value)


def paint(draw, xy, value, size, color, bold=False):
    if LANG == 'hi':
        mask, _ = hindi_mask(value, size, bold)
        draw.bitmap((round(xy[0]), round(xy[1])), mask, fill=color)
    else:
        draw.text(xy, value, font=face(size, bold, LANG), fill=color, anchor='lt')


def available_width(draw, xy):
    w, h = draw._image.size
    x, y = xy
    width = w - x - 32
    mobile = w == 560
    if PANEL == 'mancar-studio-cover' and not mobile and 120 <= y < 450:
        width = 595
    elif PANEL == 'mancar-contact':
        if y >= 280:
            width = 290 if mobile else 700
        elif y >= 80:
            width = 496 if mobile else 750
    elif PANEL == 'mancar-team' and 250 <= y < 485 and not mobile:
        width = 472 - (x - 32) % 536
    elif PANEL == 'mancar-disciplines' and not mobile:
        if x == 90:
            width = 230
        elif x > 850:
            width = 135
    elif PANEL == 'mancar-starting-points' and y > 230:
        width = 440 if mobile else 440 - ((x-80) % 524)
    elif PANEL == 'mancar-first-conversation' and y > 260 and not mobile:
        width = 310
    elif PANEL.startswith('project-'):
        if mobile and y == 681:
            width = 496
        elif not mobile and y == 224:
            width = 220 if PANEL == 'project-casanativa' else 310
        elif not mobile and y == 913:
            width = 740
    elif PANEL == 'mancar-casa-story' and y == 223:
        width = 148 if mobile else 315
    return max(45, width)


def draw_text(draw, xy, value, size=24, color='#F4F2EB', bold=False):
    value = translate(value)
    record(value)
    width = available_width(draw, xy)
    chosen = size
    while measure(value, chosen, bold) > width and chosen > 12:
        chosen -= 1
    if measure(value, chosen, bold) > width + 1:
        raise ValueError(f'Text overflow: {LANG}/{PANEL}: {value}')
    if chosen < size:
        FITS.append((PANEL, value, size, chosen))
    paint(draw, xy, value, chosen, color, bold)


def draw_paragraph(draw, xy, value, width, size=24, color='#ABB9B3'):
    value = translate(value)
    record(value)
    # Existing panels reserve 2–3 lines per description. Allow more in the story.
    max_lines = 5 if PANEL == 'mancar-casa-story' and draw._image.width > 560 else 2
    if PANEL == 'mancar-approach' and draw._image.width > 560:
        max_lines = 3
    chosen = size
    rows = wrap(value, chosen, width)
    while len(rows) > max_lines and chosen > 16:
        chosen -= 1
        rows = wrap(value, chosen, width)
    if len(rows) > max_lines:
        raise ValueError(f'Paragraph overflow: {LANG}/{PANEL}: {value}')
    for index, row in enumerate(rows):
        paint(draw, (xy[0], xy[1] + index * chosen * 1.4), row, chosen, color)
