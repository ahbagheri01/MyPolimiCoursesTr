# MAS-20260923-Exercises-AgentArchitectures — Additional Professor Notes

**Transcripts:** Francesco Amigoni's Personal Room-20260923 1417-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Multi agents\Slides and notes-20261005\02 MAS agent architectures.pdf

> **Coverage notes:** The two MDPs solved in this session were drawn on the board and are not in the slides. They had to be reconstructed from the speech alone, so some transition probabilities and intermediate numbers are partly uncertain (see the notes).

## Schedule Change: Game Theory and Coalition Formation Are Interleaved

The class schedule on WeBeep was updated. The class days stay the same, but some classes were moved. The next two topics, game theory and coalition formation, will not be taught one after the other but mixed together, because the course does not have enough days.

## Exercise MDP 1: Reading the Graph (States, Actions, Transitions, Rewards)

**Reference:** 02 MAS agent architectures.pdf, p.42 (MDP definition)

Board MDP: four states S1–S4, four actions A1–A4, γ = 0.5. What the professor stressed while reading it:

- **Not every action is applicable in every state.** For example, only A1 and A2 can be used in S1 and in S4. In S3 the agent must choose between A3 and A4, and it cannot stay in S3.
- **Reading T from the graph.** T(S1, A1, S2) = 0.8. T(S1, A1, S1) = 0.2. T(S1, A1, S3) = 0 because there is no arrow. Since T(s, a, ·) is a probability distribution, it must sum to 1 over s'. An arrow with probability 1 (A4 from S3) means the action is **deterministic**.
- **The graph says nothing about rewards.** If asked "what is the reward function?" from the drawing alone, the answer is that it cannot be known. He then gave R(S3) = 1 and R = 0 for every other state.
- **Rewards defined on the state only:** R(s, a, s') = R(s). The value depends only on the first argument, so the other two are irrelevant (e.g. R(S1, A1, S2) = 0 because R(S1) = 0). Answering a student, he added that the reward belongs to the **current** state you are in, not the next state you move to.

## Intuition First: Prefer States by Future Rewards, Not Immediate Reward

**Reference:** 02 MAS agent architectures.pdf, p.58 (V*)

Before any calculation, he asked which state the agent would like to be in:

- Answering "S3, because it gives 1" is only part of the answer. S3 is best because from it the agent can come back to S3 and collect 1 again and again.
- **S2 vs S4:** both give immediate reward 0, so looking only at the present they are equivalent. But from S4 it is more likely (in a probabilistic sense) to reach S3, so S4 is better. Comparing states by their sum of future discounted rewards is exactly what V* does.
- **In S3, choose A3 over A4:** A3 leads to S4, from which it is easier to get back to S3. The reward collected later is discounted, but S4 is still a better place to be than S2.

## Running Value Iteration by Hand: How to Write One Update

**Reference:** 02 MAS agent architectures.pdf, p.87–88, p.90

How he wrote one update on the board:

- k = 0 is initialisation: all V0 = 0 ("I know nothing").
- At k = 1, V1(S1) is the **max over the actions applicable in S1** (A1, A2), so it is the max of two numbers. Each number is a sum over the possible next states s'. For A1: 0.2·[R(S1) + 0.5·V0(S1)] + 0.8·[R(S1) + 0.5·V0(S2)] = 0. A2 gives 0 the same way (0.2 back to S1, 0.8 to S4), so V1(S1) = max(0, 0) = 0.
- Here R depends only on s, so it could be pulled out of the sum (and out of the max). Keeping it inside the sum gives the general formula, which works for any reward definition.
- Always use the values from **iteration k−1** when computing iteration k.
- Numbers reported in class: V1 = (0, 0, 1, 0) for (S1, S2, S3, S4). At k = 2, V2(S2) = 0.4 and V2(S3) is still 1. At k = 3, V3 ≈ (0.18, 0.44, 1.2, 0.457). The last value and some of the k = 2 values are ASR-uncertain. Already at k = 3, V(S4) > V(S2), which matches the intuition above.

## Why V(S3) Grows Above 1 and Why Values Never Decrease Here

**Reference:** 02 MAS agent architectures.pdf, p.86–87

- At k = 3, V(S3) = 1.2 > 1 even though S3 only pays 1. The algorithm is starting to "discover" that after leaving S3 the agent can come back with some probability and collect discounted rewards again. V looks at the future, not only at what you get now.
- In this example all rewards are non-negative, and probabilities are always non-negative. So each update can only add and multiply non-negative numbers, and the values can never decrease from one iteration to the next. This is tied to this example's non-negative rewards; it is not a general property.

## Advice: Execute Algorithms on Paper to Understand Them

Nobody solves a real MDP by hand; you use an algorithm or a library. But the professor said the best way to understand an algorithm, in this course and for the more complex ones later, is to run a few iterations or steps of it on paper at home on a small example. He suggested completing all the value-iteration numbers of the board example at home.

## When to Stop Value Iteration: Ideal vs Practical Termination

**Reference:** 02 MAS agent architectures.pdf, p.87–88 ("repeat until convergence", "if V converged then break")

- **Ideal stop:** when the values no longer change from iteration k to k+1. On a computer you stop when the change is small enough. Responding to a student, he corrected the wording: value iteration is not "learning", it is "updating".
- **Key property:** after convergence the values are the optimal V*. You cannot know in advance how many iterations that takes. The "tricky" part is that V* is computed **without knowing the optimal policy**, even though V* is defined as the value of playing optimally.
- **Stopping rule he presented** (described as one of the simplest but most elegant): choose ε > 0 and stop when

  max over s of |V_{k+1}(s) − V_k(s)| < ε·(1 − γ)/γ

  ε is **not a parameter of the problem**. It belongs to your solving approach, so you choose it.
- **Worked check on MDP 1 (γ = 0.5, so (1−γ)/γ = 1):** from k = 2 to k = 3 the changes are 0.18 (S1), 0.04 (S2), 0.2 (S3) and about 0.02 (S4, ASR unclear).
  - With ε = 0.3, every change is below 0.3, so you stop, even though the values have not truly converged.
  - With ε = 0.1, you do not stop, because S3 changed by 0.2 > 0.1.
  - Because of the max, a single state that fails the test is enough to keep iterating.

## Effect of ε and γ on How Long Value Iteration Runs

**Reference:** 02 MAS agent architectures.pdf, p.53–54 (discounting)

- **Smaller ε → more iterations**, because the inequality is harder to satisfy. At perfect convergence the left-hand side would be 0.
- **γ close to 1 → many iterations:** (1−γ)/γ goes to 0, so the threshold becomes tiny.
- **γ close to 0 → stop almost immediately:** (1−γ)/γ becomes huge, so any change satisfies the test.
- **Interpretation:** with large γ the agent is **far-sighted**. Rewards far in the future count a lot, so more iterations are needed to spread them through the values. With γ ≈ 0 the agent is **myopic** and looks only at the immediate reward, so few iterations are enough.

## Error Guarantee of the ε-Stopping Rule

When you stop with the rule above, one can prove that

max over s of |V_k(s) − V*(s)| < ε

So the unknown optimal values are guaranteed to lie within ±ε of the current estimates.

- **Extreme case:** ε = 0 means running to perfect convergence, so the final values are exactly V*.
- **Example:** in MDP 1, stopping at k = 3 with ε = 0.3 gives V(S3) = 1.2, so V*(S3) is unknown but lies between 0.9 and 1.5.
- **Trade-off:** smaller ε gives a tighter interval but more iterations. A precise estimate of V* requires running the algorithm a lot.
- **Student proposal: stop when the change is < ε (without the γ factor).** It is "more or less the same", but the guarantee is different, because that condition ignores γ. The (1−γ)/γ factor makes the stopping rule account for the bound on V* and for γ together.

## Q&A: Stopping Is Not Convergence; What the Bound Does and Doesn't Tell You

A student asked (ASR largely unclear) about what stopping implies for the values of individual states. The professor's answer:

- Stopping is not convergence. In theory you converge only when the numbers never change again, which is impossible in practice, so thresholds approximate it.
- There are "hundreds" of ways to terminate value iteration; this is just the simplest one, and it is nice because of its guarantee. Other options include putting bounds on specific states you consider critical.
- This criterion bounds only the **maximum** variation over all states. It says nothing about a specific state, and nothing about the difference between the values of two states. With a large ε the true V* can lie in a very large interval; with a small ε, in a small one.

## Extracting the Optimal Policy from (Approximate) V*

**Reference:** 02 MAS agent architectures.pdf, p.91

- After stopping you have approximate V* values. Plug them into the formula that looks like the Bellman update with **argmax instead of max**: compute one number per action and pick the action with the largest number.
- Results for MDP 1, matching the intuition (he asked students to verify them with the formula at home): S3 → A3 (back to S4), S4 → A1, S2 → A2 (the "go right" action toward S3, not A3 "go down"), S1 → A2 (toward S4 rather than S2).

## Solving the Bellman Equations Directly as a System (and Why It Is Impractical)

**Reference:** 02 MAS agent architectures.pdf, p.67–68

- **The system:** you can write one Bellman equation per state. For S1: V*(S1) = max{0.8·(0 + 0.5·V*(S2)) + 0.2·(0 + 0.5·V*(S1)), …the A2 term…}. For S3, with deterministic transitions, each term in the max has a single next state.
- **Counting:** the number of equations equals the **number of states**, not the number of actions (a student got this wrong). The unknowns are the V* values, one per state. So you have n equations in n unknowns.
- **The difficulty:** the max makes the system **non-linear**. A linear system is easy to solve; a non-linear one is hard.
- **Linearisation trick:**
  1. In each equation, call the two terms inside the max A and B and **assume** one is larger (e.g. A > B). The max disappears and the equation becomes linear.
  2. Make one such assumption per equation and solve the resulting linear system.
  3. Check that all assumptions hold for the values found. If they do, you are done. If not, change some assumptions (e.g. A < B) and solve again.
- **Cost:** in principle you must try all combinations of hypotheses, which explodes combinatorially with the number of states. This is why the method is not convenient in general.
- **Exam:** "You can find some examples in some past exams" of this kind of exercise.

## Exercise MDP 2: Where an Optimal Policy Is Even Meaningful

States S0–S3, γ = 0.9, rewards attached to states, R(S3) = 10.

- **Question asked:** in which states does it make sense to talk about an optimal policy?
- **Answer: only in S1.**
  - S3 can only loop on itself.
  - S2 has a single action, back to S0.
  - S0 has a single action that leads to S1 or S2.
  - In S1 there are two actions: A goes surely to S2; B goes to S3 or back to S1.
- With only one applicable action the policy is trivial. An optimal policy matters only where there is a real choice.
- **Intuition:** in S1 choose B. It may reach S3 and then collect 10 forever; if it falls back to S1, the agent can simply retry.

## MDP 2: V*(S3) = 100 and Why V*(S1) Exceeds 10

- **Quiz:** "Is V*(S1) larger than, smaller than, or equal to 10?" The answer is **larger**.
- **V*(S3):** the Bellman equation for S3 has no max (one deterministic action): V*(S3) = 10 + 0.9·V*(S3). So V*(S3) = 10/(1 − 0.9) = **100**: 10 now, 10 one step later, and so on, discounted by γ.
- **Bound on V*(S1):** in the equation for S1, the B term is roughly 0.5·(2 + 0.9·V*(S1)) + 0.5·(2 + 0.9·100) (ASR suggests R(S1) = 2). The second part alone is 0.5·92 = 46, plus something non-negative, so V*(S1) ≥ 46 > 10. You can answer this kind of comparison question without solving the whole system.

## Suggested Homework on MDP 2 (Bellman System + Value Iteration)

- Write the four Bellman equations (V*(S3) is already solved) and solve the others to get all optimal values.
- To linearise, use the hypothesis that B is better than A in S1. Check that the values found satisfy it. Optionally reverse the hypothesis and verify that it then fails.
- Then run value iteration step by step on the same MDP. Since you already know V*, watch how fast the iterates converge to it.
