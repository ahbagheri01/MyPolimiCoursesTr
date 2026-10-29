# SE2-20261007-AlloyPart2 — Additional Professor Notes

**Transcripts:** Software Engineering 2 20261007.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SOFTW2\Slides-20261016\03a.AlloyPart1-2.pdf

## Alloy Is Case-Sensitive: `addr` and `Addr` Are Different Things

**Reference:** 03a.AlloyPart1-2.pdf, slide 12

The professor pointed out that the lowercase relation `addr` and the uppercase signature `Addr` are completely unrelated names, because Alloy distinguishes upper and lower case. The only link between them is that the relation `addr` has `Addr` as its last column. He also compared a signature to a class in an object-oriented language: it is the way to identify a kind of entity.

## Why `addr` Must Be Ternary, and What `lone` Restricts

**Reference:** 03a.AlloyPart1-2.pdf, slide 12

- **The example behind the ternary relation:** in one book my name can be associated with my address, while in another book the same name can be associated with a different address (or a different name can share the same address). The book plays a role in the association, so a binary Name–Addr relation is not enough. You need Book × Name × Addr.
- **Scope of `lone`:** the constraint holds *within one book*. In the same book a name cannot be associated with two different addresses: it has either no address or exactly one. Across different books it can have different addresses.

## "Instance Found" With Only Signatures Means the Model Is Consistent

**Reference:** 03a.AlloyPart1-2.pdf, slides 12, 17

Before writing any predicate, the professor executed a file containing only the three signatures. The Analyzer answered that an instance was found. He read this as: the specification is syntactically correct and consistent, so one or more instances of it can be generated. If you execute a file with no predicate and no `run` command, the Analyzer runs a default command (shown as "run default").

## How to Read an Instance in the Analyzer

**Reference:** 03a.AlloyPart1-2.pdf, slides 14-15

- **Graph view:** in the first instance there were three books, three addresses and two names, all atoms. Each arrow is one tuple of the ternary relation. For example, the arrow from Book0 to Addr2 labelled `addr [Name1]` is the tuple (Book0, Name1, Addr2): the name appears in brackets on the arrow. The professor called the graph view of larger instances "a bit of a nightmare" and moved the boxes around by hand to make them readable.
- **Textual and table views** show the same instance differently. Each signature is a set of atoms, and `addr` is a set of triples such as (Book0, Name1, Addr2) and (Book1, Name0, Addr1).
- **Tuple order follows the declaration:** every triple in `addr` starts with a book, then a name, then an address. A tuple such as (address, book, name) cannot appear.
- **Next instance:** a specification usually has many instances, in principle infinitely many. The *Next* button produces other ones. Consecutive instances tend to differ only a little, so at first they look the same. If you keep going you find differences (e.g., an instance with only two books). Browsing instances this way is how you check that they match your expectations.

## Built-in Sets in Every Instance: `univ`, `Int`, `String`, `none`

**Reference:** None (not in slides)

In the textual view the professor went through the predefined sets:

- `univ` is the universal set of all atoms in the instance. Besides the books, names and addresses, it includes the integers from −8 to 7. (He first said −7 to 7, then corrected himself.)
- `Int` is the set of integers. It is a basic type shared by every specification, so you can use it without declaring it.
- There is also a set related to sequences (`seq`), which the course does not cover for lack of time.
- `String` is empty in this instance.
- `none` is the empty set.

## Q&A: Who Builds the Universe, and Why Is the String Set Empty?

**Reference:** None (not in slides)

- **Do we have to write the universe?** No. The Analyzer computes it automatically. We specify the *types* (names, addresses, books), not the instances. The Analyzer then tries to build a "world" coherent with the specification, e.g. three books, three names and two addresses. It also adds the basic elements that appear in every instance (the integers −8..7, `none`, the `String` set).
- **Why is `String` empty?** Nothing in the specification prevents an empty `String` set, so it is a possible world. Other instances could have a non-empty one.
- **The general principle:** anything that the specification does not constrain is possible, and so the Analyzer may generate it. If you want to rule something out (e.g., a cardinality constraint on a set), you must state it, and then the instances must comply.

## The Dot Is a Join, Like in Databases but the Matched Column Is Dropped

**Reference:** 03a.AlloyPart1-2.pdf, slides 15-16

The professor called `.` the **join operator**. It works much like the database join you have already seen, with one specific difference: **the element used for the join is dropped** from the result. In `Book.addr`, B0 matches the first column of (B0,N0,A0) and (B0,N1,A1). Removing B0 gives (N0,A0) and (N1,A1). B1 likewise gives (N1,A2) and (N2,A2). Joining `myName` = {N1} then gives {A1, A2}.

How to read the expression: `myName.(Book.addr)` gives the addresses associated with my name in *any* of the books in the world (here, two books). He said this notation appears in all the examples that follow.

## The Empty `show` Predicate Only Carries the Scope

**Reference:** 03a.AlloyPart1-2.pdf, slide 17

`pred show {}` contains no constraint, so it is always true, and "you may argue that it is completely useless". Its purpose here is the command `run show for 3 but 1 Book`, which sets **upper bounds** on the size of each set in the generated instances. They are bounds, not exact sizes. The instance found had one book but only two names and two addresses, i.e. at most three, not exactly three. A predicate is executed with a `run` command, and everything written as a constraint inside it must hold in the generated instance. The professor added that constraints can also be written inside the braces, which the next predicates do.

## Several Predicates and Run Commands in One File

**Reference:** 03a.AlloyPart1-2.pdf, slides 17-18

- To keep several versions of the predicate in the same file, give them different names (the professor used `show`, `show2`, `show3`). Each one gets its own `run` command.
- Once at least one `run` command exists, that command is executed instead of the default one. When there are several, you choose which one to execute from the *Execute* menu.

## How to Read `#b.addr > 1` and `#Name.(b.addr) > 1`

**Reference:** 03a.AlloyPart1-2.pdf, slide 18

- `#` is the cardinality operator.
- Predicates can take parameters. Here `b` is a single book (a singleton) passed to `show`. `b.addr` returns the name–address pairs of that book only (e.g., Giovanni–Milano, Alice–Rome).
- `Name.(b.addr)` joins the set of *all* names with those pairs. This gives every address that some name has in the book. `#Name.(b.addr) > 1` therefore means the book must contain more than one distinct address.
- Constraints written on separate lines in a predicate are implicitly combined with **and**, so both must hold.
- In the instance, the Analyzer highlights the atom chosen as the parameter (Book1 in his run). In that book, Name0 was associated with Addr1 and Name1 with Addr0, which satisfies both constraints.

## Why `some n: Name | #n.(b.addr) > 1` Has No Instance

**Reference:** 03a.AlloyPart1-2.pdf, slide 18

The slide asks "Can we fulfil the constraint below?" The professor ran it as `show3`: **"No instance found. Predicate may be inconsistent."**

- **Locating the problem:** the first line (`#b.addr > 1`) is exactly what worked before, so the inconsistency must come from the second line.
- **Meaning of the quantifier:** with `some n: Name`, the names are considered one at a time, and `n` is a singleton. This is about the specific book `b`, not every book. The line requires *some name in b to be associated with two or more addresses*.
- **The contradiction:** the declaration `addr: Name -> lone Addr` says *at most one* address per name within a book, while the predicate says *more than one*. They state opposite things.
- **Showing the fix:** replacing `lone` with `set` in the signature makes `show3` produce an instance. In that instance a single name was associated with five addresses.

## Scope Syntax, and Why Enlarging the Scope Does Not Cure an Inconsistency

**Reference:** 03a.AlloyPart1-2.pdf, slides 17-18

- While investigating `show3`, the professor tried `run show3 for 5 but 1 Book`. This means at most five atoms (possibly fewer) for every signature, except at most one Book.
- **The scope is optional.** You can just write `run show3` and rely on the default bound, which he thought is "like three or four, I don't remember exactly" (uncertain as stated). Restricting Book is convenient when you want to study one address book only.
- **The scope was not the problem:** with 3 or 5, the number of elements does not matter. The inconsistency is logical (`lone` vs. `> 1`), so no scope can produce an instance.
- **Finding the cause is up to you:** when an inconsistency exists, the Analyzer cannot create an instance, and "it is on us to understand what is wrong in our specification".

## Why the Old Before/After Style Is Taught First

**Reference:** 03a.AlloyPart1-2.pdf, slides 19, 55

The add/delete operations are first written in the style used before Alloy 6's temporal extension. The professor did this on purpose, to show step by step the line of reasoning that led to that extension. Before Alloy had a notion of time, the only way to represent an entity evolving was to use **two different atoms for the same entity**: one for its state before the operation (`b`) and one for its state after (`bpost`). In the `add` predicate you then state what you expect the final state `bpost` to be, compared with `b`.

## Operations Are Described, Not Programmed

**Reference:** 03a.AlloyPart1-2.pdf, slides 5, 19-20, 25

- `bpost.addr = b.addr + n->a` is not an assignment or an algorithm. It is a condition stating that `bpost`'s pairs are `b`'s pairs **united** (`+`) with the pair `n->a`. In general `->` is the Cartesian product, and between two singletons it yields a single pair. The professor contrasted this with operational programming languages, where you write the procedure that performs the operation. In Alloy you declaratively state a property of `bpost` with respect to `b`.
- He repeated the point for `del` ("once again we are not providing a procedure") and for functions, which also describe their result descriptively, never operationally.
- Calling a predicate means writing its name with its parameters. `showAdd` is true only if `add` and its additional constraint are both true.

## The `showAdd` Instances, Including One Where `b` and `bpost` Are the Same Book

**Reference:** 03a.AlloyPart1-2.pdf, slides 19, 22

- **A "normal" instance:** Book2 played `b`, holding Name→Addr0 and Name→Addr1. Book1 played `bpost`, holding the same two pairs plus Name→Addr2, the newly added pair. Two addresses for the same name appeared only because the professor had forgotten to switch `set` back to `lone`. He said this was fine for the analysis.
- **A "strange" instance:** one atom, Book2, was both `b` and `bpost`. It already contained all the pairs (Name→Addr0, Addr1, Addr2). This is still consistent with `add`: if the pair being added is already in the set, the union returns the same set, so `bpost.addr = b.addr` holds with `bpost = b`.
- He warned that this case would cause a "strange effect" later (see the counterexample below). He concluded that before adding an element you should probably check that it is not already in the book.

## What `n->Addr` Removes in `del`

**Reference:** 03a.AlloyPart1-2.pdf, slide 20

In `bpost.addr = b.addr - n->Addr`, the Cartesian product is between the singleton `n` and the whole set `Addr`, which can contain many addresses. So `n->Addr` is every pair "n with some address". Subtracting it removes **all** addresses associated with that name from the book, not just one specific pair.

## Run vs. Check: What You Get Back When Something Fails

**Reference:** 03a.AlloyPart1-2.pdf, slides 21, 26

Predicates and assertions look similar but have different purposes, and they report failure differently:

- **`run` a predicate:** the Analyzer creates instances compatible with the whole specification plus the predicate's constraints. If something is inconsistent, you only get a message that the predicate may be inconsistent, and no instance at all.
- **`check` an assertion:** the Analyzer tests whether the assertion holds. If it does not, you get a **counterexample**: a concrete instance that contradicts the assertion, which you can inspect.

## The `delUndoesAdd` Counterexample, Explained

**Reference:** 03a.AlloyPart1-2.pdf, slides 21-22

- Before running the check, the professor switched `set` back to `lone` so that there would be fewer name–address pairs and the counterexample would be easier to read.
- **The counterexample found:** one book (Book2) is both `b` and `bpost` and contains Name→Addr1. Another book (Book1) is `bppost` and contains no pairs at all.
- **Why this violates the assertion:** intuitively add and delete are opposite operations, but here `add` has **no effect**, because the pair was already present and the union does not change the set. `del` **does** have an effect: it removes all of that name's addresses. So `bppost` is empty and differs from `b`. This is the "strange effect" anticipated in the `showAdd` instance where `b = bpost`.

## Two Ways to Fix `delUndoesAdd`, and Why the Assertion Was Changed

**Reference:** 03a.AlloyPart1-2.pdf, slide 22

The professor named two options:

1. **Change the assertion.** You can argue it is perfectly normal for `add` to behave as it does (adding an existing pair changes nothing). In that case the assertion should be restricted to the cases where it is meant to hold.
2. **Change the `add` operation**, so that it only applies when the name–address pair is not already in the book.

The slide's fix is option 1: the precondition `no n.(b.addr)` (nothing is associated with `n` in `b`). With it, `bpost` necessarily differs from `b`, because it contains the new pair n→a, and deleting `n` then returns exactly `b`'s pairs. Rerunning the check found no counterexample. He acknowledged the example needs attention and recommended going through it yourself in the Analyzer, trying different cases and options.

## Bounded Scope: Always Ask Whether It Is Large Enough

**Reference:** 03a.AlloyPart1-2.pdf, slide 23

Writing `for 4`/`for 5 but 1 Book` puts an upper bound on the number of atoms in each set, so every analysis is bounded. As a consequence, something that is not true in a smaller scope may become true in a larger one. You should always keep this in mind and ask: *is my scope large enough to reveal the problems, or could something different appear if I expand it?* The trade-off is cost: the larger the scope, the more computationally expensive the analysis.

## Testing and Bounded Verification Complement Each Other

**Reference:** 03a.AlloyPart1-2.pdf, slide 24

- **Bounded verification** is exhaustive: it analyzes *all* cases within the chosen bounds, but it sees nothing outside them.
- **Testing** samples the whole input space (all possible inputs to the system) and can try to cover it as well as possible, but it is never exhaustive.

Each has advantages and disadvantages, which is why the two are usually performed together: each provides information the other cannot.

## Functions vs. Predicates (and a First Look at Facts)

**Reference:** 03a.AlloyPart1-2.pdf, slides 25-27, 43

- A function is like a function in a programming language: it takes parameters and returns a value of a given type. `lookup[b, n]` is a shortcut for `n.(b.addr)`, the expression used many times in the earlier constraints, so you can call it whenever you need a name's addresses in a book.
- **Key difference:** a predicate returns a Boolean (true/false), while a function returns something else, here a set of addresses. Like predicates, functions are defined descriptively, not procedurally.
- **Facts** (shown in the next example): a fact must be true at any time in the specification. A predicate is evaluated only when it is called explicitly, through a `run` command or by being used inside something else (another predicate or an assertion).

## What `addLocal` States, and Its Result

**Reference:** 03a.AlloyPart1-2.pdf, slide 25

`addLocal` says that adding the pair (n1, a) to `b` leaves every *other* name n2 (n1 ≠ n2) untouched: `lookup[b, n2] = lookup[bpost, n2]`. In words, if n2 was in `b` it is also in `bpost` (with the same addresses), and if n2 was not in `b` it is not in `bpost` either. The professor said that if you check it, the assertion is verified (no counterexample within the scope).

## Family Example Preview and the Meta-Model View

**Reference:** 03a.AlloyPart1-2.pdf, slides 28-30

- **Why `Person` is abstract:** it is meant to be specialized into `Man` and `Woman` (`extends`). `father` and `mother` are binary relations from a person to a `Man` and to a `Woman`. They are `lone` because a person has either a man as father or nobody, and the same holds for the mother.
- **Meta-model view:** the Analyzer can display the meta-model, i.e. the signatures and the relations between them. He demonstrated it on the address book (Book, Name, Addr and the `addr` relation). The meta-model is at the level of signatures, and every specific instance must conform to it. In the family model the interesting part is that several relations (mother, father, wife, husband) have to be managed properly. That is where the next lecture continues.
