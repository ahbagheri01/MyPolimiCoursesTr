# MAS-20261014-Exercises-GameTheory — Additional Professor Notes

**Transcripts:** Francesco Amigoni's Personal Room-20261014 1407-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Multi agents\Slides and notes-20261005\Notes on game theory (by prof. Nicola Gatti).pdf

## Session Overview: Three Methods for Nash Equilibria, Then Mixed and Extensive-Form Exercises

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.5, p.12-15

Amigoni ran an exercise session ("we will not see the theory, just the procedure"). He presented three ways to find Nash equilibria (NE) in normal-form games: (1) **inspection**, (2) **iterated elimination of dominated actions**, (3) **best response**, which is needed when actions are continuous. Then he showed a 3-agent game solved with dominance plus a mixed-strategy computation, and an extensive-form game solved with backward induction and then flattened to normal form. None of these exercises is in Gatti's notes.

## Exercise 1 — Finding Pure NE by Inspection, Cell by Cell

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.5

- Setup: agents A (rows A1-A3) and B (columns B1-B3). In each cell the first number is A's payoff and the second is B's (e.g. A1,B2 gives 4 to A and 8 to B).
- Procedure: for each cell, ask "would either agent want to deviate **unilaterally**?" and name which one and why. Example: in the first cell A would switch to A3 to get 8 instead of 3, and B would switch to get 8 or 6 instead of 5, so it is not stable. For the cell (4,8), A would deviate to get 7. Go through all 9 cells this way.
- Result: the only pure-strategy NE is **(A3, B1)**.
- Inspection finds **only pure-strategy NE**, meaning all probability (1) is on a single action and every other action has probability 0. He said "this is something you should know". In a mixed NE the distribution is not concentrated on one action. Inspection is only practical for small games.

## Dominated Action: The Exact Definition Used in Class

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.12

- Action a ∈ A_i of agent i is dominated if there is a' ∈ A_i with u_i(a, σ_-i) **<** u_i(a', σ_-i) for **every** σ_-i. Here σ_-i means every possible combination of actions of all agents other than i: with 2 agents that is the other agent, with 3 agents it is the other two. He used the strict version.
- Intuition: you will never play a dominated action, because some other action is always better for you, whatever the others do. That is why it can be deleted from the game.
- Wording: say "M is dominated (by U)", meaning M is always worse than U.

## Exercise 2 — Iterated Elimination of Dominated Actions, Step by Step

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.13-15

Setup: agent 1 has rows U, M, D. Agent 2 has columns L, C, R.
1. **M is dominated by U** for agent 1: 4>3 vs L, 3>2 vs C, 5>4 vs R. Remove M.
2. In the reduced game, **C is dominated** for agent 2 (by both L and R). Remove C.
3. Only now is **D dominated by U** (4>3 and 5>3). He stressed that in the original game U did **not** dominate D. The domination appears only in the simplified game, and that is why the elimination is *iterated*.
4. Agent 2 is left choosing between L and R against U and gets 12 with R instead of 11. Remove L.
Result: a single cell, **(U, R)**, which is a pure-strategy NE.

## What Iterated Dominance Guarantees and When It Gets Stuck

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.13-15

- If the procedure ends in a **1×1 game**, that cell is a pure-strategy NE. In answer to a student, he confirmed that this method can only ever give a pure NE, because at best you are left with one cell (probability 1 on U and on R).
- The procedure may **stop before** reaching one cell, because at some point there may be no dominated action. Then it **cannot tell you** what the NE are. It is still useful to shrink the game by removing useless actions before using another method.
- It works for any number of agents and actions.

## Exercise 3 — Continuous Actions: NE via Best-Response Functions

**Reference:** None (not in slides). Notes on game theory (by prof. Nicola Gatti).pdf, p.4-5 only define BR_i and NE as mutual best response

- Setup: 2 agents, each choosing a **non-negative real number** (A1 = A2 = [0, ∞)), so there are infinitely many actions and no matrix. The utilities are functions with a constant c > 0. From the derivation in class (the formula itself is not legible in the transcript) they are u1 = a1(c + a2 − a1) and u2 = a2(c + a1 − a2), so if both play 1, each gets c.
- Why best response: inspection is impossible because there is no table, and dominated actions are hard to find here.
- Best response B1(a2) is the a1 that maximizes u1 with a2 held as a constant. Start with a2 = 0: u1 = a1(c − a1). By the product rule the derivative is c − 2a1. Setting it to 0 gives a1 = c/2. A student pointed out that a maximum must be checked: the second derivative is −2 < 0, so it is a maximum.
- Generic a2: the derivative is c + a2 − 2a1 = 0, so **B1(a2) = (a2 + c)/2**. The second derivative is still −2. By symmetry **B2(a1) = (a1 + c)/2**. The case a2 = 0 gives back c/2.
- Side remark from a student exchange (ASR partly garbled): if the stationary point were a minimum, you would have to look at the extremes of the action interval instead. Here the domain has only one extreme, 0, and the other end is open.

## Solving the Best-Response System, and the Set-Valued Caveat

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.5

- NE = (a1*, a2*) with a1* = B1(a2*) and a2* = B2(a1*): each agent best-responds to the other. Strictly speaking a best response is a **set**, so the general condition is a1* ∈ B1(a2*) and a2* ∈ B2(a1*). Writing "=" is allowed only because here the best response is a single value. He also corrected himself in class: a1* must be agent 1's best response to a2*, not the reverse.
- Solve by substitution: a2* = ((a2* + c)/2 + c)/2 = a2*/4 + 3c/4, so (3/4)a2* = (3/4)c and **a2* = c**. Then a1* = c.
- Meaning: if one agent plays c, the other cannot do better than playing c, and vice versa.

## Exercise 4 — Three Agents: Remove a Dominated Agent, Then Find the Mixed NE

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.3 (3-player layered table), p.6-7 (indifference method)

- Setup: agent 1 chooses {A, B}, agent 2 chooses {a, b}, agent 3 chooses {α, β}. The 3D payoff matrix is drawn as two layers, one per action of agent 3 (e.g. B,b,α gives (3,2,2) and B,b,β gives (2,4,6)). Task: find **all pure and mixed** NE.
- Step 1: for agent 2, **b strictly dominates a** (6>5, 2>0, 3>2, 4>3) whatever agents 1 and 3 do. So agent 2 plays b, and the game reduces to a 2×2 game between agents 1 and 3. Payoffs (agent 1, agent 3): A,α = (0,4); A,β = (3,3); B,α = (3,2); B,β = (2,6).
- Step 2: inspection of the reduced game finds no pure NE, because in every cell either agent 3 or agent 1 wants to deviate. So you have to look for mixed NE.
- Step 3: indifference conditions, so each agent is indifferent between its own actions:
  - Agent 1: E[u1(A)] = 0·p(α) + 3(1 − p(α)) must equal E[u1(B)] = 3p(α) + 2(1 − p(α)). This gives **p(α) = 1/4** and p(β) = 3/4. Note that **agent 1's** indifference fixes **agent 3's** probabilities.
  - Agent 3: E[u3(α)] = 4p(A) + 2(1 − p(A)) must equal E[u3(β)] = 3p(A) + 6(1 − p(A)). This gives 5p(A) = 4, so **p(A) = 4/5** and p(B) = 1/5.
- Result: agent 1 plays (4/5 A, 1/5 B), agent 2 plays pure b, agent 3 plays (1/4 α, 3/4 β). Only agents 1 and 3 mix. The method extends to more agents and actions, but the algebra gets heavier.
- Student Q&A: computing mixed strategies by indifference falls "under the big umbrella of best response", but he treats it as a separate technique. The probabilities are justified because equal expected utilities are exactly what defines a mixed NE.

## Exercise 5 — Extensive-Form Game Solved by Backward Induction

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.11-12

- Setup: A moves first at A1 and chooses D or U.
  - After U, B moves at B2: choosing T gives (1,4) and choosing B gives B a payoff of 2.
  - After D, B moves at B1: L ends the game with (6,2), and R leads to A's second node A2.
  - At A2, Q gives (2,0) and P gives (3,3).
  - He called it a synthetic game, not a model of any real situation.
- He stated that in extensive-form games the relevant concept is the **subgame perfect equilibrium (SPE)**. It is related to NE but not identical. Informally, an SPE is the best action of each agent **at each of its decision nodes**. It is found by backward induction: go bottom-up and solve each subgame separately.
- Worked solution:
  - At A2, A picks P (3 > 2).
  - At B2, B picks T (4 > 2).
  - At B1, B picks R: L gives 2, while R gives 3 because B **already knows** A will pick P at A2. This reuse of lower results is the "backward" idea.
  - At A1, U leads to T and gives A 1, while D leads to R then P and gives A 3. So A picks D.
- SPE: **A plays (D at A1, P at A2); B plays (R at B1, T at B2).**
- In actual play B can never use both R and T, because only one of its nodes is reached. Still, the SPE gives the rational action for every node that *might* be reached, and not all of these actions will be played. If two options have the same value, either can be chosen.

## Flattening the Extensive Game to Normal Form: Strategies as Pre-Committed Plans

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.9-10

- A's strategies combine one choice per decision node: DQ, DP, UQ, UP. B's strategies are LB, LT, RB, RT.
- Why both nodes appear: think of "wiring" your strategy before the game starts. B **cannot commit just to L**, because if A plays U, B would not know what to do at B2. A combination like "DU" makes no sense, because D and U are alternatives at the *same* node. A strategy has exactly one option per decision node, even for nodes at different levels or nodes that a given play never reaches.
- Filling the table: (DQ, LB) gives 6,2 and (DQ, LT) also gives 6,2. (DQ, RB) gives 2,0 and (DQ, RT) also gives 2,0. Fill the other cells by following the tree.

## The SPE Is One of the NE of the Flattened Game

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p.11 (Solutions ⊃ Nash ⊃ SPE diagram)

- Inspecting the flattened table gives three pure NE: **(DQ, LB), (DQ, LT), (DP, RT)**.
- The SPE found by backward induction, (DP, RT), is **one of them**. In general, the SPEs of an extensive-form game are a subset of the NE of the corresponding normal-form game. So SPE is a **stronger** (more selective) concept than NE.
