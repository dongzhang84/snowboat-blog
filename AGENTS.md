# AGENTS.md

## Project Purpose

This repository is a Chinese long-form writing project for deep analysis articles by snowboat84. Topics include AI and business, education, technology, space exploration, physics, math, and writing workflows. Published articles are Markdown files at the repository root, older articles live in `archive/`, drafts live in `drafts/`, and traffic reviews live in `analysis/`.

Codex should treat this as a content repository first. Preserve the author's voice, publication history, generated assets, and Claude Code workflow compatibility.

## Repository Layout

- `*.md` at the root: current articles and project docs.
- `archive/`: older published articles.
- `drafts/`: dated notes and rough article drafts.
- `analysis/`: traffic review reports and pending traffic notes.
- `cover-image/`: default scripted typography covers, usually `cover-image/{slug}/cover.png`.
- `cover-images/`: richer cover/image generations, prompt files, and alternate aspect ratios.
- `diagram/`: generated SVG/PNG diagrams with `plan.md`.
- `images/`: article-specific image assets.
- `infographic/`: infographic outputs.
- `scripts/`: local automation, including cover and SVG-to-PNG utilities.
- `.claude/skills/`: canonical Claude Code workflow instructions.

## Claude Skill Compatibility

The `.claude/skills/` directory is the source of truth for the existing Claude Code workflows. Codex may read these files and translate their rules into its own behavior, but must not edit, rename, move, or delete them unless the user explicitly asks.

Preserve the existing directory conventions so Claude Code can continue to work:

- Article writing outputs go to the repository root unless the user says otherwise.
- Traffic reviews go to `analysis/`.
- Default typography covers go to `cover-image/{slug}/cover.png`.
- Diagrams go to `diagram/{slug}/` with `plan.md` and `diagram.svg`; PNGs are generated separately.
- Infographics go to `infographic/{topic-slug}/`.

One disabled workflow exists at `.claude/skills/gen-100day-dual-post/SKILL.md.disabled`. Treat it as inactive unless the user explicitly asks to revive or use it.

## Required Reading By Task

Before writing or substantially editing an article, read:

- `.claude/skills/write-article/SKILL.md`
- `.claude/skills/write-article/persona.md`
- `.claude/skills/write-article/style.md`
- `.claude/skills/write-article/structure.md`
- `.claude/skills/write-article/writing-rules.md`
- `.claude/skills/write-article/output-format.md`

Before reviewing traffic potential or creating a traffic review, read:

- `.claude/skills/traffic-review/SKILL.md`
- `.claude/skills/traffic-review/framework.md`
- `.claude/skills/traffic-review/output-template.md`

Before making a default cover, read:

- `.claude/skills/baoyu-cover-image/SKILL.md`
- `.claude/skills/baoyu-cover-image/EXTEND.md`

For this repository, the default cover workflow is scripted typography. When the user says "做封面" or similar, infer the slug and two-line title if possible, then run:

```bash
python3 scripts/cover.py <slug> "第一行" "第二行"
```

Only use a different cover workflow if the user explicitly asks for another style, palette, size, or generation method.

Before creating or editing diagrams, read:

- `.claude/skills/baoyu-diagram/SKILL.md`
- The referenced design, template, layout, pitfall, and per-diagram-type files needed for the requested diagram.

Before creating an infographic, read:

- `.claude/skills/baoyu-infographic/SKILL.md`
- The referenced layout, style, base prompt, analysis, and structured-content files needed for the requested infographic.

Before creating article illustrations, read:

- `.claude/skills/baoyu-article-illustrator/SKILL.md`
- The referenced workflow, style, preset, and prompt-construction files needed for the requested image set.

## Writing Rules

Follow the Claude writing rules as hard project rules:

- Write primarily in Chinese. Keep key English product and technical terms when natural.
- Do not use Chinese double em dashes `——` in new Chinese prose. Use commas, periods, or rewritten sentences.
- Avoid obvious AI-style phrasing, especially high-frequency terms listed in `writing-rules.md`.
- Avoid the negative parallel pattern "不是 X，而是 Y" / "不是 X，是 Y" unless it is truly unavoidable.
- Use direct, opinionated, data-backed prose. Avoid empty balance, generic summaries, and inflated abstractions.
- Paragraphs should usually be 2 to 4 sentences and focused on one point.
- New long-form articles must include meaningful second-level subsections under main chapters, using the `## 1.1 ...`, `## 1.2 ...` format from `structure.md`. Do not leave articles with only top-level chapters like `# 一、...`, `# 二、...` unless the piece is intentionally very short and the user explicitly asks for that.
- Cases need names and data. Do not invent examples.
- For facts, dates, names, numbers, events, policies, and current claims, verify with web search before writing them into article prose.
- Preserve the user's original draft verbatim when it is included as an appendix.

New articles should follow the output format in `.claude/skills/write-article/output-format.md`, including:

1. `## 作者其它文章`
2. `## 本文参考文献`
3. `## 附录：原始草稿`

## Content Modification Rules

Before modifying article content, Codex should:

1. Identify the exact target file or files.
2. Read the applicable Claude skill instructions.
3. Check `git status` and avoid overwriting unrelated user changes.
4. Preserve existing article intent unless the user asks for a rewrite.
5. Avoid touching published articles, drafts, assets, scripts, or workflow files outside the requested scope.

Do not casually change:

- Published article Markdown files.
- Draft files in `drafts/`.
- `README.md` article metadata.
- `CLAUDE.md`.
- `.claude/skills/` files.
- Images, covers, diagrams, infographics, or generated assets.
- Scripts in `scripts/`.
- Local configuration files such as `.env.local` or `.claude/settings.local.json`.

If a task requires touching one of these areas, state the intended files first unless the user has already made the scope explicit.

## Traffic Review Rules

Traffic reviews should use `README.md` as the source of article metadata and X view counts. Read only the openings needed to judge the reader's first 10 seconds unless the user asks for deeper content analysis.

Use the framework in `.claude/skills/traffic-review/framework.md`: reader identity, diagnosis plus self-rescue, concrete numbers plus contrast, and emotional hook. Do not overfit one-off results. At least two examples are needed before treating a pattern as a positive rule.

Weekly plans, when requested after a review, should be appended to the same review file rather than created as a separate file.

## Asset And Script Rules

Do not edit generated image assets or scripts unless the user explicitly asks.

For SVG to PNG conversion, use:

```bash
python3 scripts/svg-to-png.py <svg> [-w 1600]
```

Do not use direct `rsvg-convert` for this repository's diagrams, because the SVG dark-mode CSS requires preprocessing.

When regenerating diagrams, covers, or infographics, preserve existing outputs by following the relevant skill's backup rules rather than silently overwriting prior work.

## Git And Secrets

Never print or expose secrets from `.env.local` or remote URLs. Do not add secrets to commits.

The repository may have user changes already present. Do not revert or discard changes unless the user explicitly asks. When committing user-provided work, include only files intended for the task and avoid unrelated local configuration.
