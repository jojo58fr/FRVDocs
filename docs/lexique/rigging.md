---
title: Rigging (animation squelettique)
sidebar_label: Rigging
description: Le rigging permet de relier un squelette aux mouvements d’un avatar VTubing.
slug: /lexique/rigging
---

## Définition
Le **rigging** est le procédé qui consiste à construire un squelette virtuel (bones/joints) sous une surface polygonale de manière à pouvoir l’animer. Chaque os est hiérarchisé et transmet ses rotations aux vertices (weights), permettant à un seul contrôleur de déplacer un bras entier ou une expression faciale.

## Usage VTubing
- **Bones principaux** : colonne, clavicule, bras, mains, doigts, visage.  
- **Contraintes et physics** : ajout de malles dynamiques pour simuler les cheveux ou les vêtements.  
- **Blendshapes** : expressions faciales supplémentaires (sourire, chute de la bouche, clignement).  
- **Retargeting** : adaptation du rig à différentes captures (mocap, tracking facial, keyframes).

## Pourquoi c'est critique
Un rig propre facilite la capture en direct et la qualité des animations : il réduit la friction entre les données d’entrée (tracking) et les mouvements visibles à l’écran. Sans rigging, chaque mouvement serait une animation manuelle, difficilement compatible avec un live.

## Sources
- [Wikipedia – Rigging (computer graphics)](https://en.wikipedia.org/wiki/Rigging_(computer_graphics))
