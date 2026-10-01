import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Link } from 'react-router';
import legacyMap from '@/lib/legacy-map.json';

const LEGACY = legacyMap as Record<string, string>;

function rewriteHref(href?: string): { to: string; external: boolean } {
  if (!href) return { to: '#', external: true };
  if (href.startsWith('/')) return { to: href, external: false };
  const m = href.match(/americangroup-international\.com\/?([^?#\s]*)\/?/);
  if (m) {
    const slug = m[1].replace(/\/$/, '');
    if (LEGACY[slug]) return { to: LEGACY[slug], external: false };
  }
  if (href.startsWith('mailto:') || href.startsWith('tel:')) return { to: href, external: true };
  return { to: href, external: true };
}

export default function Markdown({ children, compact = false }: { children: string; compact?: boolean }) {
  return (
    <div className={compact ? 'content-md-compact' : 'content-md'}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: ({ href, children }) => {
            const { to, external } = rewriteHref(href);
            if (!external) {
              return <Link to={to}>{children}</Link>;
            }
            return (
              <a href={to} target={to.startsWith('http') ? '_blank' : undefined} rel="noopener noreferrer">
                {children}
              </a>
            );
          },
          img: ({ src, alt }) => (
            <img
              src={src}
              alt={alt ?? ''}
              loading="lazy"
              onError={(e) => ((e.target as HTMLImageElement).style.display = 'none')}
            />
          ),
        }}
      >
        {children}
      </ReactMarkdown>
    </div>
  );
}
