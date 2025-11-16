---
sidebar_position: 3
title: Installation de VSeeFace sous Linux ou Mac (via Wine)
description: Comment installer VSeeFace sous Linux ou Mac
slug: /installation-linux-vseeface
sidebar_label: Installation de VSeeFace sous Linux ou Mac (via Wine)
---

Ce document fournit une procédure claire pour installer et utiliser **VSeeFace** sous Linux voir peux-être Mac, ainsi que des solutions de contournement lorsque certaines fonctionnalités (comme la webcam) ne fonctionnent pas correctement.

---

## ⚠️ Problèmes connus

- **CPU très élevé** : essayez de supprimer ou renommer `LeapCV5.dll`.
- **MacOS** : OpenGL étant déprécié, VSeeFace ne fonctionne généralement pas via Wine (modèles non rendus).
- **Webcam** : les versions de Wine < 6 ne permettent pas la lecture de webcams.

---

## ✔️ Installation de VSeeFace via Wine (Linux)

### 1. Installer Wine 64 bits
Assurez-vous d'avoir la version 64 bits de Wine :

```bash
sudo apt install wine64 winetricks
```

### 2. Préparer un préfixe 64 bits

```bash
WINEARCH=win64 WINEPREFIX=~/.wine64 winecfg
```

### 3. Installer la police Arial et Visual C++ 2015

Placez `Arial.ttf` dans :

```
~/.wine64/drive_c/Windows/Fonts/
```

Puis installez le runtime VC++ 2015 :

```bash
WINEARCH=win64 WINEPREFIX=~/.wine64 winetricks vcrun2015
```

### 4. Installer VSeeFace

Décompressez VSeeFace dans :

```
~/.wine64/drive_c/VSeeFace/
```

Puis lancez‑le :

```bash
WINEARCH=win64 WINEPREFIX=~/.wine64 wine VSeeFace.exe
```

---

## 💡 Paramètres Wine spécifiques

Depuis **VSeeFace v1.13.33f** :

- Définir une couleur d'arrière‑plan :  
  ```bash
  wine VSeeFace.exe --background-color '#00FF00'
  ```
- Désactiver le mode Wine :  
  ```bash
  wine VSeeFace.exe --disable-wine-mode
  ```

Depuis **v1.13.37c**, il faut supprimer `GPUManagementPlugin.dll` pour que VSeeFace fonctionne.

---

## 📷 Solution si la webcam ne fonctionne pas sous Wine

Utiliser **OpenSeeFace** comme source de tracking.

### 1. Installer les dépendances

```bash
sudo apt-get install python3 python3-pip python3-virtualenv git
```

### 2. Installer OpenSeeFace

```bash
git clone https://github.com/emilianavt/OpenSeeFace
cd OpenSeeFace
virtualenv -p python3 env
source env/bin/activate
pip3 install onnxruntime opencv-python pillow numpy
```

### 3. Lancer le tracker

```bash
source env/bin/activate
python facetracker.py -c 0 -W 1280 -H 720 --discard-after 0 --scan-every 0 --no-3d-adapt 1 --max-feature-updates 900
```

Pour afficher les points du tracking :  
```bash
python facetracker.py ... -v 3 -P 1
```

Ce script envoie les données de tracking à VSeeFace via **UDP localhost**.

---

## ❗ Limitations sous Linux

- La **caméra virtuelle**, **Spout2** et **Leap Motion** ne fonctionneront probablement pas.
- Pour une caméra virtuelle, utilisez **OBS Studio** et son module de webcam virtuelle.
- Certains ajustements peuvent être requis selon la distribution.

---

## 📄 Fin de l'installation Linux
Félicitation ! Vous avez installé VSeeFace sur Linux, vous pouvez continuer à suivre le guide principale: \
[Continuer le guide d'installation & présentation à VSeeFace](/docs/installation-presentation-vseeface#-3-ajouter-ton-avatar-vrm)