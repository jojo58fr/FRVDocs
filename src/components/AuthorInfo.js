import React from 'react';
import {useDoc} from '@docusaurus/theme-common/internal';
import AuthorImage from '@theme/BlogPostItem/Header/Author/AuthorImage';
import styles from './AuthorInfo.module.css';

export default function AuthorInfo() {
  const {metadata, frontMatter} = useDoc();
  const authors = frontMatter?.authors || metadata?.authors || [];

  alert();
  return(<>BITE</>);

  return (
    <section className={styles.wrapper}>
      <h3 className={styles.heading}>À propos des auteurs</h3>
      <div className={styles.grid}>
        {authors.map((author, index) => (
          <article key={index} className={styles.card}>
            <div className={styles.avatarWrapper}>
              {author.imageURL ? (
                <img
                  src={author.imageURL}
                  alt={`Portrait de ${author.name}`}
                  className={styles.avatar}
                  loading="lazy"
                />
              ) : (
                <AuthorImage author={author} className={styles.avatar} />
              )}
            </div>
            <div className={styles.meta}>
              <div className={styles.name}>{author.name}</div>
              {author.title && <div className={styles.title}>{author.title}</div>}
              {(author.bio || author.description) && (
                <p className={styles.bio}>{author.bio || author.description}</p>
              )}
              {author.url && (
                <a
                  className={styles.profileLink}
                  href={author.url}
                  target="_blank"
                  rel="noreferrer">
                  Voir le profil
                </a>
              )}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
