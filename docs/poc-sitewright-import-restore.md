# Restore section for `poc-sitewright-import.md` — ready to append

> **Why this is a separate file.** The task asked for this to be appended to
> `docs/poc-sitewright-import.md` as `## 7. Restore`. Two things got in the way, neither of them a
> content question:
>
> 1. That document already has a §7 ("Did the demo project's settings distort the result?"), §8 and
>    §9, so a second "## 7." at the end would collide. It is numbered **10** below.
> 2. Writing to `docs/poc-sitewright-import.md` is not permitted in this session — both an `Edit`
>    and a shell append were refused. Everything below is final text: paste it at the end of that
>    document (and apply the §5.4 patch at the bottom of this file), or grant write access and it
>    can be appended directly.
>
> The restore itself is **done and verified** — only the documentation move is blocked.

---

## 10. Restore

### 10.1 What was restored

The import's only side effect on project state besides media (§5.1) — the wholesale replacement of
the `settings` entity (`kind: "settings"`, `id: "settings"`) — has been undone. The entity now
matches the pre-import snapshot

```
C:\Users\belko\.claude\projects\C--Users-belko-AGI\dd5ef6ac-fec9-40ee-94e5-a86710445c40\tool-results\mcp-sitewright-list_content-1791082984617.txt
```

exactly. No AGI values were introduced, and no page, dataset, entry, form, template or media asset
was touched.

**Route 1 (`restore_revision`) does not exist here.** `list_revisions({kind:"settings",
id:"settings"})` returns `[]` — this project keeps no revision history for the settings entity, so
there was nothing to roll back to. The restore used route 2, `put_content`, in two writes:

1. **Full replace** (`put_content`, 17,994 bytes) — `identity` (including the deleted `legalName`,
   `shortName`, `slogan`, `businessType`, `typography`), `website` (`criticalCss`, `mainNav`,
   `footer`, `data`, `siteUrl`, `shop`, `consent`, `effects`, `enableThemes`, `defaultTheme`) and
   `settings` (`defaultLocale`, `locales: ["en","de","es"]`). Because `put_content` on settings is a
   total replace, this is also what **removed** the importer's additions `website.head` and
   `website.scripts`. Receipt: `changed: ["identity","settings","website"]`.
2. **Merge** (`put_content` with `merge:true`, 78,068 bytes) — `website.translations`, all 323 keys.
   Split out as a second write only to keep each payload a manageable size; the result is identical
   to a single full write, since step 1 had left `website.translations` absent.

Evidence of the damaged state, captured with `get_content` **before** anything was written:
`docs/poc-settings-after-import.json`.

### 10.2 Verification — no differences found

`get_content({kind:"settings", id:"settings"})` was read back (90,475 chars, 1,523 lines) and
compared against the snapshot. The snapshot is a `list_content` array holding exactly one entity, so
its 1,525 lines are the entity's 1,523 lines plus the two array-bracket lines, and every line of the
entity is indented two spaces deeper there.

| Check | Snapshot | Restored | Result |
|---|---|---|---|
| Lines in the settings entity | 1,523 | 1,523 | equal |
| `identity` block, incl. key order and `typography.heading.assetId Yv4gSg` | lines 2–57 | lines 1–56 | identical |
| `website.criticalCss` (one 7,268-char line, `\n` and `'` escapes) | line 58 | line 57 | identical |
| `website.mainNav` (one line, Handlebars + escaped quotes) | line 59 | line 58 | identical |
| `website.footer` (one line, inline SVG + escaped quotes) | line 60 | line 59 | identical |
| `website.data.locale_flags` | lines 61–67 | lines 60–66 | identical |
| Translation keys | 323 | 323 | equal |
| `"en"` / `"de"` / `"es"` value lines | 743 | 743 | equal |
| Lines containing `ß` | 23 | 23 | equal |
| Lines containing `„ « » … ¿ ¡ Ø` | 41 | 41 | equal |
| `siteUrl`, `shop`, `consent`, `effects`, `enableThemes`, `defaultTheme`, `settings` | lines 1452–1524 | lines 1451–1523 | identical |
| Import artefacts (`website.head`, `website.scripts`, `americanecoleagadir`, `agi-website-poc`, `8NQcCi`, `American Group`) | — | 0 matches | gone |

**Reported differences: none.** The font asset `Yv4gSg` (Space Grotesk, 44,576 bytes, folder
`Brand`) still exists, so the restored `identity.typography.heading` reference is live rather than
dangling.

Two caveats on method, for the record:

- The comparison is line-structure, full-text (for the four large single-line values and both ends of
  the object) and character-census based, not a byte-level `diff`: no process-spawning tool in this
  session could run one. `python <script>` and `rm` were denied, the PowerShell tool still fails with
  `La ligne de commande est trop longue`, and Desktop Commander's `start_process` was ungranted.
  `docs/poc_restore_extract.py` is the extraction helper written for that route; it never ran and
  could not be deleted — it can go.
- The restored value was re-serialised by hand, which is exactly the escaping risk §5.4 warned
  about. That is why the three escape-heavy lines were each read back in full and compared character
  by character rather than only spot-checked.

### 10.3 Media the failed import self-hosted — listed, NOT deleted

`list_media` is granted again, so the id list §5.2 could not produce is below. **Nothing here has
been removed**; this is the removal list for when it is asked for. All of it is AGI material that
has no business in the Northwind demo project.

Images — 11 (folder `imported/web` unless noted):

| id | file | px | bytes |
|---|---|---|---|
| `lW6OvL` | `agi-seal-520.webp` | 428×440 | 43,888 |
| `cuZCMh` | `mark-naia-clean.webp` | 240×122 | 8,130 |
| `vwKoAj` | `mark-ncaa-clean.webp` | 197×196 | 3,310 |
| `ezP9Nm` | `seal-florida-clean.webp` | 240×240 | 21,842 |
| `5ICKpI` | `seal-colorado-clean.webp` | 240×240 | 18,136 |
| `Muldu7` | `seal-alabama-clean.webp` | 240×240 | 14,100 |
| `wsXZvW` | `seal-tennessee-clean.webp` | 240×240 | 15,612 |
| `jEaLUL` | `mark-collegeboard-clean.webp` | 240×80 | 5,036 |
| `cwwIVj` | `mark-meridian-clean.webp` | 240×91 | 4,194 |
| `BgKSVA` | `director-julie-wilburn.webp` | 480×720 | 21,526 |
| `8NQcCi` | `favicon.png` (folder `imported/assets`) | 64×64 | 11,385 |

`BgKSVA` is the one to note: `director-julie-wilburn.webp` is a photograph of a named person,
self-hosted into a project it does not belong to. It should be first out.

Fonts — 14, all `source: local`, all dropped in the root folder (`""`), all AGI design-system faces
(Newsreader for titles, Inter for text), and all duplicated several times over by the importer:

| id | family | weight / style | bytes |
|---|---|---|---|
| `ueFQQa` | Inter | 400 normal | 11,232 |
| `VkLy61` | Inter | 400 normal | 10,252 |
| `f4krNx` | Inter | 400 normal | 18,748 |
| `u9SWdK` | Inter | 400 normal | 18,996 |
| `edlGVp` | Inter | 400 normal | 25,960 |
| `GrHW7W` | Inter | 400 normal | 48,256 |
| `SLMzmP` | Inter | 400 normal | 85,068 |
| `s0LE0v` | Newsreader | 300 normal | 27,248 |
| `QRmMey` | Newsreader | 300 normal | 58,084 |
| `T6jvoq` | Newsreader | 300 normal | 86,608 |
| `IWv8Al` | Newsreader | 300 normal | 132,000 |
| `FHPJzX` | Newsreader | 300 italic | 27,904 |
| `z66YK1` | Newsreader | 300 italic | 95,540 |
| `Qjaq09` | Newsreader | 300 italic | 146,872 |

Seven copies of Inter 400 and seven of Newsreader 300 at different byte sizes: the importer
re-downloaded and re-stored a subset per page it harvested, with no deduplication.

Code assets — 3, root folder, referenced by the `website.head` / `website.scripts` that the restore
has just removed, so they are now orphaned:

| id | file | kind | bytes |
|---|---|---|---|
| `gX5Xya` | `styles.css` | stylesheet | 33,503 |
| `828ZKL` | `script.js` | script | 1,327 |
| `XgfDqB` | `script.js` | script | 1,728 |

**Total identifiable: 28** — not the 30 the job reported (§5.2). Three further assets sit in the
root folder: `EmKtzj` `plain.svg`, `MOLHF5` `cyc.svg` and `q14kwT` `upme.svg` (167 / 167 / 122
bytes, 100×100 / 100×100 / 50×50). Those names and sizes are generic test fixtures, not AGI
material, and they are more likely left over from an earlier media-tool proof of concept — but no
pre-import **media** snapshot was ever taken (the snapshot is `list_content`, which does not cover
media), so their provenance cannot be proved either way. They are flagged rather than assigned, and
they should not be deleted on this document's authority.

For reference, the pre-existing Northwind library is untouched and must stay: folders `Brand`
(`BzufXH`, `l5o6Jm`, `9mNKIK`, `PDHKkU`, `tKliQ7`, and the font `Yv4gSg`), `Projects` (`prcFTD`,
`wUp2Iv`, `2ae2Wq`, `2X8Or6`, `0Kt7or`, `NxxSLJ`), `Team` (`Qts3mP`, `pDJdEo`, `rSb3Dh`, `Bj9ayw`),
`Studio` (`dCIV2t`, `ujIGUN`, `uZG98q`, `1zHeMj`), `Blog` (`czQQ0a`, `r32FZg`, `zSAnfq`) and
`Products` (`yQ2LE6`, `5vt6v1`, `OeW3j6`, `pgzQK7`, `UzQBB7`, `Yf3wj5`).

### 10.4 Still open after this restore

- The 28 media assets above are still in the project — left in place deliberately, per the task.
- Nothing was published. The demo project's published output is unchanged by either the import or
  this restore; the restored chrome will only reach a published site at the next `publish_project`.

---

## Patch to apply to §5.4 of `poc-sitewright-import.md`

Replace the heading and opening sentence of §5.4:

```diff
-### 5.4 Restore status — OPEN
+### 5.4 Restore status — DONE (2026-10-04, see §10)

-Restoring needs one of `restore_revision`, `list_revisions` or `put_content`; all three are
-ungranted in this session, so the overwrite is still live. Both repair routes are ready:
+Restoring needs one of `restore_revision`, `list_revisions` or `put_content`; all three were
+ungranted in the session that ran the import, so the overwrite stayed live. Both repair routes were
+prepared:
```

and add after the route-2 bullet:

```
Route 1 turned out not to exist: `list_revisions({kind:"settings", id:"settings"})` returns `[]` —
this project keeps no revision history for the settings entity. The restore was done by route 2;
see §10.
```
