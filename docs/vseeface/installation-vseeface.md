---
title: Installation & Présentation VSeeFace
description: Comment installer VSeeFace sur Windows et présentation de son interface
slug: /installation-presentation-vseeface
sidebar_label: Installation & Présentation VSeeFace
---

### Version vidéo
**(non-officiel à FRVDocs, vidéo de la communauté)**
<div style={{ width: '100%', maxWidth: '100%', marginTop: '1rem', marginBottom: '1rem' }}>
  <div
    style={{
      position: 'relative',
      paddingBottom: '56.25%',
      height: 0,
      overflow: 'hidden',
    }}>
    <iframe
      src="https://www.youtube.com/embed/pz6UYktxuhs"
      title="Commandes sur twitch"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
      style={{
        border: 0,
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
      }}>
    </iframe>
  </div>
</div>

## 🧰 1. Télécharger VSeeFace

1.  Ouvre ton navigateur (Google, Firefox, ce que tu veux).
2.  Tape **VSeeFace** dans Google.
3.  Va sur le site : [Vseeface.icu](https://www.Vseeface.icu).
4.  Dans le menu à gauche, clique sur **Download**.
5.  Télécharge la *dernière version* de VSeeFace.

![Installation de VSeeFace](./img/installation.png)

------------------------------------------------------------------------

## 📦 2. Installation & Décompression

1.  Va dans ton dossier **Téléchargements**.
2.  Fais un **clic droit** sur le fichier compressé.
3.  Clique sur **Extraire vers VSeeFace/**.
4.  Quand l'extraction est finie, tu peux placer le dossier où tu veux. Fais glisser le dossier sur ton **Bureau** par exemple.

------------------------------------------------------------------------

## 🧙 3. Ajouter ton Avatar VRM

1.  Lance **VSeeFace**.
2.  Sur la page d'accueil, clique sur **Add Avatar**.
3.  Choisis ton fichier **.vrm**.
4.  Clique sur **Open**.

Ton avatar est maintenant chargé dans VSeeFace !

![Ajout d'un avatar VRM](./img/ajouter-avatar.png)

Les informations sur ce que tu peux faire avec ton avatar ou non sont sur la droite, on appelle ça **les métadonnées** de ton avatar.

![Les métadonnées d'un avatar VRM](./img/information-avatar.png)

------------------------------------------------------------------------

## 📷 4. Configurer la caméra & micro

Dans l'interface :

-   **Camera** → choisis ta webcam.
-   **Résolution** → prends la résolution max que ta cam supporte.
-   **Framerate** → Choisis de préférence *60 fps* ou *30 fps* au minimum pour que ça reste fluide.  
ℹ️ *15 fps* est acceptable si tu as une petite configuration mais tu risques d'avoir des sacades.
-   **Tracking Method** → par défaut tu peux prendre "medium quality" ou "high quality" si tu veux le tracking le plus précis.  

*C'est quoi les différences ?*


-   **Microphone** → sélectionne ton micro.

![Configuration des paramètres VSeeFace](./img/settings-camera.png)

Ensuite clique sur **Start**.

Ton avatar bouge ? Parfait. Sinon, check ta cam/micro.

### ✨ 4.1. Les différentes qualités de tracking en détail

**🔥 High Quality (recommandé)**
- C’est le mode par défaut.
- Le tracking est au top, super précis.
- Par contre, ça utilise pas mal de CPU.

➡️ À utiliser si ton PC tient bien la route.

**⚖️ Medium Quality**
- Légèrement plus rapide.
- Tracking un peu moins précis, mais ça reste solide.
- Un bon compromis si ton PC chauffe un peu trop en High ou sur les jeux gourmands.

➡️ Tu peux utiliser cet qualité pour alléger le PC si les jeux sont trop gourmand malgrès une grosse configuration PC


**🙂 Barely Okay Quality**
- Là, on gagne vraiment en rapidité.
MAIS le tracking devient clairement moins bon :
- clignements moins fiables,
- sourcils moins précis,
- expressions détectées beaucoup moins bien.

ℹ️ Il est recommandé d’activer l’auto-blink ici (et en Low).

**🟡 Low Quality**
- Un peu plus rapide que Medium.
- Tracking visiblement moins bon.
- Si tu veux tourner sur un gros jeu en même temps, ça peut aider.

ℹ️ Il est recommandé d’activer l’auto-blink ici (et en Low).

**🍞 Toaster (oui oui)**
- Mode spécial pour les vieux PC (les vraies machines à pain).
- Ultra rapide.
Par contre, grosse contrepartie :
- pas de clignement d’yeux,
- pas de regard,
- pas de détection d'expressions.
- ne fais vraiment pas griller ton pain (désolé)

➡️ À utiliser uniquement si ton PC n’arrive pas à suivre les autres modes.

------------------------------------------------------------------------

## 🛠️ 5. Les paramètres importants

Clique sur **Settings** puis :

### 🔧 General Settings

-   Beaucoup d'options, mais rien de critique à régler au début.
-   Si ton PC galère un peu, baisse **Anti-Aliasing** (8x → 4x ou 2x).

### 😃 Expression Settings

Tu peux : 
- Activer/Désactiver des expressions. 
- Définir des transitions. 
- Ajouter des **raccourcis clavier** pour déclencher des expressions.

### 💡 Lighting Settings

Tu peux changer : 
- La couleur de ta lumière. 
- L'ambiance générale.

Parfait pour matcher ton design ou ton ambiance stream.

### 🌈 Effects Settings

Ici tu as pleins d'effet (qui sont fun ou esthétique) : 
- **Bloom** : donne un effet lumineux
- **Ambient** : change l'éclairage global 
- **Lens distortion** : effet fisheye 
- **Chromatic aberration** : petit glitch
cool 
- **Halftone** : effet BD 
- **Grain** : effet caméra vintage

------------------------------------------------------------------------

## ✋ 6. Leap Motion (Optionnel)

Si tu as un **Leap Motion**, tu peux activer le tracking des mains.\
Il suffit de régler la position de l'appareil dans les paramètres.

------------------------------------------------------------------------

## 🔨 7. Ajouter des Props (Accessoires)

1.  Va dans l'onglet **Props**.
2.  Clique **Add**.
3.  Sélectionne une image (ex : un marteau, des lunettes, un meme).
4.  Glisse-dépose l'accessoire sur la partie du corps où tu veux
    l'attacher.

Et hop, ton avatar se balade avec l'objet.\
C'est hilarant et hyper pratique en stream.

------------------------------------------------------------------------

## 🎯 8. Recentrer ton avatar

Si ton avatar n'est pas bien positionné :

Clique sur **Reset Position**.\
Et boum, tout se remet au centre.

------------------------------------------------------------------------

## 🎥 9. Ajouter VSeeFace dans OBS

1.  Dans VSeeFace, clique sur le bouton en bas à droite pour activer le
    **fond transparent**.
2.  Ouvre **OBS**.
3.  Sous **Sources**, clique sur **+**.
4.  Choisis **Game Capture**.
5.  Nom : *VSeeFace* → OK.
6.  Mode : **Capture specific window**
7.  Window : **VSeeFace**
8.  Coche **Allow Transparency**
9.  Ajuste l'avatar dans ta scène.

------------------------------------------------------------------------

## 🎉 Conclusion

Tu es maintenant **100% prêt** pour streamer avec ton avatar 3D comme un
VTuber ! \
Hésite pas à en parler sur le discord, ça serait super cool de voir ton avatar. 🔥

Si un réglage te pose problème, tu peux demander de l'aide sur le discord D'FRVtubers dans la section `🤔｜aide-et-questions`, voir si la question as déjà été posé ou voir les guides sur `📚｜tutos-et-ressources`

## 🙌 Contributeurs
**Rédaction:** 
- [TakuDev](https://www.twitch.tv/takudev)