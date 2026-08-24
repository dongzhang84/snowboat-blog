# Relativity Paper Handoff

Date: 2026-08-05 (updated 2026-08-24)

This memo is for continuing the relativity position paper work in Claude Code.

## Status (2026-08-24)

Submitted to PhilSci-Archive on 2026-08-23 as item 30800 and returned to the
author's workspace on 2026-08-24. The return is about author eligibility under
the archive's new moderation policy, not about the content of the paper. See
`## Submission: PhilSci-Archive` below.

The paper is complete. Every section is written prose; no placeholder outlines
remain. The last compile gives 14 pages: body through page 8, references from
page 8, appendices from page 11.

Structure: Introduction, 2 The Historical Theory Space (2.1 to 2.4), 3 Other
Framings of Rediscovery (Whig, one-shot, single-mechanism), 4 Rediscovery Is Not
One Task, 5 Three Levels of Physics Intelligence (Lorentz, Poincare, gravity
tests), 6 Conclusion. Appendix A timeline, Appendix B mass-energy equivalence in
a Lorentz-Poincare framework, Appendix C AI for mathematics vs AI for physics.

## Locked Conventions

Decisions reached after long discussion. Do not reopen without a reason.

- The scale is called **physics intelligence**, not scientific intelligence. The
  evidence is a single physics case, and the wider term overclaims. `scientific`
  is reserved for describing the outside debate.
- **`principle` stays singular.** It names one object, the relativity principle.
  Section 3.1's *two postulates* is a description of the standard account and is
  correctly plural. Write that patches are *replaced by* a principle, never that
  they *follow from* one, since the transformations also need the light
  postulate. Section 5.2 carries a guard sentence beginning `Counting axioms is
  not the measure here.`
- **`aether`, not `ether`**, throughout.
- **`AI system` at the first mention in a paragraph, `the system` afterwards.**
  Do not touch the physics senses: `closed system`, `matter systems`,
  `semi-axiomatic system`, and the Appendix B mechanics.
- **Block quotations use the custom `quoteblock` environment, never `quote`.**
  Reason: `icml2026.sty` redefines `\@listi` to set only `\leftmargin`, so any
  list inherits the global `\topsep`/`\parsep` on top of this style's
  `\parskip 6pt` and the gaps are large. The same bug is why the introduction's
  itemize passes its spacing through `enumitem` options rather than `\setlength`
  calls placed after `\begin{itemize}`, which are read too late and do nothing.
- Quotations from Poincare and Einstein are the standard English translations
  (Halsted; Perrett and Jeffery). Both bib entries carry a `note` field naming
  the translation. A displayed quotation must be verbatim, so a paraphrase may
  only appear inline.

## Timeline (Appendix A) Editing Rules

The timeline records **events and measurements, not who changed their mind**.
Entries about people abandoning or adopting theories were removed for this
reason. The one survivor is 1922 Abraham, kept deliberately because it names the
rival theory he held.

Entries cite **period primary sources only**. Secondary literature belongs in the
body, where judgements about significance are made. This is why the Mie entry
cites `mie1913` rather than the Smeenk and Martin survey, which stays in
Section 2.4.

Two rejected additions, with reasons: Schwarzschild's exact solution was
initially proposed on the ground that the classical-test numbers come from it,
which is wrong, Einstein obtained both by approximation weeks earlier; it was
added later on its own merits. Black holes and cosmology stay out, since the
timeline traces how this dispute was adjudicated, not what general relativity
went on to produce.

## Open Items

Reviewed and deliberately left alone by the author on 2026-08-23: a set of small
English fixes (a reversed clause in Section 5, a comma splice in the Section 5
preamble, a fragment and a tense mismatch in Section 2.4, `Observation separated
them` in Section 2.4, and `kill` in the conclusion where Appendix C now says
`falsify`), and the two Table 1 items below. They are recorded here so they are
not rediscovered as new.

1. Table 1 row 7 lists `problem recognition` under `yes (the gravity test)`,
   but Section 5.3 hands the problem to the system rather than testing whether
   it can pose it.
2. Table 1 uses `the Lorentz test I` and `the Lorentz test II`. Section 5 has
   one Lorentz test covering tasks 2 and 4.
3. `main.tex` still contains commented-out draft paragraphs. They do not reach
   the deposit, since PhilSci-Archive takes the PDF.
4. The `Position:` title line for the ICML position-paper track is present but
   commented out. It is not needed for PhilSci-Archive.

Closed since the last update: Appendix A now has a cross-reference from the body
at the end of Section 4; the quantum paragraph in Section 2.3 became a footnote;
the keywords were changed to `AI for Science, LLMs, scientific discovery,
physics intelligence, relativity`.

## Submission: PhilSci-Archive

Submitted 2026-08-23, returned to the workspace 2026-08-24. Item URI (not
public while it sits in the workspace):
https://philsci-archive.pitt.edu/id/eprint/30800

The moderators wrote that only four kinds of author may deposit: current and
former faculty at institutions of higher education and research; current and
recent postdocs and graduate students; authors with existing items in
PhilSci-Archive; and authors formally endorsed by an author who already has work
there. They could not verify that the account belongs to any of them, and the
remedy they name is to add an academic email address to the profile and the
submission and resubmit, to write to them if the decision is an error, or to
seek an endorsement.

The profile is the likely cause. It carries a gmail address and leaves
Department, Organisation, Country, Homepage URL, and ORCID blank, so there was
nothing to verify against. Fill those in before any resubmission.

- PhilSci-Archive is the preprint archive of the Philosophy of Science
  Association, hosted by the University of Pittsburgh. Not arXiv.
- Deposit format is PDF, so the ICML two-column layout went as it is.
- Keywords and the subject classification are entered in the archive's own form,
  not read from the file.
- The submitted file is
  `latex/rediscovering-relativity-is-not-a-single-task.pdf`. The LaTeX job is
  still called `main`, so a compile writes `main.pdf` and the output has to be
  renamed before it is committed. `.gitignore` tracks only the deposit filename.
- The account record is in `private/philsci-archive-account.md`, which is not
  pushed.

## Active Files

- Main LaTeX file: `relativity/latex/main.tex` (local only, not on GitHub)
- Compiled PDF: `relativity/latex/main.pdf` (the only file in `latex/` that is pushed)
- Markdown outline/draft: `relativity/rediscovering-relativity.md`

**The LaTeX source lives only on this machine.** As of 2026-08-11 the repo tracks
`relativity/latex/main.pdf` and nothing else in that folder. `.gitignore` has:

```gitignore
relativity/latex/*
!relativity/latex/main.pdf
```

`main.tex`, `refs.bib`, `main.bbl`, `example_paper.tex`, `icml2026.sty` and
`icml2026.bst` are still on disk but were removed from the repo with
`git rm --cached`. A fresh clone will not contain them, so back the sources up
somewhere else if this machine is ever replaced.

The preprint date is not hardcoded. Line 22 uses `\today`, so every recompile
stamps the PDF with the current date.

The current writing work is focused on Section 2 of `main.tex`, especially the historical theory space around special relativity.

## Current Direction

The paper's central claim is that rediscovering relativity is not one task. It requires reconstructing a historical theory space, not just producing Einstein's final answer.

For Section 2, the author wants plain, direct English. Avoid ornate academic phrasing and avoid expanding short historical points into long textbook explanations.

Use `aether`, not `ether`, throughout the paper.

## Section 2.1 Status

Subsection title:

```tex
\subsection{19th-Century Situations}
```

Current logic:

- Newtonian mechanics and universal gravitation were highly successful in 19th-century astronomy.
- Neptune is used as the example of Newtonian success.
- Mercury's perihelion anomaly was a real problem, but it did not force new physics at the time.
- Old-model patches such as Vulcan, solar oblateness, and Hall's modification of the inverse-square law were plausible enough that Newtonian gravity remained the natural first move.
- Maxwell's equations created a different problem: electrodynamics was not covariant under Galilean transformations, which made the aether look like a natural rest frame.
- Michelson-Morley gave a null result.

Do not make Mercury sound like it directly produced general relativity. The intended point is the opposite: Mercury alone did not force Einstein.

## Section 2.2 Status

Subsection title:

```tex
\subsection{Special Relativity: Lorentz, Poincaré, Einstein}
```

Current structure:

1. Lorentz
2. Poincaré
3. Einstein

Lorentz paragraph:

- Lorentz's theory lived inside the aether framework.
- It was not only length contraction. His 1895 theory also used local time.
- Do not insert the local-time formula. The author explicitly rejected adding the formula because it makes the paragraph too long and distracts from the point.
- Better wording if needed:

```tex
His 1895 theory already combined length contraction with local time to explain why the Michelson--Morley experiment did not detect aether drift.
```

- Later Rayleigh, Brace, Morley-Miller, and Trouton-Noble pressed on consequences of the same aether/Lorentz framework.
- Lorentz updated the theory with a more elaborate electron model and stabilising assumptions, but did not abandon the aether.

Poincaré paragraph:

- Poincaré is presented as moving from Lorentz's complicated patchwork to a simpler principle.
- The principle is `the principle of relativity`.
- Current text says Poincaré did this in 1904. Earlier versions had 1905. If changing this, verify the intended historical reference before editing. Poincaré's 1904 St. Louis address states the principle; his 1905/1906 work develops the electron dynamics and Lorentz group structure.
- Poincaré still accepted the aether framework.
- He treated the time and length measured in other frames as artificial/apparent quantities.
- Current key sentence:

```tex
Physically, Poincaré still accepted the aether framework and treated the time and length measured in other frames as artificial quantities.
```

Einstein paragraph:

- Einstein removed the privilege of the aether and the absolute frame.
- His 1905 work starts from the relativity principle and constancy of light speed, without referring to a hidden rest frame.
- `t'` is not a calculational fiction; it is the real measurable time of the moving frame.
- Avoid saying the three theories are mathematically equivalent. That is too strong.
- Current safer final sentence:

```tex
For the experiments at issue, Lorentz's, Poincaré's, and Einstein's theories gave the same observable results, even though they rested on different physical pictures.
```

## Section 2.3 Status

Subsection title:

```tex
\subsection{Theory and Experiment as Mutually Generative}
```

This section has been rewritten from outline bullets into prose.

Current logic:

- From 1887 to 1902, there was no comparable new aether-drift experiment.
- Lorentz's 1895 theory was good enough for the main Michelson-Morley problem.
- The 1902-1904 experiments were not just more searches for aether wind.
- Rayleigh and Brace tested whether FitzGerald-Lorentz contraction should produce double refraction in moving matter.
- Morley and Miller tested whether the effect depended on the material construction of the interferometer.
- Trouton-Noble tested whether a charged capacitor moving through the aether should feel a torque.
- These experiments were new questions created by the theory itself.
- Their null results pushed Lorentz from contraction alone toward the full Lorentz transformation and a more complicated electron theory.
- After that, no new decisive experiment arrived. Poincaré and Einstein rebuilt the same experimental situation in cleaner ways, but were not selected by a new observation.

Keep this section concise. It should illustrate theory-experiment interaction, not become a full history of special relativity.

## Important Style Notes

- Use daily English where possible.
- Avoid meta-discussion from chat in the paper body.
- Do not paste explanatory replies to the author into the article.
- Prefer short paragraphs.
- Avoid saying "mathematically equivalent" for Lorentz/Poincaré/Einstein unless carefully qualified.
- Be careful with Poincaré dates: 1904 vs 1905/1906 depends on which contribution is being named.
- Do not add the Lorentz local-time formula unless the author explicitly asks again.

## Git Notes

The user expects every modification to be committed and pushed.

**Every edit to `main.tex` must be followed by a recompile and a push of the
resulting PDF.** Do not batch several edits and push once at the end, and do not
ask whether to push. The cycle is: edit `main.tex`, recompile, `git add
relativity/latex/main.pdf`, commit, push. Since the source is not tracked, the
PDF is the only record of the change that reaches GitHub, so an unpushed PDF
means the work is invisible.

Only commit the files relevant to the current task. There are unrelated local changes in the repository, including Chinese article files and a deleted diagram asset. Do not stage or revert them unless explicitly instructed.

Compile with:

```bash
cd relativity/latex
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Two passes are needed for references and the table of contents.

Temporary files (`main.aux`, `main.log`, `main.out`, `main.synctex.gz`) no
longer need to be deleted by hand. They are covered by the `.gitignore` rule
above and will never be staged.

Commit only the PDF:

```bash
git add relativity/latex/main.pdf
git commit -m "<message>"
git push
```

`main.tex` cannot be staged now, `git add` on it is a silent no-op because of
the ignore rule. That is intended.

For this memo commit, only `relativity/HANDOFF.md` should be staged.
