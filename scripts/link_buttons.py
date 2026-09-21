"""Generate compact, GitHub-compatible image links without preview-only styling."""
import re
from html import escape
from PIL import Image, ImageDraw
from project_motion import font
import locale_runtime as locale


def brand_links(content, out):
    directory = out / 'buttons'
    directory.mkdir(exist_ok=True)

    def replace(match):
        label, target = match.groups()
        label = label.replace(' →', '')
        name = re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')
        primary = label in ('Explore Support Options', 'Explore the Repository', 'View the Project', 'Visit Mancar Software')
        label = locale.translate(label)
        bg, fg = ('#FF866E', '#172D28') if primary else ('#193B38', '#F4F2EB')
        size = 28
        probe = ImageDraw.Draw(Image.new('RGB', (1, 1)))
        rows = locale.wrap(label, size, 490)
        width = min(608, max(160, round(max(locale.measure(row, size) for row in rows)) + 108))
        height = max(88, 40 + len(rows) * 36)
        im = Image.new('RGB', (width, height), bg)
        d = ImageDraw.Draw(im)
        if not primary:
            d.rectangle((0, 0, width-1, height-1), outline='#61847B', width=2)
        for i, row in enumerate(rows):
            locale.paint(d, (28, (height-len(rows)*36)//2+i*36), row, size, fg)
        x, y = width-35, height//2
        d.line((x-10,y,x+8,y), fill=fg, width=2)
        d.line((x+2,y-6,x+8,y,x+2,y+6), fill=fg, width=2)
        im.save(directory / f'{name}.png', optimize=True)
        return f'<a href="{escape(target, quote=True)}"><img src="assets/buttons/{name}.png" width="{width//2}" height="{height//2}" alt="{escape(label, quote=True)}" /></a>'

    # Every visible Markdown link in the public presentation uses the same system.
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace, content)
    return content.replace(' &nbsp; / &nbsp; ', '\n').replace('</a> · <a', '</a>\n<a')
