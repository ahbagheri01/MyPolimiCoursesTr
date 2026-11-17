# SMBUD-Ex-20261105-MongoDB-Practice — Additional Professor Notes

**Transcripts:** MongoDB_practice_Ettori_05-11-2026.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E03 - MongoDB\E03 - MongoDB Exercises on the Airbnb Dataset.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E03 - MongoDB\E03 - MongoDB.pdf

> **Coverage notes:** This was a short hands-on session, held right before the first mid-term test (on Neo4j), which started after the recording ended. The theory slides were not presented again. Exercises solved in class: Q1 (setup check), Q8, Q18, Q21(a–b), Q34, Q35, Q39, Q45, Q47–Q50 and Q27. The exercise sheet contains no solutions or expected counts, so the numbers below are the ones shown in class.

## Use the Simplest Construct That Answers the Question

**Reference:** E03 - MongoDB Exercises on the Airbnb Dataset.pdf p.1 (allowed constructs); Q8, Q18, Q27

- For a simple query that only needs one filter, use `findOne`/`find`. You don't need aggregation, unwind or group. You *could* write it with `aggregate`, but `find` is easier to write.
- If the question only asks for a number ("count the … listings"), use `countDocuments`. You could also use `find` or `aggregate` and count at the end, but `countDocuments` is "very handy".
- General advice: the constructs given in the sheet are enough to solve every exercise in the simplest way possible, even if other (aggregation-based) ways exist. Prefer the simplest one.

## Projections: Dropping _id, and the 0/1 Mixing Rule (Q8)

**Reference:** E03 - MongoDB.pdf slides 11–12; Exercises Q8

- `_id` is usually excluded from the output (`"_id": 0`). It is useful to the database itself (indexes, sorting), but not useful in the result. Q8 does not require removing it; the TA removed it anyway out of habit.
- Normally you cannot mix `0` and `1` in the same projection. The exception is `_id`: it can be set to `0` while the other fields are set to `1`. The TA added that this rule may depend on the MongoDB version.

## Extracting the Year Works Only Because first_review Is a Date (Q8)

**Reference:** E03 - MongoDB.pdf slide 11 ("year": {"$year": ...}); Exercises Q8

- The new fields `first_review_year` and `last_review_year` are created in the projection with `{"$year": "$first_review"}`. This works because `first_review` and `last_review` are of type **date**, not strings. Check the field types in the sheet's data-model table.
- The `$` marks an operator or a field reference. If you forget it in front of the field name, the query does not extract the year. According to the TA, you get back the date value/type instead of the year, while the field written correctly still works (ASR partly unclear). He called this "one of the moments where you need to remember the dollar sign".

## Logical Operators Are Written First, in Prefix Form (Q18)

**Reference:** E03 - MongoDB.pdf slides 15–16; Exercises Q18

- MongoDB is not a programming language. Filters are JSON-style documents, so a logical operator is not placed *between* its conditions. It goes *before* them as a key, and the conditions follow in a list.
- This is "difficult to read": in Q18 the "or" comes last in the text ("…, or have 5, 6 or 7 bedrooms"), but `$or` is written first. Its first element is the inner `$and` (more than 4 and at most 6 guests), and its second is the bedrooms condition. The TA said it is not intuitive and you just have to memorize it.
- Q18 should return **90**.
- Because a filter is a document, you cannot write `>` or `<`. Each comparison has its own keyword with a `$` (`$gt`, `$lte`, …), named as an acronym of the comparison. `$in` works like Python's `in`.

## Type Operators Are "Meta" Queries for Checking Data Quality (Q21)

**Reference:** E03 - MongoDB.pdf slide 17; Exercises Q21

- The TA called `$exists`/`$type` meta-operators. They act on the type and structure of the data, not on the values. They are simple, but "they can be asked in the exam".
- Q21(a): counting listings whose `minimum_nights` is of type `string` gives **5555**, the same as the whole collection. So every value has the right type and the data are "good". If the number were lower, some data would have the wrong type and you would need to fix them.
- Why this matters: a user never asks for this kind of query. You run it yourself to check data quality. NoSQL databases are very flexible and let you insert anything (numbers, integers, objects instead of strings). So it is up to you to keep types coherent. Otherwise "it's a mess", and queries will not find what you are looking for.

## Comparing a String Field with a Number Returns Nothing (Q21b)

**Reference:** Exercises Q21(b–c); data-model table p.2 (`minimum_nights` stored as text)

- `minimum_nights` is a string. `{"minimum_nights": {"$gt": 5}}` with 5 as a number returns **0**. Writing `"5"` as a string, which is the correct way, returns a real count.
- Lesson: comparing an integer with a string field does not work, so always pay attention to the field's type. The same applies to dates, which must be compared with a date (`ISODate(...)`), as in Q34.

## Dot Notation vs $elemMatch: The Recurring Exam Mistake (Q34–Q35)

**Reference:** E03 - MongoDB.pdf slides 20–22; Exercises Q34–Q35

- At the exam, many students use `$elemMatch` every time. That is not correct. You need it **only** when several conditions must hold in the **same** element of the array.
- Q34 ("a review by David **and** a review dated on or after 1 Jan 2019"): the two conditions don't need to be met by the same review. David's review can be one element and the recent review another. So you use dot notation twice (`reviews.reviewer_name`, `reviews.date`), and using `$elemMatch` here would give a wrong result. Result: **585**.
- Q35 (same conditions inside `$elemMatch`): result **52**. The condition is much stronger, because David's review itself must be dated on or after that date. Every listing counted by Q35 is also counted by Q34, but not the other way round.
- The TA stressed that this "shows up every time at the exam, and every time someone gets it wrong".

## Unwind: Match First, Because Unwind Explodes the Data (Q39)

**Reference:** E03 - MongoDB.pdf slides 23, 26; Exercises Q39

- The TA described Q39 as a "full query", closer to the level of complexity expected (at the exam), because it needs an aggregation pipeline and not just a count or a `findOne`.
- Put `$match` (on the name) **before** `$unwind`. Unwind creates one document per element of `amenities`, so the data grows a lot (the TA said "exponentially"). Filtering first reduces the number of documents before the explosion.
- Putting the match after the unwind, or even at the end, still gives a correct result, but it is much less efficient. Rule of thumb: "filter before and unwind after, if you can".

## Top-N Pattern: Unwind → Group → Count → Sort → Limit (Q45)

**Reference:** E03 - MongoDB.pdf slides 23–26; Exercises Q45

- Use `aggregate` when you need several filtering, projecting and sorting steps. Inside a pipeline, `$match` plays the role of `find`. Put it as early as possible (here, market = Barcelona) to reduce the data.
- How to reason about it: "top 5 reviewers who wrote the most reviews" means counting reviews **per person**. That is a signal to group by name and count. The name is inside `reviews`, which is a sub-collection (an array of documents), and you cannot group by an element of a sub-collection, only by an attribute. So you `$unwind` first. Most of the time the unwind is there only because the group needs it.
- After unwinding, each document has a single review. Group by `reviews.reviewer_name` and count with `{"$sum": 1}` (you are counting documents, not summing an attribute), naming the result e.g. `reviews_written`. A field created in a stage is visible only in the later stages.
- Then sort descending and `$limit` 5. This is the same sort-then-limit trick used in Neo4j for top/bottom N. Finally `$project` `reviewer` and `reviews_written` without `_id`.
- The TA said this group-then-count pattern for "top five / bottom three" is typical "in the exam, in the quiz", and that you should learn to recognize it immediately by doing many exercises. He added that for this query this is basically the only way to do it.

## $group Is a Barrier Like WITH in Neo4j; Typical Stage Order

**Reference:** E03 - MongoDB.pdf slide 24

- After `$group`, only what is in the group (the grouping key and the computed aggregates) survives. The TA compared it to `WITH` in Neo4j: it is a barrier. Trying to return an attribute that was not in the group is a "typical mistake". In Q45 this is not a problem, because `reviews_written` comes from the group.
- Typical order: `$match` almost always at the beginning (not required), `$group` after `$unwind`, `$limit` after `$sort`, and `$project` almost always at the end. Order matters, so "you must be extremely sure" when writing a pipeline.

## Write Operations: Read the Acknowledgement, matchedCount vs modifiedCount (Q47–Q49)

**Reference:** E03 - MongoDB.pdf slides 5, 9; Exercises Q47–Q49

- Always check the acknowledgement returned by a write, because when you change data you want to be sure it worked. Inserts return `acknowledged: true` and the new id(s): one for `insertOne` (Q47), two for `insertMany` (Q48, with comma-separated documents).
- Updates return `matchedCount` (how many documents match the filter) and `modifiedCount` (how many were actually changed). `modifiedCount ≤ matchedCount` always, because you cannot modify something you did not match.
- Q49(a): changing the price of "SMBUD Loft near Politecnico" gives matched 1 / modified 1. Q49(b): `updateMany` on `address.market: "Milan"` gives matched 3 / modified 3, i.e. exactly the three documents inserted in Q47–Q48. (The TA misspoke here, saying "update one/update many" when he meant the inserts.)
- Q49(c): running the same price update again gives matched **1**, modified **0**. The value is already the same, and MongoDB does not overwrite a value with an identical one.
- ASR note: the transcript says the new price is "10". The sheet says 110, which is probably what was said.

## Always Restore the Dataset After Write Exercises (Q50)

**Reference:** Exercises Q50 and Part F intro

- Q47–Q49 modify the data. If you don't undo them, later queries (e.g. in the next session) can give different results. So run the cleanup at the end.
- The easiest reset is a single `deleteMany({"address.market": "Milan"})`, since everything inserted has market Milan. Check `acknowledged: true` and `deletedCount: 3`, then run `countDocuments({})` again to confirm **5555**. In class the TA went straight to `deleteMany` and did not demonstrate Q50(a) (`deleteOne`).

## Commas in a Filter Are an Implicit AND; String Conditions Work Like Numeric Ones (Q27)

**Reference:** E03 - MongoDB.pdf slide 8; Exercises Q27

- Q27 is a plain `countDocuments` with three conditions: market Hong Kong, host is superhost, and response time "within an hour". All the comma-separated conditions in one filter are combined with AND "by definition", so no explicit `$and` is needed.
- Filtering on a string value uses exactly the same syntax as filtering on a number.
