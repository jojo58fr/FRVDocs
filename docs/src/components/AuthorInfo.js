import React from 'react';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import {translate} from '@docusaurus/Translate';

export default function AuthorInfo() {
  const {metadata} = useDoc();
  const authors = metadata.authors || [];

  if (authors.length === 0) return null;

  return (
    <div className="margin-top--lg">
      <h3>{translate({id: 'authorInfo.authors', message: 'Auteurs'})}</h3>
      {authors.map((author, index) => (
        <div key={index} style={{marginBottom: '0.5rem'}}>
          {author.imageURL && <img src={author.imageURL} alt={author.name} style={{width: '40px', height: '40px', borderRadius: '50%', marginRight: '0.5rem'}} />}
          <strong>{author.name}</strong>
          {author.title && <> — {author.title}</>}
          {author.url && (
            <>
              {' '}• <a href={author.url} target="_blank">{translate({id: 'authorInfo.profile', message: 'Profil'})}</a>
            </>
          )}
        </div>
      ))}
    </div>
  );
}