import pathlib
from collections import defaultdict
import re

def parse_frontmatter(text):
    if not text.startswith('---'):
        return {}
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}
    fm = parts[1]
    data = {}
    for line in fm.strip().splitlines():
        if ':' in line:
            key, val = line.split(':', 1)
            data[key.strip()] = val.strip()
    return data

base_dir = pathlib.Path('docs/lexique')
entries = []
for path in sorted(base_dir.glob('*.md')):
    if path.name == 'index.md':
        continue
    text = path.read_text('utf-8')
    fm = parse_frontmatter(text)
    title = fm.get('title', path.stem)
    slug = fm.get('slug', f'/lexique/{path.stem}')
    definition = ''
    match = re.search(r'## Définition\n(.*?)(\n##|$)', text, re.S)
    if match:
        definition = match.group(1).strip().split('\n')[0]
    entries.append({'title': title, 'slug': slug, 'definition': definition})

groups = defaultdict(list)
for entry in entries:
    letter = entry['title'][0].upper()
    if not letter.isalpha():
        letter = '0-9'
    groups[letter].append(entry)

index_lines = [
"---",
"title: Lexique VTubing",
"sidebar_label: Lexique alphabétique",
"description: Une table des matières alphabétique pour tous les termes VTubing documentés.",
"slug: /lexique",
"---",
"",
"## Lexique alphabétique du VTubing",
"",
"<div class=\"lexicon-wiki\">",
"  <p class=\"lexicon-summary\">Ce dossier rassemble chaque terme important dans une fiche à part. Chaque section alphabétique regroupe les définitions et renvoie à leur fiche dédiée.</p>",
]
for letter in sorted(groups):
    index_lines.append("  <section class=\"lexicon-section\">")
    index_lines.append("    <div class=\"lexicon-letter-row\">")
    index_lines.append(f"      <span class=\"lexicon-letter-heading\">{letter}</span>")
    index_lines.append("      <span class=\"lexicon-letter-divider\"></span>")
    index_lines.append("    </div>")
    index_lines.append("    <div class=\"lexicon-grid\">")
    for entry in sorted(groups[letter], key=lambda e: e['title']):
        index_lines.append(f"      <a class=\"lexicon-card\" href=\"/docs{entry['slug']}\">")
        index_lines.append("        <div>")
        index_lines.append(f"          <strong>{entry['title']}</strong>")
        if entry['definition']:
            index_lines.append(f"          <p>{entry['definition']}</p>")
        index_lines.append("        </div>")
        index_lines.append("      </a>")
    index_lines.append("    </div>")
    index_lines.append("  </section>")

index_lines.append("  <p class=\"lexicon-summary\">Chaque fiche approfondit le terme, les outils associés et les sources. Pour contribuer, suivez le lien vers la page concernée, ajustez le contenu, puis signalez les sources vérifiées.</p>")
index_lines.append("</div>")

path = base_dir / 'index.md'
path.write_text('\n'.join(index_lines) + '\n', encoding='utf-8')
print('index updated', len(entries))
