# AGI — American Group International Website

New website for American Group International (AGI), the K–12 American international school in Agadir, Morocco, and headquarters of Anglia Examinations Morocco. This project replaces the current WordPress site at americangroup-international.com.

## Repository layout

- `app/` — the new website (React 19 + TypeScript + Vite frontend, Hono + tRPC backend, MySQL via Drizzle ORM)
- `data/export/` — content exported from the old WordPress site (68 pages, 60 news posts) as DOCX, PDF and JSON, plus working JSON in `work/`

## Running locally

```bash
cd app
cp .env.example .env    # fill in APP_ID, APP_SECRET, DATABASE_URL
npm install
npm run db:push         # create tables in MySQL
npm run dev
```

Production build: `npm run build` then `npm start` (or use the included `Dockerfile`).

## Features

- English, French and Arabic interface (RTL for Arabic)
- Page content stored as Markdown in `app/public/content/`
- Contact, appointment, enrollment and consultation forms saved to MySQL
- Built-in FAQ chatbot (fees, admissions, calendar, contact) — keyword based, no AI service needed

## Known issues to fix before launch

1. Contact email/phone in the chatbot (`app/contracts/chat-knowledge.json`) don't match the Contact page.
2. Chatbot keyword matching needs word boundaries (`app/api/chat-router.ts`) — e.g. "made" triggers fees.
3. ~250 images/videos are hotlinked to the old WordPress site — download into `app/public/` before shutting it down.
4. Placeholder/leftover content: Lorem Ipsum on Our Vision, WordPress shortcodes on Document Request and other pages, outdated Important Dates.
5. Form submissions are stored but nobody is notified — add email alerts or an admin view.
6. Old WordPress URLs need server-side redirects (mapping in `app/src/lib/legacy-map.json`).
