# FRVDocs

<img src="./doc/images/overview/repository-banner.png"/>

[:computer: Releases](https://github.com/jojo58fr/FRVDocs/releases) | [:bug: Report an issue](https://github.com/jojo58fr/FRVDocs/issues)

FRVDocs est un site documentaire pensé pour rassembler en un seul espace des tutoriels, guides, ressources et explications autour des outils 2D/3D du VTubing. L'objectif est de faire vivre une documentation complète et francophone en mobilisant la communauté : chaque idée qui émerge dans les canaux dédiés Discord peut devenir une page publiée sur le site.

## Contribution rapide

1. Rejoins les channels Discord `📚｜tutos-et-ressources` ou `🤔｜aide-et-questions`.
2. Partage tes questions, découvertes, astuces ou liens utiles ; toute discussion (texte, lien ou média) peut être transformée en ressource documentée.
3. Un membre du staff FRVtubers prendra la suite : il rassemble, structure et publie l'information sur FRVDocs en créditant son auteur.
4. Si tu souhaites t'impliquer davantage, propose tes propres contributions directement sur le dépôt (issues/pull requests) ou discute avec la communauté pour encadrer une page.

## Contribuer via GitHub

1. Forke `https://github.com/jojo58fr/FRVDocs`, clone ton fork et crée une branche :
   ```bash
   git clone https://github.com/<ton-pseudo>/FRVDocs.git
   cd FRVDocs
   git checkout -b feature/<sujet>
   ```
2. Rédige ta documentation dans `docs/`, `docs/moderation/`, `docs/lexique/` ou un autre dossier pertinent. Complète le front matter (titre, description, slug, auteurs, etc.).
3. Installe les dépendances et teste localement :
   ```bash
   npm install
   npm run lint
   npm run build
   npm run start
   ```
4. Pousse ta branche et ouvre une pull request vers `main` avec un descriptif clair et capture les résultats de tes tests si besoin.

## Lancer Docusaurus en local

1. `npm install` pour installer les dépendances du projet.
2. `npm run start` pour démarrer le serveur de développement et voir les pages (`http://localhost:3000` par défaut).
3. `npm run build` génère un site statique dans `build/`, utile avant un déploiement.
4. `npm run serve` permet de prévisualiser la version compilée de `build/`.

Le site est basé sur Docusaurus (React + MDX). Les fichiers Markdown de `docs/`, `docs/moderation/` ou `docs/lexique/` sont compilés automatiquement par le système.

## Vision

FRVDocs fédère les meilleures pratiques et découvertes francophones liées à la création VTuber, en offrant :

- Une documentation vivante qui couvre outils, workflow, modération et contenu.
- Un processus collaboratif : la communauté propose, le staff organise, les contributeurs sont reconnus.
- Un site ouvert à tous ceux qui veulent apprendre, partager et améliorer l'expérience VTubing.

Pour toute suggestion de contact ou question précise, consulte les correspondances sur Discord ou ouvre une discussion GitHub.

## Support et communautes
- Discord FRVtubers : https://discord.gg/meyHQYWvjU

## Contributing & Support
- Suggestions / issues: https://github.com/jojo58fr/FRVDocs/issues
- Contact Discord: TakuDev
- Contact: Joachim Miens – contact@joachim-miens.com

## Licence
La licence est sous GPLV3. Vous pouvez consulter la licence complète ici: [LICENSE.md](LICENSE.md). Un résumé de la licence se trouve ici: [GPLV3.md](GPLV3.md)