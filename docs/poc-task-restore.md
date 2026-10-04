Use the agi-website skill.

TASK: Undo the side effect of the failed import in Sitewright project cSl4fD6lQjuc ("Example Project", Northwind demo).
The import_website attempt replaced the project's settings entity (kind "settings", id "settings").
A full PRE-IMPORT snapshot of the project content was saved by you earlier at:
  C:\Users\belko\.claude\projects\C--Users-belko-AGI\dd5ef6ac-fec9-40ee-94e5-a86710445c40\tool-results\mcp-sitewright-list_content-1791082984617.txt

Steps:
1. Read that snapshot file and extract the ORIGINAL settings entity (Northwind): identity (name, legalName, shortName, slogan,
   businessType, description, logo, icon, image, email, telephone, address, social, colors, typography), website (criticalCss,
   mainNav, footer, data, translations, and every other key), exactly as it was.
2. Read the CURRENT settings with get_content({kind:"settings", id:"settings"}) and save it to
   C:\Users\belko\AGI\docs\poc-settings-after-import.json (evidence, before changing anything).
3. Restore the original settings with put_content, byte-for-byte equal to the snapshot values. Do not add AGI values. Do not touch pages, datasets or media.
4. Read the settings back and compare every key with the snapshot. Report any difference.
5. Append a section "## 7. Restore" to C:\Users\belko\AGI\docs\poc-sitewright-import.md stating what was restored and the verification result,
   and list (do not delete) the media assets that the failed import self-hosted (list_media), so they can be removed later on request.
Print a short summary.
