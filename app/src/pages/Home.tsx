import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { Link } from 'react-router';
import { useTranslation } from 'react-i18next';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import {
  GraduationCap, Award, Languages, HeartHandshake, Blocks, Flag,
  ArrowRight, Star, Sparkles, BookOpenCheck, Users, Globe2, Plus,
} from 'lucide-react';
import { getNews, newsImage, useSEO, type NewsMeta } from '@/lib/content';

gsap.registerPlugin(ScrollTrigger);

const LOGO = 'https://www.americangroup-international.com/wp-content/uploads/2024/07/cropped-newlogo22.png';
const HERO_IMG = 'https://www.americangroup-international.com/wp-content/uploads/2026/04/cropped-1000005901-scaled-1.jpg';
const HERO_IMG_2 = 'https://www.americangroup-international.com/wp-content/uploads/2026/04/cropped-IMG-20260406-WA0010-1-300x295.jpg';
const STATS_BG = 'https://www.americangroup-international.com/wp-content/uploads/2026/04/20260411_142632-scaled.jpg';
const WHY_BG = 'https://www.americangroup-international.com/wp-content/uploads/2026/04/1000005901-scaled.jpg';

const PROGRAM_CARDS = [
  { key: 'k12', route: '/academics/k12-micro-school', icon: GraduationCap, bg: 'bg-blue-700', img: 'https://www.americangroup-international.com/wp-content/uploads/2022/12/cropped-cropped-IMG-20221211-WA0000-1.png' },
  { key: 'anglia', route: '/anglia', icon: Award, bg: 'bg-secondary', img: 'https://www.americangroup-international.com/wp-content/uploads/2025/04/cropped-Anglia-Poster.png' },
  { key: 'efl', route: '/efl-classes', icon: Languages, bg: 'bg-teal-700', img: 'https://www.americangroup-international.com/wp-content/uploads/2026/04/cropped-20260411_142632-scaled-1.jpg' },
  { key: 'adult', route: '/programs/adult-high-school-diploma', icon: BookOpenCheck, bg: 'bg-purple-700', img: 'https://www.americangroup-international.com/wp-content/uploads/2024/10/cropped-cropped-cropped-agi-1-1.webp' },
  { key: 'special', route: '/special-education', icon: HeartHandshake, bg: 'bg-orange-600', img: 'https://www.americangroup-international.com/wp-content/uploads/2020/04/113a393b-67ee-45dc-aa5d-94ea4a51bf1d.jpg' },
  { key: 'pods', route: '/programs/learning-pods', icon: Blocks, bg: 'bg-primary', img: 'https://www.americangroup-international.com/wp-content/uploads/2026/04/cropped-1000115194.jpg' },
];

const PARTNERS = [
  'Anglia Examinations England',
  'Chichester College Group UK',
  'Cognia Accredited LMS',
  'Florida Accredited Program',
  'IPHM & ICAHP Accredited',
  'American School Counselor Association',
  'CollegeBoard · AI 651960',
  'American Group USA LLC · Maryland',
];

const reducedMotion = () =>
  typeof window !== 'undefined' &&
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* Split a translated string into word-mask spans for the staggered entrance */
function MaskedWords({ text, className }: { text: string; className?: string }) {
  return (
    <span className={className}>
      {text.split(' ').map((w, i) => (
        <span key={i} className="word-mask">
          <span data-hero-word>{w}&nbsp;</span>
        </span>
      ))}
    </span>
  );
}

export default function Home() {
  const { t } = useTranslation();
  const [news, setNews] = useState<NewsMeta[]>([]);
  const root = useRef<HTMLDivElement>(null);

  useSEO('Home', 'American Group International — K–12 American international school in Agadir, Morocco. Home of Anglia Examinations Morocco, EFL classes, adult high school diploma, special education and holistic counselling.');

  useEffect(() => {
    getNews().then((n) => setNews(n.slice(0, 3)));
  }, []);

  useLayoutEffect(() => {
    if (reducedMotion()) return;
    const ctx = gsap.context(() => {
      /* ---- hero entrance ---- */
      gsap.from('[data-hero-word]', {
        yPercent: 110,
        duration: 0.9,
        ease: 'power4.out',
        stagger: 0.045,
        delay: 0.15,
      });
      gsap.from('[data-hero-fade]', {
        opacity: 0,
        y: 24,
        duration: 0.8,
        ease: 'power3.out',
        stagger: 0.12,
        delay: 0.55,
      });
      gsap.from('[data-hero-bg] img', {
        scale: 1.45,
        duration: 2.2,
        ease: 'power2.out',
      });
      gsap.from('[data-hero-card]', {
        opacity: 0,
        y: 60,
        rotate: 10,
        duration: 1.1,
        ease: 'power3.out',
        delay: 0.9,
      });

      /* ---- hero parallax ---- */
      gsap.to('[data-hero-bg] img', {
        yPercent: 18,
        scale: 1.32,
        ease: 'none',
        scrollTrigger: { trigger: '[data-hero]', start: 'top top', end: 'bottom top', scrub: true },
      });
      gsap.to('[data-hero-copy]', {
        yPercent: -18,
        opacity: 0.25,
        ease: 'none',
        scrollTrigger: { trigger: '[data-hero]', start: 'top top', end: 'bottom 30%', scrub: true },
      });
      gsap.to('[data-hero-card]', {
        yPercent: 24,
        ease: 'none',
        scrollTrigger: { trigger: '[data-hero]', start: 'top top', end: 'bottom top', scrub: true },
      });
      gsap.to('[data-hero-ghost]', {
        xPercent: -18,
        ease: 'none',
        scrollTrigger: { trigger: '[data-hero]', start: 'top top', end: 'bottom top', scrub: true },
      });

      /* ---- generic reveals ---- */
      ScrollTrigger.batch('[data-reveal]', {
        start: 'top 86%',
        once: true,
        onEnter: (els) =>
          gsap.fromTo(
            els,
            { opacity: 0, y: 44 },
            { opacity: 1, y: 0, duration: 0.85, ease: 'power3.out', stagger: 0.09, overwrite: true }
          ),
      });

      /* ---- stat count-up ---- */
      gsap.utils.toArray<HTMLElement>('[data-count]').forEach((el) => {
        const target = parseFloat(el.dataset.count || '0');
        const suffix = el.dataset.suffix || '';
        const obj = { v: 0 };
        gsap.to(obj, {
          v: target,
          duration: 1.6,
          ease: 'power2.out',
          scrollTrigger: { trigger: el, start: 'top 88%', once: true },
          onUpdate: () => {
            el.textContent = `${Math.round(obj.v)}${suffix}`;
          },
        });
      });

      /* ---- underline draw on section titles ---- */
      gsap.utils.toArray<HTMLElement>('[data-underline]').forEach((el) => {
        gsap.from(el, {
          scaleX: 0,
          transformOrigin: 'left center',
          duration: 0.9,
          ease: 'power3.out',
          scrollTrigger: { trigger: el, start: 'top 90%', once: true },
        });
      });
    }, root);
    return () => ctx.revert();
  }, []);

  const stats = [
    { value: 2013, suffix: '', label: t('home.stat1Label'), fixed: t('home.stat1Value') },
    { value: 46, suffix: '+', label: t('home.stat2Label'), fixed: null },
    { value: 0, suffix: '', label: t('home.stat3Label'), fixed: t('home.stat3Value') },
    { value: 8, suffix: '', label: t('home.stat4Label'), fixed: null },
  ];

  return (
    <div ref={root}>
      {/* ================= HERO (cinematic, full viewport) ================= */}
      <section data-hero className="relative flex min-h-[100svh] items-center overflow-hidden text-white">
        {/* background photo, zoomed + parallaxed */}
        <div data-hero-bg className="absolute inset-0">
          <img
            src={HERO_IMG}
            alt=""
            className="h-full w-full scale-125 object-cover"
            onError={(e) => ((e.target as HTMLImageElement).style.display = 'none')}
          />
        </div>
        {/* cinematic navy grade: darker at edges, clear in the middle-left for copy */}
        <div className="absolute inset-0 bg-gradient-to-r from-[hsl(229_62%_12%/0.97)] via-[hsl(229_62%_18%/0.82)] to-[hsl(232_70%_26%/0.55)]" />
        <div className="absolute inset-0 bg-gradient-to-t from-[hsl(229_62%_10%/0.9)] via-transparent to-[hsl(229_62%_12%/0.6)]" />
        <div className="stripes-bg absolute inset-0" />
        <div className="noise-overlay" />
        <div className="absolute -end-24 -top-24 h-96 w-96 rounded-full bg-secondary/25 blur-3xl" />
        <div className="absolute -bottom-32 -start-24 h-96 w-96 rounded-full bg-accent/15 blur-3xl" />

        {/* giant ghost word drifting on scroll */}
        <div
          data-hero-ghost
          aria-hidden
          className="text-outline pointer-events-none absolute -bottom-4 start-0 select-none whitespace-nowrap font-display text-[24vw] font-black leading-none"
        >
          AGADIR&nbsp;·&nbsp;AGI
        </div>

        <div className="relative mx-auto w-full max-w-7xl px-4 pb-28 pt-32 lg:pb-36">
          <div data-hero-copy className="max-w-3xl">
            <div data-hero-fade className="kicker text-accent">{t('home.heroKicker')}</div>
            <h1 className="font-display mt-7 text-[clamp(3rem,8.5vw,7.5rem)] font-black leading-[0.98] text-balance">
              <MaskedWords text={t('home.heroTitleA')} />
              <span className="relative inline-block text-accent">
                <MaskedWords text={t('home.heroTitleB')} />
                <svg className="hero-underline absolute -bottom-2 start-0 w-full" viewBox="0 0 200 12" preserveAspectRatio="none" aria-hidden>
                  <path d="M2 9 Q 100 -4 198 9" stroke="hsl(351 78% 55%)" strokeWidth="5" fill="none" strokeLinecap="round" />
                </svg>
              </span>{' '}
              <MaskedWords text={t('home.heroTitleC')} />
            </h1>
            <p data-hero-fade className="mt-8 max-w-xl text-lg leading-relaxed text-white/85 lg:text-2xl lg:leading-relaxed">
              {t('home.heroSubtitle')}
            </p>
            <div data-hero-fade className="mt-10 flex flex-wrap gap-4">
              <Link
                to="/apply"
                className="group inline-flex items-center gap-2 rounded-full bg-secondary px-9 py-4 text-lg font-extrabold text-white shadow-2xl shadow-secondary/40 transition-transform hover:scale-105"
              >
                {t('home.heroCta1')}
                <ArrowRight className="h-5 w-5 transition-transform group-hover:translate-x-1 rtl:rotate-180 rtl:group-hover:-translate-x-1" />
              </Link>
              <Link
                to="/programs"
                className="inline-flex items-center gap-2 rounded-full border-2 border-white/35 px-9 py-4 text-lg font-extrabold text-white backdrop-blur transition-colors hover:border-accent hover:text-accent"
              >
                {t('home.heroCta2')}
              </Link>
            </div>
            <div data-hero-fade className="mt-14 flex items-center gap-3">
              <img src={LOGO} alt="AGI" className="h-12 w-auto rounded-lg bg-white p-1" />
              <div className="text-xs font-bold uppercase tracking-widest text-white/65">
                {t('brand.motto')}
              </div>
            </div>
          </div>
        </div>

        {/* floating framed photo card, bottom-end */}
        <div data-hero-card className="absolute bottom-24 end-8 hidden w-72 rotate-3 xl:block">
          <div className="float-soft overflow-hidden rounded-2xl border-4 border-white/90 shadow-2xl">
            <img src={HERO_IMG_2} alt="" loading="lazy" className="aspect-square w-full object-cover" onError={(e) => ((e.currentTarget.parentElement as HTMLElement).style.display = 'none')} />
          </div>
          <div className="absolute -bottom-5 -start-5 flex items-center gap-2.5 rounded-xl bg-white px-4 py-3 text-foreground shadow-2xl">
            <Globe2 className="h-5 w-5 text-secondary" />
            <div>
              <span className="font-display text-lg font-black text-primary">46+</span>
              <span className="ms-1.5 text-[10px] font-bold uppercase tracking-wider text-muted-foreground">{t('home.stat2Label')}</span>
            </div>
          </div>
        </div>

        {/* scroll cue */}
        <div data-hero-fade className="absolute bottom-7 start-1/2 -translate-x-1/2 rtl:translate-x-1/2">
          <div className="flex h-12 w-7 items-start justify-center rounded-full border-2 border-white/40 p-1.5">
            <div className="scroll-dot h-2.5 w-1 rounded-full bg-accent" />
          </div>
        </div>
      </section>

      {/* ================= STATS (photo band) ================= */}
      <section className="relative overflow-hidden text-white">
        <img
          src={STATS_BG}
          alt=""
          loading="lazy"
          className="absolute inset-0 h-full w-full object-cover"
          onError={(e) => ((e.target as HTMLImageElement).style.display = 'none')}
        />
        <div className="absolute inset-0 bg-gradient-to-r from-secondary/95 via-primary/85 to-secondary/95" />
        <div className="noise-overlay" />
        <div className="relative mx-auto max-w-7xl px-4 py-16 lg:py-20">
          <p data-reveal className="text-center font-display text-xl italic text-white/90 lg:text-2xl">{t('home.statsTitle')}</p>
          <div className="mt-10 grid grid-cols-2 gap-8 lg:grid-cols-4">
            {stats.map((s, i) => (
              <div key={i} data-reveal className="text-center">
                <div className="font-display text-5xl font-black text-accent drop-shadow-lg lg:text-7xl">
                  {s.fixed ?? (
                    <>
                      <span data-count={s.value} data-suffix={s.suffix}>0{s.suffix}</span>
                    </>
                  )}
                </div>
                <div className="mt-2 text-xs font-bold uppercase tracking-[0.18em] text-white/90">{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ================= PARTNERS MARQUEE ================= */}
      <section className="border-y-4 border-accent bg-white py-5">
        <div dir="ltr" className="overflow-hidden">
          <div className="marquee-track">
            {[0, 1].map((dup) => (
              <div key={dup} className="flex shrink-0 items-center" aria-hidden={dup === 1}>
                {PARTNERS.map((p) => (
                  <span key={`${dup}-${p}`} className="mx-7 inline-flex items-center gap-2 whitespace-nowrap text-sm font-extrabold uppercase tracking-wide text-primary/70">
                    <Star className="h-3.5 w-3.5 fill-accent text-accent" /> {p}
                  </span>
                ))}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ================= PROGRAMS ================= */}
      <section className="relative mx-auto max-w-7xl px-4 py-24">
        <div aria-hidden className="text-outline-navy pointer-events-none absolute -top-4 end-4 hidden select-none font-display text-[10rem] font-black leading-none lg:block">
          01
        </div>
        <div className="grid gap-10 lg:grid-cols-12">
          <div className="lg:col-span-4">
            <div data-reveal className="lg:sticky lg:top-28">
              <span className="kicker text-secondary">{t('home.highlightsKicker')}</span>
              <h2 className="font-display mt-4 text-4xl font-black text-primary text-balance lg:text-5xl">
                {t('home.highlightsTitle')}
              </h2>
              <div data-underline className="mt-5 h-1.5 w-24 rounded-full bg-secondary" />
              <p className="mt-5 text-lg leading-relaxed text-muted-foreground">{t('home.highlightsSubtitle')}</p>
              <Link
                to="/programs"
                className="group mt-7 inline-flex items-center gap-2 font-extrabold text-secondary"
              >
                {t('common.exploreSection')}
                <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1 rtl:rotate-180 rtl:group-hover:-translate-x-1" />
              </Link>
            </div>
          </div>
          <div className="grid gap-6 sm:grid-cols-2 lg:col-span-8">
            {PROGRAM_CARDS.map((p, i) => (
              <Link
                key={p.key}
                to={p.route}
                data-reveal
                className={`group relative overflow-hidden rounded-3xl bg-card shadow-lg ring-1 ring-border transition-all duration-300 hover:-translate-y-2 hover:rotate-[0.5deg] hover:shadow-2xl ${
                  i % 3 === 0 ? 'sm:translate-y-6' : ''
                }`}
              >
                <div className="relative h-44 overflow-hidden">
                  <img
                    src={p.img}
                    alt=""
                    loading="lazy"
                    className="h-full w-full object-cover transition-transform duration-700 ease-out group-hover:scale-110"
                    onError={(e) => ((e.target as HTMLImageElement).style.display = 'none')}
                  />
                  <div className={`absolute inset-0 ${p.bg} opacity-60 mix-blend-multiply transition-opacity duration-500 group-hover:opacity-40`} />
                  <div className={`absolute bottom-3 start-3 flex h-11 w-11 items-center justify-center rounded-xl ${p.bg} text-white shadow-lg ring-2 ring-white/70`}>
                    <p.icon className="h-5 w-5" />
                  </div>
                </div>
                <div className="p-5">
                  <h3 className="font-display text-xl font-bold text-primary transition-colors group-hover:text-secondary">
                    {t(`home.programs.${p.key}`)}
                  </h3>
                  <p className="mt-2 text-sm leading-relaxed text-muted-foreground">{t(`home.programs.${p.key}Desc`)}</p>
                  <span className="mt-4 inline-flex items-center gap-1.5 text-sm font-extrabold text-secondary">
                    {t('common.readMore')}
                    <ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-1 rtl:rotate-180 rtl:group-hover:-translate-x-1" />
                  </span>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* ================= WHY AGI (photo background) ================= */}
      <section className="relative overflow-hidden text-white">
        <img
          src={WHY_BG}
          alt=""
          loading="lazy"
          className="absolute inset-0 h-full w-full object-cover"
          onError={(e) => ((e.target as HTMLImageElement).style.display = 'none')}
        />
        <div className="absolute inset-0 bg-gradient-to-br from-[hsl(229_62%_14%/0.82)] via-[hsl(232_70%_24%/0.55)] to-[hsl(229_62%_16%/0.78)]" />
        <div className="stripes-bg absolute inset-0" />
        <div className="noise-overlay" />
        <div className="relative mx-auto max-w-7xl px-4 py-24">
          <div className="grid gap-10 lg:grid-cols-12">
            <div className="lg:col-span-5">
              <div data-reveal className="lg:sticky lg:top-28">
                <span className="kicker text-accent">{t('home.whyKicker')}</span>
                <h2 className="font-display mt-4 text-4xl font-black text-balance lg:text-6xl lg:leading-[1.05]">
                  {t('home.whyTitle')}
                </h2>
                <div data-underline className="mt-6 h-1.5 w-24 rounded-full bg-accent" />
              </div>
            </div>
            <div className="grid gap-6 lg:col-span-7">
              {[
                { icon: Users, title: t('home.why1Title'), text: t('home.why1Text'), color: 'text-accent' },
                { icon: Award, title: t('home.why2Title'), text: t('home.why2Text'), color: 'text-accent' },
                { icon: Sparkles, title: t('home.why3Title'), text: t('home.why3Text'), color: 'text-accent' },
              ].map((f, i) => (
                <div
                  key={i}
                  data-reveal
                  className="group flex gap-6 rounded-3xl bg-white/[0.06] p-7 ring-1 ring-white/15 backdrop-blur transition-all duration-300 hover:bg-white/[0.12] hover:ring-accent/40"
                >
                  <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-white/10 ring-1 ring-white/20 transition-transform duration-300 group-hover:scale-110 group-hover:rotate-3">
                    <f.icon className={`h-7 w-7 ${f.color}`} />
                  </div>
                  <div>
                    <h3 className="font-display text-2xl font-bold">{f.title}</h3>
                    <p className="mt-2 leading-relaxed text-white/75">{f.text}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ================= NEWS ================= */}
      <section className="relative mx-auto max-w-7xl px-4 py-24">
        <div aria-hidden className="text-outline-navy pointer-events-none absolute -top-4 start-4 hidden select-none font-display text-[10rem] font-black leading-none lg:block">
          02
        </div>
        <div className="flex flex-wrap items-end justify-between gap-4">
          <div data-reveal>
            <span className="kicker text-secondary">{t('home.newsKicker')}</span>
            <h2 className="font-display mt-3 text-4xl font-black text-primary lg:text-5xl">{t('home.newsTitle')}</h2>
            <div data-underline className="mt-4 h-1.5 w-24 rounded-full bg-secondary" />
          </div>
          <Link data-reveal to="/news" className="group inline-flex items-center gap-2 font-extrabold text-secondary">
            {t('home.newsAll')}
            <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1 rtl:rotate-180 rtl:group-hover:-translate-x-1" />
          </Link>
        </div>
        <div className="mt-12 grid gap-6 md:grid-cols-3">
          {news.map((n) => (
            <Link
              key={n.slug}
              to={`/news/${n.slug}`}
              data-reveal
              className="group overflow-hidden rounded-3xl bg-card shadow-md ring-1 ring-border transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl"
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
                <h3 className="font-display text-lg font-bold leading-snug text-primary transition-colors group-hover:text-secondary">
                  {n.title}
                </h3>
                <span className="mt-4 inline-flex items-center gap-1.5 text-sm font-extrabold text-secondary">
                  {t('common.readMore')}
                  <ArrowRight className="h-3.5 w-3.5 rtl:rotate-180" />
                </span>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* ================= CTA ================= */}
      <section className="relative overflow-hidden bg-secondary text-white">
        <div className="noise-overlay" />
        <Flag className="absolute -end-10 -top-10 h-64 w-64 text-white/10" />
        <Plus className="spin-slow absolute -start-8 bottom-8 h-24 w-24 text-white/10" />
        <div className="relative mx-auto max-w-4xl px-4 py-24 text-center">
          <h2 data-reveal className="font-display text-4xl font-black text-balance lg:text-6xl lg:leading-[1.08]">
            {t('home.ctaTitle')}
          </h2>
          <p data-reveal className="mx-auto mt-5 max-w-2xl text-lg text-white/85">{t('home.ctaSubtitle')}</p>
          <div data-reveal className="mt-9 flex flex-wrap justify-center gap-3">
            <Link
              to="/apply"
              className="rounded-full bg-white px-9 py-4 font-extrabold text-secondary shadow-xl transition-transform hover:scale-105"
            >
              {t('home.ctaButton')}
            </Link>
            <Link
              to="/admissions/fees"
              className="rounded-full border-2 border-white/40 px-9 py-4 font-extrabold text-white transition-colors hover:border-accent hover:text-accent"
            >
              {t('fees.title')}
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}
