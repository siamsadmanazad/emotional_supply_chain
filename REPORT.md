# Emotional Supply Chains — Consolidated Report & Honest Review

**Source paper:** *Emotional Supply Chains: Why the Friendzone is Mathematically Identical to a Multi-Level Marketing Scheme*
**Author:** Farid Nahadi
**Date:** May 5, 2026
**Reviewer:** Claude (Opus 4.7)
**Review date:** 2026-05-08

---

## 1. Honest Assessment

This is a satirical paper that wears formalism well. It is funny, internally coherent, and the central reduction (unrequited affection ≅ multi-level pyramid) is sharp enough to do real explanatory work. That said, an honest read has to separate the **rhetoric** from the **mathematics**, because the paper conflates them in places.

### 1.1 What the paper genuinely gets right

- **The recursive definition of $C(u)$ is well-formed.** Treating validation as a fungible scalar lets the directed graph carry actual arithmetic, not just metaphor. The recursion $C(u) = \beta_u + \gamma \sum_{w \in N_{in}(u)} C(w)$ is unambiguous and computable.
- **The "Sink" is a legitimate term.** In graph theory a sink is a node with only inbound edges — that is exactly what a non-reciprocating love interest is in this model. Good vocabulary, not abuse of vocabulary.
- **The deficit identity $D(u) = \beta_u$ is the strongest single result.** Every non-Sink node nets out exactly their own baseline, regardless of branching factor or pass-through rate. This is genuinely elegant: it says the structural position of the middle tiers doesn't matter — they all run the same per-capita deficit. The pyramid concentrates value at the top *without changing the per-person experience in the middle*.
- **The MLM analogy is structurally apt at the mechanism level.** Both systems retain $(1-\gamma)$ at each layer and forward $\gamma m$ upstream. If $\gamma m > 1$, both produce exponential consolidation at the apex.

### 1.2 What I want to push back on

- **There is a notational error in the closed-form formula** (or an undocumented redefinition of $K$). See §3.
- **$\gamma m > 1$ is doing all the work.** The "exponential ego scaling" claim is *contingent on* $\gamma m > 1$. When $\gamma m \le 1$ the geometric series converges and $W(S)$ is bounded — i.e., the friendzone has a ceiling. The paper mentions the condition in one clause and then proceeds as if it were universal. It's actually the load-bearing assumption.
- **The closed-system assumption is heavy.** Real social networks have cycles, partial reciprocity, multi-target admirers (one person with several simultaneous crushes), and $\beta$ is heterogeneous. The arborescence is a clean fiction — fine for satire, weak for prediction.
- **"Mathematically identical to an MLM" is rhetorical, not formal.** MLMs are illegal because they combine **monetary recruitment** with **structural insolvency** (the recruit pool eventually saturates). The paper gestures at this analogy without proving the second condition. A friendzone has no fixed payout obligation, so "structurally impossible ROI" is a *narrative* claim dressed in mathematical clothing — the math shows concentration, not insolvency.
- **No exit dynamic.** Real participants eventually quit. With a constant $\gamma$ and infinite patience, the model overstates how long the supply chain holds together.

### 1.3 Bottom line
As a satirical formal model, it is well-constructed and the central insight (deficit = $\beta$ for everyone in the middle) is real. As a prescriptive claim ("the only sound strategy is to be the Sink or refuse to recruit"), it is bumper-sticker logic — true *within* the simplifying assumptions, not in the messy real graph.

---

## 2. Mathematical Verification

I re-derived the worked example from scratch to make sure the numerics are right.

**Parameters** (from the paper's worked example):
- Total tiers: 3 (Tier 0 = Sink, Tier 1 = Middlemen, Tier 2 = Base)
- Branching factor: $m = 3$
- Baseline energy: $\beta = 10$ validation units / week
- Pass-through rate: $\gamma = 0.5$

### 2.1 Recursive walk-up

| Tier | Population | Per-node investment $C$ | Computation |
|---|---|---|---|
| 2 (Base) | $m^2 = 9$ | $C(T_2) = \beta$ | $= 10$ |
| 1 (Middlemen) | $m = 3$ | $C(T_1) = \beta + \gamma \cdot m \cdot C(T_2)$ | $= 10 + 0.5 \cdot 3 \cdot 10 = 25$ |
| 0 (Sink) | $1$ | $W(S) = m \cdot C(T_1)$ | $= 3 \cdot 25 = \mathbf{75}$ |

Result: $W(S) = 75$ ✓ — matches the paper.

### 2.2 Independent derivation of the closed form

For a node at tier $k$ below the Sink, the recursion unrolls into a geometric series:

$$
C(T_k) = \beta \sum_{i=0}^{K-1-k} (\gamma m)^i = \beta \cdot \frac{(\gamma m)^{K-k} - 1}{\gamma m - 1}
$$

The Sink's wealth is the sum of its $m$ direct admirers (the Tier-1 cohort):

$$
W(S) = m \cdot C(T_1) = \beta \cdot m \cdot \frac{(\gamma m)^{K-1} - 1}{\gamma m - 1}
$$

**Plugging in** ($K = 3$, $m = 3$, $\gamma = 0.5$, $\beta = 10$):

$$
W(S) = 10 \cdot 3 \cdot \frac{(1.5)^{2} - 1}{1.5 - 1} = 30 \cdot \frac{1.25}{0.5} = 30 \cdot 2.5 = \mathbf{75} \;\checkmark
$$

The formula works **only with exponent $K-1$**, not $K$. With $K$ as written in the paper, the same parameters give $30 \cdot (3.375 - 1)/0.5 = 142.5$, which contradicts the paper's own worked example.

### 2.3 Leverage ratio
A single base-tier admirer expends $\beta = 10$ units. The Sink accumulates $W(S) = 75$ units. Leverage = $75/10 = \mathbf{7.5\times}$. Equivalently, the Sink extracts 75 units from a labor force of $9 + 3 = 12$ non-Sink participants, each of whom is in steady-state deficit $D(u) = \beta = 10$ — i.e., the *aggregate* unrequited effort is $12 \cdot 10 = 120$ units, of which 75 (62.5%) lands at the Sink and 45 (37.5%) is absorbed as middle-tier "self-esteem repair."

### 2.4 Convergence boundary (the part the paper soft-pedals)

The geometric series $\sum (\gamma m)^i$ has fundamentally different behavior depending on $\gamma m$:

| Regime | Behavior of $W(S)$ as $K \to \infty$ |
|---|---|
| $\gamma m < 1$ | Converges to $\beta m / (1 - \gamma m)$ — bounded ego, friendzone has a ceiling |
| $\gamma m = 1$ | Linear growth: $W(S) = \beta m (K-1)$ |
| $\gamma m > 1$ | Exponential growth — the paper's "Friendzone Asymptote" |

The paper's exponential narrative is a special case. With $\gamma = 0.5, m = 3$: $\gamma m = 1.5 > 1$, so we're in the exponential regime. With $\gamma = 0.3, m = 3$: $\gamma m = 0.9 < 1$, the Sink's ego is bounded above by $30 / 0.1 = 300$ units no matter how deep the pyramid runs. **This is the most important condition in the model and it deserves more emphasis than the paper gives it.**

---

## 3. Note on the $K$ Notation (Important)

The paper defines $K$ as "total tiers" with the Sink at Tier 0, so the worked example has $K = 3$ (Tiers 0, 1, 2). However, the closed-form formula as printed reads:

$$
W(S) = \beta \cdot m \left[ \frac{(\gamma m)^{K} - 1}{\gamma m - 1} \right] \quad \text{(as printed)}
$$

This is **inconsistent with the worked example**. To recover the example's value of 75, the exponent must be $K-1$:

$$
W(S) = \beta \cdot m \left[ \frac{(\gamma m)^{K-1} - 1}{\gamma m - 1} \right] \quad \text{(corrected)}
$$

Either the formula has a typo, or $K$ in the formula silently means "number of admirer tiers below the Sink" while $K$ in the example means "total tiers including the Sink." In this consolidated report I use the **corrected** form so the formula and the worked example agree.

---

## 4. Review of the User's Commentary

The user submitted a written reaction alongside the request. Honest review of it:

- ✅ **The user independently caught the $K$ vs $K-1$ issue.** Their note — *"I am using $K-1$ here because the series sum for $K$ tiers of admirers, excluding the sink, covers levels 1 to $K-1$"* — is mathematically correct, and it is in fact the single substantive error in the source paper.
- ✅ **The 7.5× leverage framing is right.** $W(S)/\beta = 75/10 = 7.5$, which captures the structural advantage cleanly.
- ✅ **The limitation they flag** ("real networks have bidirectional edges and cycles") is the same one I'd raise. The arborescence assumption is the model's biggest concession to satire.
- ➕ **One thing they could push harder on:** the model has no exit dynamic. Real participants give up; $\gamma$ is not a constant. Introducing a per-tier dropout probability $p$ would replace $(\gamma m)$ with $(\gamma m (1-p))$ in the recurrence and would substantially compress $W(S)$. The "structurally impossible ROI" claim is, in the real world, what causes people to *leave the system* — which the model doesn't represent at all.
- ➕ **Also worth naming:** the "MLM identity" is mechanistic, not legal. The paper conflates "structurally pyramid-shaped" with "structurally insolvent like an illegal MLM." Those are different claims; only the first is proven.

Net: the user's analysis is sharper than most reactions this paper would receive, and their correction to the formula is correct.

---

## 5. Full Report (verbatim, with formulas preserved)

> **Emotional Supply Chains: Why the Friendzone is Mathematically Identical to a Multi-Level Marketing Scheme**
> *Author: Farid Nahadi — May 5, 2026*

### Introduction

It is a universally acknowledged truth that the person you are currently ignoring is likely ignoring someone else to focus on you. In modern dating ecosystems, affection rarely flows in reciprocal, bidirectional pairs. Instead, it forms complex supply chains where emotional labor — such as validating outfits, listening to venting about read receipts, and analyzing ambiguous text messages — is extracted, repackaged, and passed upwards.

To make this precise, suppose that emotional validation is a fungible currency. When individual A harbors an unrequited crush on individual B, A freely transfers this currency to B. However, if B harbors an unrequited crush on C, B will often utilize the validation received from A to sustain the ego required to continue pursuing C.

This paper formalizes this dynamic. We argue that when these emotional supply chains converge on a highly desirable, emotionally unavailable individual, the network structure becomes indistinguishable from a pyramid scheme. The "uplines" reap the benefits of concentrated validation, while the "downlines" are left depleted, convinced that if they just invest a little more emotional capital, they will eventually see a return.

### The Mathematical Model

Let the social ecosystem be a directed graph $G = (V, E)$, where $V$ represents individuals and a directed edge $(u, v) \in E$ exists if $u$ is romantically invested in $v$. We assign a weight $C(u, v)$ to this edge representing the volume of emotional capital transferred per week.

In a pure unrequited pyramid structure, $G$ forms a directed tree (an arborescence) converging on a single root node $S$ (the "Sink"). We assign each node $u$ to a tier $k$, representing their path distance to $S$. The Sink is at Tier 0.

The total emotional capital $C(u)$ that a node $u$ at Tier $k$ invests into their crush at Tier $k-1$ is given by the recursive function:

$$
C(u) = \beta_u + \gamma \sum_{w \in N_{in}(u)} C(w)
$$

**Where:**
- $\beta_u$ is the baseline emotional energy generated autonomously by $u$.
- $N_{in}(u)$ is the set of $u$'s admirers (their "downline").
- $\gamma \in [0, 1]$ is the **emotional pass-through rate**: the fraction of incoming validation from admirers that $u$ successfully weaponizes to pursue their own crush.

The net emotional deficit $D(u)$ for any node $u \neq S$ is the difference between the effort they expend and the validation they retain:

$$
D(u) = C(u) - (1 - \gamma) \sum_{w \in N_{in}(u)} C(w) = \beta_u
$$

For the Sink node $S$, who pursues no one ($C(S) = 0$), the accumulated emotional wealth $W(S)$ is simply the sum of all incoming investments:

$$
W(S) = \sum_{v \in N_{in}(S)} C(v)
$$

In a perfectly symmetrical pyramid where every node has $m$ admirers (a branching factor of $m$), a uniform baseline energy $\beta$, and $K$ total tiers, the wealth accumulated by the Sink node $S$ from the entire structure is:

$$
W(S) = \beta \cdot m \left[ \frac{(\gamma m)^{K-1} - 1}{\gamma m - 1} \right]
$$

> ✎ **Erratum (corrected from v1):** the first version of this paper printed the exponent as $K$. With the convention that $K$ counts *total* tiers (including the Sink at Tier 0), the correct exponent is $K-1$, since the geometric series sums over the admirer tiers alone. The worked example below confirms the corrected form.

This geometric series proves that the Sink's ego scales exponentially with the depth of the friendzone structure beneath them, **contingent on the regime $\gamma m > 1$.** This boundary condition is doing real work and deserves explicit attention. The product $\gamma m$ — the pass-through rate times the branching factor — is the per-tier amplification of the supply chain. When $\gamma m > 1$, each layer adds *more* validation than it absorbs, so $W(S)$ grows exponentially in the pyramid's depth and the Sink's ego is, in principle, unbounded. When $\gamma m = 1$, growth is exactly linear in $K$. When $\gamma m < 1$, the series converges to a finite limit $W(S) \to \beta m / (1 - \gamma m)$ as $K \to \infty$ — the friendzone has a hard ceiling, and adding more tiers yields diminishing returns. The "Friendzone Asymptote" is therefore not a universal law but a **regime-dependent phenomenon**: it is an indictment of social ecosystems where individuals are both highly admired ($m$ large) and highly self-absorbed ($\gamma$ large). In ecosystems where either factor is small, the supply chain collapses under its own weight and the would-be Sink merely accumulates a polite quantity of unsolicited regard.

### Worked Example

Consider a 3-tier emotional pyramid where everyone has a baseline energy $\beta = 10$ "validation units" per week. Each person has exactly $m = 3$ admirers, and the pass-through rate is $\gamma = 0.5$ (meaning they use half the ego boost from their admirers to confidently flirt with their own crush).

- **Tier 2 (The Base):** 9 individuals. They have no admirers ($N_{in} = \emptyset$). They each invest their baseline energy into Tier 1. Output: $C_{T_2} = 10$.
- **Tier 1 (The Middlemen):** 3 individuals. Each receives $3 \times 10 = 30$ units from Tier 2. They absorb 15 units to repair their self-esteem and pass the rest upward. Their total output to Tier 0 is $C_{T_1} = 10 + 0.5(30) = 25$.
- **Tier 0 (The Sink):** 1 individual. They receive affection from the three Tier 1 middlemen. Accumulated wealth: $W(S) = 3 \times 25 = 75$.

Despite no one generating more than 10 units of baseline effort, the Sink receives 75 units of concentrated emotional labor. The Tier 1 middlemen feel sufficiently validated by Tier 2 to tolerate being left on "read" by the Sink. Meanwhile, the 9 individuals in Tier 2 are completely drained, receiving absolutely zero return on their investment. Thus, after just two degrees of separation, the system successfully extracts and consolidates affection at the top.

### Visualizing the Emotional Funnel

> *(Source PDF includes two figures: an arborescence diagram of the pyramid and a $W(S)$ vs $K$ plot showing exponential divergence from the flat $\beta$ line. Reproduced as ASCII for completeness:)*

```
                  [ S ]              Tier 0 (Sink)
                 /     \
              [T1]     [T1]          Tier 1 (Middlemen)
             /  |  \   /  |  \
           [T2][T2][T2][T2][T2]...   Tier 2 (Base)
```

The Sink's accumulated wealth $W(S)$ scales exponentially with tiers, while the baseline emotional investment $\beta$ remains stagnant. The "Reciprocity Gap" represents the structural impossibility of a return on investment for lower tiers.

The visualizations clarify the **"Friendzone Asymptote."** As the number of tiers $K$ increases, the validation concentrated in the Sink diverges significantly from the reality of the social ecosystem. This creates a "validation bubble" where the Sink's self-perception is subsidized by a labor force they do not even acknowledge, while individuals at Tier 2 and below are mathematically guaranteed to operate at a deficit.

### Conclusion

By modeling unrequited affection as a directed graph, we have demonstrated that linear crush dynamics are mathematically identical to illegal multi-level marketing operations. The "emotional pass-through rate" ensures that validation generated at the bottom of the social hierarchy is systematically funneled to a single, non-reciprocating individual at the top.

For the average participant in this emotional supply chain, the promised return on investment (a mutually fulfilling relationship) is structurally impossible, as the system relies on their continuous deficit to subsidize the delusions of the tier above them. Therefore, much like a financial pyramid scheme, the only mathematically sound strategy is to be the founder (the Sink) or to refuse to recruit.

---

## Appendix A — Variable Glossary

| Symbol | Meaning |
|---|---|
| $G = (V, E)$ | Directed social graph |
| $V$ | Set of individuals |
| $E$ | Set of directed romantic-investment edges |
| $(u, v) \in E$ | $u$ is invested in $v$ |
| $C(u, v)$ | Weekly emotional capital on edge $u \to v$ |
| $C(u)$ | Total capital $u$ invests upward |
| $S$ | The Sink (root of the arborescence) |
| $\beta_u$ | Baseline emotional energy of node $u$ |
| $\beta$ | Uniform baseline (symmetric case) |
| $\gamma \in [0,1]$ | Emotional pass-through rate |
| $N_{in}(u)$ | Admirers of $u$ ("downline") |
| $D(u)$ | Net emotional deficit of $u$ |
| $W(S)$ | Accumulated emotional wealth at the Sink |
| $m$ | Branching factor (admirers per node) |
| $K$ | Total tiers (Sink at Tier 0; admirers in Tiers 1…K−1) |

## Appendix B — Key Identities

$$
C(u) = \beta_u + \gamma \sum_{w \in N_{in}(u)} C(w)
$$

$$
D(u) = \beta_u \quad \text{for all } u \neq S
$$

$$
W(S) = \sum_{v \in N_{in}(S)} C(v) = \beta \cdot m \left[ \frac{(\gamma m)^{K-1} - 1}{\gamma m - 1} \right]
$$

Convergence regimes:
- $\gamma m < 1$: $W(S) \to \dfrac{\beta m}{1 - \gamma m}$ as $K \to \infty$ (bounded)
- $\gamma m = 1$: $W(S) = \beta m (K-1)$ (linear)
- $\gamma m > 1$: $W(S)$ grows exponentially in $K$ (the paper's "Friendzone Asymptote")
