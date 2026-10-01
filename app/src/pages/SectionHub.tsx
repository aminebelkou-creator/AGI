import { useEffect, useState } from 'react';
import { Link } from 'react-router';
import { useTranslation } from 'react-i18next';
import { ArrowRight } from 'lucide-react';
import { getIndex, NAV_GROUPS, SECTIONS, useSEO, type PageMeta, type SectionId } from '@/lib/content';
import { pageLabel } from '@/components/layout/Header';

export default function SectionHub({ section }: { section: SectionId }) {
  const { t, i18n } = useTranslation();
  const [index, setIndex] = useState<Record<string, PageMeta>>({});
  const group = NAV_GROUPS.find((g) => g.section === section)!;
  const meta = SECTIONS[section];

  useSEO(t(`sections.${section}`));

  useEffect(() => {
    getIndex().then(setIndex);
  }, []);

  return (
    <div>
      <div className="band-navy text-white">
        <div className="mx-auto max-w-7xl px-4 py-14 lg:py-20">
          <span className="kicker text-accent">AGI</span>
          <h1 className="font-display mt-3 text-4xl font-black lg:text-6xl">{t(`sections.${section}`)}</h1>
          <div className="mt-5 h-1.5 w-28 rounded-full bg-accent" />
        </div>
      </div>

      <div className="mx-auto max-w-7xl px-4 py-14">
        <h2 className="text-sm font-extrabold uppercase tracking-[0.2em] text-muted-foreground">
          {t('common.exploreSection')}
        </h2>
        <div className="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {group.items
            .filter((r) => index[r])
            .map((r) => (
              <Link
                key={r}
                to={r}
                className="group rounded-3xl bg-card p-6 shadow-sm ring-1 ring-border transition-all hover:-translate-y-1 hover:shadow-xl hover:ring-2 hover:ring-secondary/40"
              >
                <div className={`mb-4 h-1.5 w-12 rounded-full ${meta.bg}`} />
                <h3 className="font-display text-lg font-bold leading-snug text-primary group-hover:text-secondary transition-colors">
                  {pageLabel(r, index[r]?.title ?? r, i18n.language)}
                </h3>
                <span className="mt-4 inline-flex items-center gap-1.5 text-sm font-extrabold text-secondary">
                  {t('common.readMore')}
                  <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-1 rtl:rotate-180 rtl:group-hover:-translate-x-1" />
                </span>
              </Link>
            ))}
        </div>
      </div>
    </div>
  );
}
