import { useEffect, useState, type FormEvent } from 'react';
import { Link } from 'react-router';
import { useTranslation } from 'react-i18next';
import { CheckCircle2, Loader2, MapPin, Phone, Mail, AlertCircle } from 'lucide-react';
import { trpc } from '@/providers/trpc';
import { getPage, useSEO, type PageContent } from '@/lib/content';
import Markdown from '@/components/Markdown';

type FormType = 'contact' | 'appointment' | 'enrollment' | 'consultation';

interface Props {
  type: FormType;
  route?: string; // optional legacy content page to render beside the form
  titleKey: string;
}

const GRADES = ['Kindergarten', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12', 'Adult Program'];

export default function FormPage({ type, route, titleKey }: Props) {
  const { t } = useTranslation();
  const [page, setPage] = useState<PageContent | null>(null);
  const [done, setDone] = useState(false);
  const [error, setError] = useState(false);
  const submit = trpc.forms.submit.useMutation();

  useSEO(t(titleKey));

  useEffect(() => {
    if (route) getPage(route).then(setPage);
  }, [route]);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError(false);
    const fd = new FormData(e.currentTarget);
    const name = String(fd.get('name') ?? '');
    const email = String(fd.get('email') ?? '');
    const phone = String(fd.get('phone') ?? '');
    const payload: Record<string, string> = {};
    for (const [k, v] of fd.entries()) {
      if (!['name', 'email', 'phone'].includes(k) && typeof v === 'string' && v) payload[k] = v;
    }
    try {
      await submit.mutateAsync({ type, name, email, phone: phone || undefined, payload });
      setDone(true);
    } catch {
      setError(true);
    }
  }

  const inputCls =
    'w-full rounded-xl border-2 border-input bg-white px-4 py-3 text-sm font-medium outline-none transition-colors focus:border-secondary';

  return (
    <div>
      <div className="band-navy text-white">
        <div className="mx-auto max-w-7xl px-4 py-14 lg:py-20">
          <span className="kicker text-accent">AGI</span>
          <h1 className="font-display mt-3 text-4xl font-black lg:text-6xl">{t(titleKey)}</h1>
          <div className="mt-5 h-1.5 w-28 rounded-full bg-accent" />
        </div>
      </div>

      <div className="mx-auto grid max-w-7xl gap-10 px-4 py-14 lg:grid-cols-[1fr_380px]">
        <div className="min-w-0">
          {done ? (
            <div className="rounded-3xl bg-card p-10 text-center shadow-sm ring-1 ring-border">
              <CheckCircle2 className="mx-auto h-14 w-14 text-teal-600" />
              <p className="mt-5 text-lg font-semibold text-primary">{t('common.formSuccess')}</p>
            </div>
          ) : (
            <form onSubmit={onSubmit} className="rounded-3xl bg-card p-6 shadow-sm ring-1 ring-border md:p-8">
              <div className="grid gap-5 sm:grid-cols-2">
                <label className="block">
                  <span className="mb-1.5 block text-sm font-bold text-primary">{t('forms.name')} *</span>
                  <input name="name" required className={inputCls} />
                </label>
                <label className="block">
                  <span className="mb-1.5 block text-sm font-bold text-primary">{t('forms.email')} *</span>
                  <input name="email" type="email" required className={inputCls} dir="ltr" />
                </label>
                <label className="block">
                  <span className="mb-1.5 block text-sm font-bold text-primary">{t('forms.phone')}</span>
                  <input name="phone" type="tel" className={inputCls} dir="ltr" />
                </label>
                {(type === 'enrollment' || type === 'consultation') && (
                  <>
                    <label className="block">
                      <span className="mb-1.5 block text-sm font-bold text-primary">{t('forms.studentName')}</span>
                      <input name="studentName" className={inputCls} />
                    </label>
                    <label className="block sm:col-span-2">
                      <span className="mb-1.5 block text-sm font-bold text-primary">{t('forms.grade')}</span>
                      <select name="grade" className={inputCls} defaultValue="">
                        <option value="" disabled>
                          {t('forms.selectPlaceholder')}
                        </option>
                        {GRADES.map((g) => (
                          <option key={g}>{g}</option>
                        ))}
                      </select>
                    </label>
                  </>
                )}
                {type === 'appointment' && (
                  <>
                    <label className="block">
                      <span className="mb-1.5 block text-sm font-bold text-primary">{t('forms.preferredDate')}</span>
                      <input name="preferredDate" type="date" className={inputCls} />
                    </label>
                    <label className="block sm:col-span-2">
                      <span className="mb-1.5 block text-sm font-bold text-primary">{t('forms.preferredTime')}</span>
                      <input name="preferredTime" type="time" className={inputCls} />
                    </label>
                  </>
                )}
                {type === 'contact' && (
                  <label className="block sm:col-span-2">
                    <span className="mb-1.5 block text-sm font-bold text-primary">{t('forms.subject')}</span>
                    <input name="subject" className={inputCls} />
                  </label>
                )}
                <label className="block sm:col-span-2">
                  <span className="mb-1.5 block text-sm font-bold text-primary">
                    {type === 'contact' ? t('forms.message') : t('forms.notes')}
                  </span>
                  <textarea name="message" rows={5} className={inputCls} />
                </label>
              </div>
              {error && (
                <p className="mt-4 inline-flex items-center gap-2 rounded-xl bg-destructive/10 px-4 py-2.5 text-sm font-semibold text-destructive">
                  <AlertCircle className="h-4 w-4" /> {t('common.formError')}
                </p>
              )}
              <button
                type="submit"
                disabled={submit.isPending}
                className="mt-6 inline-flex items-center gap-2 rounded-full bg-secondary px-8 py-3.5 font-extrabold text-white shadow-lg shadow-secondary/30 transition-transform hover:scale-105 disabled:opacity-60"
              >
                {submit.isPending ? <Loader2 className="h-4 w-4 animate-spin" /> : null}
                {submit.isPending ? t('common.submitting') : t('common.submit')}
              </button>
            </form>
          )}

          {page?.markdown && (
            <article className="mt-10 rounded-3xl bg-card p-6 shadow-sm ring-1 ring-border md:p-10" dir="ltr">
              <Markdown>{page.markdown}</Markdown>
            </article>
          )}
        </div>

        {/* Contact card */}
        <aside className="space-y-6 lg:sticky lg:top-32 lg:self-start">
          <div className="rounded-3xl bg-primary p-7 text-white shadow-lg">
            <h3 className="font-display text-xl font-bold">{t('footer.contact')}</h3>
            <ul className="mt-5 space-y-4 text-sm text-white/85">
              <li className="flex gap-3">
                <MapPin className="mt-0.5 h-5 w-5 shrink-0 text-accent" />
                {t('topbar.address')}
              </li>
              <li className="flex gap-3">
                <Phone className="mt-0.5 h-5 w-5 shrink-0 text-accent" />
                <span dir="ltr">
                  +212 528 843 349 ({t('topbar.hq')})
                  <br />+212 618 639 911 ({t('topbar.arabic')})
                  <br />+212 688 739 393 ({t('topbar.english')})
                </span>
              </li>
              <li className="flex gap-3">
                <Mail className="mt-0.5 h-5 w-5 shrink-0 text-accent" />
                groupinternationala@gmail.com
              </li>
            </ul>
            <Link
              to="/book-appointment"
              className="mt-6 block rounded-full bg-secondary px-5 py-3 text-center text-sm font-extrabold text-white transition-transform hover:scale-105"
            >
              {t('nav.book')}
            </Link>
          </div>
        </aside>
      </div>
    </div>
  );
}
