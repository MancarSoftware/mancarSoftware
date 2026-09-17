"""Shared drawing helpers for project evidence assets."""
from PIL import ImageDraw, ImageFont

DARK = '#101416'
WHITE = '#F4F2EB'
MUTED = '#ABB9B3'


def font(size, bold=False):
    face = 'segoeuib.ttf' if bold else 'segoeui.ttf'
    return ImageFont.truetype(f'C:/Windows/Fonts/{face}', size)


def text(draw: ImageDraw.ImageDraw, xy, value, size=24, color=WHITE, bold=False):
    draw.text(xy, value, font=font(size, bold), fill=color, anchor='lt')
