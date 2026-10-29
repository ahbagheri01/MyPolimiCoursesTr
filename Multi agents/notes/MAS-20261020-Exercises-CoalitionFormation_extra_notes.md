# MAS-20261020-Exercises-CoalitionFormation — Additional Professor Notes

**Transcripts:** Francesco Amigoni's Personal Room-20261020 0753-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Multi agents\Slides and notes-20261005\03 MAS coalition formation.pdf

> **Coverage notes:** The characteristic functions were written on the blackboard and mostly not read aloud. The values given below were rebuilt from the inequalities and computations the professor did say aloud. Where a value could not be rebuilt for certain, this is stated. None of the five exercises below is in the slides. The slides' own examples (p.14-15, p.36, p.44, p.50) use different numbers.

## Session Overview: Payoff-Vector Exercises, Then Coalition-Structure Exercises

**Reference:** 03 MAS coalition formation.pdf, p.16, p.18

The session followed the two problems on p.16. **Payoff vector:** on three 3-agent games Amigoni asked, in this order: is the game superadditive, are given payoff vectors in the core, what is the whole core, what are the Shapley values, are they in the core, and what does that say about convexity. **Coalition structure:** on a non-superadditive 3-agent game he solved the problem with dynamic programming (DP) and then with Shehory-Kraus, and compared the two results.

## Exercise 1 — Superadditivity Check, and Writing the Outcome with the Grand Coalition

**Reference:** 03 MAS coalition formation.pdf, p.10, p.12

- Setup (rebuilt from the core inequalities he read aloud): v({1}) = 0, v({2}) = 1, v({3}) = 2, v({1,2}) = 1, v({1,3}) = 3, v({2,3}) = 3, v({1,2,3}) = 4.
- Superadditivity: the value of the merged coalition must be **not less than** the sum of the parts. His example: alone, agents 1 and 2 together get 0 + 1 = 1, and as {1,2} they also get 1. Equality is enough, so the game is superadditive.
- Consequence for the answer: since the game is superadditive, the grand coalition forms. When you write the outcome (CS, x), the coalition structure is the grand coalition {1,2,3}, and the only remaining question is the payoff vector.

## Exercise 1 — Checking Proposed Payoff Vectors Against the Core

**Reference:** 03 MAS coalition formation.pdf, p.10-11, p.20-21

With CS = {1,2,3}:
- **(1,2,1): not in the core.** Agent 3 would leave and stay alone, getting v({3}) = 2 instead of 1.
- **(0,3,2): not even an admissible payoff vector.** It distributes 5, but the grand coalition is paid only v(N) = 4: "we don't have five, we have only four".
- **(1,1,2): stable.** No agent and no subset of agents wants to deviate.
- **(0,2,2): not in the core.** Agents 1 and 3 get 2 together, but on their own as {1,3} they would get 3, so they leave the grand coalition.

## Finding the Whole Core: One Inequality per Coalition, Over Real Numbers

**Reference:** 03 MAS coalition formation.pdf, p.20

- To find **all** core payoff vectors, write x = (x1, x2, x3) and one constraint per coalition. For Exercise 1:
  - x1 ≥ 0, x2 ≥ 1, x3 ≥ 2
  - x1 + x2 ≥ 1, x1 + x3 ≥ 3, x2 + x3 ≥ 3
  - x1 + x2 + x3 = 4 (equality for the coalition that forms)
- Read each one as a reason not to leave. For example, x2 ≥ 1 holds "because otherwise agent 2 alone will leave".
- A student wrote the inequalities with integers. Amigoni stressed that the x_i are **real numbers**, not just integers.
- How to answer formally: the point-by-point answers above used intuition. A formal answer checks whether the vector satisfies **every** inequality of the system. For example, (0,2,2) breaks x1 + x3 ≥ 3.

## Computing a Shapley Value by Hand: The Permutation Table (Exercise 1, Agent 1)

**Reference:** 03 MAS coalition formation.pdf, p.26

- Procedure: (1) list all permutations of the agents. With 3 agents there are 3! = 6: 123, 132, 213, 231, 312, 321 (in general n!). (2) For each permutation, write the marginal contribution of the agent to the coalition of its predecessors. (3) Average over all permutations. This is "nothing more than the definition".
- For agent 1:
  - 123 and 132: v({1}) − v(∅) = 0, because agent 1 joins first.
  - 213: v({1,2}) − v({2}) = 0.
  - 231 and 321: v({1,2,3}) − v({2,3}) = 4 − 3 = 1.
  - 312: v({1,3}) − v({3}) = 3 − 2 = 1.
  - So φ1 = 3/6 = **1/2**.
- Repeated terms: 123 and 132 give the same marginal contribution (agent 1 is first in both), and so do 231 and 321 (agent 1 is last). They are still **different orderings**, and both must be counted in the average.
- With 3 agents, a given agent is first in two orderings and last in two. The transcript has him say "n − 1 times" in general. For n = 3 this matches (n−1)! = 2, which is the general count, so "factorial" may have been lost in the ASR (uncertain).

## Exercise 1 — φ2 by Table, φ3 by Efficiency, and the Shapley Vector in the Core

**Reference:** 03 MAS coalition formation.pdf, p.27, p.29-30

- φ2 = **1**. Students did this using the same six orderings. One student got a different value, and the professor said "you missed one somewhere". Agent 2's marginal contribution is 1 in every ordering.
- φ3: "Do not start with a long calculation. Try to reason." By **efficiency**, the Shapley values sum to v(N), so φ3 = 4 − 1/2 − 1 = **5/2**. The full formula would give the same value, which you can use as a check at home.
- Shapley payoff vector (1/2, 1, 5/2): checking all seven inequalities shows it is **in the core**.

## Shapley Vector in the Core Does NOT Prove the Game Is Convex

**Reference:** 03 MAS coalition formation.pdf, p.13, p.30

Question: the game is superadditive and its Shapley vector is in the core, so is it convex? Some students said yes. The correct answer is **"you don't know"**. The theorem on p.30 is a one-way implication: convex ⇒ Shapley vector in the core. In a non-convex game, the Shapley vector may or may not be in the core. So finding it in the core says nothing about convexity.

## Exercise 2 — Glove Game: Building v from a Story

**Reference:** None (not in slides)

- Story: agents 1 and 2 each own a **left** glove, and agent 3 owns the **right** glove. You only get value with at least one left glove and at least one right glove.
- Characteristic function: v = 0 for {1}, {2}, {3} and for {1,2} (two left gloves are useless). v({1,3}) = v({2,3}) = v({1,2,3}) = 10.
- He chose 10 but said any positive number works (1, 10, 100…). The game is superadditive, so the outcome uses the grand coalition.

## Glove Game Core: The Single Point (0, 0, 10), and Why

**Reference:** 03 MAS coalition formation.pdf, p.20-21

- System: x1, x2, x3 ≥ 0; x1 + x2 ≥ 0; x1 + x3 ≥ 10; x2 + x3 ≥ 10; x1 + x2 + x3 = 10.
- Reasoning (you can use math-course techniques or "just reason"):
  - Combine x1 + x3 ≥ 10 with the total being exactly 10. This forces x2 = 0.
  - Combine x2 + x3 ≥ 10 with the total. This forces x1 = 0.
  - So x3 = 10. If you give agent 3 less than 10, some inequality fails.
- Result: the **only** stable payoff vector is **(0, 0, 10)** with the grand coalition.
- Interpretation: all the value goes to agent 3. Given the story this is not surprising: agent 3 has the only right glove, the resource nobody else can provide, so it is "the most powerful agent".

## Glove Game Shapley Values: Not in the Core, So the Game Is Certainly Not Convex

**Reference:** 03 MAS coalition formation.pdf, p.26-28, p.30

- φ1 over the six orderings: agent 1 adds something only in **3,1,2**, where it joins {3} and v({1,3}) − v({3}) = 10. In 3,2,1, agent 3 and agent 2 already make 10, so agent 1 adds 0. Every other ordering gives 0.
- So φ1 = **10/6**. A student forgot to divide by 6 (= 3!), and the professor corrected this. Another student seems to have tried to read the Shapley values directly off the table, and he said "it is not like this" (ASR unclear).
- φ2 = 10/6 without computing, because agents 1 and 2 are **symmetric** (same role).
- φ3 = 10 − 20/6 = **40/6** by efficiency. The transcript only has "Forty", so the denominator is inferred.
- (10/6, 10/6, 40/6) is **not** in the core, which is only (0,0,10). Therefore the game is **not convex**, and "you can tell it for sure". This is the contrapositive of the p.30 theorem, unlike Exercise 1, where nothing could be concluded.

## Exercise 3 — Modified Game Where the Core Is a Segment

**Reference:** 03 MAS coalition formation.pdf, p.13, p.20, p.23

- He changed the characteristic function of the glove game "to understand why some games are called convex". Its values were not read aloud. From what he said (x1 + x2 ≥ 1, total exactly 1, agent 3 a dummy, agents 1 and 2 symmetric, non-negativity being the binding constraints), the game seems to be v({1,2}) = v({1,2,3}) = 1 and v = 0 for every other coalition. This reconstruction is uncertain.
- He stated the game is superadditive **and convex** (verify the convexity definition at home).
- Core:
  - x1 + x2 ≥ 1 and x1 + x2 + x3 = 1 with all x_i ≥ 0 force **x3 = 0**.
  - Then the core is every (x1, x2, 0) with x1 + x2 = 1 and x1, x2 ≥ 0.
  - In the x1-x2 plane, this is the **segment** of the line x1 + x2 = 1 between (1,0) and (0,1). Points of that line outside the segment break x1 ≥ 0 or x2 ≥ 0.
- How big a core can be: here the core has **infinitely many** payoff vectors. The glove game had exactly one, and some games have an empty core (as in class, p.22).

## Student Q&A: When the Sum Must Equal v(N), and Stability per Coalition

**Reference:** 03 MAS coalition formation.pdf, p.10, p.20

A student asked whether writing x1 + x2 + x3 = v(N) works only because the game is superadditive. Answer: it is written that way because the grand coalition forms. If the game is not superadditive, you write the conditions for the coalitions that actually form in the coalition structure. Stability of a coalition structure with several coalitions means **each coalition must be stable**.

## Why "Convex" Games Are Called Convex (Professor's Explanation)

**Reference:** 03 MAS coalition formation.pdf, p.13

Amigoni pointed to the segment in Exercise 3. It is a **convex set**: any core point is a convex combination of the two endpoints (the exact endpoint wording is ASR unclear). He said this is where the name comes from: "the convexity is the convexity of the core, of the stable set of solutions".

## Exercise 3 — Shapley Values with No Computation: Dummy and Symmetry

**Reference:** 03 MAS coalition formation.pdf, p.27-30

- **φ3 = 0**, because agent 3 brings nothing to any coalition it joins, so it is a **dummy**.
- Agents 1 and 2 are **symmetric**, since they always make the same marginal contributions. Efficiency then gives **φ1 = φ2 = 1/2**.
- The Shapley vector (1/2, 1/2, 0) is the **midpoint** of the core segment. It is in the core, as expected, because the game is convex. He stressed that it is in the core "not by definition, but by virtue of a theorem".

## Exercise 4 — Coalition Structure Generation by Dynamic Programming

**Reference:** 03 MAS coalition formation.pdf, p.41-44

- Setup: v({1}) = v({2}) = v({3}) = 1, v({1,2}) = 3, v({1,3}) = 6, v({2,3}) = 3, v({1,2,3}) = 5.
- First question, as usual: is it superadditive? **No.** {1,3} and {2} get 6 + 1 = 7 separately but only 5 together. So the grand coalition will not necessarily form, and you need to find the coalition structure. With 3 agents you could do it informally, but he ran DP to show how it works.
- Table columns: coalition, evaluations, **t** (the best way to split the coalition) and **f** (the value of that best split).
- Step 1, singletons: t({i}) = {i} and f({i}) = v({i}) = 1. This is just initialization.
- Step 2, pairs: there is only one way to split a pair in two.
  - {1,2}: v = 3 vs f(1) + f(2) = 2 → keep together, f = 3.
  - {1,3}: 6 vs 2 → keep together, f = 6.
  - {2,3}: 3 vs 2 → keep together, f = 3.
- Step 3, {1,2,3}: v = 5, compared with the **three** ways to split it in two:
  - f(1) + f(2,3) = 1 + 3 = 4
  - f(2) + f(1,3) = 1 + 6 = **7**
  - f(3) + f(1,2) = 1 + 3 = 4
  - Best is 7, so t({1,2,3}) = {2}, {1,3}.
- Don't stop at the top split: "we are not yet done". Look up t of each part. t({1,3}) says keep {1,3} together, and {2} cannot be split.
- Result: **CS* = {{1,3}, {2}}**, value 7. DP guarantees this is optimal, "the best that you can do".

## Exercise 5 — Same Game with Shehory-Kraus, Step by Step

**Reference:** 03 MAS coalition formation.pdf, p.48-50

- All agents compute **in parallel**. Each agent lists the coalitions it can join and scores each one by v(C)/|C|. These scores are computed from the values above, because the spoken numbers are partly garbled.
  - **Agent 1:** {1} = 1, {1,2} = 3/2, {1,3} = 6/2 = 3, {1,2,3} = 5/3. Best: C1* = {1,3}.
  - **Agent 2:** {2} = 1, {1,2} = 3/2, {2,3} = 3/2, {1,2,3} = 5/3. Best: C2* = the **grand coalition**, because for what agent 2 knows locally, that is the best choice.
  - **Agent 3:** best is {1,3} = 3.
- Each agent broadcasts its preference ("I would like to join {1,3}", "I would like to join the grand coalition"…).
- Computing C_max, the largest coalition that **all** of its own members proposed:
  - Negative example: the grand coalition was proposed only by agent 2, not by agents 1 and 3, so it cannot be C_max.
  - {1,3} was proposed by both 1 and 3, so **C_max = {1,3}**. Every agent reaches this same conclusion.
- Agents 1 and 3 join C_max and stop. Agent 2 is not in C_max, so it continues. It deletes every coalition containing 1 or 3 ({1,2}, {2,3}, {1,2,3}), because an agent can be in only one coalition and 1 and 3 have already formed theirs.
- Only {2} is left. So C2* = {2}, it is broadcast, and C_max = {2}.
- Result: CS = **{{1,3}, {2}}**.

## Shehory-Kraus Matched DP Only by Luck; Ties Must Be Broken the Same Way by All Agents

**Reference:** 03 MAS coalition formation.pdf, p.48, p.50-51

- Shehory-Kraus found the same, optimal, structure as DP here, but "this happened only by chance… we were lucky". It is **not** a structural property. In general Shehory-Kraus is sub-optimal: it is faster, but it guarantees nothing about the solution. DP always returns the optimal structure.
- Tie-breaking: the important point is that **all agents use the same tie-breaking rule**. Breaking ties **randomly is not a good rule**. A typical choice is lexicographic order, for example {1,2} comes before {1,3}.
