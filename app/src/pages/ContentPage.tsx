import { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router';
import { useTranslation } from 'react-i18next';
import { ChevronRight, Loader2 } from 'lucide-react';
import { getIndex, getPage, NAV_GROUPS, SECTIONS, useSEO, type PageContent, type PageMeta } from '@/lib/content';
import { pageLabel } from '@/components/layout/Header';
import Markdown from '@/components/Markdown';

export default function ContentPage() {
  const location = useLocation();
  const { t, i18n } = useTranslation();
  const [page, setPage] = useState<PageContent | null>(null);
  const [meta, setMeta] = useState<PageMeta | null>(null);
  const [index, setIndex] = useState<Record<string, PageMeta>>({});
  const [loading, setLoading] = useState(true);

  const route = location.pathname;

  useEffect(() => {
    let alive = true;
    setLoading(true);
    Promise.all([getIndex(), getPage(route)]).then(([idx, p]) => {
      if (!alive) return;
      setIndex(idx);
      setPage(p);
      setMeta(idx[route] ?? null);
      setLoading(false);
      window.scrollTo(0, 0);
    });
    return () => {
      alive = false;
    };
  }, [route]);

  useEffect(() => {
    if (meta) useSEO(pageLabel(route, meta.title, i18n.language));
  }, [meta, route, i18n.language]);

  if (loading) {
    return (
      <div className="flex min-h-[50vh] items-center justify-center">
        <Loader2 className="h-8 w-8 animate-spin text-secondary" />
      </div>
    );
  }

  if (!page || !meta) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-24 text-center">
        <h1 className="font-display text-4xl font-black text-primary">{t('common.notFoundTitle')}</h1>
        <p className="mt-4 text-muted-foreground">{t('common.notFoundText')}</p>
        <Link to="/" className="mt-8 inline-block rounded-full bg-secondary px-6 py-3 font-bold text-white">
          {t('common.notFoundCta')}
        </Link>
      </div>
    );
  }

  const section = SECTIONS[meta.section];
  const group = NAV_GROUPS.find((g) => g.section === meta.section);
  const siblings = group?.items.filter((r) => index[r]) ?? [];
  const title = pageLabel(route, meta.title, i18n.language);

  return (
    <div>
      {/* Page hero band */}
      <div className="band-navy relative text-white">
        <div className="mx-auto max-w-7xl px-4 py-12 lg:py-16">
          <nav className="flex flex-wrap items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-white/60">
            <Link to="/" className="hover:text-accent transition-colors">{t('nav.home')}</Link>
            <ChevronRight className="h-3 w-3 rtl:rotate-180" />
            <span className="text-accent">{t(`sections.${meta.section}`)}</span>
          </nav>
          <h1 className="font-display mt-3 text-3xl font-black text-balance lg:text-5xl">{title}</h1>
          <div className="mt-4 h-1 w-24 rounded-full bg-accent" />
        </div>
      </div>

      <div className="mx-auto grid max-w-7xl gap-10 px-4 py-12 lg:grid-cols-[1fr_300px]">
        {/* Main content — source content is in English, keep LTR */}
        <article className="min-w-0 rounded-3xl bg-card p-6 shadow-sm ring-1 ring-border md:p-10" dir="ltr">
          <Markdown>{page.markdown}</Markdown>
        </article>

        {/* Section sidebar */}
        <aside className="space-y-6 lg:sticky lg:top-32 lg:self-start">
          <div className="overflow-hidden rounded-3xl bg-card shadow-sm ring-1 ring-border">
            <div className={`${section.bg} px-5 py-4`}>
              <h2 className="text-sm font-extrabold uppercase tracking-widest text-white">
                {t(`sections.${meta.section}`)}
              </h2>
            </div>
            <nav className="p-2">
              {siblings.map((r) => (
                <Link
                  key={r}
                  to={r}
                  className={`block rounded-xl px-4 py-2.5 text-sm font-semibold transition-colors ${
                    r === route
                      ? 'bg-secondary/10 text-secondary'
                      : 'text-foreground/70 hover:bg-muted hover:text-primary'
                  }`}
                >
                  {pageLabel(r, index[r]?.title ?? r, i18n.language)}
                </Link>
              ))}
            </nav>
          </div>

          <div className="rounded-3xl bg-secondary p-6 text-white shadow-lg">
            <h3 className="font-display text-lg font-bold">{t('home.ctaTitle')}</h3>
            <p className="mt-2 text-sm text-white/80">{t('home.ctaSubtitle')}</p>
            <Link
              to="/apply"
              className="mt-4 block rounded-full bg-white px-5 py-2.5 text-center text-sm font-extrabold text-secondary transition-transform hover:scale-105"
            >
              {t('nav.apply')}
            </Link>
          </div>
        </aside>
      </div>
    </div>
  );
}
