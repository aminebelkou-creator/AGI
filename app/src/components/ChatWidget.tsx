import { useEffect, useRef, useState, type FormEvent } from 'react';
import { Link } from 'react-router';
import { useTranslation } from 'react-i18next';
import { MessageCircle, X, Send, Loader2, GraduationCap } from 'lucide-react';
import { trpc } from '@/providers/trpc';
import Markdown from '@/components/Markdown';

interface Msg {
  role: 'user' | 'assistant';
  text: string;
  links?: { route: string; title: string }[];
}

export default function ChatWidget() {
  const { t, i18n } = useTranslation();
  const [open, setOpen] = useState(false);
  const [msgs, setMsgs] = useState<Msg[]>([]);
  const [busy, setBusy] = useState(false);
  const ask = trpc.chat.ask.useMutation();
  const bodyRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bodyRef.current?.scrollTo({ top: bodyRef.current.scrollHeight, behavior: 'smooth' });
  }, [msgs, busy]);

  function openChat() {
    setOpen(true);
    if (msgs.length === 0) {
      setMsgs([{ role: 'assistant', text: t('chat.welcome') }]);
    }
  }

  async function send(question: string) {
    if (!question.trim() || busy) return;
    setMsgs((m) => [...m, { role: 'user', text: question }]);
    setBusy(true);
    try {
      const lang = (['en', 'fr', 'ar'].includes(i18n.language) ? i18n.language : 'en') as 'en' | 'fr' | 'ar';
      const res = await ask.mutateAsync({ question, lang });
      setMsgs((m) => [...m, { role: 'assistant', text: res.answer, links: res.links }]);
    } catch {
      setMsgs((m) => [...m, { role: 'assistant', text: t('common.formError') }]);
    } finally {
      setBusy(false);
    }
  }

  function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const fd = new FormData(e.currentTarget);
    const q = String(fd.get('q') ?? '');
    (e.currentTarget.querySelector('input') as HTMLInputElement).value = '';
    send(q);
  }

  const suggestions = t('chat.suggestions', { returnObjects: true }) as string[];

  return (
    <>
      {/* Floating button */}
      {!open && (
        <button
          onClick={openChat}
          aria-label={t('chat.open')}
          className="fixed bottom-5 end-5 z-50 flex h-15 w-15 items-center justify-center rounded-full bg-secondary p-4 text-white shadow-2xl shadow-secondary/50 transition-transform hover:scale-110"
        >
          <MessageCircle className="h-7 w-7" />
          <span className="absolute -end-0.5 -top-0.5 flex h-4 w-4">
            <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-accent opacity-75" />
            <span className="relative inline-flex h-4 w-4 rounded-full bg-accent" />
          </span>
        </button>
      )}

      {/* Chat panel */}
      {open && (
        <div className="fixed bottom-5 end-5 z-50 flex h-[min(600px,calc(100vh-6rem))] w-[min(400px,calc(100vw-2.5rem))] flex-col overflow-hidden rounded-3xl bg-white shadow-2xl ring-1 ring-black/10">
          {/* header */}
          <div className="diagonal-navy flex items-center gap-3 px-5 py-4 text-white">
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-accent text-primary">
              <GraduationCap className="h-5 w-5" />
            </div>
            <div className="min-w-0 flex-1">
              <div className="truncate text-sm font-extrabold">{t('chat.title')}</div>
              <div className="truncate text-xs text-white/70">{t('chat.subtitle')}</div>
            </div>
            <button onClick={() => setOpen(false)} aria-label={t('chat.close')} className="rounded-full p-1.5 hover:bg-white/15">
              <X className="h-5 w-5" />
            </button>
          </div>

          {/* messages */}
          <div ref={bodyRef} className="flex-1 space-y-4 overflow-y-auto bg-muted/40 p-4">
            {msgs.map((m, i) => (
              <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div
                  className={`max-w-[85%] rounded-2xl px-4 py-3 text-sm leading-relaxed shadow-sm ${
                    m.role === 'user'
                      ? 'rounded-br-sm bg-secondary text-white'
                      : 'rounded-bl-sm bg-white text-foreground ring-1 ring-border'
                  }`}
                >
                  {m.role === 'assistant' ? (
                    <div className="[&_strong]:text-primary">
                      <Markdown compact>{m.text}</Markdown>
                    </div>
                  ) : (
                    m.text
                  )}
                  {m.links && m.links.length > 0 && (
                    <div className="mt-2.5 border-t border-border pt-2">
                      <div className="mb-1 text-[10px] font-extrabold uppercase tracking-widest text-muted-foreground">
                        {t('chat.relatedPages')}
                      </div>
                      {m.links.map((l) => (
                        <Link
                          key={l.route}
                          to={l.route}
                          onClick={() => setOpen(false)}
                          className="block truncate rounded-lg px-2 py-1 text-xs font-bold text-secondary hover:bg-muted"
                        >
                          → {l.title || l.route}
                        </Link>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ))}
            {busy && (
              <div className="flex justify-start">
                <div className="inline-flex items-center gap-2 rounded-2xl rounded-bl-sm bg-white px-4 py-3 text-sm text-muted-foreground shadow-sm ring-1 ring-border">
                  <Loader2 className="h-4 w-4 animate-spin" /> {t('chat.thinking')}
                </div>
              </div>
            )}
            {msgs.length <= 1 && !busy && (
              <div className="flex flex-wrap gap-2">
                {suggestions.map((s) => (
                  <button
                    key={s}
                    onClick={() => send(s)}
                    className="rounded-full bg-white px-3.5 py-2 text-xs font-bold text-primary shadow-sm ring-1 ring-border transition-colors hover:bg-secondary hover:text-white"
                  >
                    {s}
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* input */}
          <form onSubmit={onSubmit} className="flex items-center gap-2 border-t border-border bg-white p-3">
            <input
              name="q"
              autoComplete="off"
              placeholder={t('chat.placeholder')}
              className="min-w-0 flex-1 rounded-full border-2 border-input px-4 py-2.5 text-sm outline-none focus:border-secondary"
            />
            <button
              type="submit"
              disabled={busy}
              aria-label={t('chat.send')}
              className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-secondary text-white transition-transform hover:scale-105 disabled:opacity-50"
            >
              <Send className="h-4 w-4 rtl:-scale-x-100" />
            </button>
          </form>
          <div className="bg-white px-4 pb-2 text-center text-[10px] text-muted-foreground">{t('chat.disclaimer')}</div>
        </div>
      )}
    </>
  );
}
