"""Build GitHub-native language editions, including localized animated artwork."""
from pathlib import Path
from html import escape
import json
import re
import argparse
from PIL import Image, ImageDraw
import locale_runtime as locale
from studio_motion import build_studio, PANELS
from project_showcases import build_showcases, PROJECTS
from project_story import build_story
from link_buttons import brand_links

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'profile/assets'
LANGUAGES = {'es': 'Español', 'en': 'English', 'zh': '简体中文', 'hi': 'हिन्दी'}


def readme_name(lang):
    return 'README.md' if lang == 'es' else f'README.{lang}.md'


def gallery_name(lang):
    return 'PROJECT-GALLERY.md' if lang == 'es' else f'PROJECT-GALLERY.{lang}.md'


def translate_document(content):
    # Translate text, not URLs, filenames, IDs, or media-query attributes.
    pieces = re.split(r'(<[^>]+>)', content)
    for i, piece in enumerate(pieces):
        if piece.startswith('<'):
            if 'src="assets/buttons/' in piece:
                continue  # brand_links already translated this accessible label.
            def alt(match):
                return 'alt="' + escape(locale.translate(match[1]), quote=True) + '"'
            pieces[i] = re.sub(r'alt="([^"]*)"', alt, piece)
        else:
            pieces[i] = locale.translate(piece)
    return ''.join(pieces)


def language_buttons(lang):
    directory = ASSETS / 'languages'
    directory.mkdir(exist_ok=True)
    original = locale.LANG
    links = []
    for code, label in LANGUAGES.items():
        locale.LANG = code
        im = Image.new('RGB', (240, 88), '#193B38')
        d = ImageDraw.Draw(im)
        d.rectangle((0, 0, 239, 87), outline='#61847B', width=2)
        size = 28
        locale.paint(d, ((240-locale.measure(label, size))/2, 28), label, size, '#F4F2EB')
        im.save(directory / f'{code}.png')
        # Each README lives beside the other editions, in root or profile/.
        links.append(f'<a href="{readme_name(code)}"><img src="assets/languages/{code}.png" width="120" height="44" alt="{label}" /></a>')
    locale.LANG = original
    return '\n'.join(links)


def localized_gallery(lang):
    parts = [f'# {locale.translate("A closer look at the work")}',
             locale.translate('Still frames from the project interface tours. All clinical names and records are fictional demonstration data; website content comes from the repositories. These previews document interface design and do not constitute evidence of a production deployment or end-to-end backend testing.')]
    anchors = {'odontocare': 'odontocare', 'vetcare': 'vetcare-pro', 'almavet': 'alma-vet', 'casanativa': 'casa-nativa'}
    for slug, project in PROJECTS.items():
        parts.append(f'<a id="{anchors[slug]}"></a>\n\n## {project["name"]}')
        for i, (step, caption) in enumerate(zip(project['steps'], project['captions'])):
            translated = locale.translate(caption)
            parts += [f'### {i+1:02} / {locale.translate(step)}', translated,
                      f'![{project["name"]}: {translated}](../profile/assets/captures/{slug}-still-{i+1:02}.png)']
    parts.append(f'[{locale.translate("Capture sources and reproduction notes")} (English)](PROJECT-EVIDENCE.md)')
    (ROOT / 'docs' / gallery_name(lang)).write_text('\n\n'.join(parts) + '\n', encoding='utf-8')


def build_edition(template, lang, artwork=True):
    locale.set_locale(lang)
    out = ASSETS if lang == 'en' else ASSETS / lang
    out.mkdir(parents=True, exist_ok=True)
    manifest = out / 'localized-labels.json'
    if artwork:
        build_showcases(out, write_gallery=False)
        build_studio(out)
        build_story(out)
        manifest.write_text(json.dumps(locale.LABELS, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    else:
        locale.LABELS.update(json.loads(manifest.read_text(encoding='utf-8')))
    # Stable IDs make cross-section navigation independent of translated headings.
    template = re.sub(r'^## (.+)$', lambda m: '<a id="' + re.sub(r' +', '-', re.sub(r'[^a-z0-9 ]', '', m[1].lower())) + '"></a>\n\n' + m[0], template, flags=re.M)
    content = brand_links(template, out)
    content = translate_document(content)
    def artwork_alt(match):
        tag = match[0]
        source = re.search(r'src="assets/([^"/]+)\.(gif|png)"', tag)
        if source:
            name = source[1].removesuffix('-mobile')
            if name in locale.LABELS:
                label = escape(' · '.join(locale.LABELS[name]), quote=True)
                tag = re.sub(r'alt="[^"]*"', lambda _: f'alt="{label}"', tag)
        return tag
    content = re.sub(r'<img\b[^>]+>', artwork_alt, content)
    if lang != 'en':
        content = re.sub(r'"assets/(?!captures/|logos/)', f'"assets/{lang}/', content)
    content = content.replace('../docs/PROJECT-GALLERY.md', '../docs/' + gallery_name(lang))
    content = language_buttons(lang) + '\n\n' + content
    profile = ROOT / 'profile' / readme_name(lang)
    profile.write_text(content, encoding='utf-8')
    (ROOT / readme_name(lang)).write_text(content.replace('"assets/', '"profile/assets/').replace('href="../docs/', 'href="docs/'), encoding='utf-8')
    localized_gallery(lang)
    print(f'Built {lang}: {len(locale.LABELS)} localized animated panels and translated README/gallery.', flush=True)


def build_all(template):
    parser = argparse.ArgumentParser()
    parser.add_argument('--locale', choices=LANGUAGES, action='append')
    parser.add_argument('--content-only', action='store_true', help='Reuse existing localized media for copy-only changes')
    args = parser.parse_args()
    for lang in args.locale or LANGUAGES:
        build_edition(template, lang, artwork=not args.content_only)
