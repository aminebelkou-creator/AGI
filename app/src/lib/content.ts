// Content layer — loads per-page JSON on demand from /content/pages/
export type SectionId =
  | 'about'
  | 'academics'
  | 'anglia'
  | 'programs'
  | 'efl'
  | 'special-ed'
  | 'admissions'
  | 'usa'
  | 'resources';

export interface PageMeta {
  title: string;
  fullTitle: string;
  section: SectionId;
  file: string;
}

export interface PageContent {
  title: string;
  markdown: string;
  date?: string;
}

export interface NewsMeta {
  title: string;
  slug: string;
  date: string;
  file: string;
  image?: string;
}

/* Stable per-slug fallback thumbnails (school photos) for posts without a featured image */
const NEWS_FALLBACKS = [
  'https://www.americangroup-international.com/wp-content/uploads/2026/04/20260411_142632-scaled.jpg',
  'https://www.americangroup-international.com/wp-content/uploads/2026/04/1000115194.jpg',
  'https://www.americangroup-international.com/wp-content/uploads/2026/04/1000005901-scaled.jpg',
  'https://www.americangroup-international.com/wp-content/uploads/2026/04/cropped-1000005901-scaled-1.jpg',
];

export function newsImage(n: NewsMeta): string {
  if (n.image) return n.image;
  let h = 0;
  for (let i = 0; i < n.slug.length; i++) h = (h * 31 + n.slug.charCodeAt(i)) >>> 0;
  return NEWS_FALLBACKS[h % NEWS_FALLBACKS.length];
}

let indexCache: Record<string, PageMeta> | null = null;
let newsCache: NewsMeta[] | null = null;
const pageCache = new Map<string, PageContent>();

export async function getIndex(): Promise<Record<string, PageMeta>> {
  if (!indexCache) {
    const res = await fetch('/content/index.json');
    indexCache = await res.json();
  }
  return indexCache!;
}

export async function getPage(route: string): Promise<PageContent | null> {
  const idx = await getIndex();
  const meta = idx[route];
  if (!meta) return null;
  if (pageCache.has(route)) return pageCache.get(route)!;
  const res = await fetch(`/content/pages/${meta.file}`);
  if (!res.ok) return null;
  const data = (await res.json()) as PageContent;
  pageCache.set(route, data);
  return data;
}

export async function getNews(): Promise<NewsMeta[]> {
  if (!newsCache) {
    const res = await fetch('/content/news.json');
    newsCache = await res.json();
  }
  return newsCache!;
}

export async function getNewsArticle(slug: string): Promise<PageContent | null> {
  const list = await getNews();
  const meta = list.find((n) => n.slug === slug);
  if (!meta) return null;
  const res = await fetch(`/content/pages/${meta.file}`);
  if (!res.ok) return null;
  return (await res.json()) as PageContent;
}

// ---------- Section metadata ----------
export const SECTIONS: Record<
  SectionId,
  { color: string; bg: string; text: string; icon: string }
> = {
  about: { color: 'hsl(229 62% 30%)', bg: 'bg-primary', text: 'text-primary', icon: 'School' },
  academics: { color: 'hsl(217 91% 45%)', bg: 'bg-blue-700', text: 'text-blue-700', icon: 'GraduationCap' },
  anglia: { color: 'hsl(351 78% 41%)', bg: 'bg-secondary', text: 'text-secondary', icon: 'Award' },
  programs: { color: 'hsl(262 60% 45%)', bg: 'bg-purple-700', text: 'text-purple-700', icon: 'Blocks' },
  efl: { color: 'hsl(174 72% 32%)', bg: 'bg-teal-700', text: 'text-teal-700', icon: 'Languages' },
  'special-ed': { color: 'hsl(25 90% 42%)', bg: 'bg-orange-600', text: 'text-orange-600', icon: 'HeartHandshake' },
  admissions: { color: 'hsl(351 78% 41%)', bg: 'bg-secondary', text: 'text-secondary', icon: 'ClipboardList' },
  usa: { color: 'hsl(229 62% 24%)', bg: 'bg-primary', text: 'text-primary', icon: 'Flag' },
  resources: { color: 'hsl(215 16% 40%)', bg: 'bg-slate-600', text: 'text-slate-600', icon: 'FolderOpen' },
};

// ---------- Navigation structure ----------
export interface NavItem {
  route: string;
  key: string; // i18n key suffix under sections/pages, or raw label from index
}

export const NAV_GROUPS: { section: SectionId; root: string; items: string[] }[] = [
  {
    section: 'about',
    root: '/about',
    items: ['/about', '/about/vision', '/about/agi-school', '/about/partners-network'],
  },
  {
    section: 'academics',
    root: '/academics',
    items: [
      '/academics/k12-micro-school',
      '/academics/student-life',
      '/academics/homework-guidelines',
      '/academics/volunteer-hours',
      '/academics/supplies-list',
      '/academics/independent-studies',
    ],
  },
  {
    section: 'anglia',
    root: '/anglia',
    items: [
      '/anglia',
      '/anglia/cite-teacher-training',
      '/cite',
      '/anglia/business-examinations',
      '/anglia/aim-accreditation',
      '/anglia/saturday-schedule',
      '/anglia/class-pricing',
      '/anglia/practice-test',
      '/anglia/network-centers',
      '/anglia/cefr-benchmarks',
      '/anglia/learning-pods',
    ],
  },
  {
    section: 'programs',
    root: '/programs',
    items: [
      '/programs/adult-high-school-diploma',
      '/programs/learning-pods',
      '/programs/teacher-sponsorship',
      '/programs/proctoring-services',
      '/programs/document-editing',
      '/programs/english-castle-workshop',
      '/programs/stem-educators-workshop',
    ],
  },
  {
    section: 'efl',
    root: '/efl-classes',
    items: [
      '/efl-classes',
      '/efl-classes/one-on-one',
      '/efl-classes/medical-efl',
      '/efl-classes/corporate-business',
      '/efl-classes/self-helps',
      '/efl-classes/nursery-rhymes',
      '/efl-classes/sight-words',
    ],
  },
  {
    section: 'special-ed',
    root: '/special-education',
    items: [
      '/special-education',
      '/special-education/adhd-coaching',
      '/special-education/play-therapy',
      '/special-education/i-heart-counselling',
    ],
  },
  {
    section: 'admissions',
    root: '/admissions',
    items: [
      '/admissions',
      '/admissions/enrollment',
      '/admissions/fees',
      '/admissions/calendar',
      '/admissions/important-dates',
      '/admissions/handbook',
      '/admissions/document-request',
      '/admissions/attendance-policy',
      '/admissions/promotion-retention',
      '/admissions/parent-policy',
      '/admissions/placement-assessment',
      '/admissions/refunds-complaints',
      '/admissions/media-policy',
      '/admissions/why-attendance',
      '/apply',
    ],
  },
  {
    section: 'usa',
    root: '/usa',
    items: [
      '/usa',
      '/usa/tutoring-prices',
      '/usa/tutoring-session-length',
      '/usa/zoom-teams-instructions',
      '/usa/teachers-database',
      '/usa/education-consultancy',
      '/usa/university-agent',
    ],
  },
  {
    section: 'resources',
    root: '/forms',
    items: ['/forms', '/partnerships', '/partners/rb-college-uk', '/book-appointment', '/privacy-policy', '/terms'],
  },
];

export function useSEO(title: string, description?: string) {
  if (typeof document === 'undefined') return;
  document.title = `${title} | American Group International — Agadir`;
  let meta = document.querySelector('meta[name="description"]');
  if (!meta) {
    meta = document.createElement('meta');
    meta.setAttribute('name', 'description');
    document.head.appendChild(meta);
  }
  meta.setAttribute(
    'content',
    description ??
      'American Group International (AGI) — K–12 American international school in Agadir, Morocco. Home of Anglia Examinations Morocco. Inclusive, creative and affordable since 2013.',
  );
}
