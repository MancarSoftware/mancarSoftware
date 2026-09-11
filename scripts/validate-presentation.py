"""Validate generated README paths, gallery coverage, and animated media integrity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
from PIL import Image, ImageChops, ImageSequence
import re

ROOT=Path(__file__).resolve().parents[1]
class References(HTMLParser):
    def __init__(self):
        super().__init__();self.paths=[];self.images=0;self.reduced=0
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='img':
            assert attrs.get('alt'), 'Missing image alternative'
            self.images+=1
        if tag=='source' and 'prefers-reduced-motion' in attrs.get('media',''):
            assert attrs['srcset'].endswith('.png'), 'Reduced-motion source must be static'
            self.reduced+=1
        for key in ('src','srcset','href'):
            if key in attrs:self.paths.append(attrs[key])

root_text=(ROOT/'README.md').read_text(encoding='utf-8')
profile_text=(ROOT/'profile/README.md').read_text(encoding='utf-8')
assert profile_text.replace('"assets/','"profile/assets/').replace('(../docs/','(docs/')==root_text,'README variants diverged'
assert 'beauty' not in root_text.lower(),'Removed project reintroduced'
for relative in ('README.md','profile/README.md','docs/PROJECT-GALLERY.md'):
    path=ROOT/relative;content=path.read_text(encoding='utf-8');refs=References();refs.feed(content)
    refs.paths.extend(re.findall(r'\]\(([^)]+)\)',content))
    for target in refs.paths:
        target=urlsplit(target)
        if target.scheme or not target.path:continue
        local=(path.parent/unquote(target.path)).resolve()
        assert local.is_file(), f'{relative}: missing {local}'
        if target.fragment and local.suffix=='.md':
            headings=re.findall(r'^#{1,6} (.+)$',local.read_text(encoding='utf-8'),re.M)
            slugs=[re.sub(r' +','-',re.sub(r'[^a-z0-9 ]','',h.lower())) for h in headings]
            assert target.fragment in slugs,f'Missing gallery anchor: {target.fragment}'
    # Original header has one static source; eight responsive animations have two.
    if relative.endswith('README.md'): assert refs.reduced>=17,'An animated panel is missing static sources'

gif_bytes=0
for slug in ('odontocare','vetcare','almavet','casanativa'):
    for suffix in ('','-mobile'):
        path=ROOT/f'profile/assets/project-{slug}{suffix}.gif'
        with Image.open(path) as media:
            expected_size=(560,740) if suffix else (1080,950)
            assert media.size==expected_size,(path,media.size)
            frames=[frame.convert('RGB') for frame in ImageSequence.Iterator(media)]
            assert any(ImageChops.difference(frames[0],frame).getbbox() for frame in frames[1:]),f'Static GIF: {path}'
            media.seek(0)
            duration=sum(frame.info.get('duration',0) for frame in ImageSequence.Iterator(media))
            assert duration==(4 if slug=='casanativa' else 3)*4560,(path,duration)
            assert path.with_suffix('.png').is_file()
        gif_bytes+=path.stat().st_size
    count=4 if slug=='casanativa' else 3
    for i in range(count):
        with Image.open(ROOT/f'profile/assets/captures/{slug}-still-{i+1:02}.png') as still:
            still.verify()
print(f'PASS: README variants, local paths, gallery anchors, alt text, static sources, 8 animated tours, and 13 stills. Tour assets: {gif_bytes/1024/1024:.2f} MiB across desktop + mobile.')
