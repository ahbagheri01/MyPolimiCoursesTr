# MAS-20260930-CoalitionFormation-Part1 — Additional Professor Notes

**Transcripts:** Francesco Amigoni's Personal Room-20260930 1405-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Multi agents\Slides and notes-20261005\03 MAS coalition formation.pdf

## Cooperative Games: Binding Agreements and Group Actions

**Reference:** 03 MAS coalition formation.pdf, slide 5

- A binding agreement works like signing a contract: once the agents agree to do something together, they must stick to it.
- Making groups the unit that acts (a joint action of the group) is a big change from the single-agent architectures seen earlier in the course.

## TU vs NTU Games: Soccer Team vs Work Bonus

**Reference:** 03 MAS coalition formation.pdf, slide 5

- **Transferable utility (TU):** a soccer team wins a match. The win belongs to the group, not to any single player. How the group then shares its payoff is a separate question.
- **Non-transferable utility (NTU):** you work in a company team and get an end-of-year bonus. You achieved the result together, but your bonus differs from your colleague's, because the payoff goes straight to each person.
- The area is large, so the course studies only TU games, and within them only characteristic function games.

## Monotonicity Is Not Always Realistic: Robot Congestion

**Reference:** 03 MAS coalition formation.pdf, slide 7

Monotonicity (a bigger coalition earns at least as much) is only sometimes assumed. Counterexample: robots moving in a finite space. If you keep adding robots, performance stops improving, because at some point congestion is so bad that no robot can move.

## Ice-Cream Game: Where the Values Come From, and Why There Is No Split Yet

**Reference:** 03 MAS coalition formation.pdf, slide 8

- Payoff is measured in grams of ice cream. Alone, nobody can buy anything (Charlie's $6 is less than the $7 small tub), so every singleton gets 0. C+M have $10 and C+P have $9, so each pair buys the 750 g tub. M+P have only $7, so they get 500 g. The grand coalition has $13 and buys 1000 g.
- A student asked why the value isn't divided among the members. The professor said the model only gives the amount the coalition gets, which is the best it can do. Splitting it is a separate, later problem. (He said "non-transferable" at this point, but from context he meant transferable utility. Slip or ASR error.)

## Real-World Applications of Coalition Formation

**Reference:** 03 MAS coalition formation.pdf, slide 9 (figures only)

- **Mobile phone cells:** users are grouped onto different antennas. The payoff is the bandwidth or quality of service each grouping gives.
- **Precision agriculture:** different drones must do different jobs on a field (some monitor, others do other operations). Instead of fixing the teams in advance, coalition formation lets the system decide by itself which drones do what.
- **Robots moving a soft object (cloth):** the robots must split into groups, for example one group pushes and another pulls.

## Outcomes: No "Bank Account", and Not All Outcomes Are Equal

**Reference:** 03 MAS coalition formation.pdf, slides 10-11

- Each coalition must hand out everything it earns: "there is no bank account" where it can keep money. It also cannot hand out more than it earns. That is why (2,3,2,3,3) fails: the green coalition {4,5} earns 4 but would give out 6, and {1,2,3} earns 9 but would give out 7.
- Payoffs inside a coalition do not have to be equal (student question).
- One game can have many outcomes. Some will be good for some reasons and others bad. For some coalition structures no good payoff vector exists, which means that coalition structure itself is not good.
- He called imputation and the x(C) notation technicalities that do not matter at this point.

## Superadditivity: Intuition and Scope

**Reference:** 03 MAS coalition formation.pdf, slide 12

- In plain words, in a superadditive game it always pays to join into bigger and bigger groups. This is not a general property: some games have it and some do not.
- Superadditivity settles the coalition structure (the grand coalition), but the payoff vector is "completely another story".
- In v(C) = |C|², the value depends only on how many agents are in C, not which ones. The game is superadditive for any set N. The formal proof that the grand coalition is the best structure was promised for the next lecture.
- Only the coalition's total value matters, not what individual members want (student question).

## Convex Games: C and D Need Not Be Disjoint

**Reference:** 03 MAS coalition formation.pdf, slide 13

- A student asked whether C and D must form a partition. The answer: no. Convexity is required for **all** subsets C, D of N, including overlapping ones (hence the v(C∩D) term). Superadditivity, by contrast, uses only disjoint coalitions.
- The professor set two home exercises: prove that a convex game is superadditive, and find a superadditive game that is not convex.

## Simple Games: Tasks That Need a Minimum Number of Agents

**Reference:** 03 MAS coalition formation.pdf, slide 13

Simple games (v ∈ {0,1}) model tasks that get done once enough agents join:
- **Moving a table** needs at least 4 agents. With 6 or 8 agents it is still done, but there is no extra value because there is no other table to move.
- **Tennis:** you can play once you have at least two players.

## Worked Reasoning for the Two Classification Examples

**Reference:** 03 MAS coalition formation.pdf, slides 14-15

- **Example 1 (Alice, Bob, Celine):** not superadditive because A and B alone get 80 + 56 = 136, but together only 80. Not convex: the "typical mistake" is to check convexity directly, when convex ⇒ superadditive already means a non-superadditive game cannot be convex. Not simple: the values are not just 0/1.
- **Example 2:** checking superadditivity means trying every pair of disjoint coalitions. Smarter methods exist but are not covered in the course. Sample checks: {a},{b}: 0 + 4 = 4 < 11; {a,c},{b}: 6 + 4 = 10 < 20. Convexity holds, and he left checking it as homework. Not simple.
- The course order: the payoff vector (core, Shapley) this lecture, the coalition structure problem the next.

## Intuition for Instability and the Core

**Reference:** 03 MAS coalition formation.pdf, slides 19-21

- With (200,200,350), Charlie and Marcie get 400 together. If they leave the grand coalition and buy a tub on their own, they get 500. The split gives a subgroup a reason to leave, so it is unstable. The professor compared this to everyday life: when you hand out favours unevenly, people who feel short-changed may walk away.
- Core in words: for **every** coalition C, the total you give its members is at least what they could earn by forming C. G need not be superadditive.
- The game (all characteristic-function values) is assumed known to the agents. C ranges over every subset of N, not just the coalitions in CS. In the slide 20 example, the blocking coalition {2,4} takes one agent from each existing coalition: they get 3 + 3 = 6 < 7, so both would leave their coalitions to form {2,4}.

## The Core Captures Stability, Not Fairness: (250,250,250) vs (750,0,0)

**Reference:** 03 MAS coalition formation.pdf, slide 21

- (250,250,250): every pair gets 500, the same as on its own. With equal payoff there is no incentive to leave, so they stay (the inequality is weak).
- (750,0,0) is also in the core. C+M get 750 > 500. M+P get 0, but with $3 each they cannot buy anything, so leaving still gives 0. Yet it is clearly unfair. All the power is with Charlie: only with his $4 can anything be bought, so he can threaten to leave and leave Marcie and Pattie with nothing.
- The core encodes only stability (nobody can object or do better). It is an appealing idea, but it can contain "strange things". This is why fairness (Shapley) is introduced next.
- So far they had only checked whether a given outcome is in the core. How to actually compute the core was deferred to the exercise sessions.

## Empty-Core Game: Full Argument

**Reference:** 03 MAS coalition formation.pdf, slide 22

- This game (v = 1 if |C| > 1, else 0) is also a simple game. It **is** superadditive. A student tried to combine overlapping coalitions, but superadditivity only compares disjoint coalitions. So the grand coalition forms, and he still went through every structure.
- **CS = ({1,2},{3}):** x1 + x2 = 1, so at least one of them gets less than 1. That agent can team up with 3 and get 1, so it deviates.
- **Grand coalition:** x1 + x2 + x3 = 1 (you must hand out exactly 1, no more), so some agent gets more than 0. The other two then get less than 1 combined but would get 1 by leaving. For (1,0,0), agents 2 and 3 leave. For (0,0,1), agents 1 and 2 leave. He also tried a fractional split (the exact numbers are ASR-unclear). There, the second and third agents got 0.5 together and would leave for 1. Any split fails, so the core is empty.

## Marginal Contribution: Why the Sum Works and Why Order Breaks It

**Reference:** 03 MAS coalition formation.pdf, slides 24-26

- This is a switch in viewpoint from stability to contribution: as humans, we feel people should receive according to how much they contributed.
- The marginal-contribution payments add up to v(N) because the sum telescopes: all the intermediate terms cancel.
- In the 2-player example, the agents are identical, so paying 5 to the first and 15 to the second "makes no sense". Reversing the order just swaps the values.
- The number of orderings is n! (3 agents → 6, 4 agents → 4!), not 2^n. A student mixed up orderings with subsets.
- Averaging gives (10,10), which is fair because the grand coalition earns 20 and the two agents are perfectly symmetric.
- Asked whether this works only for superadditive games, he said it applies to any game, and within any coalition of a coalition structure. Superadditive games are used only to keep things simple.

## Reading the Shapley Formula Procedurally

**Reference:** 03 MAS coalition formation.pdf, slide 26

- P(N) is the **set** of permutations and π is one permutation (student question).
- Procedure: fix a permutation, find agent i in it, and take i's marginal contribution to the agents before it, S_π(i). Do this for every permutation, add up the contributions, and divide by n!. This is exactly the 2-agent average, generalised. The formula will be applied in the exercise sessions.

## Shapley Properties: Intuition and Two Ways to Read the Uniqueness Theorem

**Reference:** 03 MAS coalition formation.pdf, slides 27-29

- **Dummy:** adding the agent to any coalition changes nothing, so all its marginal contributions are 0 and its Shapley value is 0.
- **Symmetric:** for every coalition containing neither i nor j, adding i or adding j gives the same value. Their marginal contributions are always equal, so their Shapley values are equal.
- **Additivity:** he described it as "more technical, not more complex".
- Each property has a proof, but the proofs are not covered in the course.
- **Uniqueness, two perspectives:** (a) define Shapley values, then prove they satisfy the four properties; or (b) start without Shapley, ask for any payoff scheme that satisfies efficiency, dummy, symmetry and additivity, and find that Shapley is the only one. He called this result very strong (not proved in the course).

## Convex Games: Fair Is Also Stable

**Reference:** 03 MAS coalition formation.pdf, slide 30

Shapley gives a fair split and the core gives a stable one. In convex games the Shapley payoff vector is in the core, so the fair split is also stable: no agent or group would object to it. The professor called this "quite remarkable". The next lecture covers finding a good coalition structure when the game is not superadditive.
