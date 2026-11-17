# SMBUD-Ex-20261029-MongoDB-Introduction — Additional Professor Notes

**Transcripts:** MongoDB_introduction_Ettori_29-10-2026.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E03 - MongoDB\E03 - MongoDB.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E03 - MongoDB\E03 - MongoDB Atlas Setup Guide.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-07-document-db.pdf

## Exam and Quiz Information Given in This Session

**Reference:** E03 - MongoDB.pdf p.6, p.26

- **The quiz after next is on MongoDB.** The TA said the next quiz would not be the one next week but the one after, and that it would be "on Neo4j". He then corrected himself: "sorry, on MongoDB".
- **Sketch the shape of the data after each pipeline stage, "both for the exam but also for the quiz".** You can memorize instructions, patterns and where the dollar goes, but knowing the shape of the data is how you spot errors, both in your own query and in the queries you read at the exam.
- **No MongoDB UI at the exam.** At the exam you only have your code on your PC. The MongoDB application (Compass/Atlas) helps by structuring the query for you and showing where things go, so you must also be able to write the whole query yourself, from beginning to end.
- **The dollar sign** "is one of the main sources of confusion also in the exam" (see the next note).
- The pipeline on slide 26 (`$unwind` → `$group` → `$match` → `$sort` → `$project`) is "the typical structure of the query that you will need to write also for the exam".
- Logistics at the end (partly garbled in the recording): next week, Thursday, in the same room and at the same time, there is first the quiz and then practical MongoDB exercises on your own computer. The quiz seems to be closed questions (ASR unclear).

## The Many Meanings of the Dollar Sign

**Reference:** E03 - MongoDB.pdf p.3, p.9, p.11, p.15, p.23–25

The TA listed the different jobs the `$` does, because mixing them up is a main source of mistakes:

1. **Special/complex field values.** In `"birth_date": {"$date": "..."}` the dollar tells MongoDB the value is not a normal string but a packaged date (year, month, day).
2. **Commands and operators.** `$set` in an update, `$or`, `$gt`, `$unwind`, `$group`, `$sort`… Here the dollar means "this is a function".
3. **Field paths in aggregation.** In `{"$unwind": {"path": "$mobile_phone_numbers"}}` and `"_id": {"provider": "$mobile_phone_numbers.service_provider"}` the value is a key, not a function, but it still needs a dollar because it is a pointer to the attribute's (changing) values rather than a fixed value. The TA said this case is the one you "normally don't think you need", and that ironically the hardest thing in these stages is remembering this dollar. It is just syntax to memorize.

## Documents, Sub-documents and Sub-collections Compared With SQL and Neo4j

**Reference:** E03 - MongoDB.pdf p.3; SMBUD-07-document-db.pdf p.12

- A document is what an entity is in SQL and a node is in Neo4j.
- Sub-collections (keys pointing to a *list* of documents, not to one document) are what you use to model relationships. The TA said they are the most complex part and that the most complex MongoDB queries involve them.
- As with Neo4j, you have to change mindset: think of the data and the queries as documents, not tables or graphs.

## ObjectId Uniqueness Is Not Actually Checked

**Reference:** E03 - MongoDB.pdf p.4

MongoDB does not check that a generated `_id` is unique. Because it is built from a timestamp, a random value and a counter initialized to a random value, a duplicate is "basically impossible", so it is treated as a primary key. You never need to build a primary key yourself as in SQL, and `_id` is what you use to identify documents (also in indexes).

## Flexibility on Insert: Keeping the Data Coherent Is Your Job

**Reference:** E03 - MongoDB.pdf p.5

Like Neo4j, MongoDB lets you insert anything, with any type and any cardinality of attributes. Most of the time inconsistent data does not raise errors. It just creates confusion, and the data quickly becomes impossible to retrieve. So keep the documents consistent yourself.

## Indexes: When to Create Them and What They Store

**Reference:** E03 - MongoDB.pdf p.6; SMBUD-07-document-db.pdf p.38

- Create an index on an attribute when you know in advance that you will filter or search on it many times, e.g. all people whose name starts with A, or all events that took place in a certain year. Searching sorted data is much faster.
- The index does not copy or re-sort all the data, which would waste a lot of space. It stores only the ordering of the documents' ids, i.e. pointers to the documents.
- Indexes are usually created from the DBMS UI rather than inside a query, since they are a data-management technique more than a query. The TA said this is the only thing you should use the UI for.
- In a multi-attribute index the first attribute is the most important, then the next one, and so on.

## Dot Notation on a Sub-collection Reaches All Elements at Once

**Reference:** E03 - MongoDB.pdf p.7, p.20

`address.city` on a sub-document just gives the value (Milan). On a sub-collection, `mobile_phone_numbers.service_provider` does not pick one element: it looks at all the elements at the same time. Sometimes that is what you want, but often it is not. Keep this in mind whenever you use dot notation on a sub-collection (see the `$elemMatch` note below).

## Filters Mimic the Document; Stick to the Functions Taught

**Reference:** E03 - MongoDB.pdf p.8

- Just as a Cypher pattern mimics the graph, a MongoDB filter is itself a document that mimics the documents you want to match.
- `countDocuments` exists so that when you only need the number of matches you don't have to find and then count with a grouping operation.
- The TA advised using only the functions taught in class. All the queries they ask can be solved with them. Newer functions not on the slides may work, but they tend to confuse you or lead to a query more complex than intended.

## Date Fields: Type Mismatches Fail Silently

**Reference:** E03 - MongoDB.pdf p.3, p.9

If a field is a date and you filter or update it with an integer or a string, the type mismatch often does not raise an error. Instead you get unexpected behaviour, e.g. the filter simply finds nothing. The TA called the date field a typical error because a date looks like a string but is not. Always check whether a field is a date, an integer or a string.

## Projections: Positional Argument, No Mixing of 1 and 0

**Reference:** E03 - MongoDB.pdf p.11

- `find` has no keyword for the projection: the language knows it because it is always the **second** argument. First the filter, then the projection, and the order cannot be changed.
- You cannot mix `1` (return only these) and `0` (return everything except these) in the same projection. The TA thought newer versions give an error if you try.
- A new field such as `"year": {"$year": "$birth_date"}` is temporary and is never saved in the database. Asked by a student, he confirmed it is like renaming/returning a new attribute in Neo4j.

## find Ends After the Projection; Chained Method Order Matters

**Reference:** E03 - MongoDB.pdf p.12–13

- With `find` you get one filter and then one projection, and the query is over: you cannot filter again after projecting. For more, use the aggregation pipeline, which has no such limit. If one filter is all you need, `find` is faster and easier.
- You can chain methods (`.sort()`, `.limit()`) in any order, and the order changes the result. `sort` then `limit(5)` gives the top five (e.g. oldest or youngest people). `limit` then `sort` gives a completely different, probably wrong, result.
- The `$sort`/`$limit` stage versions are for the aggregation pipeline. With the simple `find` you use the methods.

## Logical and Comparison Operators Go in Front, as Keys

**Reference:** E03 - MongoDB.pdf p.15–16

- Because everything is a document, every key needs a value. So the operator is the **key** and is written once at the start (`"$or": [cond1, cond2, …]`), not between conditions as in programming languages. The list can contain any number of conditions.
- Comparisons work the same way: "age greater than 19" becomes `"age": {"$gt": 19}`, a small sub-document with the operator as the key. The TA admitted this is hard to read at first and said to practise reading it. In nested examples, follow the brackets to see what is nested in what.
- Even when a condition is on a sub-document field (`name.last`), the query returns the whole root document, not just the matched sub-document.
- `$eq` is rarely used, because `{"name.first": "Mark"}` already means equality. Adding an extra document only for `$eq` is usually pointless, though allowed.

## $exists and $type as "Meta" Operators and Navigation Tricks

**Reference:** E03 - MongoDB.pdf p.17, p.27

- Element operators check conditions on the data structure itself rather than on values. In MongoDB, a field being `null` and a field not existing are very different. `$exists` is true even if the value is null, as long as the field is there.
- Besides being used when a question explicitly asks about existence, they help you work out where you are in the data. Example: an ISA hierarchy pet → dog/cat. If you test `$exists` on an attribute that only dogs have and it exists, you are in a dog document; otherwise you are in a cat. The TA said this is the typical use for an **exclusive** hierarchy. `$type` can be used the same way.

## Evaluation Operators: $text Is Rarely the Right Tool; $regex and $where Not Required

**Reference:** E03 - MongoDB.pdf p.18

- `$text` matches documents whose string attribute contains the given text. The TA's example was searching for "Mark" in the name (the recording says it matches people named "Marco", which may be an ASR error for "Mark").
- `$regex` and `$where` (which lets you write JavaScript) are "just to know". The TA said they will never ask you to write a regex and that `$where` is never really necessary.
- Even `$text`, the most used of the three, is usually not a good choice. Scanning all documents and matching text is not efficient in this kind of database. Elasticsearch, covered later in the course, does this much more efficiently.

## $all, $size and $elemMatch: Collection vs Element Conditions

**Reference:** E03 - MongoDB.pdf p.19

- `$all` is a shortcut for checking several values at once on one array attribute. The values are in AND: every listed nickname must be among the person's nicknames.
- `$size` is a condition on the collection itself (e.g. people with exactly two phone numbers).
- `$elemMatch` is the condition on the elements. The TA called it a key function, because it is how you force MongoDB to check several conditions on one element instead of across all of them.

## Multiple Conditions on an Array Without $elemMatch: A Common Mistake

**Reference:** E03 - MongoDB.pdf p.20–22

- A single condition such as `"mobile_phone_numbers.service_provider": "Wind"` works as you would expect. Read it as "**at least one** phone number has provider Wind".
- With two conditions (provider Wind *and* a given phone number), nothing tells MongoDB to check them on the same element. It finds Wind in one element and the number in another element (with a different provider), and the document still matches. The TA called this a very common mistake. Usually you want both values in the same sub-document, i.e. inside the same curly brackets. That is what `$elemMatch` enforces. With `$elemMatch` on TIM and the number, a document where TIM is in one element and the number in another is **not** returned.
- Student questions clarified the scope: the conditions are always evaluated once per root document, "basically a for loop" over the documents of the collection. Wind in one person's document and the number in another person's document is never a match. When a document matches, the whole root document is returned.

## $unwind: How Many Documents It Creates and Why to Be Careful

**Reference:** E03 - MongoDB.pdf p.23

- Example drawn in class: a document whose sub-collection `U` holds three items A, B, C. Unwinding on `U` gives three documents. Everything else is copied unchanged, and in place of the array each one has a single element (A, then B, then C).
- The number of output documents is the sum over all input documents of the size of their `U`. Sizes can differ from document to document (3 here, maybe 100 in the next). For example, 9 documents with 10 elements each give 90 documents.
- You can unwind again on another collection, and the data then grows multiplicatively ("exponentially"). Do it only when you really need it. The result is temporary and disappears at the end of the query.
- The usual reason to unwind is grouping. You cannot group on the elements of a sub-collection without unwinding first.
- Design smell: if you often need to group or analyse an attribute buried deep in nested sub-collections, the database may be badly designed for your queries, rather than the query being wrong.
- Forgetting the `$` in the path means unwinding by a fixed value, which means nothing and does not unwind anything.
- After unwinding, the shape changes (the TA described it as going from a list of documents to "a list of list of documents"). Keep track of it. You can project right after to keep only what you need.

## Why It Is Called aggregate, and Efficiency of Stage Order

**Reference:** E03 - MongoDB.pdf p.23, p.26

- Answering a student, the TA said the name `aggregate` refers to aggregating several **stages** into one sequential pipeline (hence the square brackets), not to aggregating data. With it you can run any operations, in any order, as many times as you want.
- He thought `$unwind` is the only stage that increases the amount of data.
- Student question on whether stage order affects efficiency: yes. Everything a stage produces flows to the next one, so the fewer documents pass through the pipeline, the better. For example, filter before unwinding when possible. The TA said they do not check that your query is the most efficient one, but you should try to unwind as few documents as possible.

## $group: _id Keys, the WITH Analogy, and $sum

**Reference:** E03 - MongoDB.pdf p.24

- The `_id` of `$group` holds the grouping key(s). There can be several, just like several keys in a Neo4j `WITH`. The values of `_id` are automatically distinct, as in Neo4j.
- The key needs the `$` because you are not filtering for one provider. You are grouping by all of its values.
- `$group` usually comes right after `$unwind`. Unwind explodes the data and group shrinks it back, doing the opposite.
- `$group` is a barrier like `WITH`: whatever is not in the group (or created by it) is lost to all later stages.
- `{"$sum": 1}` adds 1 per document, so it is a count. The more common use is summing or averaging a real attribute, e.g. `{"$sum": "$price"}` to get the total price paid per provider.

## Forgetting the $ in _id vs Grouping Everything With true

**Reference:** E03 - MongoDB.pdf p.25

The slide's red circle shows a typical error. Without the `$`, `_id` is a fixed value, not a pointer to the attribute's values, so everything ends up in a single group. That is in effect the same as `_id: true`. When you actually want to group all documents together (e.g. count all phone numbers of all providers), write `true` by convention so your intention is clear. This is the only case where omitting the `$` is correct, because there you specifically want a fixed value.

## Reading the Full Pipeline Stage by Stage

**Reference:** E03 - MongoDB.pdf p.26

- Shape after each stage: `$unwind` turns the documents into one per phone number. `$group` shrinks them to one document per service provider (e.g. just three).
- `$match` (not explained on the slides) is the general, pipeline version of `find`'s filter. It behaves exactly the same but can be placed anywhere in the pipeline, any number of times.
- `phone_numbers_per_provider` does not exist in the database. It is created by `$group`, and anything created in the pipeline is visible to all later stages, then disappears at the end. Here it is a temporary variable created to filter (`> 10`) and sort on, then removed.
- `$sort` is the pipeline counterpart of `.sort()`. Inside an aggregation you must "speak the language of aggregation" and use the stage.
- The final `$project` with `0` is just to show it is possible. The TA advised listing what you need with `1`. Otherwise you get a bunch of useless attributes you may not even remember.

## Typical Stage Order and Two Student Questions

**Reference:** E03 - MongoDB.pdf p.26

- Typical order: `$unwind` before `$group`, `$match` before `$sort` (there is no point sorting 1000 documents and then keeping two), `$project` at the end. The TA said this is the general structure you should more or less follow.
- Ideally you also `$match` before `$unwind`, to explode as few documents as possible.
- Can the projection be moved right after `$group`? Projecting as much and as early as possible is a good idea. Here, though, projecting `phone_numbers_per_provider: 0` right after the group would remove the attribute that `$match` needs.
- Can this `$match` go before the `$unwind`? No. It filters on `phone_numbers_per_provider`, which only exists once `$group` has created it, so it must come after.

## ER to MongoDB: Multiple Valid Designs, Driven by the Queries

**Reference:** E03 - MongoDB.pdf p.27; SMBUD-07-document-db.pdf p.23

- Unlike Neo4j, where there is basically one correct translation (entity → node, relationship → edge), MongoDB offers several valid options, and some are better than others.
- Look at the ER diagram *and* at the queries you will have to run. Keep the attributes you need often as high as possible in the document. Less nesting is usually easier. If you keep filtering on an attribute inside a sub-collection of a sub-collection of a sub-document, the design is probably wrong.
- The TA warned that a wrong choice leaves you writing very complex, time-consuming queries at the exam. Spending five more minutes on the design makes all the following queries much easier.

## 1:N by Embedding (Person–Car); Why N:N Is Avoided

**Reference:** E03 - MongoDB.pdf p.27

- Example: a person can own many cars, and each car has one owner. You delete the car document and give the person a `cars` attribute holding the list of all their cars. A sub-document inside a collection is just another document, so this is natural. The TA said this 1:N conversion is the thing to remember.
- N:N would require embedding the cars in the person *and* the persons in the car, which creates many copies of the same data and wastes space. So N:N relationships are usually not dealt with in MongoDB, and the TA said you are not going to see them.
- Student question on relationship attributes: they can again be embedded inside the collection of the document. The TA also mentioned creating an index and unwinding it later to analyse it, and said this works only for 1:N. (This exchange is partly unclear in the recording.)

## ISA Hierarchies: Overlapping and Exclusive in Practice

**Reference:** E03 - MongoDB.pdf p.27

- Overlapping: one document may carry attributes from several entities of the hierarchy, which the TA said is not a problem at all.
- Exclusive: each document has its own attributes. This is where `$exists` is typically used: if a dog-only attribute exists, you are in a dog document.
- Apart from embedding 1:N, these rules are natural. What has no fixed rule is choosing the structure from the queries, which you must reason out yourself.
