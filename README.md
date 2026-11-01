# Open-Book Exam Notes Skill

A Codex skill for turning mixed course materials into compact, exam-ready Word notes.

It is designed for workflows such as:

- continuing Day-by-Day revision notes in an established style;
- prioritising sample-exam questions and marking cues;
- extracting evidence from PDF, PPTX, DOCX, XLSX/CSV, and Orange `.ows` files;
- preserving English technical terms with concise Chinese explanations;
- producing a searchable `.docx` with exam maps, formulas, software steps, worked results, answer templates, and common mistakes;
- rendering and checking every page before delivery.

## Install

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/Kristen-hehe/open-book-exam-notes-skill.git ~/.codex/skills/open-book-exam-notes
```

Restart Codex if the skill does not appear immediately.

## Use

Invoke it explicitly:

```text
Use $open-book-exam-notes to turn this course folder and sample exam into a compact open-book exam guide. Match the attached reference note.
```

The skill can also be selected automatically for requests such as “整理 Day 3 复习资料” or “优先按样卷整理开卷考试 note.”

## Repository contents

- `SKILL.md`: invocation rules and core workflow
- `references/source-processing.md`: format-specific evidence extraction
- `references/docx-design-and-qa.md`: Word layout and verification rules
- `scripts/inventory_sources.py`: read-only source manifest generator

No course materials, student submissions, or private datasets are included.

## License

MIT
