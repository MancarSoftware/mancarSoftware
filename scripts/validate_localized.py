"""Verify all four README editions, navigation, typography, and animated assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import re
import json
from PIL import Image, ImageChops, ImageSequence
import freetype
from localize_presentation import LANGUAGES, readme_name, gallery_name
from studio_motion import PANELS
from locale_runtime import font_path

ROOT = Path(__file__).resolve().parents[1]


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths, self.ids = [], []
        self.reduced = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'img':
            assert attrs.get('alt'), 'Missing image alternative'
        if tag == 'source' and 'prefers-reduced-motion' in attrs.get('media', ''):
            assert attrs['srcset'].endswith('.png')
            self.reduced += 1
        for key in ('src', 'srcset', 'href'):
            if key in attrs:
                self.paths.append(attrs[key])


def anchors(content):
    refs = References()
    refs.feed(content)
    headings = re.findall(r'^#{1,6} (.+)$', content, re.M)
    return set(refs.ids) | {re.sub(r' +', '-', re.sub(r'[^\w -]', '', h.lower())) for h in headings}


def check_paths(path, content):
    refs = References()
    refs.feed(content)
    refs.paths.extend(re.findall(r'\]\(([^)]+)\)', content))
    for value in refs.paths:
        target = urlsplit(value)
        if target.scheme:
            continue
        local = (path.parent / unquote(target.path)).resolve() if target.path else path
        assert local.is_file(), f'{path}: missing {value}'
        if target.fragment and local.suffix == '.md':
            assert target.fragment in anchors(local.read_text(encoding='utf-8')), f'Missing anchor: {value}'
    return refs


def check_gif(path, size, duration):
    with Image.open(path) as media:
        assert media.size == size, (path, media.size)
        assert media.info.get('loop') == 0
        first, changed, elapsed = None, False, 0
        for frame in ImageSequence.Iterator(media):
            rgb = frame.convert('RGB')
            if first is None:
                first = rgb
            else:
                changed |= ImageChops.difference(first, rgb).getbbox() is not None
            elapsed += frame.info.get('duration', 0)
        assert changed, f'Static GIF: {path}'
        assert elapsed == duration, (path, elapsed)
    with Image.open(path.with_suffix('.png')) as still:
        assert still.size == size
        still.verify()


def main():
    for lang in LANGUAGES:
        root = ROOT / readme_name(lang)
        profile_path = ROOT / 'profile' / readme_name(lang)
        content = root.read_text(encoding='utf-8')
        profile = profile_path.read_text(encoding='utf-8')
        assert profile.replace('"assets/', '"profile/assets/').replace('href="../docs/', 'href="docs/') == content, f'{lang}: divergent README variants'
        assert 'beauty' not in content.lower()
        ids = re.findall(r'<a id="([^"]+)"', content)
        assert len(ids) == len(set(ids)), 'Duplicate IDs'
        assert ids[0] == 'selected-projects'
        assert all(x in ids for x in ('odontocare', 'vetcare', 'almavet', 'casanativa', 'working-with-us'))
        for path, text in ((root, content), (profile_path, profile)):
            refs = check_paths(path, text)
            assert refs.reduced == 26, f'{lang}: missing static alternatives'
            for code, label in LANGUAGES.items():
                assert f'href="{readme_name(code)}"' in text
                assert f'alt="{label}"' in text
        gallery = ROOT / 'docs' / gallery_name(lang)
        check_paths(gallery, gallery.read_text(encoding='utf-8'))
        folder = ROOT / 'profile/assets' / ('' if lang == 'en' else lang)
        prefix = 'profile/assets/' + ('' if lang == 'en' else lang + '/')
        for source in re.findall(r'(?:src|srcset)="([^"]+\.(?:gif|png))"', content):
            if '/captures/' not in source and '/languages/' not in source:
                assert source.startswith(prefix), f'{lang}: wrong language asset {source}'
        button_paths = set(re.findall(r'src="([^"]+/buttons/[^"/]+\.png)"', content))
        assert {p.name for p in (folder/'buttons').glob('*.png')} == {Path(p).name for p in button_paths}, f'{lang}: unused button'
        for button in button_paths:
            with Image.open(ROOT / button) as image:
                assert image.width <= 608 and image.height >= 88
        for name, _, dh, mh in PANELS:
            for suffix, size in (('', (1080, dh)), ('-mobile', (560, mh))):
                check_gif(folder / f'{name}{suffix}.gif', size, 7680)
        for slug in ('odontocare', 'vetcare', 'almavet', 'casanativa'):
            for suffix, size in (('', (1080, 950)), ('-mobile', (560, 740))):
                check_gif(folder / f'project-{slug}{suffix}.gif', size, (4 if slug == 'casanativa' else 3) * 4360)
        for suffix, size in (('', (1080, 700)), ('-mobile', (560, 850))):
            check_gif(folder / f'mancar-casa-story{suffix}.gif', size, 17580)
        labels = json.loads((folder/'localized-labels.json').read_text(encoding='utf-8'))
        assert len(labels) == 13
        if lang in ('hi', 'zh'):
            font = freetype.Face(str(font_path(lang=lang)))
            missing = {c for values in labels.values() for value in values for c in value if not c.isspace() and not font.get_char_index(ord(c))}
            assert not missing, f'{lang}: missing glyphs {missing}'
        if lang != 'en':
            assert 'We bring strategy' not in content and 'Core Functionality' not in content
            assert 'YOUR BUSINESS SETS THE DIRECTION.' not in labels['mancar-studio-cover']
        print(f'PASS {lang}: README/profile/gallery, switches, links, glyphs, 26 animated assets and static alternatives.', flush=True)
    for still in (ROOT/'profile/assets/captures').glob('*-still-*.png'):
        with Image.open(still) as image:
            image.verify()
    print('PASS: Spanish default; all four presentation editions validated.')


if __name__ == '__main__':
    main()
