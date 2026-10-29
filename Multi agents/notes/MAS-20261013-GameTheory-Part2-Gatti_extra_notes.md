# MAS-20261013-GameTheory-Part2-Gatti — Additional Professor Notes

**Transcripts:** Nicola Gatti's Personal Room-20261013 0810-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Multi agents\Slides and notes-20261005\Notes on game theory (by prof. Nicola Gatti).pdf

## Odd Number of Equilibria Tells You a Mixed Equilibrium Must Exist (or Cannot)

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 5-7

The professor recalled a property from the previous lecture: except in degenerate games, the number of Nash equilibria is odd. He used it in two ways:
- Bach or Stravinsky has two pure Nash equilibria, (B,B) and (S,S), and is not degenerate. So there must be a third equilibrium, and it must be mixed. This is why the mixed one is worth looking for.
- In the prisoner's-dilemma-like game discussed later, there is exactly one pure equilibrium. So there can be no mixed equilibrium, because adding one would make the count even. That game has a single Nash equilibrium, and it is pure.

He used the same reasoning when building the normal form of a game tree: two pure equilibria were found, so a third, mixed equilibrium must also exist (its probabilities were not computed).

## Indifference Principle Behind the Mixed-Equilibrium Computation

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 6-7

The written notes show the algebra. The professor named the rule behind it, the **indifference principle**: a player can randomize over several actions only if every action played with strictly positive probability gives the same expected utility.
- With σ2 = (β, 1−β) on (B, S): E[U1(B)] = 2β + 0, and E[U1(S)] = 0 + 1·(1−β). This is one linear equation in one variable, giving 3β = 1, so β = 1/3.
- Computing an expected utility just means keeping the row of the action you are evaluating, then summing each payoff times the probability that the opponent plays that column ("value of the event times probability of the event"). Terms with payoff 0 vanish.
- The equilibrium probabilities depend on the exact payoffs. Changing the numbers even slightly changes them.
- Sanity check: the result is "reversed" for the two players (σ1 = (2/3, 1/3), σ2 = (1/3, 2/3)). This makes sense because each player gets 2 in a different outcome.

## Why Mixed Equilibria Are Only Computed for 2×2 Games (Exam Scope)

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 6-7

Beyond two actions per player, finding a mixed Nash equilibrium becomes a **combinatorial problem**. The hard part is identifying the **support**, i.e. which actions are played with positive probability:
- In Rock-Paper-Scissors you may "know" the answer is (1/3, 1/3, 1/3), but only because you know those specific payoffs. With arbitrary payoffs and 3 actions, the equilibrium could randomize over any pair of actions. Each player has 3 possible pairs (RP, RS, PS), so there are 9 pair combinations.
- With k actions per player, the number of pair-of-pairs combinations is of the order of k^4. Supports of size 3 or more must also be considered.
- You do not know in advance whether a mixed equilibrium exists on a given support. You must check.

**Exam:** the professor stated that the only mixed-equilibrium computation students can be asked to do is for **two players with two actions each, no more**.

## Expected Utility at the Mixed Equilibrium of Bach or Stravinsky (Common Mistake)

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 6-7

The professor plotted the three equilibria in the (U1, U2) plane: (2,1), (1,2), and the mixed one. Students answered 5/3 or proposed summing 2/3 + 2/3. Both are wrong. The correct calculation for player 1:
- E[U1(B)] = 2·(1/3) + 0 = 2/3, and E[U1(S)] = 1·(2/3) = 2/3. They are equal, as the indifference principle requires.
- Player 1's overall expected utility mixes these with player 1's own probabilities: (2/3)·(2/3) + (1/3)·(2/3) = 2/3. Combining two equal values with any probabilities gives the same value. Also, 2/3 is player 1's probability of playing B, not his utility. Do not confuse the two.
- By the (near-)symmetry of the game, player 2 also expects 2/3. So the mixed equilibrium sits at (2/3, 2/3).

He urged students to revise basic probability and expected values, noting they are essential in any machine-learning course.

## Pareto Efficiency: Mixed BoS Equilibrium Is Pareto-Dominated

**Reference:** None (not in the notes)

Pareto efficiency applies to **multi-criteria decision making**, i.e. several objective functions instead of one.
- Example: buying a service while considering not only its cost but also its quality, or its response time for a computation service.
- Pareto efficiency **does not tell you which solution is best**. It only discards inefficient ones: a solution is dominated if another one is at least as good on all criteria and better on some.
- In a game, the criteria are the players' expected utilities. In Bach or Stravinsky, both pure equilibria (2,1) and (1,2) are better for **both** players than the mixed one (2/3, 2/3). So the mixed equilibrium lies in the dominated region (below and to the left) and is Pareto-dominated by the pure equilibria.

## Nash Is Individually Rational, Not Socially Efficient (Collusion)

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 3, 5 (prisoner's dilemma)

The professor then applied Pareto analysis to **all** pure outcomes of a prisoner's-dilemma-like game, not just the equilibria. In that game the only Nash equilibrium is (A,C) with payoffs (1,1), while (B,D) gives (3,3).
- The other outcomes lie on the Pareto frontier. The unique Nash equilibrium lies **in the inefficient (Pareto-dominated) region**.
- Message: a Nash equilibrium is always **individually rational**, meaning no player can do better by deviating alone. It is not necessarily **socially efficient**.
- (3,3) is not stable: each player has an incentive to switch and get 4.
- If players could agree to play something else, they could get more. In markets such an agreement is **collusion**. In Europe and worldwide, competition authorities monitor markets and punish collusion: they accept that firms play a Nash equilibrium, but not that firms coordinate to raise prices at customers' expense.

## Clarifications From Student Questions on Equilibria and Efficiency

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 5

- **Deviations are unilateral:** player 1 controls only the rows and player 2 only the columns. Player 1 can switch from A to B but cannot change C to D. A single player can never move the outcome "diagonally" towards the mutually better cell, because that needs both players to change.
- **A Nash equilibrium is a profile for all players.** There is no "Nash of player 1". What can differ between players is the utility each gets at the equilibrium, and that depends on the game.
- **A Nash equilibrium is not always inefficient, it only may be.** In a game where the equilibrium gives (10,10) and the other outcomes give (1,1) or (0,0), the equilibrium is Pareto efficient (payoffs ASR unclear). In the prisoner's dilemma, the unique equilibrium is Pareto-dominated.

## Dominated Strategies Left for Self-Study

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 12-15

For lack of time, the professor skipped dominated strategies in class and told students to study them on their own from the notes uploaded by Francesco Amigoni. He warned that **dominance of strategies is not the same as Pareto domination**. They are different concepts.

## Game-Tree Node Labels and Degenerate Nodes

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 8

- In the label "i.j", i is the player and j is **only an identifier**. It is not the order in which the player moves. For example, player 2 has nodes 2.1 (left) and 2.2 (right), but she plays at only one of them, depending on player 1's move. She never plays at 2.1 and then at 2.2.
- A decision node can have any number of actions. A node with a single action can be drawn but is useless, because the player has no real decision there.

## Where Perfect Information Fails, and How the Information Set Models It

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 8-9

- Perfect information means that whenever a player moves, he knows exactly which node he is at, i.e. everything played before.
- Two everyday counterexamples:
  - In poker, the first player to move does not know the opponents' cards.
  - In Rock-Paper-Scissors, you choose without knowing the opponent's choice.
- The **information structure** describes what each player knows.
- In the tree version of Bach or Stravinsky, the two nodes of player 2 are joined into one information set. Player 2 **plays only once**, but is uncertain about which of the two nodes she is actually at, because she has not seen whether player 1 chose B or S.

## Three-Card Example: Modelling Nature and Building Information Sets

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 8-9 (the notes use a die and a K/Q example instead)

The professor's in-class example used three cards (King, Queen, Jack) and two players:
- Drawing a card is not a strategic choice. It is modelled by **nature**, a non-strategic player whose action probabilities are fixed and controlled by no one. Nature first deals player 1 a card (1/3 each), then deals player 2 one of the remaining two cards (1/2 each).
- The two levels could be merged into a single nature node with 6 actions, which is "absolutely the same". They were split only for clarity.
- After the deal, player 1 has two actions, A or B (e.g. in poker: bid or leave the game).
- **Player 1's information sets:** nodes are connected when player 1 holds the same card. For example, "player 1 has K, player 2 has Q" and "player 1 has K, player 2 has J" are the same information set. This gives 1.1, 1.2, 1.3.
- **Player 2's information sets:** actions are **public**, so player 2 observes player 1's move. Player 2's nodes are connected only when player 2 holds the same card **and** player 1 played the same action. The professor did not draw them all, because doing so is "a mess": not difficult, but a lot of work.

## Computing Nash Equilibria of a Tree via Its Normal Form; Plans

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 9-11

- The standard approach, the one mathematicians and economists followed, is: from the game tree, generate the equivalent normal form, then find Nash equilibria in the table as before.
- A **plan** is a tuple with **one position per information set** of the player, each holding an action. It fixes the player's behaviour at every decision point.
- A singleton node is a "degenerate" information set but still counts. So player 1 with nodes 1.1 and 1.2 has pairs of actions, while a player with one information set has tuples of length one.
- Plans such as L1L2 and L1R2 look strange: playing L1 prevents player 1 from ever moving again, so the two plans always give the same outcome. The **reduced normal form** removes this redundancy, but the professor said it is "not important". The course keeps the basic (unreduced) representation.
- A student asked whether a particular cell was a Nash equilibrium. The answer was no, because player 1 could switch to R1L2 and get 2 instead of 1 (exact payoffs ASR unclear).
- The professor said students will never be given a game with nature to translate into normal form, because the calculation is long (as stated in class).

## Why Nash Is Unsatisfactory in Trees: Non-Credible Threats

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 11 (the notes use payoffs (1,4), (0,0), (4,1))

In extensive-form games, Nash equilibrium may give **unreasonable** solutions, so a stronger concept is needed: **subgame perfect equilibrium**. The in-class example had different numbers from the notes:
- Player 1 chooses L, ending at (2,2), or R. After R, player 2 chooses L (low payoff for her, below 1) or R, giving (4,1). (Some payoffs ASR unclear.)
- The normal form has two pure Nash equilibria: (L, l) giving (2,2), and (R, r) giving (4,1).
- (2,2) does not make sense. The reason is **not** simply that player 2 never gets to move, since you must still specify what she would do. The reason is that if player 2 ever reaches her node, R gives her more than L, so playing L there is never rational.
- Her "I will play L" is a **fake threat**: it is meant to push player 1 to choose L, but she would not carry it out. (2,2) is a Nash equilibrium but **not credible** given the sequential structure of the game.

## Subgames and Backward Induction in Practice

**Reference:** Notes on game theory (by prof. Nicola Gatti).pdf, p. 11-12

- A subgame must start at a decision node that is a **singleton information set**. You cannot start a subgame at a node belonging to a larger information set, even if the part below looks self-contained.
- **Procedure:**
  1. Start from the bottom.
  2. In each smallest subgame, find the player's best behaviour.
  3. Replace that subgame with the resulting payoffs (e.g. (4,1)).
  4. Move up a level and repeat. In the example, player 1 compares 2 and 4 and plays R.
- In a larger example, the root player ended up getting 3 either way. He is **indifferent and can choose anything**, so several subgame perfect equilibria can exist.
- A subgame perfect equilibrium is always a Nash equilibrium. The SPE are a subset of the Nash equilibria, and this set is **always non-empty**.
- In answer to a student's question (ASR unclear), the professor said the model has no constraint on what it can represent: in principle, even a game with a single player is allowed.
