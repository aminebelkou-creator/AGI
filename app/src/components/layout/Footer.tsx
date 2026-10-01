import { Link } from 'react-router';
import { useTranslation } from 'react-i18next';
import { MapPin, Phone, Mail, Star } from 'lucide-react';

export default function Footer() {
  const { t } = useTranslation();
  return (
    <footer className="mt-auto">
      <div className="stars-divider" />
      <div className="diagonal-navy text-white">
        <div className="mx-auto grid max-w-7xl gap-10 px-4 py-14 md:grid-cols-2 lg:grid-cols-4">
          <div>
            <div className="flex items-center gap-3">
              <img
                src="https://www.americangroup-international.com/wp-content/uploads/2024/07/cropped-newlogo22.png"
                alt="AGI logo"
                className="h-14 w-auto rounded-lg bg-white p-1"
              />
              <div className="font-display text-lg font-bold leading-tight">{t('brand.name')}</div>
            </div>
            <p className="mt-4 text-sm leading-relaxed text-white/75">{t('footer.about')}</p>
            <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-white/10 px-4 py-1.5 text-xs font-bold text-accent">
              <Star className="h-3.5 w-3.5 fill-accent" /> {t('footer.inclusive')}
            </div>
          </div>

          <div>
            <h4 className="kicker text-accent">{t('footer.quickLinks')}</h4>
            <ul className="mt-4 space-y-2 text-sm">
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/about">{t('nav.about')}</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/admissions">{t('nav.admissions')}</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/admissions/fees">{t('fees.title')}</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/admissions/calendar">{t('sections.admissions')} — Calendar</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/news">{t('nav.news')}</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/book-appointment">{t('nav.book')}</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="kicker text-accent">{t('footer.programs')}</h4>
            <ul className="mt-4 space-y-2 text-sm">
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/academics/k12-micro-school">{t('home.programs.k12')}</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/anglia">{t('home.programs.anglia')}</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/efl-classes">{t('home.programs.efl')}</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/programs/adult-high-school-diploma">{t('home.programs.adult')}</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/special-education">{t('home.programs.special')}</Link></li>
              <li><Link className="text-white/80 hover:text-accent transition-colors" to="/usa">{t('nav.usa')}</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="kicker text-accent">{t('footer.contact')}</h4>
            <ul className="mt-4 space-y-3 text-sm text-white/80">
              <li className="flex gap-2.5">
                <MapPin className="mt-0.5 h-4 w-4 shrink-0 text-accent" />
                {t('topbar.address')}
              </li>
              <li className="flex gap-2.5">
                <Phone className="mt-0.5 h-4 w-4 shrink-0 text-accent" />
                <span dir="ltr">+212 528 843 349 · +212 618 639 911 · +212 688 739 393</span>
              </li>
              <li className="flex gap-2.5">
                <Mail className="mt-0.5 h-4 w-4 shrink-0 text-accent" />
                groupinternationala@gmail.com
              </li>
            </ul>
            <p className="mt-4 text-xs text-white/60">{t('footer.usa')}</p>
            <p className="text-xs text-white/60">{t('footer.collegeboard')}</p>
          </div>
        </div>
        <div className="border-t border-white/15">
          <div className="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-2 px-4 py-4 text-xs text-white/60">
            <span>© {new Date().getFullYear()} {t('brand.name')}. {t('footer.rights')}</span>
            <span className="flex gap-4">
              <Link to="/privacy-policy" className="hover:text-accent">Privacy Policy</Link>
              <Link to="/terms" className="hover:text-accent">Terms & Conditions</Link>
            </span>
          </div>
        </div>
      </div>
    </footer>
  );
}
