# Relativity Paper Handoff

Date: 2026-08-05

This memo is for continuing the relativity position paper work in Claude Code.

## Active Files

- Main LaTeX file: `relativity/latex/main.tex`
- Compiled PDF: `relativity/latex/main.pdf`
- Markdown outline/draft: `relativity/rediscovering-relativity.md`

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

Only commit the files relevant to the current task. There are unrelated local changes in the repository, including Chinese article files and a deleted diagram asset. Do not stage or revert them unless explicitly instructed.

Before committing LaTeX changes, compile with:

```bash
cd relativity/latex
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Then clean temporary files:

```bash
rm -f relativity/latex/main.aux relativity/latex/main.log relativity/latex/main.out relativity/latex/main.synctex.gz 'relativity/latex/main.synctex(busy)' relativity/latex/main.blg
```

Commit only the intended files, usually:

```bash
git add relativity/latex/main.tex relativity/latex/main.pdf
git commit -m "<message>"
git push
```

For this memo commit, only `relativity/HANDOFF.md` should be staged.
