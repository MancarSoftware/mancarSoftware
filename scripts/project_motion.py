"""Shared drawing helpers for project evidence assets."""
from PIL import ImageDraw, ImageFont
import locale_runtime as locale

DARK = '#101416'
WHITE = '#F4F2EB'
MUTED = '#ABB9B3'


def font(size, bold=False):
    return locale.face(size, bold, locale.LANG)


def text(draw: ImageDraw.ImageDraw, xy, value, size=24, color=WHITE, bold=False):
    locale.draw_text(draw, xy, value, size, color, bold)
