# Contribution

Merci d'envisager une contribution à FRVDocs ! Le projet fonctionne grâce aux partages de la communauté, et chaque contribution compte. Voici comment participer :

## Sur Discord

1. Rejoins `📚｜tutos-et-ressources` ou `🤔｜aide-et-questions`.
2. Poste ton contenu (astuce, lien, question, ressource) avec un contexte : outil, étape, public visé…
3. L'équipe FRVtubers relaye, structure et intègre ta contribution dans la documentation. Tu es crédité(e) par ton pseudo.

## Sur GitHub

1. Forke le dépôt officiel (`https://github.com/jojo58fr/FRVDocs`) et clone ton fork :
   ```bash
   git clone https://github.com/<ton-pseudo>/FRVDocs.git
   cd FRVDocs
   git checkout -b feature/<sujet>
   ```
2. Crée ou mets à jour un document dans `docs/`, `docs/moderation/`, `docs/lexique/` ou un dossier adapté, en renseignant bien le front matter (titre, description, slug, auteurs, etc.).
3. Vérifie ton travail avec les commandes Docusaurus :
   ```bash
   npm install
   npm run lint
   npm run build
   npm run start
   ```
4. Pousse ta branche et ouvre une pull request vers `main` avec un résumé des changements et le résultat des tests (si tu en as fait).
5. Un membre du staff relira et fusionnera en valorisant ta contribution.

## Bonnes pratiques

- Favorise les sources francophones ou contextualise les ressources étrangères.
- Rédige avec une orthographe soignée : la qualité écrit reflète l'image FRVtubers.
- Respecte les licences : cite les auteurs, liens et captures.
- Besoin d'inspiration ? Consulte `docs/` et `docs/lexique/` pour voir les formats en place.

Le staff FRVtubers s'engage à reprendre les contributions bénévolement, les mettre à jour et les valoriser dans la documentation. Merci pour ton soutien !
