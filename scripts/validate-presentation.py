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
assert profile_text.replace('"assets/','"profile/assets/').replace('(../docs/','(docs/').replace('href="../docs/','href="docs/')==root_text,'README variants diverged'
assert 'beauty' not in root_text.lower(),'Removed project reintroduced'
assert not re.search(r'\[[^\]]+\]\([^)]+\)', root_text), 'Presentation text links must use branded buttons'
button_paths = set(re.findall(r'src="(profile/assets/buttons/[^"]+)"', root_text))
assert button_paths, 'Missing branded link buttons'
for relative in button_paths:
    with Image.open(ROOT / relative) as button:
        assert button.width <= 608 and button.height >= 88, 'Button exceeds mobile width or minimum target height'
        button.verify()
assert {p.name for p in (ROOT/'profile/assets/buttons').glob('*.png')} == {Path(p).name for p in button_paths}, 'Unused button artwork'
headings=re.findall(r'^#{1,6} .+$',root_text,re.M)
assert headings[0]=='# Mancar Software','Public profile must introduce Mancar before its projects'
assert headings[1] == '## Selected Projects', 'Projects must immediately follow the introduction'
assert '## Working With Us' in headings, 'Missing practical FAQ'
assert '## Selected Projects' in headings,'Public profile must retain its project catalogue'
project_headings=[heading for heading in headings if heading.endswith(('01 / OdontoCare','02 / VetCare Pro','03 / Alma Vet','04 / Casa Nativa'))]
for heading,project in zip(project_headings,('01 / OdontoCare','02 / VetCare Pro','03 / Alma Vet','04 / Casa Nativa')):
    assert heading.endswith(project),f'Unexpected project heading: {heading}'
assert len(project_headings)==4,'Public profile must retain all four selected projects'
for anchor in ('odontocare','vetcare','almavet','casanativa'):
    assert f'<a id="{anchor}"></a>' in root_text,f'Missing project anchor: {anchor}'
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
    # Eight animated studio panels, one featured story, and four project tours.
    if relative.endswith('README.md'): assert refs.reduced==26,'Unexpected or missing animated presentation sources'

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
            assert duration==(4 if slug=='casanativa' else 3)*4360,(path,duration)
            assert path.with_suffix('.png').is_file()
        gif_bytes+=path.stat().st_size
    count=4 if slug=='casanativa' else 3
    for i in range(count):
        with Image.open(ROOT/f'profile/assets/captures/{slug}-still-{i+1:02}.png') as still:
            still.verify()

studio_bytes=0
for name,desktop_h,mobile_h in (('starting-points',720,970),('first-conversation',530,745),('studio-cover',620,750),('disciplines',690,815),('approach',560,770),('contact',410,460),('team',670,950),('support',650,910)):
    for suffix,height in (('',desktop_h),('-mobile',mobile_h)):
        path=ROOT/f'profile/assets/mancar-{name}{suffix}.gif'
        with Image.open(path) as media:
            assert media.size==(560 if suffix else 1080,height),(path,media.size)
            frames=[frame.convert('RGB') for frame in ImageSequence.Iterator(media)]
            assert any(ImageChops.difference(frames[0],frame).getbbox() for frame in frames[1:]),f'Static GIF: {path}'
            media.seek(0)
            assert sum(frame.info.get('duration',0) for frame in ImageSequence.Iterator(media))==7680
        with Image.open(path.with_suffix('.png')) as still:
            assert still.size==(560 if suffix else 1080,height)
            still.verify()
        studio_bytes+=path.stat().st_size
assert studio_bytes<4*1024*1024,'Studio animation exceeds the 4 MiB combined budget'
for suffix, size in (('', (1080,700)), ('-mobile', (560,850))):
    path = ROOT/f'profile/assets/mancar-casa-story{suffix}.gif'
    with Image.open(path) as media:
        assert media.size == size
        frames = [frame.convert('RGB') for frame in ImageSequence.Iterator(media)]
        assert any(ImageChops.difference(frames[0], frame).getbbox() for frame in frames[1:])
        media.seek(0)
        assert sum(frame.info.get('duration',0) for frame in ImageSequence.Iterator(media)) == 17580
    with Image.open(path.with_suffix('.png')) as still:
        assert still.size == size
        still.verify()
print(f'PASS: synchronized README variants, local paths, gallery anchors, alt text, static sources, 16 studio animations, 2 featured stories, 8 project tours, and 13 stills. Studio: {studio_bytes/1024/1024:.2f} MiB; projects: {gif_bytes/1024/1024:.2f} MiB across desktop + mobile.')
