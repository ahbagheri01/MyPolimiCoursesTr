# MAS-20261006-GameTheory-Part1-Gatti — Additional Professor Notes

**Transcripts:** Nicola Gatti's Personal Room-20261006 0806-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\Multi agents\Slides and notes-20261005\Notes on game theory (by prof. Nicola Gatti).pdf

## Lecture Format and Where the Material Comes From

**Reference:** None (not in slides)

Gatti taught the two game-theory lectures on the blackboard. His handwritten notes are published on the course website by the teaching assistant, Francesco Amigoni. For his last lecture of the course he will use slides, and these will also be posted only after the lecture. This lecture covered only the normal form (one-shot) part. Extensive-form games were left for the next lecture.

## Why Formal Game Theory Matters for Agents (GANs Example)

**Reference:** None (not in slides)

Gatti said formal tools are needed if you want any guarantees about how agents behave, and game theory exists to provide those formal results. He also argued that game theory shows up in modern AI: training a generative adversarial network is exactly a two-player game between the generator and the discriminator.

## One-Shot vs Sequential Games, and Why Chess and Poker Differ

**Reference:** Notes on game theory, p.1, p.8–9

- **One-shot games** (e.g., rock-paper-scissors): each player makes a single move and the game ends. These are modelled with the **normal form**, also called the **strategic form**.
- **Sequential games** (chess, poker): players can make several moves, one after another. These are modelled with the **extensive form** (next lecture).
- Chess and poker are both sequential but structurally different. In chess every player observes every move. In a card game, drawing a card is technically a move by **nature**, and the other players do not observe it: you see your own card but not the others'. Information is therefore partial, which is called **imperfect information**.

## Utility Numbers Are Arbitrary: Fix the Meaning of Outcomes First

**Reference:** Notes on game theory, p.2

- Agents are utility maximizers: if one outcome is better for an agent, its utility must be higher. "Agent" and "player" mean the same thing. U1 and U2 generally differ because each player values the outcomes differently.
- Method: first label what each outcome means (tie, win for player 1, win for player 2), then assign numbers. The values are in principle arbitrary.
- RPS convention: tie = 0, meaning that if you neither win nor lose your current state of the world does not change. Winner = 1, loser = −1. You could use 10, 12 or 100 for the winner instead, and "nothing changes" as long as the loser gets exactly the opposite.
- Battle of the sexes / Bach or Stravinsky: the worst outcome for both is going to a concert **alone**, whichever concert it is. The boy prefers Bach and the girl prefers Stravinsky. The story only gives a **ranking**, not how strongly each one prefers their concert, so the textbook numbers (2,1 / 0,0 / 1,2) are just one arbitrary choice.

## The Normal Form Describes Rules, Not Behaviour

**Reference:** Notes on game theory, p.1–3

Gatti stressed that the normal-form table is a **static description of the rules**: it says what actions exist and which outcome follows if they are played. It says nothing about how the players will actually behave. Behaviour is a separate concept, the **strategy**.

## Why Randomization Is Natural: RPS and Bluffing in Poker

**Reference:** Notes on game theory, p.3–4

- The best strategy in rock-paper-scissors is to play each action with probability 1/3, **independently of what you or the opponent played before**.
- A **bluff** means playing differently in different situations while holding the same cards, which is the same as randomizing over actions. So finding the best poker strategy means finding the best randomization over actions.
- This is why a player's behaviour is in general a probability distribution over actions, not a single action. Gatti noted that writing σ_i as a function A_i → [0,1] is "formally not exactly correct" but acceptable at this level. A strategy is **pure** if one action has probability 1. It is **mixed** if at least two actions have strictly positive probability.

## Mixed Profiles Produce Lotteries: Worked RPS Expected-Utility Example

**Reference:** None (not in slides)

- If both players play pure strategies (e.g., both (1,0,0), so R vs R), the outcome is a single cell. In this example it is a tie, and both players get 0.
- If both play R with 1/2 and P with 1/2 (S never played), there is no single outcome. There is a **lottery**, i.e., a probability distribution over outcomes: RR, RP, PR and PP each have probability 1/4.
- The right notion is then **expected utility**: the sum over outcomes of utility × probability.
  - Player 1: 0·¼ + (−1)·¼ + 1·¼ + 0·¼ = 0.
  - Player 2: 0·¼ + 1·¼ + (−1)·¼ + 0·¼ = 0.
- Interpretation: half the time the game is a tie and each player wins one time in four, so they have equal chances.
- Answering a student, Gatti said you cannot define a player's utility from their own action alone. Without the others' strategies you cannot tell which cells will be reached.
- He also said that in this setting the players know the utility functions, but this is not true in general. These strategies were only an example for computing expected utility, not a claim that they are the solution.

## Why "Best Strategies" Is Not an Ordinary Optimization Problem

**Reference:** Notes on game theory, p.4–5

- The question game theory asks: the input is a game, and the output is one strategy per player such that these are the "best" strategies.
- This is unlike optimization or operations research, where there is a single objective to maximize. Here there are several players.
- It is not true in general that maximizing one player's utility minimizes the other's. In Bach or Stravinsky there is no outcome that is best for both. So defining "best" is not simple, and game theory has no single notion of equilibrium.
- The Nash equilibrium is "probably the most famous" notion and the first one taught.

## Reading the Nash Definition as "No Profitable Unilateral Deviation"

**Reference:** Notes on game theory, p.5

Gatti wrote the definition in expected-utility form: σ* = (σ1*, …, σn*) is a Nash equilibrium if, for every player i and every strategy σ_i, E[U_i(σ*)] ≥ E[U_i(σ_i, σ*_{−i})].

- The left side is what player i expects if everyone follows the equilibrium.
- The right side is what player i gets if all the others follow the equilibrium's recommendation while i alone plays something else.

The meaning: no player can get more by individually changing away from the recommended strategy.

## How to Verify a Profile (as Opposed to Finding an Equilibrium)

**Reference:** Notes on game theory, p.5

- This lecture only covered **verifying** whether a given profile is a Nash equilibrium, not searching for one.
- To show a profile is **not** a Nash equilibrium, it is enough to find **one** player who gains by deviating. Example in BoS with (B,S), outcome 0,0: if player 1 switches to S the outcome becomes (S,S) and player 1 gets 1 instead of 0, so (B,S) is not a Nash equilibrium.
- Only **unilateral** deviations are checked, with the other players' strategies kept fixed. Player 1 moves along the column (changes row) and player 2 moves along the row (changes column). The "diagonal" move, where both change at once, is not part of Nash's definition. It would only matter for a concept that allows joint deviations.

## Multiple Equilibria and the Equilibrium Selection Problem

**Reference:** Notes on game theory, p.5

- In BoS both (B,B) and (S,S) are Nash equilibria. A game can have several equilibria.
- Gatti remarked that one equilibrium may look better than another for the players, yet both are still Nash equilibria. (The transcript says "better for both players", which does not literally hold in BoS, so this is ASR-unclear.)
- A Nash equilibrium is just a **stable state** that no player wants to leave unilaterally. Nash only checks stability. Choosing among several equilibria is **not a problem Nash's concept addresses**.

## Pure Strategies Can Fail, But a Nash Equilibrium Always Exists

**Reference:** Notes on game theory, p.5, p.7

- In matching pennies (blackboard labels: A/B for player 1, C/D for player 2), every pure profile has a deviator, and the deviator alternates between the players around the table. RPS behaves the same way: from each cell the next deviator moves to the action that beats the current one.
- A student suggested that Nash equilibria exist only under some conditions. Gatti said: "No way. Nash equilibrium always exists. Always." What had been left out was that σ need not be pure. It can be mixed.

## Indifference Principle: Why a Rational Player Randomizes Only When Indifferent

**Reference:** Notes on game theory, p.6–7

Gatti warned that this is "usually the most difficult point to understand by the students."

- **Gift analogy:** if you can choose between a gift worth one million and a gift worth one euro, you always take the million. Whenever one option is strictly better you always choose it, so you never randomize.
- A rational player can play either of two actions only when **indifferent** between them, i.e., when the two expected utilities are **equal**.
- The mixed strategies are written (α, 1−α) for player 1 and (β, 1−β) for player 2, with α and β strictly between 0 and 1. Otherwise the strategy is the degenerate pure case.

## The Indifference Calculation Is "Crossed"

**Reference:** Notes on game theory, p.6–7

- **Matching pennies, player 1:**
  - E[A] = 1·β + (−1)·(1−β)
  - E[B] = −1·β + 1·(1−β)
  - Setting them equal gives β = 1/2. So for player 1 to actually randomize over A and B, **player 2** must play C and D with probability 1/2 each.
- **Player 2:**
  - E[C] = −1·α + 1·(1−α)
  - E[D] = 1·α − 1·(1−α)
  - Setting them equal gives α = 1/2.
- Key point: player 1's indifference condition fixes the **opponent's** probability, not player 1's own. Requiring player 1 to be indifferent between A and B does not say with what probability player 1 plays A or B.

## Exercise and the Odd-Number-of-Equilibria Result

**Reference:** Notes on game theory, p.6–7

- **Exercise for next time:** look for a mixed-strategy Nash equilibrium in Bach or Stravinsky using the same reasoning. Gatti said that if you can find it, you have understood the method. (The published notes already contain the BoS mixed computation, p.6–7.)
- Gatti cited a result attributed to Nash: except for **degenerate games**, the number of Nash equilibria is **odd**.
- BoS is not degenerate and has two pure equilibria, so a third, mixed one must exist.
