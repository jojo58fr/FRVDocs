import pathlib
from textwrap import dedent

terms = [
    ('2-5d-idol', 'Idol 2.5D', '2.5D Idol',
     'Idol VTuber qui se produit à la fois dans des espaces virtuels et en live-action, parfois sans révéler son visage.',
     'Idol VTubers who perform in both virtual and live-action spaces (which may or may not include a face reveal), sometimes blending both styles. Examples of 2.5D idol groups are 22/7 and Strawberry Prince (STPR).'),
    ('affiliate', 'Affiliate', 'Affiliate',
     'Sur Twitch, un affilié est un streamer validé pour la monétisation ; chez Hololive cela désigne un talent inactif mais toujours rattaché pour des apparitions ou la marchandise.',
     'On Twitch, a streamer whose channel has been approved for monetization. In hololive specifically, refers instead to a streamer who has ceased general activities but is still associated with the company for cameo appearances and merchandise.'),
    ('akasupa', 'Akasupa', 'Akasupa',
     'Un don hautement valorisé sur YouTube, reconnaissable à son fond rouge (akai), autrement dit un superchat premium.',
     'A high value donation message on YouTube, denoted by its red (赤, aka?) background color (see: superchat). Short for "akai superchat" in Japanese.'),
    ('asmrtist', 'ASMRtist', 'ASMRtist',
     'Un VTuber spécialisé dans l’ASMR : des triggers doux (sleep, nettoyage d’oreilles) ou plus suggestifs, parfois aussi appelé ASMRist.',
     'A VTuber who specializes in ASMR content. Not necessarily lewd: covers clean triggers as well as more suggestive ones. Also called "ASMRist".'),
    ('anti', 'Anti', 'Anti',
     'Un troll ou un hater qui critique ouvertement un VTuber.',
     'A troll or hater.'),
    ('avtuber', 'AVTuber', 'AVTuber',
     'Un VTuber qui produit du contenu R-18 en dehors de YouTube/Twitch, parfois associé à une agence de niche.',
     'A VTuber who mainly does R-18 content outside of mainstream platforms, sometimes including live-action work.'),
    ('babiniku', 'Babiniku', 'Babiniku',
     'Un VTuber masculin qui incarne un personnage féminin en assumant son genre réel.',
     'A VTuber who is male in real life but uses a female model, often using a voice changer or no voice.'),
    ('bj', 'Broadcast Jockey', 'Broadcast Jockey',
     'Terme coréen pour désigner un livestreamer.',
     '"Broadcast Jockey," a Korean term for a livestreamer.'),
    ('black-company', 'Black company', 'Black company',
     'Une agence exploitante qui maltraite ses talents (non-paiement, doxxing, harcèlement).',
     'A VTuber agency that conducts exploitative, controversial and unethical practices.'),
    ('carrier-pigeon', 'Carrier pigeon', 'Carrier pigeon',
     'Un spectateur relayant les messages d’un stream vers un autre, souvent perçu comme du stream sniping.',
     'A viewer who relays messages between two streams via Live Chat, often frowned upon.'),
    ('clipper', 'Clipper', 'Clipper',
     'Une chaîne qui crée des clips à partir d’un stream, parfois officielle, parfois fan.',
     'A channel that creates clips of a VTuber’s content, often third-party but sometimes official.'),
    ('clipping', 'Clipping', 'Clipping',
     'Créer des vidéos à partir d’extraits d’un stream pour immortaliser les moments marquants.',
     'Creating videos from segments of a stream, sometimes restricted by clipping rules.'),
    ('collab', 'Collab', 'Collab',
     'Une collaboration réunissant plusieurs VTubers dans un stream.',
     'A collaboration stream where multiple VTubers appear together.'),
    ('delivery', 'Delivery (haishin)', 'Delivery',
     'Traduction de 配信 : le terme japonais pour "stream" ou "diffusion."',
     'Literal translation of the Japanese term for a broadcast or live stream (配信, haishin).'),
    ('doxxing', 'Doxxing', 'Doxxing',
     'Révéler l’identité réelle d’un talent : acte condamné mettant fin à l’anonymat.',
     'Revealing a VTuber talent’s real-life identity and personal details, widely condemned.'),
    ('dullahan', 'Dullahan', 'Dullahan',
     'Terme coréen pour un streamer sans visage visible, souvent avec une image statique.',
     'A Korean term for a streamer who does not show their face, sometimes only showing neck-down.'),
    ('endurance', 'Endurance stream', 'Endurance stream',
     'Défi de stream souvent orienté sur un objectif de souscriptions ou de durée.',
     'A challenge stream focusing on a goal, typically a YouTube subscriber milestone.'),
    ('enjou', 'Enjou', 'Enjou',
     'Controverse massive en ligne, équivalent japonais de "getting flamed."',
     'Massive online backlash against a VTuber, similar to getting canceled.'),
    ('fan-name', 'Fan name', 'Fan name',
     'Surnom collectif attribué aux fans d’un VTuber.',
     'A group nickname for a VTuber’s fans, often given by the talent.'),
    ('fleshtuber', 'Fleshtuber', 'Fleshtuber',
     'Un streamer qui n’utilise pas de modèle virtuel.',
     'A streamer who is not a VTuber.'),
    ('free-chat', 'Free Chat', 'Free Chat',
     'Salle de chat persistante créée via une diffusion programmée sur YouTube.',
     'A scheduled YouTube chat room that uses a stream as a persistent waiting area.'),
    ('gachikoi', 'Gachikoi', 'Gachikoi',
     'Fan obsessionnel qui "tombe amoureux" d’un VTuber et dépasse souvent les limites.',
     'An obsessed fan who seriously falls in love with a VTuber.'),
    ('graduation', 'Graduation', 'Graduation',
     'Stream d’adieu ou départ d’une agence qui marque la retraite du talent.',
     'A retirement stream marking a VTuber leaving the scene or agency.'),
    ('guerrilla', 'Guerrilla stream', 'Guerrilla stream',
     'Unstream non annoncé, souvent spontané.',
     'Unscheduled stream with minimal prior notice, used for surprise content.'),
    ('gyakutotsu', 'Gyakutotsu', 'Gyakutotsu',
     'Généralement un stream anniversaire où le VTuber appelle des amis (reverse call-in).',
     'Reverse call-in stream where the streamer calls selected friends.'),
    ('kami-oshi', 'Kami-oshi', 'Kami-oshi',
     'Super favori du fan, le coup de cœur ultime.',
     'Super-favorite or top favorite.'),
    ('kirinuki', 'Kirinuki', 'Kirinuki',
     'Terme japonais pour désigner un clip vidéo.',
     'Japanese term for clips, literally "cut-out."'),
    ('kojin-zei', 'Kojin-zei', 'Kojin-zei',
     'VTuber indépendant, souvent freelance ou dans un groupe indie.',
     'Independent VTuber, often freelancing and not tied to an agency.'),
    ('kusa', 'Kusa', 'Kusa',
     'Exprime le rire, l’équivalent de "LOL" en japonais.',
     'An expression of laughter derived from the Japanese word for grass, like "LOL".'),
    ('liver', 'Liver', 'Liver',
     'Contraction japonaise de "livestreamer."',
     'A wasei-eigo pseudo-loanword meaning livestreamer.'),
    ('lore', 'Lore', 'Lore',
     'Les éléments fictionnels autour d’un VTuber.',
     'Fictional background and setting of a VTuber.'),
    ('mama', 'Mama', 'Mama',
     'Le designer/illustrateur du VTuber.',
     'The designer, illustrator, or rigger of a VTuber model.'),
    ('member', 'Member', 'Member',
     'Spectateur payant à un abonnement de chaîne.',
     'A paid channel member with perks and a green name badge.'),
    ('mengen', 'Mengen', 'Mengen',
     'Contenu réservé aux membres (member-exclusive).',
     'Members-only streams or content from the term "member gentei."'),
    ('moderator', 'Moderateur', 'Moderator',
     'Personne chargée de modérer le chat, parfois un autre VTuber.',
     'A viewer granted the privilege to moderate chat, often identified by a spanner icon.'),
    ('mute', 'Mute', 'Mute',
     'VTuber qui ne parle pas pendant ses streams.',
     'A VTuber who never speaks in their content.'),
    ('off-collab', 'Off-collab', 'Off-collab',
     'Collaboration en personne entre VTubers.',
     'An offline collaboration where VTubers meet IRL.'),
    ('oshi-mark', 'Oshi mark', 'Oshi mark',
     'Emoji officiel représentant le VTuber.',
     'Emoji or icon officially chosen to represent a VTuber.'),
    ('oshi', 'Oshi', 'Oshi',
     'Ton VTuber préféré.',
     'Your favorite VTuber.'),
    ('otsu', 'Otsu', 'Otsu',
     '"Otsukaresama" utilisé pour dire merci à la fin d’un stream.',
     'Short for "otsukaresama," meaning thanks after a stream.'),
    ('papa', 'Papa', 'Papa',
     'Designer/rigueur masculin du modèle VTuber.',
     'The male illustrator or rigger of a VTuber model.'),
    ('past-life', 'Past life', 'Past life',
     'Identité du talent avant le VTubing, habituellement taboue.',
     'The identity a VTuber had before debuting, usually taboo to reveal.'),
    ('pngtuber', 'PNGTuber', 'PNGTuber',
     'VTuber utilisant une image statique (PNG).',
     'A VTuber using a static PNG instead of an animated model.'),
    ('pre-debut', 'Pre-debut', 'Pre-debut',
     'Design révélé avant un début officiel.',
     'A VTuber whose design is unveiled but has no official debut yet.'),
    ('raid', 'Raid', 'Raid',
     'Transfert automatique de spectateurs vers un autre stream.',
     'Automatic viewer transfer to another stream when closing a live.'),
    ('re-debut', 'Re-debut', 'Re-debut',
     'Nouvel arrival après un changement de modèle ou d’agence.',
     'Another debut stream after a redesign or agency move.'),
    ('redesign', 'Redesign', 'Redesign',
     'Modification permanente du design du VTuber.',
     'A permanent overhaul of the VTuber’s appearance.'),
    ('relay', 'Relay stream', 'Relay stream',
     'Série de streams sur un thème, chacun passant la main au suivant.',
     'Series of themed streams where each VTuber passes viewers like a baton.'),
    ('reincarnation', 'Réincarnation', 'Reincarnation',
     'VTuber retiré revenant sous une nouvelle identité.',
     'Retired VTuber restarting activities under a new character.'),
    ('rtx-model', 'RTX model', 'RTX model',
     'Cosplay d’un modèle VTuber en live-action, pour un rendu réaliste.',
     'Cosplaying one’s VTuber model, jokingly called RTX for realism.'),
    ('seiso', 'Seiso', 'Seiso',
     'VTubers à l’image pure, sans vulgarité ni sujets salaces.',
     'VTubers whose content stays clean and wholesome.'),
    ('stream-sniping', 'Stream sniping', 'Stream sniping',
     'Regarder un stream pour obtenir un avantage dans un jeu.',
     'Watching a stream to gain an unfair advantage in a multiplayer game.'),
    ('subathon', 'Subathon', 'Subathon',
     'Stream marathon où chaque abonnement prolonge l’événement.',
     'Marathon streaming session where each subscription adds time.'),
    ('talent', 'Talent', 'Talent',
     'La personne derrière l’avatar, considérée irremplaçable.',
     'The performer behind the VTuber, considered irreplaceable.'),
    ('teetee', 'Teetee', 'Teetee',
     'Terme affectueux décrivant une relation chérie entre deux VTubers.',
     'Affectionate slang for cherished connections between VTubers, often pairings.'),
    ('totsumachi', 'Totsumachi', 'Totsumachi',
     'Stream «凸待ち» où le VTuber attend des appels entrants.',
     'A call-in stream where a VTuber waits for friends or guests to call in.'),
    ('unarchived', 'Unarchived', 'Unarchived',
     'Stream sans VOD sauvegardée, souvent pour des raisons de droits.',
     'A stream destined to have no retained VOD, frequently for copyright reasons.'),
    ('utaite', 'Utaite', 'Utaite',
     'Chanteur amateur qui publie des covers, souvent sur Niconico ou YouTube.',
     'A singer known for cover songs on Niconico or YouTube.'),
    ('utattemita', 'Utattemita', 'Utattemita',
     'Cover song (歌ってみた) ponctuant la scène utaite.',
     'A cover song (lit. "I tried to sing").'),
    ('utawaku', 'Utawaku', 'Utawaku',
     'Stream de chant ou de karaoké (歌枠).',
     'A karaoke or singing stream.'),
    ('vliver', 'VLiver', 'VLiver',
     'Live-streamer virtuel sur IRIAM (Japon).',
     'Virtual livestreamer on IRIAM JP, short for virtual liver.'),
    ('vup', 'VUP', 'VUP',
     'Terme chinois pour VTuber, issu de "Virtual UP" sur bilibili.',
     'Chinese term for VTuber, popular on bilibili, derived from "Virtual UP."'),
    ('zatsudan', 'Zatsudan', 'Zatsudan',
     'Stream de discussion libre (雑談), équivalent du "Just Chatting".',
     'A chat stream, also known as the Just Chatting category on Twitch.'),
]

base_fr = dedent("""---

title: {title_fr}
sidebar_label: {title_fr}
description: Lexique VTubing - {title_fr}
slug: /lexique/{slug}
---

## Définition
{fr_def}

## Sources
- https://streamlabs.com/content-hub/post/vtubing-custom-slang-beginners
""")

base_en = dedent("""---

title: {title_en}
sidebar_label: {title_en}
description: VTubing glossary entry
slug: /lexique/{slug}
---

## Definition
{en_def}

## Sources
- https://streamlabs.com/content-hub/post/vtubing-custom-slang-beginners
""")

out_dir_fr = pathlib.Path('docs/lexique')
out_dir_en = pathlib.Path('i18n/en/docusaurus-plugin-content-docs/current/lexique')
out_dir_fr.mkdir(parents=True, exist_ok=True)
out_dir_en.mkdir(parents=True, exist_ok=True)

for slug, title_fr, title_en, fr_def, en_def in terms:
    fr_path = out_dir_fr / f"{slug}.md"
    en_path = out_dir_en / f"{slug}.md"
    fr_path.write_text(base_fr.format(slug=slug, title_fr=title_fr, fr_def=fr_def), encoding='utf-8')
    en_path.write_text(base_en.format(slug=slug, title_en=title_en, en_def=en_def), encoding='utf-8')
print('wrote', len(terms))
