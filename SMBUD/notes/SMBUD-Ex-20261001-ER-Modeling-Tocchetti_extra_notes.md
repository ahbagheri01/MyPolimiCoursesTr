# SMBUD-Ex-20261001-ER-Modeling-Tocchetti — Additional Professor Notes

**Transcripts:** Andrea Tocchetti's Personal Room-20261001 1551-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\E01 - ER [A-N].pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\Exercise Session - Group [A-N]-20261016\Exercise Sessions - Introduction [A-N].pdf

> **Material limitations:** The full solution of the museum exercise (E01 - ER [A-N].pdf, p. 16, "Exercise 2 - Solution") and the full diagrams listed on p. 24 are only external links (diagrams.net). They could not be inspected, so the base museum diagram (Type entity, Hall–Type–Artwork cycle) was compared only against the extra-exercise slides (pp. 18, 20, 22).

> **Coverage notes:** The session covered Exercise 1 (car rental, pp. 2–11) and the museum exercise with Extras I–III (pp. 13–22). The second "Exercise 2" in the same PDF (Dungeons & Dragons, pp. 25–38) and the Introduction deck were not presented in this recording. Page numbers below are PDF page numbers.

## At the Exam You Read an ER Model, You Do Not Build One

**Reference:** None (not in slides)

- At the exam you will **not** have to build an ER diagram, only understand it. You are given an ER model and then asked questions about NoSQL databases starting from it (see the exam facsimile). So you must be able to read every part of a diagram and how the parts interact.
- Exam texts describe ordinary scenarios such as managing flights or train tickets. The museum text was built from the TA's own visit to the Van Gogh Museum in Amsterdam. Exams are "just basic stuff", not exotic domains.

## ER Is Graded Leniently; NoSQL Mistakes Will Cost Stated Points

**Reference:** None (not in slides)

- The course does not go deep into ER. The aim is a refresh of what previous courses taught and to show the ER representations the course uses. A perfect or most-optimized ER diagram is not required, and you may optimize the shown diagrams as you like.
- The main topic is NoSQL, and there the TA will be much stricter. In the following sessions, mainly the one on Elasticsearch, he will say which common mistakes are made at the exam and exactly how many points each one costs ("usually a lot").

## Notes in an Exam Text Are Binding

**Reference:** E01 - ER [A-N].pdf, p. 14

- Example: "Opening and closing times are the same every day of the week" lets you use just two attributes (opening and closing time). Without it you would need seven entries with different times, which is redundant.
- Exam texts can contain such notes that either simplify the exercise or forbid something. You must follow them. If you ignore one, the point penalty is usually written to the right of that sentence.

## Primary Keys Must Be Truly Unique, So Never Use Names or Birth Dates

**Reference:** E01 - ER [A-N].pdf, p. 22 (Artist keyed by name, surname, birth date)

- Class quiz: name is not a valid key, and neither is name + surname or name + surname + birth date. E-mail is valid because e-mails are unique. Even name + surname + birth date + birth *time* can fail in rare cases where "the stars align" and two people with the same name are born at the same moment.
- The Artist entity on p. 22 uses name/surname/birth date as key **on purpose**: it was a test of whether students were listening, justified only by the claim that there is no record in history of two such artists born on the same date ("highly improbable"). "Don't try this at home": use real IDs (e.g., personal ID), never names or name + birth date.

## Meaning of the ISA Hierarchy Types (Total/Partial, Exclusive/Overlapping)

**Reference:** E01 - ER [A-N].pdf, p. 2 (ISA hierarchy with (P,O) label, no explanation)

- **Total:** only the child entities can exist in the database, whatever kind of database it is (graph, document, …). **Partial:** instances of the parent can exist too. With Pet → Cat, Dog: if total, you can store only cats and dogs. If partial, you can store cats, dogs and generic pets.
- **Exclusive:** each instance is of exactly one child type (a cat *or* a dog, or with partial just a pet). **Overlapping:** an instance can be of several child types, e.g., a pet that is both a cat and a dog.

## Cardinality Reading Direction: Always Add a Legend

**Reference:** E01 - ER [A-N].pdf, p. 2 (cardinality arrows)

- A student read the cardinalities on p. 2 in a different direction from the TA. The TA admitted that the later screenshots in the deck may not follow the convention drawn on p. 2.
- Advice: on every ER diagram you draw, add a small legend (top right, bottom right, anywhere) that says how to read the cardinality direction. Any convention is fine as long as it is stated. At the exam, a legend/mark in a top corner will explain how to read the given diagram.
- Many ER notations exist, and you may use another standard you know.

## Method for Turning a Text Into an ER Diagram

**Reference:** E01 - ER [A-N].pdf, pp. 3–7 (highlighted text, per-entity attributes)

- Read the text and highlight what you think are entities, relationships and attributes. Build a skeleton from entities and relationships only, then enrich it with attributes.
- Attributes are not always given where an entity is first mentioned. In the car rental text, the invoice's **status** ("closed") appears only at the end of the text, so scan the whole text for such hidden attributes.

## What Is Not an Entity in the Car Rental Text

**Reference:** E01 - ER [A-N].pdf, p. 4 (highlighted entities, no justification)

- **The system** is not an entity: it is what we are modeling. The **company** is not needed: we model the system *for* the company, not companies that run rental systems.
- **Payment** and **keys** are not recorded. The keys have no attributes and are not a list, so they have no meaning in this context. You can consider them part of the car.
- **Operations** is the "sneaky" entity. The text gives it no attributes, but every inspection includes a set of operations, so it must be an entity. Its attributes come from a hypothesis (next note).
- In the museum text, **location** is not an entity but a composite attribute (address, city).

## How to Make Hypotheses When the Text Is Silent

**Reference:** E01 - ER [A-N].pdf, p. 7 ("Assumption: Customer is identified through an E-Mail")

- Why e-mail: the text says nothing about the customer, so the TA imagined the system as a portal you log into. E-mail is unique and is what you use to enter a website or rental system. Operation ID and description were also invented, because the text gives Operation no attributes.
- At the exam, write the hypothesis on the side of your sheet ("the text doesn't say anything about X, so I assume…").
- A valid hypothesis must **not contradict the text** and should not make the problem more complex. Use hypotheses to make things easier. But if one makes the exercise *too* easy, it most likely contradicts the text, because the text is meant to make you use specific structures.

## Why Customer and Customer ID Card Are Separate Entities

**Reference:** E01 - ER [A-N].pdf, pp. 7–8

The Customer has only the e-mail, while the Customer ID Card holds the attributes that really describe the person (name, surname, birth date, …). In a real project the TA would put all of these attributes directly in Customer. Here they are split only because the text says the customer *owns* a personal ID card. (A student's suggestion that the split is about sensitive data was rejected.)

## Ternary "Renting" Relationship vs Rental Invoice as a "Bridge"

**Reference:** E01 - ER [A-N].pdf, p. 9 (ternary Renting among Rental Invoice, Customer, Car)

- The TA said ternary relationships are usually used when there is a cycle. Here the cycle can be broken: Renting is equivalent to linking Customer–Rental Invoice and Rental Invoice–Car and dropping any direct Customer–Car relationship.
- Why: a customer has 1..N invoices, and each invoice belongs to exactly one customer and concerns exactly one car. A car has 1..N invoices. Starting from a customer, you go through their invoices and reach every car they rented. Starting from a car, you go through its invoices and reach each customer. Since the invoice in the middle (a "bridge") uniquely identifies both ends in either direction, a direct Customer–Car relationship is pointless and can be removed.
- **Exam:** you will never find ternary relationships at the exam, only simple binary structures. The ternary is shown only so you meet it once.

## Composite Attribute "Drives" Mirrors the Table on a Driving License

**Reference:** E01 - ER [A-N].pdf, pp. 5, 8 (Drives: Truck, Cars, Bus, …)

"Drives" represents the table on the back of a driving license that lists which vehicles you may drive: truck, car, motorbike, motorbikes up to a certain engine size (the transcript says "up to 150cc"; ASR unclear), and so on. When the ER model is mapped to the final SQL tables or to a NoSQL representation (graph, document, …), it is exploded into separate attributes such as drives_truck and drives_car. The composite attribute is just a more compact notation.

## Lists: A Relationship in ER/SQL, a Native Structure in NoSQL

**Reference:** E01 - ER [A-N].pdf, pp. 10–11 (Includes relationship; "ER models will be mapped on tables")

- Every entity and relationship you draw will later be mapped to tables, or to graph nodes, or other structures, in the target DBMS.
- An ER diagram cannot define list attributes. "The list of operations the car underwent" is therefore not a list-typed column in a SQL table but a **relationship** with a new table/entity Operation.
- In NoSQL technologies, lists, arrays and other complex structures are allowed. Complex structure is acceptable there, and redundancy is not a big concern ("if there's redundancy, who cares?"). This was announced for the following sessions.

## Museum: Why Type Is an Entity (It Could Be an Attribute)

**Reference:** E01 - ER [A-N].pdf, p. 15 (TYPE highlighted); full diagram only via link (p. 16)

- Making Type an attribute would have been perfectly fine.
- The TA made it an entity because he assumed (without writing it in the text, which he called his mistake) that the museum wants to run queries on type. An example is finding all halls of a given type that contain artworks of several types, which is simpler when Type is an entity.
- The phrase "type (same as the hall types)" is the cue to notice: halls and artworks share the same **set of possible values**. It does not mean that they have the same types.

## Museum: A Hall–Type–Artwork Cycle That Cannot Be Removed

**Reference:** None (base museum diagram only behind the link on p. 16)

The diagram has a cycle: Hall *contains* Artwork, Hall is *described by* Type, Artwork is *assigned* a Type. Unlike the car rental case, this is one of the very few cycles that **cannot** be broken:

- **Remove Contain:** going Hall → Type → Artwork reaches *every* artwork of that type in the database, not the ones in that hall. The text never says that a hall of type X contains only artworks of type X.
- **Remove Describe** (a student's proposal) and derive the hall's types from its artworks: this wrongly assumes that a hall's type is defined by the types of the artworks it contains. Example: a "paintings" hall that also has a few sculptures is still a paintings hall, not "paintings and sculptures". Another example: a Leonardo da Vinci hall of paintings that also shows a small machine he built, next to a painting depicting it. The hall's type is still paintings, but the artworks' types include something else.
- **Remove Assign:** you could no longer identify the type of each artwork.
- A hall can have several types (e.g., 49% one type, 49% another, 2% a third).

## Museum: Why Visiting Time Sits on the Buy Relationship

**Reference:** E01 - ER [A-N].pdf, p. 20 (Visiting Time on Visitor–Ticket "Buy")

- The TA judged that the visiting time is neither an attribute of the ticket nor of the visitor. His assumption: you might book (lock) your visiting slot later rather than when buying. The text is silent on this.
- If the text required stating the time at purchase, you could put it on either the ticket or the relationship. In the final database (relational, graph, …) it ends up in the ticket anyway.

## Museum: Why Shop Is Kept as a Separate Entity

**Reference:** E01 - ER [A-N].pdf, p. 20 (Shop 1:1 Include 1:1 Museum)

The text states that a museum has a shop (one to one), so Shop is modeled. Linking gadgets directly to Museum and removing Shop would only be justified if the text said that "museums sell gadgets".

## Extra I (Lending Artworks): Put the Period on the Relationship and Make It 1:N

**Reference:** E01 - ER [A-N].pdf, p. 18

- **Student proposal: an Agreement entity.** It is linked to Artwork (an artwork has 0..N agreements, 0 if it never leaves its museum) and to Museum. This is acceptable but not optimal. The agreement is really between two museums, and the text does not ask to model the agreement at all, only the period each artwork spends in each museum. Add the Agreement entity only if you also want to track the agreement.
- **Better:** add begin/end exposition dates. Put them on the **Contain relationship**, not on Artwork. On Artwork, the same artwork entry would be repeated many times with only those two attributes changing, which is a sign that they do not belong to the artwork.
- **The "incredibly wrong" part:** the artwork side of Contain must become 1:N (or 0:N) instead of 1:1. With 1:1 there can be only one entry, so the first hall that receives the artwork keeps it forever and it can never move. The diagram may look fine, but think about the data in the database.
- **Ownership** is not tracked because the text says nothing about it (in reality private owners also lend artworks to museums). If needed, you could add attributes or relationships, or treat the first museum in the artwork's timeline as the owner by tracing back its history. Periods when an artwork is in no hall are also not a concern here.
- **Leaving the end date empty** is acceptable depending on your assumption about the agreement. Real traveling exhibitions usually fix start and end dates (e.g., three weeks here, then four weeks in Bologna, then Naples). Whether to leave it empty depends on how often you want to update the database.
- The TA remarked that minimum cardinalities 0 and 1 are usually quite interchangeable unless a specific constraint says otherwise (context partly unclear in the transcript).

## Missing Values: NULL in SQL, Absent Attribute in NoSQL

**Reference:** None (not in slides)

The TA flagged this as **very important**:

- In SQL you leave an attribute empty by setting it to NULL or to a placeholder such as −1.
- In NoSQL, NULL exists, but setting attributes to null is bad practice. It is much better to leave the attribute out, because objects of the same entity can have different numbers and kinds of attributes. Example: some people have a "hair" attribute, others simply do not have it.

## Extra II (Three Kinds of Shops): Food Is Not a Gadget

**Reference:** E01 - ER [A-N].pdf, p. 20

- Trap: "food is described by the same attributes as gadgets" tempts you to make Food a child of Gadget. But food is not a gadget (a restaurant serving gadgets would serve "Lego-made food").
- The fix is to introduce a common parent (Item; "Product" on the slide) and specialize Food and Gadget from it. Sweets are a specialization of Food. Gadget Shop, Restaurant and Sweets Shop become children of Shop, each with its own sell relationship to the right product type.

## Always Specify the Hierarchy Type, and Ask for It at the Exam if It Is Missing

**Reference:** E01 - ER [A-N].pdf, p. 20 (hierarchies drawn without type labels)

- When building a model, the type of each ISA hierarchy matters. The TA called it more important than missing cardinalities.
- At exams he has often forgotten to write the hierarchy types. In that case you either add them or ask him ("Professor, you missed the type of the hierarchy") and he will tell you.
- The types for Extra II given in class: Shop → Gadget Shop/Restaurant/Sweets Shop is **total, exclusive**. Item → Food/Gadget is **total, exclusive**. Food → Sweets is **partial**. Exclusive vs overlapping does not matter there because there is only one child.

## Extra III (Artist Friendships): Self-Relationship on Each Child, Exclusive Hierarchy

**Reference:** E01 - ER [A-N].pdf, p. 22

- The "astounding discovery" is only flavour text. There is no hidden constraint: just model that painters befriend only painters and sculptors befriend only sculptors.
- The hierarchy type depends on your assumption and decides how hard the problem is. **Partial** leaves room for other kinds of artists. **Exclusive** keeps it simple. With **overlapping**, a sculptor who is also a painter could befriend both groups, which "messes it up".
- Put a separate self-relationship *Befriend* on Sculptor and on Painter. Do **not** put Befriend on Artist, and do not keep it there in addition to the child relationships. Relationships are inherited by children, so any artist, painters and sculptors included, could then befriend anyone, including cross-type friendships. That is even worse than the overlapping case.

## Extra Exercises Must Stay Coherent With the Base Text; Model Constraints in the ER

**Reference:** E01 - ER [A-N].pdf, pp. 14, 21–22

- A student proposed moving the type from Artwork to Artist instead of using the Painter/Sculptor hierarchy. This was rejected because each extra text must stay coherent with the base text: the base text gives the type to the artwork, so you cannot add a type to the artist.
- The goal is to express the constraint in the ER diagram itself. You could instead add a type attribute and enforce "both types must be equal" with a DBMS constraint (e.g., in SQL/MySQL), but that is implementation, a lower level than ER modeling.
