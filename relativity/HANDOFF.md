# Relativity Paper Handoff

Date: 2026-08-05 (updated 2026-08-14)

This memo is for continuing the relativity position paper work in Claude Code.

## Where Work Stopped (2026-08-14)

The introduction is the active area. Done in this session:

- Paragraph 3 of the introduction now carries citations, all reusing keys
  already cited later in the paper, no new bib entries: `michelson1887` on the
  null result, `lorentz1895` on the contraction hypothesis, and
  `rayleigh1902,trouton1903,brace1904` as one group on the 1902-1904
  experiments. Maxwell is still uncited in both the introduction and Section 2,
  because `refs.bib` has no Maxwell entry.
- The introduction's three-question list had oversized gaps. Cause:
  `icml2026.sty` line 643 redefines `\@listi` to set only `\leftmargin`, so a
  list keeps the global `\topsep 4pt` / `\itemsep 2pt` / `\parsep 2pt` on top of
  this style's `\parskip 6pt`. The old `\setlength` calls placed after
  `\begin{itemize}` were dead, since `\list` had already read those values.
  Fixed by loading `enumitem` and passing the spacing as options:
  `\begin{itemize}[topsep=2pt, partopsep=0pt, parsep=0pt, itemsep=2pt,
  leftmargin=1.4em]`. The `\vspace{-0.45em}` that used to follow `\end{itemize}`
  was a workaround for the same problem and is gone. The narrower `leftmargin`
  also stopped the first bullet from hyphenating.
- Bullets 1 and 2 were rewritten to make the framework contrast explicit, which
  the old wording hid: bullet 1 is revision *inside* an existing framework
  (Lorentz), bullet 2 is leaving it (Poincare and Einstein). This matches the
  Level 1 and Level 2 rows of `tab:three-tests`.
- Section 5.2 gained a guard sentence at the end of its second paragraph,
  starting `Counting axioms is not the measure here.` It exists because 5.2
  says a set of patches is replaced by *a single statement*, and a reader who
  knows that special relativity rests on two postulates will read that as an
  error. The sentence says the second postulate carries over what Maxwell
  already asserted in the aether frame, so what is scored is the statement that
  has to be added, not the size of the final axiom set.

Resolved terminology decision: `principle` stays **singular** throughout. The
paper uses the singular in six places (lines 262, 288, 328 twice, 343, and the
Level 2 row of `tab:three-tests`), and it refers to one named object, the
relativity principle. Section 3.1's *two postulates* is a description of the
standard account and is correctly plural. The verb is what matters: writing that
patches are *replaced by* a principle is safe, writing that they *follow from*
one principle is not, since the transformations need the light postulate too.

Open items, for the next session:

1. Bullet 3 of the introduction list is still unrevised. The author stopped
   there. The paragraph that follows the list has since been rewritten as a
   staircase: step one moves inside a supplied framework, step two gives up the
   repairs and puts a principle in their place, step three lays out the theories
   the framework still permits and produces physics that was not among the
   inputs. Keep bullet 3 consistent with that third step when it is revised.
2. Principle formation happens twice in the history, the relativity principle at
   the special relativity stage and the equivalence principle at the gravity
   stage, but only the first is a test level. The gravity test explicitly
   withholds the equivalence principle. Consider one sentence in Section 5.2
   noting that Nordstrom's theory also required `m_i = m_g`, so the equivalence
   principle was a constraint shared by every candidate and therefore separates
   no system. Not yet decided by the author.
3. Section 5.2's withheld list says `Einstein's postulates`, but Maxwell's
   equations are supplied and Maxwell fixes `c`. What is actually withheld is
   not that light travels at `c`, but that it travels at `c` in every inertial
   frame. The quantifier should be made explicit.
4. The Discussion section list at `\section{Discussion and Conclusion}` is still
   a bare outline and still uses default list spacing. Give it the same
   `enumitem` options when it is written.

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
