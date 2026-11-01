# DOCX design and QA

## Information architecture

Use the smallest structure that supports fast lookup:

1. title and topic subtitle;
2. exam map;
3. concept/method sections in assessment order;
4. source-specific worked examples;
5. answer templates, common errors, and final checklist.

Do not force a fixed page count. Compactness matters, but legibility and complete exam-relevant reasoning come first.

## Visual system

- Follow a supplied reference note before applying defaults.
- Use one consistent heading hierarchy and stable table widths.
- Reserve colour for meaning: for example, blue for worked answers and red for warnings.
- Keep table headers visually distinct, repeat headers across pages, and prevent rows from splitting when possible.
- Use fonts with reliable Chinese and Latin coverage. Verify glyphs in the rendered pages.
- Include page numbers and a short running header when the document is long enough to benefit.

## Exam-writing patterns

For each major method, prefer a compact table with columns such as:

| Identify | Procedure/formula | Output to read | What to write | Warning |
|---|---|---|---|---|

For software workflows, include both the click/widget path and the analytical reason for each step.

For worked results, preserve the exact model, statistic, unit, validation method, and limitation. A number without its meaning is not an exam-ready answer.

## Final verification

Render the latest DOCX and inspect every page at readable zoom. Require:

- no blank spill pages;
- no clipped, overlapping, or missing text;
- no orphaned headings or table headers;
- no split rows that make a rule or worked result hard to read;
- correct page numbering and running header;
- consistent Chinese/English fonts and symbols;
- all sample-exam priorities and verified worked results present;
- no build notes, placeholders, source instructions, or citation tokens in the document.

Run structural/accessibility audits when available. Re-render after every layout-sensitive fix. Confirm reference and source files remain unchanged.
