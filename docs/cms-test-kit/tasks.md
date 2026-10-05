# The 8 tasks (after the first build) – one prompt each, same wording for every CMS

Give each prompt to the same agent session. Record for each: success (yes/partial/no), interventions, minutes, notes.

1. **Change a global value everywhere**
   "The monthly price is now 950 MAD. Update it once so that every place showing it changes. Show me where it changed."
   ✔ Pass: both places show 950 MAD and only ONE data value was edited.

2. **Add a new section from a description**
   "Add a 'Testimonials' section before the FAQ with three short quotes (make them clearly marked as SAMPLE text),
   reusing existing components and styles."
   ✔ Pass: native components reused, styling consistent, marked as sample.

3. **Arabic version, right-to-left**
   "Add an Arabic version of this page. Translate the visible texts into Modern Standard Arabic, keep the same global data,
   make the whole page right-to-left with an Arabic font, and make the EN | ع switch link the two versions."
   ✔ Pass: dir=rtl on the page, layout mirrored, Arabic font, language switch works both ways, hreflang/lang correct.

4. **Image**
   "Replace the hero image with a different free stock photo of students, with a meaningful alt text in each language."
   ✔ Pass: image replaced in the CMS media library, alt text set per language.

5. **Fix a broken link**
   "One of the buttons points to a wrong anchor. Find and fix any broken internal link on the page."
   (Before giving this task, break one link yourself in the CMS, e.g. the 'See prices' button → #pricess.)
   ✔ Pass: the agent finds and fixes it using the CMS's tools.

6. **Rollback**
   "Undo your last two changes (the image and the link fix) and show me the restored state. Then redo them."
   ✔ Pass: native revision history used; state restored exactly; then re-applied.

7. **Publish / export**
   "Publish the site (or export it as static files) so it can be hosted outside the CMS. Tell me where the output is."
   ✔ Pass: static output opens in a browser without the CMS running; both languages present.

8. **Self-check report**
   "Audit the page: accessibility, mobile layout, speed and SEO. Fix what you can and list what remains."
   ✔ Pass: the agent uses CMS tools (or Lighthouse) and fixes issues; remaining items listed honestly.

## Human test (you, not the agent)
In the CMS's visual editor, as a non-technical editor: change the hero subtitle, change the price, replace an image.
Score 0–3 for ease (3 = obvious, no help needed) and note anything confusing.
