import { useEffect, useRef, useState } from 'react';
import { Link, NavLink, useLocation } from 'react-router';
import { useTranslation } from 'react-i18next';
import { ChevronDown, Menu, X, Phone, Mail, MapPin, Globe } from 'lucide-react';
import { NAV_GROUPS, getIndex, type PageMeta } from '@/lib/content';
import { LANGUAGES, setLanguage } from '@/i18n';

const NAV_LABEL_KEYS: Record<string, string> = {
  about: 'nav.about',
  academics: 'nav.academics',
  anglia: 'nav.anglia',
  programs: 'nav.programs',
  efl: 'nav.efl',
  'special-ed': 'nav.specialEd',
  admissions: 'nav.admissions',
  usa: 'nav.usa',
  resources: 'nav.resources',
};

// Per-language short labels for page links in nav dropdowns
const PAGE_LABEL_I18N: Record<string, { fr: string; ar: string }> = {
  '/about': { fr: 'À propos', ar: 'من نحن' },
  '/about/vision': { fr: 'Notre vision', ar: 'رؤيتنا' },
  '/about/agi-school': { fr: "École AGI — Agadir", ar: 'مدرسة AGI — أكادير' },
  '/about/partners-network': { fr: 'Réseau de partenaires', ar: 'شبكة الشركاء' },
  '/academics/k12-micro-school': { fr: 'Micro-école K–12', ar: 'مدرسة K–12 الصغيرة' },
  '/academics/student-life': { fr: 'Vie scolaire', ar: 'الحياة المدرسية' },
  '/academics/homework-guidelines': { fr: 'Devoirs', ar: 'الواجبات المنزلية' },
  '/academics/volunteer-hours': { fr: 'Heures de bénévolat', ar: 'ساعات التطوع' },
  '/academics/supplies-list': { fr: 'Fournitures scolaires', ar: 'اللوازم المدرسية' },
  '/academics/independent-studies': { fr: 'Études indépendantes', ar: 'الدراسات المستقلة' },
  '/anglia': { fr: 'Examens Anglia', ar: 'امتحانات أنجليا' },
  '/anglia/cite-teacher-training': { fr: 'Formation C.I.T.E', ar: 'تدريب المعلمين C.I.T.E' },
  '/cite': { fr: 'Certificat C.I.T.E', ar: 'شهادة C.I.T.E' },
  '/anglia/business-examinations': { fr: 'Examens business', ar: 'امتحانات الأعمال' },
  '/anglia/aim-accreditation': { fr: 'Accréditation AIM', ar: 'اعتماد AIM' },
  '/anglia/saturday-schedule': { fr: 'Cours du samedi', ar: 'جدول دروس السبت' },
  '/anglia/class-pricing': { fr: 'Tarifs des cours', ar: 'أسعار الدروس' },
  '/anglia/practice-test': { fr: 'Test blanc gratuit', ar: 'اختبار تجريبي مجاني' },
  '/anglia/network-centers': { fr: 'Réseau Anglia Maroc', ar: 'شبكة أنجليا المغرب' },
  '/anglia/cefr-benchmarks': { fr: 'Référentiels CECR', ar: 'معايير الإطار الأوروبي' },
  '/anglia/learning-pods': { fr: 'Learning Pods Anglia', ar: 'مجموعات أنجليا' },
  '/programs/adult-high-school-diploma': { fr: 'Diplôme adultes (16+)', ar: 'دبلوم الكبار (16+)' },
  '/programs/learning-pods': { fr: 'Learning Pods AGI', ar: 'مجموعات التعلم AGI' },
  '/programs/teacher-sponsorship': { fr: 'Parrainage enseignants USA', ar: 'رعاية المعلمين في أمريكا' },
  '/programs/proctoring-services': { fr: 'Surveillance d’examens', ar: 'خدمات مراقبة الامتحانات' },
  '/programs/document-editing': { fr: 'Édition de documents', ar: 'تحرير الوثائق' },
  '/programs/english-castle-workshop': { fr: 'Atelier English Castle', ar: 'ورشة القلعة الإنجليزية' },
  '/programs/stem-educators-workshop': { fr: 'Atelier STEM', ar: 'ورشة STEM للمعلمين' },
  '/efl-classes': { fr: 'Cours EFL', ar: 'دروس EFL' },
  '/efl-classes/one-on-one': { fr: 'Cours individuels', ar: 'دروس فردية' },
  '/efl-classes/medical-efl': { fr: 'Anglais médical', ar: 'الإنجليزية الطبية' },
  '/efl-classes/corporate-business': { fr: 'Anglais d’entreprise', ar: 'إنجليزية الأعمال' },
  '/efl-classes/self-helps': { fr: 'Auto-apprentissage', ar: 'موارد التعلم الذاتي' },
  '/efl-classes/nursery-rhymes': { fr: 'Comptines Pre-K', ar: 'أناشيد ما قبل الروضة' },
  '/efl-classes/sight-words': { fr: 'Mots fréquents McGuffey', ar: 'الكلمات البصرية' },
  '/special-education': { fr: 'Éducation spécialisée', ar: 'التربية الخاصة' },
  '/special-education/adhd-coaching': { fr: 'Coaching TDAH', ar: 'دعم فرط الحركة' },
  '/special-education/play-therapy': { fr: 'Thérapie par le jeu', ar: 'العلاج باللعب' },
  '/special-education/i-heart-counselling': { fr: 'Accompagnement i-Heart', ar: 'مرافقة i-Heart' },
  '/admissions': { fr: 'Procédure d’admission', ar: 'إجراءات القبول' },
  '/admissions/enrollment': { fr: 'Inscription', ar: 'التسجيل' },
  '/admissions/fees': { fr: 'Frais de scolarité', ar: 'الرسوم الدراسية' },
  '/admissions/calendar': { fr: 'Calendrier scolaire', ar: 'التقويم المدرسي' },
  '/admissions/important-dates': { fr: 'Dates importantes', ar: 'تواريخ مهمة' },
  '/admissions/handbook': { fr: 'Manuel académique', ar: 'الدليل الأكاديمي' },
  '/admissions/document-request': { fr: 'Demande de documents', ar: 'طلب الوثائق' },
  '/admissions/attendance-policy': { fr: 'Politique d’assiduité', ar: 'سياسة الحضور' },
  '/admissions/promotion-retention': { fr: 'Promotion & redoublement', ar: 'الانتقال والإعادة' },
  '/admissions/parent-policy': { fr: 'Politique des parents', ar: 'سياسة أولياء الأمور' },
  '/admissions/placement-assessment': { fr: 'Évaluation de placement', ar: 'تقييم المستوى' },
  '/admissions/refunds-complaints': { fr: 'Remboursements & réclamations', ar: 'الاسترداد والشكاوى' },
  '/admissions/media-policy': { fr: 'Politique média', ar: 'سياسة الإعلام' },
  '/admissions/why-attendance': { fr: 'Importance de l’assiduité', ar: 'أهمية الحضور' },
  '/apply': { fr: 'Consultation gratuite', ar: 'استشارة مجانية' },
  '/usa': { fr: 'American Group USA', ar: 'المجموعة الأمريكية USA' },
  '/usa/tutoring-prices': { fr: 'Tarifs tutorat en ligne', ar: 'أسعار الدروس عبر الإنترنت' },
  '/usa/tutoring-session-length': { fr: 'Durée des sessions', ar: 'مدة الجلسات' },
  '/usa/zoom-teams-instructions': { fr: 'Guide Zoom/Teams', ar: 'تعليمات Zoom/Teams' },
  '/usa/teachers-database': { fr: 'Base d’enseignants', ar: 'قاعدة المعلمين' },
  '/usa/education-consultancy': { fr: 'Conseil éducatif', ar: 'الاستشارات التعليمية' },
  '/usa/university-agent': { fr: 'Agent universitaire', ar: 'وكيل الجامعات' },
  '/forms': { fr: 'Formulaires', ar: 'النماذج' },
  '/partnerships': { fr: 'Partenariats', ar: 'الشراكات' },
  '/partners/rb-college-uk': { fr: 'RB College UK', ar: 'كلية RB البريطانية' },
  '/book-appointment': { fr: 'Rendez-vous', ar: 'حجز موعد' },
  '/privacy-policy': { fr: 'Politique de confidentialité', ar: 'سياسة الخصوصية' },
  '/terms': { fr: 'Conditions générales', ar: 'الشروط والأحكام' },
};

export function pageLabel(route: string, fallback: string, lng: string): string {
  if (lng === 'en') return fallback;
  const entry = PAGE_LABEL_I18N[route];
  if (!entry) return fallback;
  return entry[lng as 'fr' | 'ar'] ?? fallback;
}

export default function Header() {
  const { t, i18n } = useTranslation();
  const [open, setOpen] = useState<string | null>(null);
  const [mobileOpen, setMobileOpen] = useState(false);
  const [index, setIndex] = useState<Record<string, PageMeta>>({});
  const location = useLocation();
  const navRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    getIndex().then(setIndex);
  }, []);

  useEffect(() => {
    setOpen(null);
    setMobileOpen(false);
  }, [location.pathname]);

  useEffect(() => {
    const onClick = (e: MouseEvent) => {
      if (navRef.current && !navRef.current.contains(e.target as Node)) setOpen(null);
    };
    document.addEventListener('click', onClick);
    return () => document.removeEventListener('click', onClick);
  }, []);

  const label = (route: string) => pageLabel(route, index[route]?.title ?? route, i18n.language);

  return (
    <header className="sticky top-0 z-50 shadow-lg" ref={navRef}>
      {/* Top bar */}
      <div className="diagonal-navy text-white text-xs">
        <div className="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-1.5">
          <div className="hidden items-center gap-4 md:flex">
            <span className="inline-flex items-center gap-1.5 opacity-90">
              <MapPin className="h-3 w-3 text-accent" /> {t('topbar.address')}
            </span>
          </div>
          <div className="flex items-center gap-4">
            <a href="tel:+212528843349" className="inline-flex items-center gap-1.5 hover:text-accent transition-colors">
              <Phone className="h-3 w-3 text-accent" />
              <span dir="ltr">+212 528 843 349</span>
            </a>
            <a href="mailto:groupinternationala@gmail.com" className="hidden items-center gap-1.5 hover:text-accent transition-colors sm:inline-flex">
              <Mail className="h-3 w-3 text-accent" /> groupinternationala@gmail.com
            </a>
            {/* Language switcher */}
            <div className="relative">
              <button
                onClick={() => setOpen(open === '__lang' ? null : '__lang')}
                className="inline-flex items-center gap-1 rounded-full bg-white/10 px-2.5 py-0.5 font-bold hover:bg-white/20 transition-colors"
                aria-label={t('common.language')}
              >
                <Globe className="h-3 w-3" />
                {i18n.language.toUpperCase()}
                <ChevronDown className="h-3 w-3" />
              </button>
              {open === '__lang' && (
                <div className="absolute end-0 top-full z-50 mt-1 w-36 overflow-hidden rounded-xl bg-white text-foreground shadow-2xl ring-1 ring-black/10">
                  {LANGUAGES.map((l) => (
                    <button
                      key={l.code}
                      onClick={() => {
                        setLanguage(l.code);
                        setOpen(null);
                      }}
                      className={`flex w-full items-center gap-2 px-4 py-2.5 text-sm font-semibold hover:bg-muted transition-colors ${
                        i18n.language === l.code ? 'text-secondary' : ''
                      }`}
                    >
                      <span>{l.flag}</span> {l.label}
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Main nav */}
      <div className="bg-white/95 backdrop-blur border-b-4 border-secondary">
        <div className="mx-auto flex max-w-7xl items-center justify-between gap-3 px-4 py-2.5">
          <Link to="/" className="flex items-center gap-3 shrink-0">
            <img
              src="https://www.americangroup-international.com/wp-content/uploads/2024/07/cropped-newlogo22.png"
              alt="American Group International logo"
              className="h-12 w-auto"
            />
            <div className="hidden sm:block leading-tight">
              <div className="font-display text-lg font-extrabold text-primary">{t('brand.name')}</div>
              <div className="text-[10px] font-bold uppercase tracking-widest text-secondary">{t('brand.tagline')}</div>
            </div>
          </Link>

          {/* Desktop nav */}
          <nav className="hidden items-center gap-0.5 lg:flex">
            <NavLink
              to="/"
              className={({ isActive }) =>
                `rounded-lg px-3 py-2 text-sm font-bold transition-colors ${isActive ? 'text-secondary' : 'text-primary hover:bg-muted'}`
              }
            >
              {t('nav.home')}
            </NavLink>
            {NAV_GROUPS.map((g) => (
              <div key={g.section} className="relative">
                <button
                  onClick={() => setOpen(open === g.section ? null : g.section)}
                  className={`inline-flex items-center gap-1 rounded-lg px-2.5 py-2 text-sm font-bold transition-colors ${
                    location.pathname.startsWith(g.root) && g.root !== '/forms'
                      ? 'text-secondary'
                      : 'text-primary hover:bg-muted'
                  }`}
                >
                  {t(NAV_LABEL_KEYS[g.section])}
                  <ChevronDown className={`h-3.5 w-3.5 transition-transform ${open === g.section ? 'rotate-180' : ''}`} />
                </button>
                {open === g.section && (
                  <div className="absolute start-0 top-full z-50 mt-1 max-h-[70vh] w-72 overflow-y-auto rounded-2xl bg-white p-2 shadow-2xl ring-1 ring-black/10">
                    {g.items.map((route) => (
                      <Link
                        key={route}
                        to={route}
                        className="block rounded-lg px-3 py-2 text-sm font-medium text-foreground/80 hover:bg-muted hover:text-secondary transition-colors"
                      >
                        {label(route)}
                      </Link>
                    ))}
                  </div>
                )}
              </div>
            ))}
            <NavLink
              to="/news"
              className={({ isActive }) =>
                `rounded-lg px-3 py-2 text-sm font-bold transition-colors ${isActive ? 'text-secondary' : 'text-primary hover:bg-muted'}`
              }
            >
              {t('nav.news')}
            </NavLink>
          </nav>

          <div className="flex items-center gap-2">
            <Link
              to="/apply"
              className="hidden rounded-full bg-secondary px-5 py-2.5 text-sm font-extrabold text-white shadow-md shadow-secondary/30 transition-transform hover:scale-105 lg:inline-block"
            >
              {t('nav.apply')}
            </Link>
            <button
              className="rounded-lg p-2 text-primary hover:bg-muted lg:hidden"
              onClick={() => setMobileOpen(!mobileOpen)}
              aria-label={mobileOpen ? t('nav.close') : t('nav.menu')}
            >
              {mobileOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile menu */}
      {mobileOpen && (
        <div className="max-h-[75vh] overflow-y-auto border-b-4 border-secondary bg-white px-4 pb-6 pt-2 lg:hidden">
          <Link to="/" className="block rounded-lg px-3 py-2.5 font-bold text-primary hover:bg-muted">
            {t('nav.home')}
          </Link>
          {NAV_GROUPS.map((g) => (
            <details key={g.section} className="group">
              <summary className="flex cursor-pointer items-center justify-between rounded-lg px-3 py-2.5 font-bold text-primary hover:bg-muted">
                {t(NAV_LABEL_KEYS[g.section])}
                <ChevronDown className="h-4 w-4 transition-transform group-open:rotate-180" />
              </summary>
              <div className="ms-3 border-s-2 border-accent/50 ps-3 pb-1">
                {g.items.map((route) => (
                  <Link
                    key={route}
                    to={route}
                    className="block rounded-lg px-3 py-2 text-sm text-foreground/75 hover:bg-muted hover:text-secondary"
                  >
                    {label(route)}
                  </Link>
                ))}
              </div>
            </details>
          ))}
          <Link to="/news" className="block rounded-lg px-3 py-2.5 font-bold text-primary hover:bg-muted">
            {t('nav.news')}
          </Link>
          <Link to="/contact" className="block rounded-lg px-3 py-2.5 font-bold text-primary hover:bg-muted">
            {t('nav.contact')}
          </Link>
          <Link
            to="/apply"
            className="mt-3 block rounded-full bg-secondary px-5 py-3 text-center font-extrabold text-white"
          >
            {t('nav.apply')}
          </Link>
        </div>
      )}
    </header>
  );
}
