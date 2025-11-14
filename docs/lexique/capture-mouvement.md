---
title: Capture de mouvement
sidebar_label: Capture de mouvement
description: De la capture optique aux formats BVH utilisés par les VTubers pour animer leurs avatars.
slug: /lexique/capture-mouvement
---

## Définition
La **capture de mouvement** (motion capture ou mocap) consiste à enregistrer la position et l’orientation d’un corps réel grâce à des capteurs (optique, inertiel ou à profondeur). Ces données sont stockées sous forme de fichiers (BVH, FBX, CSV) puis appliquées à la structure squelettique d’un avatar pour reproduire fidèlement les gestes et les expressions.

## Technologies courantes
- **Suites** : capteurs OptiTrack/Vicon (studios pro), Kinect, iPhone Face ID, webcams + outils open source (OpenTrack, VSeeFace).  
- **Formats** : BVH (Biovision Hierarchy) pour la hiérarchie osseuse, FBX pour l’intégration 3D, blendshapes pour les expressions.  
- **Pipeline** : capture → nettoyage → retargeting (adaptation au rig) → live ou export.

## Application
Les VTubers utilisent la mocap pour obtenir une animation naturelle tout en restant en direct. La solution peut être mobile (tracking facial avec smartphone) ou studio (full body). Cela augmente la qualité perçue et réduit l’effort de keyframe manuel.

## Sources
- [Wikipedia – Capture de mouvement](https://fr.wikipedia.org/wiki/Capture_de_mouvement)
