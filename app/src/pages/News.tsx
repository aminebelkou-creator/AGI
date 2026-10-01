import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router';
import { useTranslation } from 'react-i18next';
import { ArrowLeft, ArrowRight, Loader2 } from 'lucide-react';
import { getNews, getNewsArticle, newsImage, useSEO, type NewsMeta, type PageContent } from '@/lib/content';
import Markdown from '@/components/Markdown';

export function NewsList() {
  const { t } = useTranslation();
  const [news, setNews] = useState<NewsMeta[]>([]);
  const [loading, setLoading] = useState(true);

  useSEO(t('nav.news'), 'Latest news from American Group International School Agadir — events, partnerships, graduations and announcements.');

  useEffect(() => {
    getNews().then((n) => {
      setNews(n);
      setLoading(false);
    });
  }, []);

  return (
    <div>
      <div className="band-navy text-white">
        <div className="mx-auto max-w-7xl px-4 py-14 lg:py-20">
          <span className="kicker text-accent">{t('home.newsKicker')}</span>
          <h1 className="font-display mt-3 text-4xl font-black lg:text-6xl">{t('home.newsTitle')}</h1>
          <div className="mt-5 h-1.5 w-28 rounded-full bg-accent" />
        </div>
      </div>
      <div className="mx-auto max-w-7xl px-4 py-14">
        {loading ? (
          <div className="flex justify-center py-16">
            <Loader2 className="h-8 w-8 animate-spin text-secondary" />
          </div>
        ) : (
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {news.map((n) => (
              <Link
                key={n.slug}
                to={`/news/${n.slug}`}
                className="group overflow-hidden rounded-3xl bg-card shadow-sm ring-1 ring-border transition-all hover:-translate-y-1 hover:shadow-xl"
              >
                <div className="relative h-48 overflow-hidden">
                  <img
                    src={newsImage(n)}
                    alt=""
                    loading="lazy"
                    className="h-full w-full object-cover transition-transform duration-700 ease-out group-hover:scale-110"
                    onError={(e) => {
                      const el = e.target as HTMLImageElement;
                      el.style.display = 'none';
                      el.parentElement?.classList.add('bg-gradient-to-br', 'from-primary', 'to-secondary');
                    }}
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-primary/60 via-transparent to-transparent" />
                  <time className="absolute bottom-3 start-3 rounded-full bg-white/90 px-3 py-1 text-[11px] font-extrabold uppercase tracking-widest text-primary backdrop-blur">
                    {n.date}
                  </time>
                </div>
                <div className="p-6">
                  <h2 className="font-display text-lg font-bold leading-snug text-primary group-hover:text-secondary transition-colors">
                    {n.title}
                  </h2>
                  <span className="mt-4 inline-flex items-center gap-1.5 text-sm font-extrabold text-secondary">
                    {t('common.readMore')}
                    <ArrowRight className="h-3.5 w-3.5 rtl:rotate-180" />
                  </span>
                </div>
              </Link>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export function NewsArticle() {
  const { slug } = useParams<{ slug: string }>();
  const { t } = useTranslation();
  const [article, setArticle] = useState<PageContent | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!slug) return;
    setLoading(true);
    getNewsArticle(slug).then((a) => {
      setArticle(a);
      setLoading(false);
      window.scrollTo(0, 0);
    });
  }, [slug]);

  useEffect(() => {
    if (article) useSEO(article.title);
  }, [article]);

  if (loading) {
    return (
      <div className="flex min-h-[50vh] items-center justify-center">
        <Loader2 className="h-8 w-8 animate-spin text-secondary" />
      </div>
    );
  }

  if (!article) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-24 text-center">
        <h1 className="font-display text-4xl font-black text-primary">{t('common.notFoundTitle')}</h1>
        <Link to="/news" className="mt-8 inline-block rounded-full bg-secondary px-6 py-3 font-bold text-white">
          {t('common.backTo')} {t('nav.news')}
        </Link>
      </div>
    );
  }

  return (
    <div>
      <div className="band-navy text-white">
        <div className="mx-auto max-w-4xl px-4 py-12 lg:py-16">
          <Link to="/news" className="inline-flex items-center gap-2 text-sm font-bold text-white/70 hover:text-accent transition-colors">
            <ArrowLeft className="h-4 w-4 rtl:rotate-180" /> {t('nav.news')}
          </Link>
          <h1 className="font-display mt-4 text-3xl font-black text-balance lg:text-5xl">{article.title}</h1>
          {article.date && (
            <time className="mt-4 inline-block rounded-full bg-white/10 px-4 py-1.5 text-xs font-bold uppercase tracking-widest text-accent">
              {article.date}
            </time>
          )}
        </div>
      </div>
      <div className="mx-auto max-w-4xl px-4 py-12">
        <article className="rounded-3xl bg-card p-6 shadow-sm ring-1 ring-border md:p-10" dir="ltr">
          <Markdown>{article.markdown}</Markdown>
        </article>
      </div>
    </div>
  );
}
