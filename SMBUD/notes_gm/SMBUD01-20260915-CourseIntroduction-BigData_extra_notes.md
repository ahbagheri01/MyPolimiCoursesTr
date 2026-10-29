# SMBUD01-20260915-CourseIntroduction-BigData — Additional Professor Notes

**Transcripts:** SMBUD01-Marco Brambilla PoliMi-20260915 1410-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-00-intro_course.pdf, E:\amirhossein\Polimi\POLIMI\SMBUD\SMBUD-01-bigdata.pdf

## Course Email Labeling Requirement and Research Lab Context

**Reference:** SMBUD-00-intro_course.pdf, slide 2

All email correspondence with the teaching team must include the exact tag '[SMBUD]' in the subject line to prevent emails from being lost among high volumes of messages. Routine theory questions should be directed to the instructor, practical questions to the teaching assistants (Andrea Tocchetti and Davide Ettori), and administrative/exam queries to both simultaneously. Professor Brambilla also leads the Data Science Lab at DEIB, offering future thesis opportunities in data science, AI, machine learning, explainable AI, and big data.

## Detailed Exam Structure, Browser Constraints, and Continuous Evaluation

**Reference:** SMBUD-00-intro_course.pdf, slide 9

The written exam is conducted on the student's laptop using Safe Exam Browser, which does not run reliably on Linux (requiring students with Linux to borrow a Mac/Windows machine or request advance accommodations). The written test consists of two parts: a strict 10–12 minute closed-book theory quiz (6 points, multiple choice/true-false) that locks upon completion, immediately followed by a 2-hour practical section (24 points). The optional continuous evaluation program offers 3 intermediate tests during the course (one pass/fail threshold test each, worth +1 point each, bringing the total base mark potential to 33 points). Students scoring 29 or higher can optionally request a small practical project to achieve 30 or 30 cum laude. If proctors doubt authorship or integrity, an oral examination will be mandated.

## Cognitive Scale Distortion of Volume: The Intangibility and Money Analogy

**Reference:** SMBUD-01-bigdata.pdf, slide 5

Humans fail to perceive the exponential severity of volume in big data because data is intangible (unlike physical objects or dirt piles). Brambilla uses a currency scaling analogy to demonstrate how rapid scale multiplication is: if 1 KB equals 1 Euro, then 1 MB is 1,000 Euros, 1 GB is 1 million Euros, 1 TB is 1 billion Euros, and 1 PB is 1 trillion Euros—a monetary threshold exceeding personal wealth. While storage up to terabytes is cheap or nearly free for consumers, organizational big data management costs escalate drastically at petabyte and exabyte scales.

## Ephemeral Streaming Data Loss vs. Real-Time Ingestion

**Reference:** SMBUD-01-bigdata.pdf, slide 7

High-velocity streaming data from IoT devices, sensors, and smart monitors is often inherently transient: devices produce, transmit, and immediately delete raw readings. If ingestion and streaming analytics pipelines are not fast enough to process data in motion in real time, the raw observations are lost forever, leaving only pre-computed aggregates or completely missing critical signals.

## Veracity Degradation, Data Integration Hazards, and Data Cleaning Overhead

**Reference:** SMBUD-01-bigdata.pdf, slide 8

Unlike historical corporate datasets that were tightly curated, modern big data suffers severe veracity issues due to uncontrolled external sources and integration errors (e.g., mismatches when joining disparate systems or aligning missing and real values). Consequently, industrial studies show that machine learning and data science experts spend 60% to 75% of their project time and budget merely cleaning tables, imputing missing/null values, and rectifying low-level numerical discrepancies rather than engineering models.

## Economic Virtuous Cycle of Storage/Network Costs and the Plateau Risk

**Reference:** SMBUD-01-bigdata.pdf, slides 12-16

The big data explosion was driven by an economic cycle: logarithmic drops in storage ($600/GB in 1990 down to fractions of a cent) and bandwidth costs ($1,200/mo in 1999 down to ~€20 fiber) transformed user behavior (e.g., saving massive files, photos of food). This usage expanded consumer markets, attracting ad revenues and infrastructure investments. However, if data growth hits an empirical logistic plateau in 20–30 years, capital investments into faster processing hardware and technology development will stagnate.

## Market Layering Trade-offs: Cross-Infrastructure Vendor Lock-in vs. Open-Source TCO

**Reference:** SMBUD-01-bigdata.pdf, slides 32-33

The big data market comprises three layers: infrastructure, analytics, and applications. Cross-infrastructure vendors (e.g., Microsoft Azure, AWS, Google Cloud) offer tight vertical integration across the entire stack, reducing development friction but creating severe vendor lock-in where migration costs mimic monopolistic entrapment. Conversely, open-source software (e.g., open versions of MongoDB, Redis, Neo4j) avoids licensing lock-in and provides source access, but is not financially 'free': it incurs substantial total cost of ownership (TCO) in hardware, operations, continuous maintenance, and skilled personnel compared to fully managed commercial cloud offerings.

## Perceived vs. Infrastructure Value: Twitter vs. VMware Acquisition Discrepancy

**Reference:** SMBUD-01-bigdata.pdf, slides 32-33

Consumers and mainstream media only perceive the customer-facing application layer (e.g., Instagram, Twitter/X, ChatGPT), ignoring the foundational infrastructure and analytics layers. To illustrate this distortion, Brambilla contrasts Elon Musk's heavily publicized $44 billion acquisition of Twitter with the simultaneously occurring, higher-value ~$48+ billion acquisition of VMware (a virtualization/cloud distribution company unnoticed by the public despite powering the very enterprise infrastructure applications rely upon).

## Population Shifts: From Paper Surveys and Auditel Sampling to Continuous Full Monitoring

**Reference:** SMBUD-01-bigdata.pdf, slides 20-22

Traditional statistics used sampling because processing the entire population was computationally and logistically impossible (e.g., sending supermarket pollsters for Barilla pasta to get 50–100 responses, or the Italian agency Auditel using 5,000 hardware-monitored household remote controls to estimate the viewing habits of 60 million people for the Sanremo music festival). In contrast, big data shifts from sample inference to capturing 100% of user activity via continuous stream analytics on platforms like Netflix.

## Bottom-Up Data Exploration vs. Scientific Method in Complex Domains

**Reference:** SMBUD-01-bigdata.pdf, slides 23-25

Traditional scientific inquiry is deductive: an expert observes a phenomenon, poses a question, formulates a hypothesis, and gathers specific data to validate it. Modern big data enables an inductive, bottom-up exploratory approach where machine learning detects correlations, patterns, and anomalies across raw data without a prior hypothesis. This shift is essential in complex domains like genomics and DNA sequencing, where datasets are terabytes of bits and humans cannot form upfront hypotheses.

## Evolution of Business Intelligence: Periodic Ex-Post Reports to Dynamic Interactive Dashboards

**Reference:** SMBUD-01-bigdata.pdf, slides 29-31

Traditional corporate decision-making relies on batch-processed data warehouses yielding ex-post, delayed reports (e.g., monthly sales reports, quarterly and annual financial reviews). Modern big data pipelines feed interactive real-time dashboards where managers can zoom, slice, filter, and pivot up-to-the-minute data independently on demand, avoiding the business obsolescence of operating on outdated reports.

## Netflix Case Study: DVD Logistics Forecasting vs. Micro-Clustering Computational Economics

**Reference:** SMBUD-01-bigdata.pdf, slides 46-50

In its DVD rental era, Netflix operated on 4 sparse data points (Customer ID, Movie ID, Rating, Date) primarily to solve physical logistics (predicting regional DVD stock and overnight shipping demands across the US to beat Blockbuster's local convenience). In the streaming era, fine-grained telemetry (pauses, clicks, preview scrolls) captures millions of behavioral points. Rather than computing 400 million individual personalization models, Netflix clusters users into roughly 2,000 archetypes and clusters content into tens of thousands of alt-genres, mapping cluster-to-cluster to drastically reduce computational complexity while achieving near-perfect personalization.

## Netflix Case Study: Upstream Content Bidding and Algorithmic Thumbnail A/B Testing

**Reference:** SMBUD-01-bigdata.pdf, slides 51-55

Netflix leverages viewer analytics across two upstream and presentation dimensions: (1) Strategic acquisitions: Netflix outbid major cable networks with a $25 million commitment for 'House of Cards' because correlation data showed their audience strongly favoured David Fincher's directing combined with Kevin Spacey's acting; (2) Algorithmic presentation: Every visual element of movie thumbnails (colors, fonts, faces) is dynamically tested via real-time A/B testing on live users (e.g., showing a romantic Good Will Hunting thumbnail to romance fans and Robin Williams to comedy fans). Brambilla warns this optimization carries an ethical dark side, as continuous personalized nudging can artificially manipulate long-term human preferences in media and politics.
