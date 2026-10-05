# Test page brief – "Atlas Language Studio" (fictional)

A one-page website for a small language school in Agadir. Fictional business, used only to test CMSs.
Build it with the CMS's own building blocks (components/blocks/sections), not one big HTML blob.

## Global data (must be stored ONCE and reused)
Create these as global settings / a dataset / site data – NOT typed twice:
- `phone`: +212 600 000 000
- `email`: hello@atlas-studio.example
- `address`: 12 Avenue Hassan II, Agadir
- `monthly_price`: 900 MAD
- `opening_hours`: Mon–Fri 9:00–19:00 · Sat 9:00–13:00
`monthly_price` must appear in TWO places (hero badge and pricing card). `phone` must appear in the header and the footer.

## Design
- Colors: deep teal #0F4C5C (primary), coral #E36414 (accent), sand #F7F3EE (background), ink #1B1B1B (text).
- Fonts: a serif for headings (e.g. Fraunces or Newsreader), a sans-serif for text (e.g. Inter). Arabic: Noto Naskh Arabic.
- Clean, modern, generous spacing. Must work on a phone (no sideways scrolling at 390 px).

## Sections (in this order)
1. **Header** (shared): logo text "Atlas Language Studio", menu links (Courses · Prices · FAQ · Contact – anchors on this page), language switch EN | ع, button "Book a free level test" → #contact, phone number (global).
2. **Hero**: headline "Speak with confidence."; subtitle "English, French and Arabic courses for children and adults in Agadir – small groups, certified teachers."; buttons "Book a free level test" (#contact) and "See prices" (#prices); a badge "From {monthly_price} a month" (global); one image (any free stock photo of a classroom; alt text required).
3. **Three feature cards**: "Small groups" – "Never more than 8 students per class."; "Certified teachers" – "Every teacher holds an international teaching certificate."; "Free level test" – "We place you at the right level before you start."
4. **Courses** (a list of 4 items, each: name + age + short description):
   - English for kids (6–12) – "Playful lessons with songs, games and stories."
   - English for adults (16+) – "Conversation and grammar for work, travel and study."
   - French conversation (12+) – "Speak French with confidence in everyday situations."
   - Arabic for beginners (all ages) – "Learn to read, write and speak Modern Standard Arabic."
   *(Descriptions added on 2026-10-05 after the EmDash first build, which correctly left them empty because the brief gave no text.)*
5. **Prices** (#prices): one pricing card "Monthly course" – {monthly_price} – "8 hours a month · materials included · free level test"; button "Enrol" → #contact.
6. **FAQ** (#faq): 3 questions with expandable answers:
   - "Do you offer trial lessons?" – "Yes, the level test includes a 20-minute trial lesson."
   - "Can I join in the middle of the year?" – "Yes, groups start every month."
   - "Do you prepare for exams?" – "Yes, we prepare for international English exams."
7. **Contact** (#contact): a form (name, email, phone, message, consent checkbox "I agree to be contacted") with a confirmation message; next to it address, phone, email, opening hours (all global).
8. **Footer** (shared): short sentence "A small language school in Agadir since 2015.", address/phone/email (global), links Privacy · Terms, © 2026 Atlas Language Studio.

## SEO
Page title: "Atlas Language Studio – language courses in Agadir". Meta description: "English, French and Arabic courses for children and adults in Agadir. Small groups, certified teachers, free level test."

## Arabic version (added later in tasks.md – do NOT build now)
The same page in Arabic, right-to-left, sharing the same global data.
