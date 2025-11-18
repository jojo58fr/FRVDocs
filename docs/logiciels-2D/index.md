---
sidebar_position: 3
title:  
description: Un hub clair pour choisir quel logiciel de VTubing 2D explorer et pour accéder directement aux fiches VSeeFace, Warudo et VNyan.
slug: /logiciels-vtubing-2d
sidebar_label: Logiciels de VTubing 2D
---

<style>{`
.logiciels-3d-shell {
  max-width: 1100px;
  margin: 2.5rem auto 4rem;
  padding: 0 1rem 2rem;
  font-family: "Space Grotesk", "Segoe UI", system-ui, sans-serif;
  color: #f4f6ff;
}
.logiciels-3d-hero {
  background: linear-gradient(145deg, #0f172a, #111828 60%, #1f2a44);
  border: 1px solid rgba(148, 163, 184, 0.35);
  border-radius: 1.25rem;
  padding: 2.25rem;
  box-shadow: 0 20px 45px rgba(15, 23, 42, 0.55);

  position: relative;
}

.logiciels-3d-hero::after {
  content: "";
  position: absolute;
  inset: 0;
  background-repeat: no-repeat;
  background-size: 500px 100%;
  background-position: right center;
  opacity: 0.07;
  pointer-events: none;
  z-index: 0;
  background-image: url('/img/kokori_bg_2.png');
  transition: all 0.5s;
}

.logiciels-3d-hero:hover::after {
  opacity: 0.15;
}

.logiciels-3d-hero-eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.3em;
  font-size: 0.75rem;
  color: #94a3b8;
  margin-bottom: 0.35rem;
}
.logiciels-3d-hero h1 {
  margin: 0;
  font-size: clamp(2.2rem, 1.6rem + 1.2vw, 3rem);
  color: #f8fafc;
}
.logiciels-3d-hero-desc {
  margin: 0.75rem 0 1rem;
  max-width: 680px;
  line-height: 1.6;
  color: #cbd5f5;
}
.logiciels-hero-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.logiciels-hero-tags span {
  font-size: 0.85rem;
  padding: 0.35rem 0.9rem;
  border-radius: 999px;
  border: 1px solid rgba(248, 250, 252, 0.35);
  background: rgba(148, 163, 184, 0.1);
  color: #e2e8f0;
}
.logiciels-3d-grid {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.logiciels-card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-height: 220px;
  background: linear-gradient(180deg, rgba(15, 23, 42, 0.82), rgba(15, 23, 42, 0.95));
  border-radius: 1rem;
  padding: 1.75rem;
  border: 1px solid rgba(148, 163, 184, 0.2);
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.45);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
  overflow: hidden;
}

.logiciels-card.vskin::after {
  background-image: url('/img/vskin_bg.png');
}

.logiciels-card.vtube-studio::after {
  background-image: url('/img/vtubestudio_bg.png');
}

.logiciels-card::after {
  content: "";
  position: absolute;
  inset: 0;
  background-repeat: no-repeat;
  background-size: 400px 100%;
  background-position: right center;
  opacity: 0.07;
  pointer-events: none;
  z-index: 0;

  transition: all 0.5s;
}
.logiciels-card > * {
  position: relative;
  z-index: 1;
}
.logiciels-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 18px 50px rgba(15, 23, 42, 0.55);
  border-color: rgba(148, 163, 184, 0.5);
}
.logiciels-card:hover::after {
  opacity: 0.3;
}
.logiciels-card-link {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  color: inherit;
  text-decoration: none;
}
.logiciels-card-link:focus-visible,
.logiciels-card-link:hover {
  outline: none;
}
.logiciels-card h3 {
  margin: 0.25rem 0 0.5rem;
  font-size: 1.4rem;
  color: #fff;
}
.logiciels-card p {
  margin: 0;
  color: #cbd5f5;
  line-height: 1.5;
}
.logiciels-card-eyebrow {
  font-size: 0.85rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #94a3b8;
}
.logiciels-card-meta {
  margin-top: 1.2rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
  font-size: 0.85rem;
  color: #a5b4fc;
}
.logiciels-card-meta span:first-child {
  padding-right: 0.5rem;
  border-right: 1px solid rgba(148, 163, 184, 0.3);
}
.logiciels-card-badge {
  padding: 0.2rem 0.6rem;
  border-radius: 0.6rem;
  background: rgba(59, 130, 246, 0.18);
  border: 1px solid rgba(59, 130, 246, 0.45);
  color: #bfdbfe;
}
.logiciels-card-suffix {
  font-size: 0.9rem;
  color: #94a3b8;
}
.logiciels-card-actions {
  margin-top: 1rem;
  display: flex;
  flex-direction: row;
  gap: 2%;
}
.logiciels-card-quickstart {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.6rem 1rem;
  border-radius: 0.75rem;
  border: 1px solid rgba(59, 130, 246, 0.45);
  background: rgba(59, 130, 246, 0.25);
  color: #e0f2ff;
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  transition: background-color 0.2s ease, transform 0.2s ease;
}
.logiciels-card-quickstart:hover {
  background: rgba(59, 130, 246, 0.4);
  transform: translateY(-1px);
}

.logiciels-card-explore {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.6rem 1rem;
  border-radius: 0.75rem;
  border: 1px solid rgba(248, 250, 252, 0.35);
  background: rgba(148, 163, 184, 0.1);
  color: #e0f2ff;
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  transition: background-color 0.2s ease, transform 0.2s ease;
  
}
.logiciels-card-explore:hover {
  background: rgba(148, 163, 184, 0.4);
  transform: translateY(-1px);
}

@media (max-width: 600px) {
  .logiciels-3d-hero {
    padding: 1.75rem;
  }
  .logiciels-card {
    min-height: unset;
  }
}
`}</style>


<div class="logiciels-3d-shell">
  <section class="logiciels-3d-hero">
    <p class="logiciels-3d-hero-eyebrow">Logiciels de VTubing 2D</p>
    <h1>Vous voulez vous lancer dans le VTubing avec un avatar 2D ?</h1>
    <p class="logiciels-3d-hero-desc">
      Cette page rassemble les outils de VTubing 2D les plus connues. Clique sur une fiche pour être redirigé vers les différents guides, astuces et explications pour commencer à utiliser les outils !
    </p>
    <div class="logiciels-hero-tags">
      <span>Modèle 2D</span>
      <span>Live 2D</span>
      <span>Rigging</span>
      <span>VTube Studio</span>
    </div>
  </section>
  <div class="logiciels-3d-grid">
    <article class="logiciels-card vtube-studio">
      <a class="logiciels-card-link" href="/docs/category/vtube-studio">
        <div>
          <p class="logiciels-card-eyebrow">VTube Studio</p>
          <h3>VTube Studio, l'incontournable pour la 2D</h3>
          <p>
            Un des logiciels le plus apprécié et le plus complet pour le support des modèles Live 2D au sein de la communauté VTubing.
          </p>
        </div>
      </a>
      <div class="logiciels-card-actions">
        <a class="logiciels-card-quickstart" href="/docs/vtube-studio">Démarrage rapide</a>
        <a class="logiciels-card-explore" href="/docs/category/vtube-studio">Explorer la catégorie</a>
      </div>
    </article>
    <article class="logiciels-card vskin">
      <a class="logiciels-card-link" href="/docs/category/vskin">
        <div>
          <p class="logiciels-card-eyebrow">V-Skin</p>
          <h3>V-Skin, le logiciel alliant Live2D et 3D</h3>
          <p>
            [En cours de rédaction...]
          </p>
        </div>
      </a>
      <div class="logiciels-card-actions">
        <a class="logiciels-card-quickstart" href="/docs/vskin">Démarrage rapide</a>
        <a class="logiciels-card-explore" href="/docs/category/vskin">Explorer la catégorie</a>
      </div>
    </article>
  </div>
</div>
