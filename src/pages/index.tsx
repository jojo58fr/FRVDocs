import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

const contentByLocale = {
  'fr': {
    heroSubtitle: 'La référence pour débuter en tant que VtuberFR',
    heroText:
      'FRVDocs rend la documentation la plus accessible possible : ressources, tutoriels, outils (2D ou 3D) ainsi que les articles validés par la communauté francophone.',
    heroNote:
      'Si vous souhaitez débuter en tant que VTuber, toutes les ressources & lexiques sont disponibles ici !',
    heroPrimary: 'Contribuer au projet',
    heroSecondary: 'Explorer les articles communautaires',
    categorySectionTitle: 'Accès rapide',
    categorySectionIntro:
      'Choisis une thématique et accède directement aux pages qui t\'intéresses !',
    categoryCtaLabel: 'Explorer la catégorie',
    categoryCards: [
      {
        title: 'VTubing en général',
        description:
          'Guide pour débuter, Comment faire un Debut/Redebut..etc',
        link: 'docs/category/vtubing-en-général',
      },
      {
        title: 'Logiciels de VTubing 2D',
        description:
          'VTube Studio, V-Skin, tous les astuces sur ces logiciels.',
        link: 'docs/logiciels-vtubing-2d',
      },
      {
        title: 'Logiciels de VTubing 3D',
        description:
          'Warudo, VSeeFace, VNyan, tous les astuces sur ces logiciels.',
        link: 'docs/logiciels-vtubing-3d',
      },
      {
        title: 'La modération',
        description:
          'Les bonnes pratiques et outils pour créer un espace protégé qui te correspond.',
        link: '/docs/category/la-modération',
      },
      {
        title: 'Twitch',
        description:
          'Tout ce que tu dois savoir pour préparer tes lives Twitch.',
        link: '/docs/category/twitch',
      },
    ],
    highlights: [
      {
        title: 'Tous le monde peux créer une documentation 📝',
        description:
          'Toutes les pages ont été écrit par la communauté sur discord. FRVDocs s\'occupe juste de mettre en avant le contenu de la communauté, il suffit d\'écrire sur discord au format Markdown et le staff s\'occupe de tout !',
      },
      {
        title: 'Une mise en avant du contenu Francophone 🇫🇷',
        description:
        'Les articles mettent en avant tout le contenu vidéo fait par la communauté. Vous avez un tutoriel dont vous traiter en vidéo ? Contacter le #ticket-support sur Discord pour être ajouté parmis les créateurs francophones présenté dans la documentation !',
      },
      {
        title: 'Un espace communautaire lié 👥',
        description:
        'FRVDocs est lié à l\'initiative FRVtubers permettant d\'avoir un discord actif sur l\'actualité du VTubing francophone & international !',
      },
    ],
    communityTitle: 'On co-écrit le savoir ensemble !',
    contributionText:
      'Il suffit simplement de contribuer dans les channels Discord spécifiquement dédiés : chaque message peut ensuite être transformé en documentation via GitHub. Le staff FRVtubers s\'engage à reprendre ces contributions bénévolement pour garder la doc à jour avec les derniers outils, astuces et tutoriels francophones autour du VTubing.',
    discordButton: 'Rejoindre le discord communautaire',
    openCollectiveButton: 'Soutenir le projet sur Open Collective',
  },
  en: {
    heroSubtitle: 'The reference for getting started as a VTuberFR',
    heroText:
      'FRVDocs keeps documentation as accessible as possible: resources, tutorials, tooling (2D/3D), and community-approved articles for francophone creators.',
    heroNote:
      'Everything you need to start as a VTuberFR (resources & glossaries) is right here!',
    heroPrimary: 'Contribute to the project',
    heroSecondary: 'Browse community articles',
    categorySectionTitle: 'Quick access',
    categorySectionIntro:
      'Pick a theme and land directly on what you need !',
    categoryCtaLabel: 'Visit the category',
    categoryCards: [
      {
        title: 'VTubing in general',
        description: 'Launch guides, glossaries, and fundamentals for francophone VTubers.',
        link: '/docs/category/vtubing',
      },
      {
        title: '2D VTubing software',
        description: 'VTube Studio, V-Skin, and quickstart tips for 2D avatars.',
        link: '/docs/category/logiciels-2d',
      },
      {
        title: '3D VTubing software',
        description: 'VSeeFace, Warudo, and best practices for 3D tracking setups.',
        link: '/docs/category/logiciels-3d',
      },
      {
        title: 'Moderation',
        description: 'Policies, playbooks, and tools to keep chats healthy.',
        link: '/docs/category/moderation',
      },
      {
        title: 'Twitch',
        description: 'Commands, automations, and prep notes for streaming on Twitch.',
        link: '/docs/category/twitch',
      },
    ],
    highlights: [
      {
        title: 'Clear foundations',
        description:
          'FRVDocs shares a step-by-step path covering technical prep, character design, streaming, and audience growth so newcomers can build skills confidently.',
      },
      {
        title: 'Living documentation',
        description:
          'Articles are reviewed, expanded, and refreshed with Discord feedback, illustrated with snippets and practical checklists.',
      },
      {
        title: 'Community hub',
        description:
          'Internal guides, streamer insights, and templates from Discord are refined and published to keep a reliable archive.',
      },
    ],
    communityTitle: 'We co-write knowledge together!',
    contributionText:
      'Post in the dedicated Discord channels: anyone can have their message turned into documentation on GitHub. The FRVtubers staff commits to polishing those contributions so the docs stay up to date with the latest francophone VTubing tools and tutorials.',
    discordButton: 'Join the community Discord',
    openCollectiveButton: 'Support the project on Open Collective',
  },
};

function HomepageHeader() {
  const {i18n} = useDocusaurusContext();
  const locale = i18n.currentLocale;
  const localeContent = contentByLocale[locale] ?? contentByLocale[i18n.defaultLocale];

  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <div className={styles.heroLogoWrapper}>
          <img src="/img/logo.png" alt="FRVDocs" className={styles.heroLogo} />
        </div>
        <p className={styles.heroSubtitle}>{localeContent.heroSubtitle}</p>
        <p className={styles.heroText}>
          {localeContent.heroText}
          <br />
          <br />
          {localeContent.heroNote}
        </p>
        <div className={styles.ctaGroup}>
          <Link className="button button--primary button--lg" to="https://github.com/jojo58fr/FRVDocs">
            {localeContent.heroPrimary}
          </Link>
          <Link className="button button--secondary button--lg" to="/docs/intro">
            {localeContent.heroSecondary}
          </Link>
        </div>
        <div className={styles.heroArtWrapper}>
          <img
            src="/img/Koko-Chan_FRVtubers.png"
            alt="Koko-Chan FRVtubers"
            className={styles.heroArt}
          />
          <span className={styles.heroArtCredit}>
            <a href="https://x.com/Twiinkii_" target="blank">
              Art by @twiinkii_
            </a>
          </span>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {i18n} = useDocusaurusContext();
  const locale = i18n.currentLocale;
  const localeContent = contentByLocale[locale] ?? contentByLocale[i18n.defaultLocale];

  return (
    <Layout
      title={
        locale === 'en' ? 'FRVDocs - VTubing documentation' : 'FRVDocs - Documentation pour les VtuberFR'
      }
      description={
        locale === 'en'
          ? 'FRVDocs centralizes accessible guides, tips, and community contributions for francophone VTubers.'
          : 'FRVDocs centralise les guides accessibles, les bons plans techniques et les contributions communautaires pour tout aspirant Vtuber francophone.'
      }
    >
      <HomepageHeader />
      <main>
        <section className={styles.categorySection}>
          <div className="container">
            <Heading as="h2" className={styles.sectionTitle}>
              {localeContent.categorySectionTitle}
            </Heading>
            <p className={styles.categoryIntro}>{localeContent.categorySectionIntro}</p>
            <div className={styles.categoryGrid}>
              {localeContent.categoryCards.map((category) => (
                <Link key={category.title} to={category.link} className={styles.categoryCard}>
                  <div>
                    <p className={styles.categoryLabel}>{category.title}</p>
                    <p className={styles.categoryDescription}>{category.description}</p>
                  </div>
                  <span className={styles.categoryCta}>{localeContent.categoryCtaLabel}</span>
                </Link>
              ))}
            </div>
          </div>
        </section>
        <section className={styles.section}>
          <div className="container">
            <Heading as="h2" className={styles.sectionTitle}>
              {locale === 'en' ? 'Open documentation for everyone' : 'Une documentation ouvert(e) à tous !'}
            </Heading>
            <div className={styles.sectionGrid}>
              {localeContent.highlights.map((item) => (
                <article key={item.title} className={styles.card}>
                  <Heading as="h3" className={styles.cardTitle}>
                    {item.title}
                  </Heading>
                  <p className={styles.cardDescription}>{item.description}</p>
                </article>
              ))}
            </div>
          </div>
        </section>
        <section className={styles.communitySection}>
          <div className="container">
            <div className={styles.communityContent}>
              <Heading as="h2" className={styles.sectionTitle}>
                {localeContent.communityTitle}
              </Heading>
              <div className={styles.contributionExplain}>
                <div className={styles.contributionImage}>
                  <img src="/img/channels.png" alt="Channels Discord pour contributions" />
                </div>
                <div className={styles.contributionText}>
                  <p>{localeContent.contributionText}</p>
                </div>
              </div>
              <div className={styles.communityActions}>
                <Link className="button button--outline button--lg" to="/docs/intro">
                  <i className={clsx('fa-brands fa-discord', styles.discordIcon)} aria-hidden="true" />
                  {localeContent.discordButton}
                </Link>
                <Link
                  className="button button--primary button--lg"
                  href="https://opencollective.com/frvtubers"
                  target="_blank"
                  rel="noreferrer"
                >
                  {localeContent.openCollectiveButton}
                </Link>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
