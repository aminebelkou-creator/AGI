import { z } from "zod";
import { createRouter, publicQuery } from "./middleware";
import { getDb } from "./queries/connection";
import { chatLogs } from "@db/schema";
import knowledge from "../contracts/chat-knowledge.json";

// ---------- types ----------
interface Chunk { route: string; title: string; text: string }
interface FeeRow { grade: string; amount: string }
interface Facts {
  contact: Record<string, string>;
  fees: { inscription: FeeRow[]; tuition: string; summer_school: string; note: string };
  key_facts: string[];
}

const CHUNKS = (knowledge as { chunks: Chunk[] }).chunks;
const FACTS = (knowledge as unknown as { facts: Facts }).facts;

// ---------- multilingual templates ----------
type Lang = "en" | "fr" | "ar";

const T = {
  fees: {
    en: (f: Facts) =>
      `Here are the current AGI school fees:\n\n**Annual inscription fees (paid once per year):**\n${f.fees.inscription
        .map((r) => `• ${r.grade}: **${r.amount}**`)
        .join("\n")}\n\n**Monthly tuition:** ${f.fees.tuition}\n\n**Summer school (high school):** ${f.fees.summer_school}\n\n_${f.fees.note}_`,
    fr: (f: Facts) =>
      `Voici les frais scolaires actuels d'AGI :\n\n**Frais d'inscription annuels (payés une fois par an) :**\n${f.fees.inscription
        .map((r) => `• ${r.grade} : **${r.amount}**`)
        .join("\n")}\n\n**Mensualités :** ${f.fees.tuition}\n\n**École d'été (lycée) :** ${f.fees.summer_school}\n\n_${f.fees.note}_`,
    ar: (f: Facts) =>
      `إليك الرسوم الدراسية الحالية لمدرسة AGI:\n\n**رسوم التسجيل السنوية (تدفع مرة واحدة في السنة):**\n${f.fees.inscription
        .map((r) => `• ${r.grade}: **${r.amount}**`)
        .join("\n")}\n\n**القسط الشهري:** ${f.fees.tuition}\n\n**المدرسة الصيفية (الثانوية):** ${f.fees.summer_school}\n\n_${f.fees.note}_`,
  },
  contact: {
    en: (f: Facts) =>
      `You can reach American Group International here:\n\n📍 **${f.contact.address}**\n📞 Headquarters: **${f.contact.phone_hq}**\n📞 Arabic: **${f.contact.phone_arabic}**\n📞 English: **${f.contact.phone_english}**\n✉️ **${f.contact.email}**\n\n${f.contact.usa_entity}`,
    fr: (f: Facts) =>
      `Vous pouvez joindre American Group International ici :\n\n📍 **${f.contact.address}**\n📞 Siège : **${f.contact.phone_hq}**\n📞 Arabe : **${f.contact.phone_arabic}**\n📞 Anglais : **${f.contact.phone_english}**\n✉️ **${f.contact.email}**\n\n${f.contact.usa_entity}`,
    ar: (f: Facts) =>
      `يمكنك التواصل مع المجموعة الأمريكية الدولية هنا:\n\n📍 **${f.contact.address}**\n📞 المقر الرئيسي: **${f.contact.phone_hq}**\n📞 العربية: **${f.contact.phone_arabic}**\n📞 الإنجليزية: **${f.contact.phone_english}**\n✉️ **${f.contact.email}**\n\n${f.contact.usa_entity}`,
  },
  calendar: {
    en: () =>
      `The 2025–2026 school year at AGI starts on **September 8th, 2025**. The calendar includes Moroccan national holidays (Green March, Independence Day, Amazigh New Year…), Thanksgiving, winter and spring breaks, and exam periods. See the full academic calendar for all dates.`,
    fr: () =>
      `L'année scolaire 2025–2026 à AGI commence le **8 septembre 2025**. Le calendrier comprend les jours fériés marocains (Marche Verte, Fête de l'Indépendance, Nouvel An amazigh…), Thanksgiving, les vacances d'hiver et de printemps et les périodes d'examens. Consultez le calendrier scolaire complet pour toutes les dates.`,
    ar: () =>
      `تبدأ السنة الدراسية 2025–2026 في AGI يوم **8 شتنبر 2025**. يشمل التقويم العطل الوطنية المغربية (المسيرة الخضراء، عيد الاستقلال، رأس السنة الأمازيغية…)، وعيد الشكر، والعطل الشتوية والربيعية، وفترات الامتحانات. راجع التقويم المدرسي الكامل لجميع التواريخ.`,
  },
  admissions: {
    en: () =>
      `Enrolling at AGI is simple:\n\n1. **Book a free consultation** or placement assessment\n2. Bring prior school paperwork and a behaviour report (IEP documentation if applicable)\n3. Pay the annual inscription fee to secure the place\n4. Tuition is paid monthly over 10 months\n\nAll parents need a valid email, phone number and address. Places are limited, so we recommend enrolling early.`,
    fr: () =>
      `S'inscrire à AGI est simple :\n\n1. **Réservez une consultation gratuite** ou un test de niveau\n2. Apportez les documents scolaires antérieurs et un rapport de comportement (documentation IEP si applicable)\n3. Payez les frais d'inscription annuels pour réserver la place\n4. Les mensualités sont payées sur 10 mois\n\nLes parents doivent fournir un e-mail, un téléphone et une adresse valides. Les places sont limitées — inscrivez-vous tôt.`,
    ar: () =>
      `التسجيل في AGI بسيط:\n\n1. **احجز استشارة مجانية** أو اختبار تحديد المستوى\n2. أحضر الوثائق المدرسية السابقة وتقرير السلوك (وثائق IEP إن وجدت)\n3. ادفع رسوم التسجيل السنوية لحجز المقعد\n4. يدفع القسط شهرياً على 10 أشهر\n\nيحتاج جميع أولياء الأمور إلى بريد إلكتروني وهاتف وعنوان صالحين. المقاعد محدودة، لذا ننصح بالتسجيل مبكراً.`,
  },
  fallback: {
    en: () =>
      `I found some information that might help — see the excerpts and pages below. You can also ask me about **fees**, **admissions**, **programs**, the **school calendar**, or **contact details**.`,
    fr: () =>
      `J'ai trouvé des informations qui pourraient vous aider — voir les extraits et pages ci-dessous. Vous pouvez aussi me poser des questions sur les **frais**, les **admissions**, les **programmes**, le **calendrier scolaire** ou les **coordonnées**.`,
    ar: () =>
      `وجدت بعض المعلومات التي قد تساعدك — راجع المقتطفات والصفحات أدناه. يمكنك أيضاً أن تسألني عن **الرسوم** أو **القبول** أو **البرامج** أو **التقويم المدرسي** أو **معلومات الاتصال**.`,
  },
  noResult: {
    en: () =>
      `I couldn't find a precise answer in the school's website content. Try rephrasing your question, or contact the school directly at **groupinternationala@gmail.com** / **+212 528 843 349** — the team will be happy to help.`,
    fr: () =>
      `Je n'ai pas trouvé de réponse précise dans le contenu du site. Essayez de reformuler votre question, ou contactez l'école directement : **groupinternationala@gmail.com** / **+212 528 843 349**.`,
    ar: () =>
      `لم أجد إجابة دقيقة في محتوى موقع المدرسة. حاول إعادة صياغة سؤالك، أو تواصل مع المدرسة مباشرة: **groupinternationala@gmail.com** / **+212 528 843 349** — سيسعد الفريق بمساعدتك.`,
  },
};

// ---------- intent detection ----------
const INTENTS: { name: "fees" | "contact" | "calendar" | "admissions"; route: string; patterns: RegExp }[] = [
  {
    name: "fees",
    route: "/admissions/fees",
    patterns:
      /fee|fees|tuition|price|pricing|cost|costs|pay|payment|mad|dirham|scolarité|frais|tarif|prix|payer|رسوم|ثمن|تكلفة|أداء|واجب/i,
  },
  {
    name: "contact",
    route: "/contact",
    patterns:
      /contact|phone|email|mail|address|location|where|reach|call|whatsapp|téléphone|adresse|email|e-mail|joindre|contacter|situé|هاتف|بريد|عنوان|اتصال|تواصل|أين/i,
  },
  {
    name: "calendar",
    route: "/admissions/calendar",
    patterns:
      /calendar|calandar|holiday|holidays|break|vacation|start.*(year|school)|first day|vacances|calendrier|rentrée|férié|تقويم|عطلة|عطل|بداية السنة|الدخول المدرسي/i,
  },
  {
    name: "admissions",
    route: "/admissions",
    patterns:
      /enrol|enroll|admission|admissions|register|registration|inscri|apply|application|join|inscription|admission|inscrire|تسجيل|التحاق|قبول|تسجيل ابني|inscrire mon enfant/i,
  },
];

// ---------- retrieval ----------
const STOPWORDS = new Set(
  (
    "the a an and or of to in for on at is are was were be been with by from as it its this that these those what when where which who how why do does did can could should would i you he she we they my your our their me him us them " +
    "le la les de des du un une et ou au aux en dans sur par pour avec ce cet cette ces son sa ses mon ma mes ton ta tes notre nos votre vos leur leurs je tu il elle nous vous ils elles qui que quoi quand où comment pourquoi est sont être avoir fait faire " +
    "في من إلى على عن أن إن هذا هذه ذلك تلك الذي التي ما ماذا متى أين كيف لماذا هو هي نحن أنا أنت هم هل كان كانت يكون تكون مع أو و لا لم لن"
  ).split(/\s+/),
);

function tokenize(s: string): string[] {
  return s
    .toLowerCase()
    .replace(/[^\p{L}\p{N}\s]/gu, " ")
    .split(/\s+/)
    .filter((w) => w.length > 2 && !STOPWORDS.has(w));
}

interface ScoredChunk extends Chunk { score: number }

function retrieve(query: string, limit = 3): ScoredChunk[] {
  const tokens = tokenize(query);
  if (!tokens.length) return [];
  const scored: ScoredChunk[] = [];
  for (const c of CHUNKS) {
    const hay = `${c.title} ${c.text}`.toLowerCase();
    let score = 0;
    for (const tk of tokens) {
      let idx = hay.indexOf(tk);
      while (idx !== -1) {
        score += idx < c.title.length ? 4 : 1;
        idx = hay.indexOf(tk, idx + tk.length);
        if (score > 40) break;
      }
    }
    if (score > 0) scored.push({ ...c, score });
  }
  scored.sort((a, b) => b.score - a.score);
  // dedupe by route
  const seen = new Set<string>();
  const out: ScoredChunk[] = [];
  for (const s of scored) {
    if (!seen.has(s.route)) {
      seen.add(s.route);
      out.push(s);
    }
    if (out.length >= limit) break;
  }
  return out;
}

function detectLang(q: string, fallback: Lang): Lang {
  if (/[؀-ۿ]/.test(q)) return "ar";
  if (/[àâçéèêëîïôùûœ]/i.test(q) || /\b(le|la|les|des|est|sont|pour|avec|quelle|quelles|comment)\b/i.test(q)) return "fr";
  return fallback;
}

export const chatRouter = createRouter({
  ask: publicQuery
    .input(
      z.object({
        question: z.string().min(2).max(1000),
        lang: z.enum(["en", "fr", "ar"]).default("en"),
      }),
    )
    .mutation(async ({ input }) => {
      const lang = detectLang(input.question, input.lang);
      const q = input.question;

      // 1) intent answers
      for (const intent of INTENTS) {
        if (intent.patterns.test(q)) {
          const answer = T[intent.name][lang](FACTS);
          const links = [{ route: intent.route, title: "" }];
          log(q, answer, lang);
          return { answer, links, lang };
        }
      }

      // 2) retrieval answers
      const hits = retrieve(q, 3);
      if (hits.length && hits[0].score >= 4) {
        const excerpts = hits
          .map((h) => `**${h.title}** — ${h.text.slice(0, 260).trim()}…`)
          .join("\n\n");
        const answer = `${T.fallback[lang]()}\n\n${excerpts}`;
        const links = hits.map((h) => ({ route: h.route, title: h.title }));
        log(q, answer, lang);
        return { answer, links, lang };
      }

      const answer = T.noResult[lang]();
      log(q, answer, lang);
      return { answer, links: [{ route: "/contact", title: "" }], lang };
    }),
});

async function log(question: string, answer: string, lang: Lang) {
  try {
    await getDb().insert(chatLogs).values({ question, answer, lang });
  } catch {
    // logging is best-effort
  }
}
