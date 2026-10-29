# MAS-20261007-CoalitionFormation-Part2 — Additional Professor Notes

**Transcripts:** Francesco Amigoni's Personal Room-20261007 1400-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Multi agents\Slides and notes-20261005\03 MAS coalition formation.pdf

> **Material limitations:** The course schedule also links external notes (NotesAAMAS2017-2018.pdf) that are not among the mapped materials. They were not inspected, so these notes were compared against the slide deck only.

## Representation Is Already Intractable Before Any Computation

**Reference:** 03 MAS coalition formation.pdf, slide 31

Amigoni stressed that the first obstacle is not computational but representational: just writing down the characteristic function needs one number per subset of agents. With 4 agents that is 16 numbers. With 100 agents it is 2^100 entries, which is more than the estimated number of atoms in the universe (about 2^80), so no memory could hold the table.

## How the Two Compact-Representation Approaches Work

**Reference:** 03 MAS coalition formation.pdf, slides 32-33

- **Restricted classes:** instead of listing values, you give a (usually compact) *rule* that generates the value of any coalition. The cost is that some games cannot be expressed this way.
- **Giving up worst-case succinctness:** the representation can express *any* game. It is compact for the games you typically care about and inefficient for the others.
- The slide-33 example (give singleton values plus a few chosen coalitions, and sum the singletons for every unlisted coalition) belongs to the **second** approach. With 100 agents you specify about 100 numbers instead of 2^100, plus any extra coalitions of interest (e.g. v({1,4})). Any game can still be represented: in the worst case you list every coalition and are back to the original problem.
- Amigoni said the course does not go further into this field, but it is a real issue in practical applications, which typically involve many agents.

## Counting Coalitions vs. Coalition Structures

**Reference:** 03 MAS coalition formation.pdf, slides 36, 39

- With 3 agents there are 8 possible coalitions (all subsets). This count includes the empty coalition, which "doesn't make much sense".
- The number of coalition structures (partitions) of n agents is the **Bell number**. It is defined recursively, grows very quickly, and its derivation was not covered ("more related to algebra"). He wrote a recursive formula, but the transcript of it is garbled (ASR unclear).
- When the 4-agent graph shows 15 partitions, the match with another count of 15 (presumably the 2^4 − 1 = 15 non-empty coalitions) is "just by chance". What the student compared it to is uncertain.
- About the notation P^A: it is a set whose elements are partitions, and each partition is itself a set of subsets of the agents. Don't confuse the levels.

## The 3-Agent Example Is Not Superadditive, Which Is Why the Grand Coalition Is Not Optimal

**Reference:** 03 MAS coalition formation.pdf, slides 36-37

In the slide-36 game, {a1,a3} together with {a2} alone gives 60 + 40 = 100, which beats the grand coalition's 90, so the game is not superadditive. Amigoni used the definition of the optimal coalition structure (CS* maximizes the sum of coalition values) to justify a claim from the previous lecture: in a superadditive game the grand coalition always has the best possible value, so that is the structure that forms. He noted that brute-force enumeration of all partitions works, but more efficient algorithms exist.

## Meaning of the Edges in the Coalition Structure Graph (a Lattice)

**Reference:** 03 MAS coalition formation.pdf, slide 39

- Each layer groups the partitions by how many coalitions they contain (4, 3, 2, 1).
- The edges mean different things depending on the direction you read them:
  - **upward (bottom to top):** take one coalition of the partition and split it in two;
  - **downward (top to bottom):** take two coalitions and merge them (e.g. {a2} and {a3,a4} become {a2,a3,a4}).
- A structure with these up/down operations is a **lattice** (Italian *reticolo*).
- Why it matters: the lattice is the search space. Every node gets one value (the sum of its coalitions' values), and you move between nodes by splitting or joining to find the node with the maximum value.

## Why Splitting in Two Is Enough in the DP Algorithm

**Reference:** 03 MAS coalition formation.pdf, slides 41-43

- **What the theorem saves:** you do not have to examine every partition. You only try every way of splitting the set in two, and for each half you recursively find its best partition. Because the same two-way split is applied recursively inside each half, combining the levels covers all possible partitions. A student asked whether the result is really the maximum: yes, the theorem guarantees optimality. It was stated, not proved, in class.
- **Order of computation:** in practice you start from the singletons (the top of the graph) and work by increasing coalition size, so the answer for the full set comes last. The size order is not by chance: computing f({1,2,4}) needs f({2,4}) and the other smaller values, which are already stored. You build on previous work, which is the typical dynamic programming pattern of splitting a problem into smaller subproblems of the same kind.
- **Why not split in three?** A student asked this. The theorem says splitting in three is useless, and skipping it saves a lot of work once there are many agents.
- The algorithm is still exponential.

## Reconstructing the Solution From t, and Tie-Breaking

**Reference:** 03 MAS coalition formation.pdf, slide 44

- **Ties at the last step:** in the 4-agent example several splits of {1,2,3,4} reach 150. Amigoni simply picked {1,2} + {3,4}.
- **t(A) is not the answer yet:** "we are not yet done", because {1,2},{3,4} is not the optimal structure. You must go back through t:
  - t({1,2}) = {1},{2}
  - t({3,4}) = {3,4}
  - so the optimal structure is {1},{2},{3,4}, with value 150. (A student had asked about this earlier, and he said it is resolved by this final reconstruction.)
- **The other tied choices give the same result:** {2} + {1,3,4} unfolds through t({1,3,4}) = {1},{3,4}, and {1} + {2,3,4} unfolds through t({2,3,4}) = {2},{3,4}. Both end at the same structure.
- **Rule:** if the optimum is unique, how you break ties does not matter. If several partitions share the optimal value, just pick one.
- Before running the algorithm he checked that the 4-agent game is not superadditive (if it were, the grand coalition would be optimal and no algorithm would be needed).

## How IDP Removes Redundant Operations

**Reference:** 03 MAS coalition formation.pdf, slide 45

In the 4-agent example, many of the evaluations turn out to be useless for the final result, and with 50 agents the number of useless operations grows. IDP uses bounds: a split is cut when it cannot lead to a result better than one already obtainable from what has been discovered, similar to branch and bound.

A student asked whether the pruning rule is something you choose. Amigoni said no: it is automatic, it does not change the final result, and it only improves efficiency. Even with this improvement, finding the optimal solution is still exponential, about O(3^n) in the worst case.

## Q&A: Starting From the Grand Coalition Instead

**Reference:** None (not in slides)

A student asked about searching in the opposite direction, starting from the whole set. Amigoni said other algorithms work that way, some of them optimal and some not, and that he was not 100% sure such an approach would be optimal in every situation. He also mentioned algorithms that put agents together and then "freeze" some subsets so they always stay together, which reduces the size of the problem.

## Optimality vs. Time in Applications, and the Missing Quality Bound

**Reference:** 03 MAS coalition formation.pdf, slides 46-47

**Trading optimality for speed:** in applications such as grouping robots, computing the optimal coalition structure might take three hours, while a non-optimal but acceptable structure might be found in two seconds. Trading solution quality for time is common, which is why the non-optimal (metaheuristic) family is the one usually applied in practice.

**No quality guarantee at all:** Amigoni distinguished two levels of guarantee:

- an approximation guarantee, i.e. the solution is not optimal but is known to be within some epsilon of the optimum;
- no guarantee at all, which is the case for these metaheuristics: the solution can be as bad as possible, but it is found very quickly.

## Centralized vs. Distributed Algorithms

**Reference:** 03 MAS coalition formation.pdf, slides 48, 51

**DP is centralized by nature:** to run it you need all values of the characteristic function for all agents. You can parallelize the calculations over cores or processors, but the algorithm itself remains centralized.

**Shehory and Kraus is distributed:** each agent reasons by itself on the information it has, possibly partial, and makes local decisions. The final coalition structure results from the collection of these local decisions. Amigoni noted this is the first distributed algorithm of the course, and this kind of algorithm will come back many times.

When asked about other non-optimal algorithms, he cited genetic algorithms. He added that in practice you can also invent your own heuristic (e.g. take the best agent, add other agents, and use your own partitioning rules).

Shehory and Kraus is attractive because it is distributed, while genetic algorithms are typically centralized. With robots, you can spread the computation over the robots themselves: you only need processors on the agents and a network to exchange messages, with no central server. He also seemed to agree that coalitions can be built and then dissolved over time (ASR unclear).

## Shehory–Kraus Worked Example: Full Run and Why It Is Suboptimal

**Reference:** 03 MAS coalition formation.pdf, slides 49-50

**The selection criterion:** each agent scores a coalition it can join by v(C)/|C|, i.e. the coalition's value divided by its number of members. (ASR renders the name as "Scherrian/Sharing Krauss".)

**Is the game superadditive?** The class first answered this: yes. So the grand coalition (value 120) is optimal, and in practice no algorithm would be needed. Amigoni ran the algorithm anyway to show what it does. The slide shows only agent 1's evaluation; the other steps were given orally.

**Round 1 — proposals:**

| Agent | Scores it computes | Proposal |
|---|---|---|
| 1 | {1,2} = 90/2 = 45 (best) | {1,2} |
| 2 | {1,2} = 45 (best) | {1,2} |
| 3 | {3} = 0, {1,3} = 40, {2,3} = 35, {1,2,3} = 40 | {1,2,3} |

Agent 3 has a tie between {1,3} and {1,2,3} and picks the grand coalition because it is the bigger one.

**Round 1 — C_max:** {1,2,3} was proposed only by agent 3, since agents 1 and 2 do not want it. {1,2} was proposed by both of its members, so C_max = {1,2}. That coalition forms, and agents 1 and 2 leave the algorithm.

**Round 2:** agent 3 deletes every coalition that involves 1 or 2. Only {3} is left, so it proposes itself and forms {3}.

**Result:** the structure {1,2},{3} has value 90 against the optimal 120. This is the price of being fast: the algorithm misses the optimum even in a superadditive game.

If several coalitions qualify as C_max at once, you choose the biggest one.

## Why All Agents Compute the Same C_max, and Why It Always Exists

**Reference:** 03 MAS coalition formation.pdf, slides 49-50

- **Same C_max for everyone:** the broadcast is a synchronization point "not in time but in knowledge". After it, every agent knows what every other agent wants to join (common knowledge) and computes C_max from the same information, so all reach the same conclusion. This includes agents who are not part of C_max: agent 3 also knows that {1,2} is forming.
- **C_max always exists:** a student asked what happens if v({2}) = 50. Then agent 2 proposes to stay alone, and {2} is C_max, because every member of that coalition (just agent 2) wants it. Amigoni called this the "magic" of the algorithm.
- **The one requirement:** all agents must use the same deterministic tie-breaking rule when choosing their proposal (e.g. lexicographic; any rule works as long as it is shared). If agents break ties differently, C_max may not exist.

## Why Shehory–Kraus Is Cheap

**Reference:** 03 MAS coalition formation.pdf, slide 51

- **At most n rounds:** every round forms at least one coalition, so with 3 agents there are at most 3 rounds, and with n agents at most n.
- **Each round is simple:** the hardest work in one round is listing the coalitions you can join, dividing each value by its size, and scanning the list of received proposals.
- Amigoni's conclusion: "there is nothing that is exponential", so the algorithm is very quick. The cost of this speed is possibly suboptimal solutions.

## Upcoming Classes

**Reference:** None (not in slides)

The next class is the second lecture on basics of game theory. The two classes after that are exercise sessions on game theory and on coalition formation.
