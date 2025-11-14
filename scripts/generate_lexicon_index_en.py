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

base_dir = pathlib.Path('i18n/en/docusaurus-plugin-content-docs/current/lexique')
entries = []
for path in sorted(base_dir.glob('*.md')):
    if path.name == 'index.md':
        continue
    text = path.read_text('utf-8')
    fm = parse_frontmatter(text)
    title = fm.get('title', path.stem)
    slug = fm.get('slug', f'/lexique/{path.stem}')
    gd = re.search(r'## Definition\n(.*?)(\n##|$)', text, re.S)
    definition = gd.group(1).strip().split('\n')[0] if gd else ''
    entries.append({'title': title, 'slug': slug, 'definition': definition})

groups = defaultdict(list)
for entry in entries:
    letter = entry['title'][0].upper()
    if not letter.isalpha():
        letter = '0-9'
    groups[letter].append(entry)

lines = [
"---",
"title: VTubing Lexicon",
"sidebar_label: Alphabetical Lexicon",
"description: English table of contents for VTubing terms.",
"slug: /lexique",
"---",
"",
"## Alphabetical VTubing lexicon",
"",
"<div class=\"lexicon-wiki\">",
"  <p class=\"lexicon-summary\">This glossary gathers each key term under alphabetical sections with a link to its dedicated page.</p>",
]
for letter in sorted(groups):
    lines.append("  <section class=\"lexicon-section\">")
    lines.append("    <div class=\"lexicon-letter-row\">")
    lines.append(f"      <span class=\"lexicon-letter-heading\">{letter}</span>")
    lines.append("      <span class=\"lexicon-letter-divider\"></span>")
    lines.append("    </div>")
    lines.append("    <div class=\"lexicon-grid\">")
    for entry in sorted(groups[letter], key=lambda e: e['title']):
        lines.append(f"      <a class=\"lexicon-card\" href=\"/docs{entry['slug']}\">")
        lines.append("        <div>")
        lines.append(f"          <strong>{entry['title']}</strong>")
        if entry['definition']:
            lines.append(f"          <p>{entry['definition']}</p>")
        lines.append("        </div>")
        lines.append("      </a>")
    lines.append("    </div>")
    lines.append("  </section>")
lines.append("  <p class=\"lexicon-summary\">Each article deep-dives into the term, tools, and sources while inviting contributions in English or French.</p>")
lines.append("</div>")

(pathlib.Path('i18n/en/docusaurus-plugin-content-docs/current/lexique') / 'index.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('english index updated', len(entries))
