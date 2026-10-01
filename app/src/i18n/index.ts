import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import en from './locales/en.json';
import fr from './locales/fr.json';
import ar from './locales/ar.json';

export const LANGUAGES = [
  { code: 'en', label: 'English', dir: 'ltr' as const, flag: '🇺🇸' },
  { code: 'fr', label: 'Français', dir: 'ltr' as const, flag: '🇫🇷' },
  { code: 'ar', label: 'العربية', dir: 'rtl' as const, flag: '🇲🇦' },
];

const stored = typeof localStorage !== 'undefined' ? localStorage.getItem('agi-lang') : null;
const initial = stored && LANGUAGES.some((l) => l.code === stored) ? stored : 'en';

i18n.use(initReactI18next).init({
  resources: {
    en: { translation: en },
    fr: { translation: fr },
    ar: { translation: ar },
  },
  lng: initial,
  fallbackLng: 'en',
  interpolation: { escapeValue: false },
});

export function applyDir(lng: string) {
  const lang = LANGUAGES.find((l) => l.code === lng);
  document.documentElement.dir = lang?.dir ?? 'ltr';
  document.documentElement.lang = lng;
}

export function setLanguage(lng: string) {
  localStorage.setItem('agi-lang', lng);
  i18n.changeLanguage(lng);
  applyDir(lng);
}

applyDir(initial);

export default i18n;
