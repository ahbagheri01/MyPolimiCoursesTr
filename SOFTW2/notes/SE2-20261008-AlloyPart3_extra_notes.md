# SE2-20261008-AlloyPart3 — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261008.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf

> **Coverage notes:** Slide references use the printed slide numbers. The PDF has no printed slide 61, so from slide 62 on the PDF page number is one lower (e.g. slide 62 = PDF p. 61). The deck is shared with the 30/09 and 07/10 lectures; this lecture covered roughly slides 30–65 (family tree through `eventually`). The transcript has a gap: the introduction of the `NoSelfFather` assertion (slide 44) is cut off, and the recording resumes mid-sentence ("…equal to m dot father").

## Binary vs. Ternary Fields: The Enclosing Signature Is the First Column

**Reference:** 03a.AlloyPart1-2.pdf, slides 12, 30–32

The professor compared the family-tree fields with the address-book field:

- In `Book { addr: Name -> lone Addr }` the declared type is itself a Cartesian product (Name × Addr). Adding the enclosing signature (the context, Book) gives three elements per tuple, so `addr` is **ternary**.
- In `Person { father: lone Man }` the declared type is a single signature, so `father` is **binary**: pairs (Person, Man). Likewise `mother` is pairs (Person, Woman).
- Tuples are **ordered**. In `father`, the first element is any Person (a man or a woman) and the second must be a Man.
- Analogy: a signature is like a class, and its fields are like attributes in OO programming. In Alloy, though, fields are relations between the signature's atoms and the atoms of the field's type.
- In the meta-model figure, the black arrows are the `extends` links and the coloured arrows are the declared relations.

## Signature Multiplicity: `one`, `some`, and the Default

**Reference:** 03a.AlloyPart1-2.pdf, slide 31

- `one sig Book` means every instance has exactly one Book atom. It constrains how many atoms the signature can have.
- `some sig …` means every instance must contain at least one atom of that signature.
- If you write nothing, the signature behaves as a plain set: it can be empty or contain one or more atoms. This is the usual case, but sometimes adding such a constraint is convenient.

## The Unconstrained Family Model Gives a "Mess", and Alloy Considers It Legal

**Reference:** 03a.AlloyPart1-2.pdf, slides 30, 36

The professor ran the bare model (only the signatures) in the Analyzer. Because there was no predicate or `run` command, the Analyzer created a default predicate and a default run command.

The instance it found:

- Woman0's father is a man who is also her husband.
- That man is his own father.
- From the man's side, his wife is not Woman0 but Woman1, who is also the mother.

All of this is a perfectly legal model for Alloy. The Analyzer just connects atoms through the declared relations, because no rule says otherwise. Adding constraints (e.g. "a woman cannot marry her father") is the modeller's job, and these rules must hold at all times, which is what facts are for.

## What Facts Mean for `run` and `check`, and Why Predicates Need Not Hold

**Reference:** 03a.AlloyPart1-2.pdf, slides 42–43

- Whatever is in a fact must hold in **every** instantiation: for every predicate you run and also for every assertion you check.
- A predicate's constraints must be true only when that predicate is the one being run. A model can contain many predicates and many `run` commands. The constraints in predicates that are not part of the executed run do not have to hold.

## Worked Join Example: When `p.(mother+father).father` Contains `p`

**Reference:** 03a.AlloyPart1-2.pdf, slides 34–35

The professor built a small instance on the board to show how `grandpas` evaluates. The tuples are partly garbled in the ASR; this is the most consistent reading:

- mother = {(M1,W1), (M2,W1), (W1,W2)}
- father = {(M1,M3), (W3,M3)}
- p = {M1}

Evaluation:

1. `mother + father` is the union of the two sets of pairs.
2. Joining p with it keeps the pairs whose first element is M1, so `p.(mother+father)` = {W1, M3}.
3. Joining with `father` looks for pairs that start with W1 or M3. There are none, so the result is the **empty set**: M1 has no grandfathers.
4. Now add (W1, M1) to `father`. W1 now joins with M1, so the function returns {M1}. M1 is his own grandfather and `ownGrandpa[M1]` is true.

Running `ownGrandpa` without any fact does find such an instance. Pressing *New* in the Analyzer shows other instances that also satisfy the predicate. The slide's command uses `for 4 Person`. The professor noted that without an explicit bound, the Analyzer uses its default scope.

`p in p.grandpas` and `p in grandpas[p]` are fully equivalent. Note the **square brackets** in the call (not round parentheses). The second form is probably more intuitive because p is the function's parameter.

## Why Transitive Closure Is Needed, Shown on the Same Example

**Reference:** 03a.AlloyPart1-2.pdf, slides 37–39

- The enumerated fact on slide 37 (parent, or grandparent, or great-grandparent, …) cannot be written in full. We do not know in advance how many atoms an instantiation will have, so we do not know how many levels to list. `^` states "at any level" compactly.
- On the worked example, with (M1,W1) in `mother` and (W1,M1) in `father`, the closure `^(mother+father)` contains the derived pair **(M1, M1)**, because M1 reaches W1 and W1 reaches M1. This is exactly the pair that the fact `no p: Person | p in p.^(mother+father)` forbids.

## Demo After Adding the No-Ancestor Fact

**Reference:** 03a.AlloyPart1-2.pdf, slides 39, 46

- With the fact added, `run ownGrandpa` finds **no instance**, as expected.
- Commenting out the run command (with `//`) makes the Analyzer fall back to the default run command, which does not call `ownGrandpa`, so instances appear again.
- In those instances the "own ancestor" problem is gone, but others remain. For example, two people are linked both by `mother` and by `husband`. More facts are needed.

## Two Equivalent Styles for the Husband/Wife Constraint

**Reference:** 03a.AlloyPart1-2.pdf, slides 40–41

- `all m: Man, w: Woman | m.wife = w iff w.husband = m` is the **logic style**. `wife = ~husband` is the **set-operator style**. The professor said they are exactly equivalent, just written in two completely different styles. In general, Alloy offers several ways to express the same constraint.
- Why the transpose works: by definition, `wife` holds (Man, Woman) pairs and `husband` holds (Woman, Man) pairs. Transposing `husband` flips every pair to (Man, Woman), and the fact requires the two sets to be identical.
- On the board he also transposed his example set, giving pairs such as (M3,M1), (M3,W3), (M1,W1): every pair is simply reversed.

## Why Write an Assertion the Facts Already Guarantee

**Reference:** 03a.AlloyPart1-2.pdf, slide 44

Once the no-ancestor fact is in the model, checking `NoSelfFather` (`no m: Man | m = m.father`) can never give a counterexample. Writing such assertions is still worth it. You may think the model says something, but if you made a mistake, an assertion you expected to pass will produce a counterexample. Assertions therefore also serve to **debug** the model and check that it makes sense.

## Fact Names Are Ignored by the Analyzer, Unlike Predicate, Function and Assertion Names

**Reference:** 03a.AlloyPart1-2.pdf, slide 45

A fact's name (e.g. `SocialConvention`) only helps us read the model and understand what the fact is about. The Analyzer does not use it. Names of predicates and functions do matter, because you call them. Assertion names matter too, since `check` refers to them. For facts, the name is "just for us".

## Reading `SocialConvention`, and Why It Still Allows Married Siblings

**Reference:** 03a.AlloyPart1-2.pdf, slides 45–46

- **Reading it:** `^(mother+father)` is the set of all (person, ancestor) pairs. `wife + husband` holds both (Man, Woman) and (Woman, Man) pairs. `&` is intersection (he let the class guess it), and `no` requires that intersection to be empty.
- **What the run showed:** the man's wife has him as her husband, so the husband/wife fact works. But both of them have the same father, so they are brother and sister.
- **Why the fact misses this:** it only forbids the *same pair* from appearing in both relations, e.g. you cannot be married to your father. It says nothing about two spouses sharing a father, a mother, or a grandfather. He called fixing this "not easy" and invited students to run the different attempts in the Analyzer.

## `SocialConvention2` Is the Same Fact in Logic Style: Set vs. Logic Style

**Reference:** 03a.AlloyPart1-2.pdf, slide 47

- `SocialConvention2` says that if m and w are husband and wife, m is not among w's ancestors and w is not among m's ancestors. This is exactly what `SocialConvention` says, so it does **not** solve the common-ancestor problem.
- **Trade-off between the styles:** the set-operator style gives very compact facts. The logic style is more verbose but probably easier for us to write. Which one to use depends on taste and on how comfortable you are with set operators.
- The various attempts on slides 47–53 came from proposals students made in a class three or four years ago. There was no time this year for that kind of session, because the time-related features of Alloy 6 still had to be covered.

## Using the Analyzer to Decide Which of Two Facts Is Stronger

**Reference:** 03a.AlloyPart1-2.pdf, slides 48–51

- Whether `noCommonAncestors` (slide 48) actually works was left as an exercise: copy it into the Analyzer and test it. `none` is the empty set.
- **Method for comparing two facts** without analysing complex formulas by hand:
  1. Rewrite each fact as a predicate. These predicates have no parameters, so they are declared without brackets.
  2. Write two assertions, one for each implication (`Stronger`: noCommonAncestors ⇒ SocialConvention3, and `NotStronger`: the reverse).
  3. Check both. The one with no counterexample tells you which fact is stronger.
- It is also possible that **both** checks find counterexamples. Then neither fact is stronger than the other.

## `SocialConvention4` Fixes the Slide-52 Case, but the Model Is Never "Complete"

**Reference:** 03a.AlloyPart1-2.pdf, slides 52–53

- Even with `noCommonAncestors`, you can get the slide-52 situation: a man has a mother and a father, and the mother's father is that same man's father.
- The professor answered the slide-53 question ("Does this address the problem?") with yes. `SocialConvention4` says that if p1 is a parent of p2, then p1's parents and p2's parents share no one. Try it and the problem disappears, because a parent's parents can no longer reappear at another level of the ancestor hierarchy.
- Other problems still remain. Fixing everything would take many constraints, and the goal is not a fully correct family model. The example is there to show different facts and different styles of writing constraints, and to encourage playing with them.

## Without `var`, Every Instance Is a Snapshot

**Reference:** 03a.AlloyPart1-2.pdf, slides 55–56

The professor said he had not stressed this enough before: in the Alloy seen so far, everything is static. An instance is a snapshot at one point in time, and the passing of time cannot be modelled. The only way around it was tricks like `b`/`bpost`, i.e. two Book atoms standing for two versions of the same book. With `var`, a single Book atom is enough, and you describe how its `addr` tuples change over time.

## Time Is Discrete Steps, and a Cardinality Constraint Does Not Impose Continuity

**Reference:** 03a.AlloyPart1-2.pdf, slides 56–57

- Time in Alloy 6 is modelled simply: an initial step followed by later steps. It is **not continuous**. `after` moves forward exactly one step.
- In `show`, the constraints are only about the **size** of `b.addr` (0, then 1, then 2). Nothing forces the tuples to carry over. For example, step 1 could contain (N0, A3) and step 2 could contain (N1, A1) and (N2, A2), without (N0, A3). Requiring that earlier tuples are kept is possible, but it has to be stated explicitly.
- The `;` version on slide 57 is completely equivalent to the nested `after` version.

## Running and Reading Temporal Instances in the Analyzer

**Reference:** 03a.AlloyPart1-2.pdf, slide 58

- `run show for 3 but 1 Book, 3 steps`: at most 3 atoms for each signature except Book (exactly 1 allowed here), and traces of 3 steps.
- The visualizer shows **two steps at a time**: the current step on the left and the next one on the right. In the slide's trace bar, the third step is grey because it is not on screen. A button moves the view forward, so you can see step 1 next to step 2. In the live run, step 2 contained (Name0, Addr) in addition to step 1's (Name1, Addr).
- *New* starts a completely new instantiation, so you can explore other evolutions.
- **Practical pitfalls from the live demo:** code pasted from PowerPoint brought in bad characters that caused syntax errors. After fixing those, he still had to add a missing parenthesis and the missing parameter declaration (`b: Book`) before the predicate would run.

## Primed Expressions Replace the `b`/`bpost`/`bppost` Atoms

**Reference:** 03a.AlloyPart1-2.pdf, slides 59–60

- The prime can be applied to sets in general, not only to fields. `b.addr'` is the value of `b.addr` in the next step.
- Primes can be stacked: `b.addr''` is the value two steps later. It plays the role that `bppost` played in the old version of `delUndoesAdd`, so the assertion no longer needs extra Book atoms. The professor called this a more elegant formulation.

## `always`: Needed for "At Any Time", and Used in Almost Every Fact

**Reference:** 03a.AlloyPart1-2.pdf, slide 62

- Without a temporal operator in front, the slide-60 assertion only describes what happens from the initial instant. To require that delete undoes add at any point in the system's execution, the whole expression has to be wrapped in `always`. (This passage is partly garbled in the ASR.)
- **Rule of thumb:** facts that state the rules of a model with variable elements are meant to hold at any time and in any situation. So in about "99% of the cases" a fact over mutable elements uses `always`.

## When to Use `enum` and When Abstract Signatures Are Needed

**Reference:** 03a.AlloyPart1-2.pdf, slide 63

- `enum DevStatus { Working, Broken }` is equivalent in the end to an abstract signature with extending sub-signatures, just as Person is divided into Man and Woman.
- `enum` suits DevStatus because Working and Broken have no characteristics of their own, and no relations need to be declared on them. Using abstract signatures there would only make the model longer (the ASR says "more buttons", probably "more verbose").
- Person/Man/Woman **cannot** be modelled with `enum`, because Man and Woman need their own fields (`wife`, `husband`).

## `NoRepair`: Why an Always-Working Device Satisfies It, and an Open Question

**Reference:** 03a.AlloyPart1-2.pdf, slides 64–65

- The fact combines two temporal operators, `after` and `always`. The professor left a question for the next lecture: could one of them be dropped without changing the meaning, or not? (ASR unclear on exactly which operator he meant, most likely the `after`.)
- A trace that is Working, Working, then Broken forever satisfies the fact.
- A device that stays Working its whole life also satisfies it, because the premise of the implication (status = Broken) is never true.
- `NotAlwaysFunctioning` (slide 65) instead makes the break certain: a working device must become Broken at some future instant, though the fact does not say when.

## Wrap-Up and Next Lecture

**Reference:** 03a.AlloyPart1-2.pdf, slides 66–71

The remaining temporal operators were postponed to the next lecture, the following week. The deck continues with the past operators on slides 66–71. The professor asked students to run all the examples in the Analyzer, try variants of them, and experiment.
