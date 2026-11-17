# SMBUD-Ex-20261112-Cassandra-Redis-Tocchetti — Additional Professor Notes

**Transcripts:** Andrea Tocchetti's Personal Room-20261112 1650-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E05 - Cassandra  Redis\E05 - Cassandra - Redis.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E05 - Cassandra  Redis\E05 Extra - Cassandra  Redis Setup.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-08-keyvalue-db.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-09-columnar-db.pdf

> **Coverage notes:** The TA went through the Cassandra theory slides (E05 p.2–32) and all the Redis slides (p.35–57). The "Cassandra Exercise Session" car_dealer slides (p.59–66) and the setup PDF were not discussed. The TA said he accidentally deleted the slide with the user-defined-type example.

## Why Cassandra Looks Like "Simple SQL": Built Only for Speed

**Reference:** E05 - Cassandra - Redis.pdf, p.2–6, p.30

- The TA called Cassandra a fairly **legacy** technology that is not really used nowadays, but said it is important to know that it existed. Facebook (now Meta) built it to collect huge amounts of data very quickly, not to run complex queries. "It's all about speed, it's about nothing else."
- He explained every restriction in the session from this purpose: no joins, no foreign keys, and strict rules on what can go in `WHERE`. He added that he thinks these constraints are one of the reasons Cassandra is no longer used much.
- CQL was kept as close to SQL as possible for historical reasons, because SQL was the dominant database language when Cassandra was created.
- The theory lecture covered the architecture, and the TA said it explains *why* the partition-key and clustering-key rules exist.

## Keyspace → Tables → Indexes Hierarchy (Q&A)

**Reference:** E05 - Cassandra - Redis.pdf, p.7–10

- Student question: you can create as many keyspaces as you want. Creating a keyspace is like creating a new database. Tables live inside it, and indexes live inside each table. Switching keyspace (`USE`) switches the set of tables you are working with.
- The TA's MongoDB analogy was garbled. His corrected version: a keyspace is like a MongoDB database, and tables are like collections.
- `ALTER KEYSPACE` example: raise the replication factor from 3 to 6. In the recording he said "partition factor", but he meant the replication setting from p.7. Replication is just one of many properties that can be set when a keyspace is created and changed later.

## Partition Key Without Parentheses: Only the First Attribute

**Reference:** E05 - Cassandra - Redis.pdf, p.8, p.12, p.14

- In `PRIMARY KEY (a, b, c)` **without inner parentheses**, only the first attribute (`a`) is the partition key and everything after it is a clustering key. To get a multi-attribute partition key, you must write the extra parentheses: `PRIMARY KEY ((a, b, c), ...)`.
- Board example (Q&A): table `person(name text, surname text, age int, height float)`. With `PRIMARY KEY ((name, surname, age))`, all three are partition keys. Without the inner parentheses, `surname` and `age` would be clustering keys.
- You must know exactly which attributes are partition keys and which are clustering keys, because a query that does not use the full partition key fails with an error.
- TA's picture of the two levels: the partition key decides how the data is split across the nodes of the cluster. With a string partition key, the data is ordered by that string and split into partitions. Inside each partition, rows are ordered by the clustering key. These keys define the default indexes, which is what makes the queries fast.

## The Core Rule: Full Partition Key, in Order; Clustering Keys After

**Reference:** E05 - Cassandra - Redis.pdf, p.21–23

- Without a secondary index, a `WHERE` works **if and only if** it uses **all** the partition-key attributes. If the partition key has three fields and the query uses only one or two, the query fails and you need an index.
- The TA also said the partition-key attributes must appear in the `WHERE` **in the same order as in the definition** (name, surname, age). Otherwise the query fails, again because of efficiency. The slides do not state this ordering rule.
- **Why a partial key does not work:** a composite partition key is **one** index that sorts on all its attributes together, not three independent indexes. If `age` is dropped from a query on `((name, surname, age))`, you have to create secondary indexes on `name` and `surname`.
- Once the partition-key part is satisfied, the TA said clustering keys "can be freely added" to the condition. Note that p.23 is stricter: to filter on a later clustering key, all preceding clustering keys must be specified, and non-contiguous clustering ranges fail.
- The TA called this the only really challenging part of Cassandra.
- `SELECT * FROM person WHERE age = 26` with no index on `age` gives an invalid request error. The system refuses any query that would not run efficiently.

## Exam: ALLOW FILTERING Gives Zero for That Query

**Reference:** E05 - Cassandra - Redis.pdf, p.22–23 (also used in the exercise slide p.64)

- **Exam rule:** "At the exam, if anyone adds `ALLOW FILTERING`, it gets zero for the query." The TA stated this explicitly so that it is clear in advance.
- Reason: `ALLOW FILTERING` bypasses the indexing/speed constraint the system is built on. Using it means saying "I don't care how the system is built, I run my query anyway." You are expected to work out when a secondary index is needed and when the partition key is enough.
- Note: the car_dealer exercise slide p.64 uses `ALLOW FILTERING` for `price > 100000`. That slide was not discussed, and by the TA's rule it would not be acceptable at the exam.

## Exam: Creating an Unnecessary Index Is a Mistake

**Reference:** E05 - Cassandra - Redis.pdf, p.18, p.23

- **Exam rule:** create indexes only when strictly needed. If a query could be answered with the full partition key and you create an index anyway, it counts as a mistake, because it shows you did not understand how the system works. Otherwise you could just index every field.
- A custom (secondary) index on a field that is not a partition key (a clustering key or any other attribute) lets you filter on that field alone or combined with others. This is how the partition-key constraint is legitimately bypassed.
- Example from the slide: `CREATE INDEX person_name ON person (name)` sorts names in ascending or descending order, depending on the system default, so queries on `name` run faster.

## Exam Format for Cassandra

**Reference:** E05 - Cassandra - Redis.pdf (whole Cassandra part)

- The exam usually has an exercise where you **design a Cassandra table from an ER model**, followed by a few **queries** on it.
- The table design is usually not tricky: you put together the attributes from the ER model and decide on the primary key. The queries are usually simple `WHERE`s with one condition. The real difficulty is deciding **when a secondary index is needed and when it is not**. If the query needs an index, create it and then query. If it doesn't, don't.
- "At the exam we can ask you anything" from the slides. If you know SQL, Cassandra is only about 6–10 new operators. The only real complexity is how partition keys and clustering keys behave.
- Advice: install Cassandra (it runs in the terminal) and play with it. The TA built the slides after about half a day of experimenting.

## Terminal Tip: Always End with a Semicolon

**Reference:** E05 - Cassandra - Redis.pdf, p.15–16; E05 Extra - Cassandra  Redis Setup.pdf, p.4

When you work in `cqlsh` in the terminal, always end each statement with `;`. Otherwise the terminal looks stuck: it keeps waiting for the semicolon before running anything, just like a SQL terminal.

## TRUNCATE Use Case

**Reference:** E05 - Cassandra - Redis.pdf, p.17

`TRUNCATE` removes all rows but keeps the table definition. Typical use: you need to import a new dataset because the old one was incomplete. You truncate the table, alter it if needed, then load the new data.

## INSERT: Type Inference and the Unquoted-Date Trap

**Reference:** E05 - Cassandra - Redis.pdf, p.20

- The system infers how to store each value from the column types in the table definition. If `birth_date` were declared as a date, `'12-05-1995'` would be stored as a date.
- If you **forget the quotes**, `12-05-1995` is read as a subtraction and gives a negative number. These systems are "smart, but not that smart sometimes", so be careful with how you write values.
- As in SQL, you can omit the column list if the values follow the definition order, or list the columns in any order as long as the values match.
- The TA had never used the `USING <option>` clause personally.
- Student question: to insert several rows, the TA said you list the tuples separated by commas, as with SQL `VALUES`. This answer is not on the slides and was not demonstrated.

## SELECT-FROM-WHERE Is All There Is

**Reference:** E05 - Cassandra - Redis.pdf, p.21; SMBUD-09-columnar-db.pdf, p.34

- Anecdote: one of the TA's professors used to say that writing "SELECT FROM WHERE" earns you half a point and the challenge is the rest. That doesn't work here, because a select-from-where is the most complex query you'll be asked in Cassandra.
- No grouping, no filtering on groups, no subqueries. The system was built to collect huge amounts of data efficiently, so only `WHERE` conditions matter.

## UPDATE and DELETE Conditions: TA vs Slides

**Reference:** E05 - Cassandra - Redis.pdf, p.24–25

- **UPDATE:** the TA said the `WHERE` follows the same rules as `SELECT`. For example, you can update by `personal_id`, but not by `age` unless `age` has a secondary index. Asked again by a student, he confirmed that the partition key is always used to identify rows, so if you need to update by a field outside the full partition key, you must define a secondary index. Note: slide p.24 is stricter. It says the `WHERE` of an UPDATE must include **all primary-key components** (partition and clustering), and that primary-key values cannot be changed.
- **DELETE:** the TA was first unsure ("maybe it's better if you check it"). He then said a delete not on the primary key fails and that you must use the **full primary key**, not a part of it. Note: slide p.25 says the **full partition key** is required and clustering keys are not strictly required. The slide's version is the one written in the materials.

## BATCH, CAPTURE, EXPAND, SOURCE: Theory-Test Keywords

**Reference:** E05 - Cassandra - Redis.pdf, p.26–29

- **Exam:** these keywords (e.g. `BEGIN BATCH` / `APPLY BATCH`) sometimes appear in the **theory test**, more than in the practical part, as questions on whether they behave one way or another.
- `BEGIN BATCH` … `APPLY BATCH`: you type it in the terminal, followed by a mix of insert, update and delete statements. On `APPLY BATCH` they all run, one after the other. The TA said this is not very useful in itself. `SOURCE <path>` is the more practical way to run a file of saved statements with one command, instead of typing everything.
- `CAPTURE <path/file.txt>`: from then until `CAPTURE off`, the output of every operation goes only to that file, not to the terminal. It is especially useful before running a batch, so that hundreds of output rows don't flood the terminal. You can inspect the file later or process it with code.
- `EXPAND on/off`: the TA said it shows extra output when you run queries, e.g. how long the query took and extra table parameters. It is off by default. (His description of what it shows was vague.)

## No Foreign Keys or Joins: What You Do Instead

**Reference:** E05 - Cassandra - Redis.pdf, p.30

Instead of joins, you either keep one very big table and collect data from it, or you query one table first and then the other. The motivating use case was something like storing all the data about Facebook's users and retrieving it very quickly, which needs no joins.

## Collections and User-Defined Types

**Reference:** E05 - Cassandra - Redis.pdf, p.31–32

- Lists are still possible because Cassandra is a NoSQL database. You append with `+` in an `UPDATE … SET email = email + [values] WHERE …`.
- User-defined types are like **structs**. `CREATE TYPE` lists the fields with their types, and a table column is then declared with that type. When you insert into that table, you must give values for **all** the fields of the type.
- The TA said lists and custom types are the two most complex structures you will see. (The `frozen` keyword on p.62 was not discussed.)

## Redis at the Exam: Know the Operations

**Reference:** E05 - Cassandra - Redis.pdf, p.35–57

- Redis questions are usually straightforward operations, e.g. "create a key-value pair", "return the key-value pair with a given name", "assign it a duration". "Either you know it or you don't."
- Besides Cassandra's keys, the TA said the only non-trivial Redis topic is atomic operations and synchronization.
- Practice: there is a website made by the Redis creators (search for something like "try Redis") where you can try all the basic commands from the slides. The TA used it to build the slides. After writing and trying the commands three or four times, you should be fine.

## Redis Use Case: Cookies in Front of a Web Application

**Reference:** E05 - Cassandra - Redis.pdf, p.35; SMBUD-08-keyvalue-db.pdf, p.10

- The TA said Redis is mainly used for browser cookies. You put a Redis database in front of your web architecture so that when someone connects, you can quickly look up their cookies: whether it's their first visit, any stored preferences, and so on.
- `INCR`/`DECR` fit this use: keeping track of how many people connected to a page, or creating cookies with incremental values.
- With `EXPIRE`, Redis also works as a temporary cache. When someone connects, you store a key with a time-to-live, and it disappears once you're done with it.

## EXISTS and INCR: Practical Caveats

**Reference:** E05 - Cassandra - Redis.pdf, p.37, p.39

- Checking with `EXISTS` before a `GET` matters because keys can have a timer after which they stop existing.
- `INCR`/`INCRBY` only work if the value is an integer. Otherwise the operation fails.

## Why INCR Beats a GET/+1/SET Script: Lost Update

**Reference:** E05 - Cassandra - Redis.pdf, p.40–47

- In the two-client animation, both clients `GET` 10, both compute 11 and both `SET` 11. The final value **should be 12**, because two increments were requested, but the database records only one.
- `INCR`/`DECR` are atomic. Even if the two requests arrive at the same moment, the server decides an order and performs both. A client-side script gives no guarantee about ordering or about which update survives.
- So, when several clients may update the same variable, always use the atomic operators, not scripting.

## Time-to-Live Details: EXPIRE, TTL −2, SET … EX, PERSIST

**Reference:** E05 - Cassandra - Redis.pdf, p.48–50

- Student question: if `EXPIRE` is applied twice to the same key, the TA said the latest one wins (he was "quite sure", not certain).
- The TA's explanation of `TTL = -2` ("already expired"): the system keeps a kind of log of the keys that were created, so it can tell you that a key existed and has expired.
- Setting the TTL directly in `SET key value EX seconds` is better than a separate `EXPIRE` on the next line, because you might forget which key you worked on last.
- `PERSIST` example (partly garbled): a key has a 1-hour TTL. After 10 minutes you realise you need it longer, so you `PERSIST` it to cancel the automatic expiry. Later you can set a new short expiry (e.g. 10 seconds) to have it removed.

## Lists: Created by Pushing, LRANGE Negative-Index Mnemonic, Pop as a Stack

**Reference:** E05 - Cassandra - Redis.pdf, p.51–53

- You never create an empty list and then add to it. The first `LPUSH`/`RPUSH` on a key creates the list. When pops remove all elements, the key is deleted.
- `LPUSH`, like `SADD`, can take several values at once, which are all added at the left (or the right, for `RPUSH`).
- `LRANGE` mnemonic for a negative last index `-n`: drop the minus sign and subtract one. The result is the number of elements excluded from the end. So `0 -2` returns all but the last element, and `0 -1` excludes nothing. The TA admitted he often got this wrong himself.
- `LPOP`/`RPOP` work like popping from the bottom or the top of a stack. You need to remember on which side you pushed elements in order to pop the right one.

## Sets: Exam Trap — SISMEMBER, Not SMEMBERS

**Reference:** E05 - Cassandra - Redis.pdf, p.54–55

- **Exam:** when a question asks you to **check whether an element is in a set**, use `SISMEMBER key value`. Many students used `SMEMBERS` and argued that by reading the whole set you can tell whether the element is there. The TA's answer: fair, but that is not what was asked. Use `SMEMBERS` only when asked to return all the elements.
- `SREM` only works if the values exist and the key itself still exists, because a set can also have an expiry time.
- Sets need no left/right variants because order doesn't matter. The TA suggested sets for building enumerations (without ordering).
- `SUNION`: the TA said ("if I remember correctly") that the second set is merged **into the first** key. This is uncertain. The slide only says it "combines two or more sets into one set".

## Sorted Sets as a Leaderboard; ZRANGE Indexes

**Reference:** E05 - Cassandra - Redis.pdf, p.56

- In `ZADD`, each element is given as **score first, then value**, repeated for as many elements as you want. For example, a leaderboard: `ZADD leaderboard 1 Mark 2 Frank 3 Pedro`. As with lists, the first `ZADD` creates the sorted set. You never declare an empty one.
- The order comes from the score, not necessarily from the values themselves.
- `ZRANGE` uses the same index behaviour as `LRANGE`: `0 -1` returns everything and `0 -2` returns all but the last. The TA also said `0 1` returns "just the first element" (as stated in the recording).

## Hashes as Object Descriptions

**Reference:** E05 - Cassandra - Redis.pdf, p.57

Hashes are used to describe "complex classes". For example, a person hash with fields such as hair colour = brown and eye colour = blue, created with `HSET person field1 value1 field2 value2 …`. `HGETALL person` returns the full description, and `HGET person eye_color` returns just that field.
