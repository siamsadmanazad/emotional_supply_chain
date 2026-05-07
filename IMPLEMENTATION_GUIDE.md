# Implementation Playbook — Making "Emotional Supply Chains" an Interactive, Cinematic Repo

**Goal:** Take the static paper and turn it into a GitHub repository that *feels* like a piece of art — half academic, half installation. Visitors should land on the README and want to scroll. Power users should be able to tweak $\gamma$, $m$, $K$, $\beta$ and watch the pyramid breathe.

This playbook is **prompts and steps, not code**. Each numbered step is something you (or an AI assistant) can act on. Stack them in order. Skip nothing in Phase 0 — the foundation is what makes the rest feel intentional rather than thrown together.

---

## Phase 0 — Identity, Tone, and Repo Skeleton

The aesthetic decisions made here propagate through every later phase. Don't rush this.

**Step 0.1 — Define the visual language.**
Prompt yourself (or your design tool): *"Give me a moodboard for a satirical academic paper that sits at the intersection of network theory, economics, and 2010s indie web art. Reference: Edward Tufte's books, the Are.na homepage, mid-century operations-research diagrams, and the closing credits of a Wes Anderson film. Output: 5 hex colors, 2 fonts (one serif for body, one mono for code/math), and a one-sentence design thesis."*
Lock the palette and fonts in a `STYLE.md` before writing any code.

**Step 0.2 — Pick the central metaphor for motion.**
Pick **one** dominant motion idea and use it everywhere: a *pulse traveling up the tree*, *fluid filling a vessel*, or *currency stacking at the apex*. Don't mix metaphors — that's what makes things look cluttered. Recommended: the validation pulse, because it doubles as the model's actual mechanism (capital flowing tier-to-tier).

**Step 0.3 — Lay out the repo.**
Create top-level folders: `paper/` (the original PDF + LaTeX source if you have it), `assets/` (SVG, GIF, palette swatches), `simulator/` (the interactive app), `docs/` (anything that becomes a GitHub Pages page), `notebooks/` (a single Jupyter notebook for the formal derivation, rendered to HTML for the docs site). Add a `LICENSE` (CC-BY for the paper, MIT for the code is a clean split).

**Step 0.4 — Decide the hook.**
Pick one of: (a) a slider that drives an exploding $W(S)$ chart in the README's hero GIF, (b) a hover-over arborescence diagram, or (c) a single big number — *"the Sink's leverage at γm=1.5 is 7.5×"* — that animates as the page loads. Pick *one*. The README should answer "what is this?" in under 4 seconds.

---

## Phase 1 — The README as a Front Door

The README is the front door. Treat it like a magazine spread, not a manifest.

**Step 1.1 — Hero block.**
Write a banner SVG (export from Figma) that sets the title in the chosen serif, with a faint pyramid-of-arrows watermark behind it. Below it, **one** sentence — the paper's thesis distilled. Below that, three Shields.io badges: a "Live Simulator" link badge, a paper-version badge (`v1.0`), and a "γ regime: exponential" badge that *visually* indicates whether the current default parameters put the system in the bounded vs. exponential regime. The third badge is the surprise — it's not just metadata, it's a tiny piece of the model on the page.

**Step 1.2 — Animated GIF or SVG hero.**
Render a 6–8 second loop of the validation pulse traveling up the arborescence, with the Sink visibly inflating. Export at 2× DPI. If GIF size becomes a problem, use an inline `<svg>` with CSS keyframe animations (GitHub's README sanitizer strips `<script>` but allows CSS animations inside SVG). This is the single asset most people will see.
*Prompt to generate it:* *"Animate a 3-tier directed arborescence with branching factor 3. Show small light-colored circles moving from base nodes upward along edges. Each time a pulse arrives at a node, the node fades brighter and a fraction of the pulse continues upward. The root node visibly grows in radius proportional to accumulated pulses. Loop seamlessly. Style: minimal, off-white background, single accent color from the palette in STYLE.md."*

**Step 1.3 — Three-section structure below the hero.**
Use this exact rhythm: (1) **The Claim** — 2 paragraphs of plain-English thesis, no math. (2) **The Math, on Demand** — the recurrence $C(u) = \beta_u + \gamma \sum C(w)$ shown openly, with the heavier derivations hidden inside `<details>` blocks so the page doesn't intimidate. (3) **Try It** — the call-to-action button to the live simulator, plus a one-paragraph guided experiment ("set γ=0.3, watch the pyramid collapse"). End with the worked example as a clean numeric table.

**Step 1.4 — Use `<details>` strategically.**
Hide every derivation step, every appendix, every table-of-symbols inside collapsible blocks with evocative summary text — not "Click to expand" but *"View the convergence proof,"* *"Inspect the deficit identity,"* *"See the variable glossary."* The whole page should read like a beautifully condensed essay until someone pokes it.

**Step 1.5 — End with a kicker.**
Last line of the README is a callback to the paper's punchline: *"The only mathematically sound strategy is to be the founder, or to refuse to recruit."* In italics, no link, no emoji, no follow-up. Let it land.

---

## Phase 2 — The Interactive Simulator

This is where the work earns its claim of being "interactive." Build it as a small **Streamlit** app, hosted on Streamlit Community Cloud, linked from the README.

**Step 2.1 — Define the simulator's job.**
The app must let the user manipulate four sliders: $\gamma \in [0,1]$, $m \in \{1..6\}$, $K \in \{1..8\}$, $\beta$ (free positive). It must show, simultaneously: (a) the live arborescence diagram with node radii proportional to $C(u)$, (b) the closed-form $W(S)$ as a single large number with a leverage ratio next to it, (c) a $W(S)$-vs-$K$ chart with the user's current $K$ highlighted, and (d) a "regime indicator" that switches between "Bounded ($\gamma m < 1$)," "Linear ($\gamma m = 1$)," and "Exponential ($\gamma m > 1$)" with matching colors.

**Step 2.2 — Make the regime switch the centerpiece.**
The most surprising thing about this model is the $\gamma m = 1$ phase boundary. The simulator should make crossing that threshold *feel* like something — color shift on the chart, a subtle pulse on the regime indicator, the Sink node visibly stops growing. Tell whoever is implementing this: *"When the user crosses γm = 1, every visual element on the page should acknowledge it within 200ms, even if subtly."*

**Step 2.3 — Add the 'Drainage' panel.**
Below the main chart, show how much each tier *retains* vs. how much it *passes upward*. This is where the deficit identity $D(u) = \beta_u$ becomes legible — every middle tier shows the same deficit regardless of where it sits. Label it explicitly: "Per-capita deficit: β units, identical at every tier (the model's central inequality)."

**Step 2.4 — Add a Reset to Worked Example button.**
$\beta=10, m=3, \gamma=0.5, K=3$ → $W(S)=75$. One click brings the visitor back to the canonical state shown in the paper. This is the "home" of the simulator.

**Step 2.5 — Optional: add a 'Generative Audio' toggle.**
A single sine-wave hum whose pitch tracks $\log W(S)$. When the user pushes $\gamma$ past the regime boundary, the pitch starts climbing audibly. This is the kind of detail that turns "neat" into "I'm sending this to my friends." Make it off by default with a clearly labeled toggle.

**Step 2.6 — Deploy.**
Push to Streamlit Cloud, enable the public link, then add the URL to the "Live Simulator" badge in the README. Test on mobile — Streamlit's layout breaks on narrow screens unless you wrap the columns in conditional logic.

---

## Phase 3 — The "Friendzone Map" (Optional but the Aesthetic Climax)

A separate, GitHub-Pages-hosted page using **D3.js** or **Cytoscape.js**. This is the page you link to from a "Visualize the network" call-to-action below the simulator.

**Step 3.1 — Generate a procedural pyramid.**
Build a single-page HTML at `docs/map/index.html`. On load, render a 4-tier symmetric arborescence using your D3 library of choice. Use force-directed layout with strong tier-locking constraints so it always looks like a pyramid, never a hairball.

**Step 3.2 — Make every node clickable.**
Clicking a base-tier node fires a "validation packet" — a small dot — that travels along the edge to its parent, then (with probability $\gamma$) onward, recursively. The Sink visibly accumulates. Add a small counter at the top: "Total ego accumulated at the Sink: 47 units."

**Step 3.3 — Add a 'Drain' button.**
A "Reset" / "Drain" button in the corner that empties the Sink with a satisfying animation — pulses cascading back down and dissipating off the bottom of the screen. This is the cathartic counterpart to the upward funnel.

**Step 3.4 — Style it like the rest of the repo.**
Same palette, same typography, same single-accent-color rule as Phase 0. The map should feel like a continuation of the README, not a separate project.

**Step 3.5 — Record a 4-second loop of someone using it. That becomes the GIF in the README's "Visualize the Network" section.**

---

## Phase 4 — The Notebook (Credibility Layer)

A single Jupyter notebook at `notebooks/derivation.ipynb`, rendered to HTML at `docs/derivation.html`.

**Step 4.1 — Walk the recurrence to closed form.**
Plain-text and LaTeX cells, alternating. Show the unrolling step-by-step, then the geometric-series collapse. End by reproducing the worked-example numerics from the recurrence and from the closed form, side by side, with both equal to 75.

**Step 4.2 — Empirical phase-diagram cell.**
A heatmap of $W(S)$ over $(\gamma, m)$ at fixed $K=5$, with the $\gamma m = 1$ contour drawn explicitly. This single image is one of the strongest visual artifacts you can produce — print-quality, suitable as a paper figure.

**Step 4.3 — Sensitivity analysis.**
Three small charts: $W(S)$ vs. $K$ at fixed $\gamma m$, $W(S)$ vs. $\gamma$ at fixed $m, K$, $W(S)$ vs. $m$ at fixed $\gamma, K$. Each gets one sentence of caption. The point isn't quantity — it's that an interested reader can see the model behave under perturbation.

**Step 4.4 — Render to HTML and link from the README under "Formal derivation."**

---

## Phase 5 — Polish & Ship

**Step 5.1 — Add a `CITATION.cff` file.**
This makes GitHub show a "Cite this repository" button on the right rail. Tiny detail, enormous credibility.

**Step 5.2 — Pin the repo on your profile.**
Do this once everything else is shipped. The pinned card uses your hero image automatically.

**Step 5.3 — Write a single-paragraph release note.**
Tag `v1.0`. The release description is two sentences: what this is, and the live simulator URL. Nothing else. Restraint is the aesthetic.

**Step 5.4 — Quietly seed it.**
Post once, in one place, with a single screenshot. Don't oversell it. The repo's polish does the talking.

---

## Phase 6 — Optional Mood-Setters (Pick Two, Not Five)

These are the final 5% — nice if you have time, distracting if you do them all.

- **Dynamic Shields.io badge** that recomputes the leverage ratio from a tiny serverless function and displays it as a badge in the README. Updates every time someone visits.
- **An ASCII-art sigil at the top of the README** (a tiny pyramid built from `▲` and `△`). Looks like decorative noise; rewards the careful reader.
- **A `git tag`-driven changelog** styled as a research-journal version history ("v1.1 — Reformulated the closed form to remove the K vs K-1 ambiguity").
- **A 404 page on the GitHub Pages site** that says, in the chosen serif: *"The validation you are looking for has been forwarded upstream."*
- **An RSS feed for the docs site.** Nobody will subscribe. That's the point.

---

## A Note on Restraint

The mistake most "flashy" research repos make is doing seven things at half-effort. This playbook produces one thing — *a clean, intentional, slightly haunting research artifact* — at full effort. Cut anything that doesn't reinforce the central metaphor. If you're not sure whether to include a feature, ask: *does this make the validation pulse feel more real, or less?*

If less, kill it.
