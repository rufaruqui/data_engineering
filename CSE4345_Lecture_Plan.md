# CSE 4345 — Big Data Analytics
## OBE-Based 11-Week Lecture Plan

**Department of CSE | Premier University**
**Credits:** 3 | **Pre-requisite:** CSE 2221 — Database Management System
**Instructor Reference Email:** rufaruqui@cu.ac.bd

---

## Course Learning Outcomes (CLOs)

| CLO | Statement |
|-----|-----------|
| CLO1 | Understand big data characteristics |
| CLO2 | Analyze the existing challenges in big data |
| CLO3 | Explain the importance and performance of different big data techniques and tools |
| CLO4 | Utilize the knowledge to solve problems and build own project |

---

## Textbook & Core References

| Code | Reference |
|------|-----------|
| **[TW]** | Tom White, *Hadoop: The Definitive Guide*, O'Reilly Media, 4th ed., 2015 |
| **[SA]** | Seema Acharya & Subhashini Chellappan, *Big Data and Analytics*, Wiley, 2015 |
| **[TE]** | Thomas Erl, Wajid Khattak & Paul Buhler, *Big Data Fundamentals*, Prentice Hall, 2016 |
| **[LRU]** | Leskovec, Rajaraman & Ullman, *Mining of Massive Datasets*, Cambridge Univ. Press, 3rd ed., 2020 (free PDF: mmds.org) |
| **[MMS]** | Viktor Mayer-Schönberger & Kenneth Cukier, *Big Data: A Revolution*, Houghton Mifflin, 2013 |

---

## Ivy League Alignment

This plan draws syllabus benchmarks from:
- **Stanford CS246** — Mining Massive Datasets (Leskovec et al.)
- **MIT 6.830 / 6.S897** — Database Systems & ML for Healthcare
- **Harvard CS265** — Big Data Systems (Idreos)
- **CMU 15-721** — Advanced Database Systems (Pavlo)
- **Columbia COMS 4995** — Big Data Analytics

---

---

# WEEK 1
## Topic: Digital Data Landscape, Introduction to Big Data, and the 3Vs Framework

**CLO Addressed:** CLO1
**PLO Alignment:** PLO(a)

---

### 1. Basic Introduction

Data is generated every second — from social networks, sensors, financial transactions, and scientific instruments. Traditional relational databases struggle to ingest, store, and query data at this scale. "Big Data" is the umbrella term for datasets whose Volume, Velocity, and Variety exceed the capacity of conventional database tools to capture, manage, and process within a tolerable elapsed time.

**Why it matters:** By 2025, IDC forecasts the global datasphere will reach **175 zettabytes**. Organizations that can mine this data gain competitive, scientific, and social advantage.

---

### 2. Formal Introduction — Research Article

> **Doug Laney (2001):** *"3D Data Management: Controlling Data Volume, Velocity and Variety."* META Group Research Note.

Laney coined the **3Vs** that remain the canonical definition of Big Data:

| Dimension | Definition | Example |
|-----------|------------|---------|
| **Volume** | Scale of data | Facebook: 500 TB/day ingested |
| **Velocity** | Speed of generation and processing | Twitter: 6,000 tweets/second |
| **Variety** | Diversity of data types | Text, images, sensor streams, logs |

Later scholars extended to **5Vs** (adding **Veracity** — data quality uncertainty, and **Value** — business utility):
> Beyer & Laney (2012), Gartner: *"Big data is high-volume, high-velocity and/or high-variety information assets that demand cost-effective, innovative forms of information processing."*

**Types of Digital Data:**
- **Structured:** RDBMS tables, CSV (easy to query, ~20% of world data)
- **Semi-structured:** JSON, XML, logs (schema-on-read)
- **Unstructured:** images, video, free text (~80% of world data — the frontier)

---

### 3. Scalable Data Science Context

- **Distributed computing problem:** Single-machine RAM limits (terabytes ≠ petabytes). Solution: horizontal scaling across commodity clusters.
- **CAP Theorem** (Brewer, 2000): A distributed system can guarantee only two of — Consistency, Availability, Partition tolerance. Big Data systems (Cassandra, HBase) explicitly trade consistency for availability.
- **Batch vs. Stream processing:** Batch (Hadoop) processes stored data; stream (Kafka, Flink) processes in motion.

---

### 4. Case Study — McKinsey Global Institute (2011)

> *"Big Data: The Next Frontier for Innovation, Competition, and Productivity"* — James Manyika et al.

Key findings:
- Retailers using big data analytics could increase operating margin by **>60%**.
- The US healthcare system could create **>$300 billion** in value annually.
- Big data is a new factor of production alongside capital and labor.

**Discussion point:** Where does Bangladesh's healthcare or fintech sector stand? What 3V challenges does it face?

---

### 5. Textbook Reference

- **[SA]** Chapter 1 — Introduction to Big Data
- **[TE]** Chapter 1 — Understanding Big Data
- **[MMS]** Chapter 1 — Now (narrative of big data's emergence)
- **[LRU]** Chapter 1 — Data Mining (context and scale)

---

### 6. Ivy League Connection

Stanford CS246 — Week 1 opens with "The World of Large-Scale Data" and the challenge of algorithms whose runtime must be *sub-quadratic*. Students benchmark against Google and Facebook production scale.

---

### 7. Student Assessment Pool — Week 1

**MCQ (select one correct answer)**

1. Who first formally introduced the 3Vs framework for Big Data?
   - a) Jim Gray b) **Doug Laney** c) Jeffrey Dean d) Erik Brynjolfsson

2. Which of the following is an example of unstructured data?
   - a) SQL table b) CSV file c) **MRI scan image** d) JSON array

3. The CAP theorem states that a distributed system cannot simultaneously guarantee more than two of which three properties?
   - a) Cost, Availability, Performance
   - b) **Consistency, Availability, Partition Tolerance**
   - c) Correctness, Atomicity, Persistence
   - d) Concurrency, Accuracy, Partitioning

4. Which "V" of big data refers to the speed at which data is generated and processed?
   - a) Volume b) Variety c) **Velocity** d) Veracity

**True / False**

| Statement | Answer |
|-----------|--------|
| Structured data accounts for approximately 80% of all digital data. | **False** |
| The 3Vs framework was extended to 5Vs by adding Veracity and Value. | **True** |
| Horizontal scaling adds more RAM to a single server. | **False** |
| Batch processing is suitable for real-time fraud detection. | **False** |

**Descriptive Questions**

1. Explain the 3Vs (and optionally 5Vs) of Big Data with one real-world example for each dimension.
2. Differentiate between structured, semi-structured, and unstructured data with examples from the healthcare domain.
3. What is the CAP theorem? Why is it fundamentally important for designing distributed big data systems?

**Analytical Questions**

1. A ride-sharing company (like Uber) collects GPS pings every 3 seconds from 5 million active drivers. Analyze this scenario using the 5Vs framework. Which V poses the greatest engineering challenge and why?
2. Compare batch processing vs. stream processing. For which use cases would you choose each, and what are the trade-offs?

---
---

# WEEK 2
## Topic: Challenges of Big Data — Extraction, Integration, and Heterogeneous Information

**CLO Addressed:** CLO2
**PLO Alignment:** PLO(b), PLO(c)

---

### 1. Basic Introduction

Even after collecting big data, organizations face a harder problem: **making sense of it**. Data lives in silos — relational databases, flat files, NoSQL stores, APIs, and data streams — often with inconsistent schemas, formats, and semantics. Extracting and integrating this heterogeneous information is the central challenge of data engineering.

---

### 2. Formal Introduction — Research Article

> **Halevy, Rajaraman & Ordille (2006):** *"Data Integration: The Teenage Years."* Proceedings of VLDB.

The paper surveys 30 years of data integration research and frames the core problem: given a set of heterogeneous data sources, provide unified query access. Key contributions:
- **Schema mapping:** translating one schema to another
- **Data exchange:** materializing data from source to target schema
- **Entity resolution:** deciding if two records refer to the same real-world entity

> **Doan, Halevy & Ives (2012):** *Principles of Data Integration.* Morgan Kaufmann. *(Foundational graduate textbook at MIT and Stanford)*

---

### 3. Key Challenges Explored

| Challenge | Description | Big Data Specific Issue |
|-----------|-------------|------------------------|
| **Heterogeneity** | Different formats, schemas | CSV + JSON + XML + streaming logs |
| **Scale** | Volume overwhelms ETL pipelines | Cannot load 100TB into memory |
| **Noise & Missing Values** | Data quality problems | Sensor dropout, OCR errors |
| **Provenance** | Tracking data origins | Regulatory compliance (GDPR) |
| **Latency** | Time to integrate | Real-time decision vs. nightly batch |

**ETL vs. ELT:**
- **ETL** (Extract-Transform-Load): Transform *before* loading — traditional data warehouses
- **ELT** (Extract-Load-Transform): Load raw data first, transform on demand — modern data lakes (S3 + Spark)

---

### 4. Case Study — Healthcare Interoperability (HL7/FHIR)

US hospitals use dozens of incompatible EHR systems. The HL7 FHIR standard defines APIs for health data exchange. A 2019 Johns Hopkins study showed that **integration failures cost US hospitals $8.3 billion annually**. This is a real-world CLO2 scenario: analyze the challenges, propose solutions.

---

### 5. Textbook Reference

- **[SA]** Chapter 2 — Big Data Sources and Challenges
- **[TE]** Chapter 3 — Big Data Adoption and Planning Considerations
- **[LRU]** Chapter 1.3 — Distributed File Systems

---

### 6. Student Assessment Pool — Week 2

**MCQ**

1. Which technique determines whether two records from different datasets refer to the same real-world entity?
   - a) Schema mapping b) Data exchange c) **Entity resolution** d) Data partitioning

2. In the ELT paradigm, when does transformation occur?
   - a) Before extraction b) During extraction c) Before loading d) **After loading**

3. Which of the following is NOT a common challenge in big data integration?
   - a) Heterogeneity b) Provenance tracking c) **Low network bandwidth at a single node** d) Data quality noise

**True / False**

| Statement | Answer |
|-----------|--------|
| ETL is preferred over ELT in modern data lake architectures. | **False** |
| Entity resolution is needed when integrating data from multiple sources about the same object. | **True** |
| GDPR requires organizations to track the provenance of personal data. | **True** |

**Descriptive Questions**

1. Define the ETL process and explain each step with a concrete big data example.
2. What is schema heterogeneity? Give an example of structural heterogeneity and semantic heterogeneity.
3. Describe three major data quality challenges in big data pipelines and how they can be mitigated.

**Analytical Questions**

1. A government agency wants to build a unified healthcare analytics platform by integrating data from 50 public hospitals, each using a different EHR system. Identify at least four integration challenges and propose a strategy for each.
2. Compare the data integration needs of a batch analytics system (nightly report) vs. a real-time fraud detection system. How does the choice of ETL/ELT change?

---
---

# WEEK 3
## Topic: The Big Data Ecosystem — HDFS, Hadoop, and the Distributed Storage Foundation

**CLO Addressed:** CLO1
**PLO Alignment:** PLO(a)

---

### 1. Basic Introduction

The "Big Data Ecosystem" is a stack of interoperable open-source tools built around a core insight: **move computation to data, not data to computation**. At its foundation lies distributed storage. Before 2003, no open-source system could reliably store and process petabytes. Google published the paper that changed everything.

---

### 2. Formal Introduction — Research Article

> **Ghemawat, Gobioff & Leung (2003):** *"The Google File System."* ACM SOSP 2003.

Key design principles (directly adopted by Hadoop's HDFS):
- Commodity hardware **will fail** — design for fault tolerance from the start
- Files are large (multi-GB); optimize for **sequential reads**, not random access
- **Replication factor** of 3: one copy local, one on same rack, one off-rack
- **Master/Worker architecture:** single NameNode (metadata) + many DataNodes (blocks)

This paper is required reading at MIT 6.830 and Harvard CS265.

**Hadoop Ecosystem Map:**

```
┌──────────────────────────────────────────────┐
│  Applications (Pig, Hive, HBase, Spark, ...)  │
├──────────────────────────────────────────────┤
│        YARN — Resource Management             │
├──────────────────────────────────────────────┤
│     MapReduce — Distributed Computation       │
├──────────────────────────────────────────────┤
│     HDFS — Distributed File System            │
└──────────────────────────────────────────────┘
         Commodity Hardware Cluster
```

---

### 3. HDFS Architecture Deep Dive

| Component | Role | Fault behavior |
|-----------|------|----------------|
| **NameNode** | Stores metadata (file→block mapping) | If it fails, cluster is unavailable → use HA with Standby NameNode |
| **DataNode** | Stores actual data blocks (default 128 MB) | Replication handles single node failure |
| **Secondary NameNode** | Periodically merges edit log — NOT a failover | Common misconception on exams |

**Block size rationale:** Large blocks (128 MB vs. traditional 4 KB) reduce metadata overhead and favor sequential I/O patterns typical in big data analytics.

---

### 4. Case Study — Yahoo!'s Hadoop Deployment (2008)

Yahoo! ran the world's largest Hadoop cluster (10,000 cores, 5 PB storage) to power web search indexing. This production deployment validated Hadoop's industrial viability and led to the creation of the **Apache Software Foundation's Hadoop project**, spun off from Yahoo!'s internal codebase.

---

### 5. Textbook Reference

- **[TW]** Chapter 1 — Meet Hadoop; Chapter 3 — The Hadoop Distributed File System
- **[SA]** Chapter 3 — Hadoop Distributed File System
- **[TE]** Chapter 8 — Big Data Storage Technology

---

### 6. Student Assessment Pool — Week 3

**MCQ**

1. What is the default block size in HDFS (Hadoop 2.x+)?
   - a) 32 MB b) 64 MB c) **128 MB** d) 256 MB

2. In HDFS, which node stores the metadata (file-to-block mappings)?
   - a) DataNode b) **NameNode** c) Secondary NameNode d) ResourceManager

3. What is the default replication factor in HDFS?
   - a) 1 b) 2 c) **3** d) 5

4. The Secondary NameNode in HDFS primarily serves as:
   - a) A hot standby for the NameNode
   - b) **A checkpoint mechanism to merge the edit log with the FsImage**
   - c) A backup data storage node
   - d) A load balancer for DataNodes

**True / False**

| Statement | Answer |
|-----------|--------|
| HDFS is optimized for low-latency random reads. | **False** |
| The Google File System paper directly inspired HDFS design. | **True** |
| In HDFS, computation is moved to where data resides on DataNodes. | **True** |
| Losing a NameNode makes the cluster's data permanently unrecoverable. | **False** (HA Standby + FsImage backups can recover) |

**Descriptive Questions**

1. Explain the master/worker architecture of HDFS. What happens when a DataNode fails?
2. Why does HDFS use a large block size (128 MB)? What workloads benefit and which are harmed?
3. Draw and explain the Hadoop ecosystem stack, identifying the role of each layer.

**Analytical Questions**

1. A DataNode storing blocks B1, B2, B3 (each replicated 3×) crashes permanently. Trace exactly what the NameNode does to restore the replication factor. Which nodes are chosen and why?
2. Compare HDFS design goals with a traditional NFS (Network File System). In which scenarios would you choose each?

---
---

# WEEK 4
## Topic: Key-Value Paradigm — MapReduce, Pig, Hive, and HBase

**CLO Addressed:** CLO1
**PLO Alignment:** PLO(a)

---

### 1. Basic Introduction

Once data is stored in HDFS, how do we compute over it? The answer Google invented in 2004 — **MapReduce** — is a programming model so elegant that it can be explained in two lines: **Map** transforms records into key-value pairs; **Reduce** aggregates values by key. Every distributed computation in the Hadoop ecosystem is, at its core, a variation of this pattern.

---

### 2. Formal Introduction — Research Article

> **Dean & Ghemawat (2004):** *"MapReduce: Simplified Data Processing on Large Clusters."* OSDI 2004. *(One of the most cited systems papers in history — 20,000+ citations)*

Key insight from the abstract:
> *"Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key."*

**Bigtable (the precursor to HBase):**
> **Chang et al. (2006):** *"Bigtable: A Distributed Storage System for Structured Data."* OSDI 2006.

HBase is the open-source implementation of Google's Bigtable — a sparse, distributed, persistent multidimensional sorted map.

---

### 3. Core Concepts

**MapReduce Word Count (canonical example):**
```
Input:  "the cat sat on the mat"
Map:    (the,1), (cat,1), (sat,1), (on,1), (the,1), (mat,1)
Shuffle: (cat,[1]), (mat,[1]), (on,[1]), (sat,[1]), (the,[1,1])
Reduce: (cat,1), (mat,1), (on,1), (sat,1), (the,2)
```

**Ecosystem Tools:**

| Tool | Abstraction Level | Use Case |
|------|------------------|----------|
| **MapReduce** | Low-level Java API | Custom distributed algorithms |
| **Pig** | Dataflow scripting (Pig Latin) | ETL pipelines; procedural |
| **Hive** | SQL-like (HiveQL) | Ad-hoc queries by analysts |
| **HBase** | NoSQL column-family store | Random read/write; OLTP on Hadoop |

**Pig vs. Hive:**
- Pig: procedural, good for complex multi-step transformations
- Hive: declarative SQL, good for analysts who know SQL, compiles to MapReduce/Tez/Spark underneath

---

### 4. Case Study — Facebook's Data Warehouse with Hive (2009)

> Thusoo et al. (2009): *"Hive – A Warehousing Solution Over a Map-Reduce Framework."* VLDB 2009.

Facebook had **2 PB of data** and thousands of engineers who knew SQL but not Java/MapReduce. Hive was built internally and then open-sourced. It translated SQL queries into MapReduce jobs, democratizing big data analytics at Facebook's scale.

---

### 5. Textbook Reference

- **[TW]** Chapter 2 — MapReduce; Chapter 12 — Hive; Chapter 20 — HBase
- **[SA]** Chapter 4 — MapReduce; Chapter 5 — Pig and Hive
- **[LRU]** Chapter 2 — MapReduce and the New Software Stack

---

### 6. Student Assessment Pool — Week 4

**MCQ**

1. In the MapReduce model, which phase sorts and groups intermediate key-value pairs before passing them to Reducers?
   - a) Map b) **Shuffle and Sort** c) Combine d) Partition

2. Which Hadoop ecosystem tool uses a scripting language called "Pig Latin"?
   - a) Hive b) **Pig** c) HBase d) Sqoop

3. HBase is the open-source implementation of which Google system?
   - a) MapReduce b) GFS c) **Bigtable** d) Dremel

4. Which of the following best describes HBase's data model?
   - a) Relational table with foreign keys
   - b) Document store
   - c) **Sparse, distributed, persistent multidimensional sorted map**
   - d) Graph database

**True / False**

| Statement | Answer |
|-----------|--------|
| MapReduce was first published by Facebook. | **False** (Google) |
| Hive queries are compiled into MapReduce (or Tez/Spark) jobs at runtime. | **True** |
| Pig is better suited than Hive for analysts who already know SQL. | **False** |
| HBase supports low-latency random read/write operations unlike HDFS. | **True** |

**Descriptive Questions**

1. Walk through the MapReduce execution model — Map, Shuffle, Reduce — using the word count example.
2. Compare Pig and Hive: when would you choose each in a production ETL pipeline?
3. Explain HBase's column-family data model. How does it differ from a relational schema?

**Analytical Questions**

1. You have a 500 GB log file containing web server access records. Design a MapReduce job to find the top-10 most visited URLs. Write the pseudocode for both the Map and Reduce functions.
2. A startup must choose between Hive and HBase for their analytics backend. They have SQL-fluent data analysts and need both ad-hoc queries (batch) and real-time lookups. What would you recommend and why?

---
---

# WEEK 5
## Topic: Handling Big Data Files in Hadoop — YARN, File Formats, and Optimization

**CLO Addressed:** CLO3
**PLO Alignment:** PLO(e), PLO(f)

---

### 1. Basic Introduction

Storing data in HDFS is only half the battle. How data is **formatted, compressed, and scheduled** fundamentally determines whether your analytics jobs run in minutes or hours. This week explores Hadoop's resource manager (YARN), production-grade file formats (Avro, Parquet, ORC), and optimization strategies used by Netflix, LinkedIn, and Google.

---

### 2. Formal Introduction — Research Article

> **Vavilapalli et al. (2013):** *"Apache Hadoop YARN: Yet Another Resource Negotiator."* ACM SoCC 2013.

YARN decoupled resource management from the MapReduce programming model, enabling **multiple computation frameworks** (Spark, Tez, Storm) to run on the same Hadoop cluster. This was the "Hadoop 2.0" inflection point.

**YARN Architecture:**
```
ResourceManager (global scheduler)
    ├── NodeManager (per-node agent, manages containers)
    └── ApplicationMaster (per-job, negotiates resources)
```

---

### 3. File Formats Comparison

| Format | Type | Schema | Splittable | Best For |
|--------|------|--------|-----------|---------|
| **Text/CSV** | Row | External | Yes (with codec) | Small data, portability |
| **Avro** | Row | Self-describing (JSON schema) | Yes | Write-heavy, schema evolution |
| **Parquet** | Columnar | Self-describing | Yes | Read-heavy analytics, high compression |
| **ORC** | Columnar | Self-describing | Yes | Hive-optimized; best compression |

**Why columnar matters:** An analytics query reading 3 of 100 columns only reads 3% of the data with Parquet/ORC vs. 100% with CSV.

**Compression codecs:** Snappy (fast, moderate compression), Gzip (slow, high compression), LZO (splittable).

---

### 4. Case Study — LinkedIn's Avro Adoption

LinkedIn introduced Avro to handle **schema evolution** in their Kafka-Hadoop pipeline. When a producer adds a new field, consumers using older schemas must not break. Avro's schema registry pattern (later popularized by Confluent) solved this in production at LinkedIn's 5 TB/day ingestion scale.

---

### 5. Textbook Reference

- **[TW]** Chapter 3 — HDFS; Chapter 4 — YARN; Chapter 5 — Hadoop I/O (compression, serialization, file formats)
- **[SA]** Chapter 6 — YARN and Resource Management

---

### 6. Student Assessment Pool — Week 5

**MCQ**

1. Which component in YARN is responsible for global resource allocation across the cluster?
   - a) NodeManager b) ApplicationMaster c) **ResourceManager** d) NameNode

2. Which Hadoop file format stores data in columnar format and is best suited for analytical read-heavy workloads?
   - a) Avro b) Text/CSV c) **Parquet** d) JSON

3. What does "splittable" mean for a file format in Hadoop?
   - a) The file can be deleted in parts
   - b) **Multiple mappers can process different parts of the file simultaneously**
   - c) The file can be split across NameNodes
   - d) The file format supports schema splitting

4. YARN was introduced in which major Hadoop version?
   - a) Hadoop 1.0 b) **Hadoop 2.0** c) Hadoop 3.0 d) Hadoop 0.20

**True / False**

| Statement | Answer |
|-----------|--------|
| Parquet is a row-oriented file format optimized for writes. | **False** |
| YARN allows multiple computation frameworks (Spark, Tez) to run on the same cluster. | **True** |
| Gzip-compressed files are natively splittable in Hadoop. | **False** |
| ORC format is specifically optimized for Hive workloads. | **True** |

**Descriptive Questions**

1. Explain YARN's three-component architecture (ResourceManager, NodeManager, ApplicationMaster) and how they interact to execute a job.
2. What is columnar storage? Why does it improve performance for analytics queries that select only a subset of columns?
3. Compare Avro and Parquet. In which scenarios would you use each?

**Analytical Questions**

1. A data lake holds 10 TB of web click data stored as gzip-compressed CSV. Query performance is poor. Propose a migration strategy to improve performance — what format would you choose, how would you partition the data, and what compression codec?
2. A NodeManager fails mid-job in YARN. Trace what happens: which components detect the failure, and how is the running container restarted?

---
---

# WEEK 6
## Topic: MapReduce Deep Dive and Apache Spark — RDDs, DataFrames, and In-Memory Computing

**CLO Addressed:** CLO3
**PLO Alignment:** PLO(e), PLO(f)

---

### 1. Basic Introduction

MapReduce has a critical weakness: every intermediate result is written to disk. For iterative algorithms (machine learning, graph processing), this means thousands of expensive disk reads/writes. In 2010, a UC Berkeley PhD student named Matei Zaharia asked: *what if we kept intermediate data in memory?* The answer was **Apache Spark** — now the dominant big data processing engine.

---

### 2. Formal Introduction — Research Article

> **Zaharia et al. (2010):** *"Spark: Cluster Computing with Working Sets."* USENIX HotCloud 2010.

> **Zaharia et al. (2012):** *"Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing."* USENIX NSDI 2012. *(Best Paper Award)*

Key abstraction — **Resilient Distributed Dataset (RDD):**
- An immutable, partitioned collection of records
- Tracks **lineage** (how it was derived) instead of replicating data
- Recompute lost partitions from lineage on failure (fault tolerance without replication overhead)
- **10–100× faster** than MapReduce for iterative workloads

---

### 3. MapReduce vs. Spark

| Aspect | MapReduce | Spark |
|--------|-----------|-------|
| Data storage between stages | **Disk** (HDFS) | **Memory** (with disk spill) |
| Programming model | Map + Reduce only | Rich: map, filter, join, groupBy, SQL, ML |
| Languages | Java (primarily) | Scala, Python (PySpark), R, Java |
| Iterative algorithms | Slow (disk I/O each iteration) | Fast (cache RDD in memory) |
| Stream processing | No | Yes (Spark Streaming / Structured Streaming) |
| Learning curve | Low (simple model) | Moderate |

**Spark Architecture:**
```
Driver Program (SparkContext)
    ├── Cluster Manager (YARN / Mesos / Standalone)
    └── Executors (on Worker Nodes)
            ├── Tasks (unit of computation)
            └── Cache (in-memory RDD partitions)
```

**Spark Ecosystem:**
- **Spark SQL / DataFrames** — structured data with schema
- **MLlib** — distributed machine learning
- **GraphX** — graph computation
- **Structured Streaming** — real-time stream processing

---

### 4. Case Study — Databricks and the Logistic Regression Benchmark (2014)

In a published benchmark (Zaharia et al., 2014), Spark ran logistic regression **100× faster than Hadoop MapReduce** on the same cluster because each iteration reused the cached training dataset from memory rather than re-reading from HDFS. This benchmark drove enterprise adoption at LinkedIn, Netflix, and Alibaba.

---

### 5. Textbook Reference

- **[TW]** Chapter 2 — MapReduce; Chapter 19 — Spark (4th edition appendix)
- **[SA]** Chapter 7 — Introduction to Apache Spark
- **[LRU]** Chapter 2.4 — Spark's Model

**Additional:** Karau et al., *Learning Spark*, O'Reilly, 2015 (free 1st edition PDF available)

---

### 6. Student Assessment Pool — Week 6

**MCQ**

1. What makes Spark significantly faster than MapReduce for iterative algorithms?
   - a) Spark uses more CPU cores
   - b) Spark writes intermediate results to faster SSDs
   - c) **Spark caches intermediate data in memory (RDDs)**
   - d) Spark skips the shuffle phase

2. How does Spark achieve fault tolerance in RDDs without full data replication?
   - a) Checkpointing to HDFS every minute
   - b) **Tracking lineage and recomputing lost partitions**
   - c) Copying each RDD partition twice
   - d) Using a write-ahead log

3. Which of the following is NOT a component of the Spark ecosystem?
   - a) MLlib b) GraphX c) Structured Streaming d) **HBase**

4. In Spark, a "transformation" (e.g., map, filter) is:
   - a) Immediately executed when called
   - b) **Lazily evaluated — only executed when an action is called**
   - c) Persisted to HDFS automatically
   - d) Only available in the Scala API

**True / False**

| Statement | Answer |
|-----------|--------|
| Spark can only run on top of Hadoop/YARN. | **False** (also Mesos, Kubernetes, Standalone) |
| RDDs are mutable — you can modify individual elements in place. | **False** |
| Spark's DataFrame API provides schema-aware operations similar to SQL tables. | **True** |
| MapReduce is generally better than Spark for machine learning workloads. | **False** |

**Descriptive Questions**

1. Explain the concept of a Resilient Distributed Dataset (RDD). What does "resilient" mean in this context?
2. Differentiate between Spark transformations and actions. Give two examples of each.
3. Describe Spark's lazy evaluation model. What is the advantage of not executing transformations immediately?

**Analytical Questions**

1. You need to train a K-Means clustering model over 50 GB of data with 100 iterations. Compare the I/O cost of this computation in MapReduce vs. Spark (with data cached in memory). Quantify the difference assuming HDFS reads take 100 ms per 128 MB block.
2. A Spark job fails halfway through because an executor crashes. Explain how Spark recovers using RDD lineage. What is the worst-case cost of this recovery?

---
---

# WEEK 7
## Topic: Querying Big Data — Hive, HiveQL, and the SQL-on-Hadoop Ecosystem

**CLO Addressed:** CLO3, CLO4
**PLO Alignment:** PLO(e), PLO(f)

---

### 1. Basic Introduction

Most business analysts speak SQL, not Java. The SQL-on-Hadoop movement created declarative query interfaces over distributed data — enabling teams to query petabytes of data without writing a single line of MapReduce code. Hive pioneered this, and the ecosystem now includes Presto (Meta), Impala (Cloudera), Drill (Apache), and Spark SQL.

---

### 2. Formal Introduction — Research Article

> **Thusoo et al. (2009):** *"Hive – A Warehousing Solution Over a Map-Reduce Framework."* PVLDB 2009.

> **Thusoo et al. (2010):** *"Hive – A Petabyte Scale Data Warehouse Using Hadoop."* IEEE ICDE 2010.

Key architectural insight: Hive stores metadata (schemas, partitions, locations) in a **Metastore** (relational DB like MySQL) and translates HiveQL queries into a **DAG of MapReduce/Tez/Spark jobs**.

**Presto comparison (Meta, 2013):**
> Venkataraman et al.: *"Presto: SQL on Everything."* ICDE 2019. — Presto runs queries in memory without materializing intermediate results to disk, giving 10× faster interactive query performance vs. Hive+MapReduce.

---

### 3. HiveQL Essentials

**Hive vs. SQL differences (important exam topics):**

| Feature | SQL (RDBMS) | HiveQL |
|---------|-------------|--------|
| Schema enforcement | On write | **On read** (schema-on-read) |
| ACID transactions | Full support | Limited (ORC tables + ACID mode) |
| UPDATE/DELETE | Supported | Limited |
| Index | B-tree indexes | Partitions + Buckets |
| Latency | Milliseconds | Minutes (batch) |

**Partitioning and Bucketing:**
```sql
-- Partitioned table: data physically organized by year/month
CREATE TABLE sales (id INT, amount DOUBLE)
PARTITIONED BY (year INT, month INT)
STORED AS ORC;

-- Query only reads 2024/01 partition — avoids full table scan
SELECT SUM(amount) FROM sales WHERE year=2024 AND month=1;
```

**Bucketing:** Divides partitions into fixed-number buckets using a hash function — enables efficient JOIN operations (bucket map joins).

---

### 4. Case Study — Spotify's Hive-Based Analytics Platform

Spotify processes **600+ billion events per day** (stream plays, skips, searches). Their analytics pipeline uses Hive on top of HDFS for batch analytics — computing recommendation signals, artist royalty reports, and A/B test analysis. The Hive Metastore catalogs over **1 million tables**. (Source: Spotify Engineering Blog, 2020)

---

### 5. Textbook Reference

- **[TW]** Chapter 12 — Hive (comprehensive)
- **[SA]** Chapter 5 — Hive
- **[LRU]** Chapter 2 — SQL analogies in MapReduce

---

### 6. Student Assessment Pool — Week 7

**MCQ**

1. In Hive, where is table schema metadata (column names, types, partitions) stored?
   - a) HDFS NameNode b) **Hive Metastore** c) HBase d) ZooKeeper

2. What does "schema-on-read" mean in the context of Hive?
   - a) Schema is validated when data is inserted
   - b) **Schema is applied when data is queried, not when it is stored**
   - c) Schema is stored separately from data
   - d) Schema is inferred automatically from column names

3. Which optimization technique in Hive physically organizes data by a column's value to avoid full table scans?
   - a) Bucketing b) Indexing c) **Partitioning** d) Compression

4. Presto's primary advantage over Hive+MapReduce is:
   - a) Supports more SQL functions
   - b) Better integration with HBase
   - c) **In-memory query execution without materializing intermediate results to disk**
   - d) Native Python support

**True / False**

| Statement | Answer |
|-----------|--------|
| HiveQL supports full ACID transactions on all table types. | **False** |
| Partitioning in Hive reduces query time by eliminating irrelevant data partitions from scan. | **True** |
| Hive directly executes queries without any translation layer. | **False** |
| Bucketing in Hive is useful for optimizing JOIN operations. | **True** |

**Descriptive Questions**

1. Explain the Hive architecture: what role does the Metastore play, and how is a HiveQL query compiled and executed?
2. Differentiate between partitioning and bucketing in Hive. When would you use each?
3. What is "schema-on-read"? What are its advantages and disadvantages compared to "schema-on-write" in traditional RDBMS?

**Analytical Questions (CLO4 — Apply)**

1. You have a 5 TB e-commerce transaction table with columns: `(transaction_id, user_id, product_id, amount, country, date)`. Design the partitioning and bucketing strategy to optimize: (a) daily revenue reports by country, (b) joins with a 10M-row user profile table.
2. Write HiveQL queries to: (a) find the top 5 products by total revenue in 2023, (b) compute the monthly average transaction amount per country for Q1 2024. Explain how Hive would compile each query into MapReduce stages.

---
---

# WEEK 8
## Topic: Data Integration at Scale — Pipelines, Data Lakes, and Modern Architectures

**CLO Addressed:** CLO3, CLO4
**PLO Alignment:** PLO(e), PLO(f)

---

### 1. Basic Introduction

Data integration at big data scale is not just a technical challenge — it is an architectural one. Modern enterprises have moved from single-system ETL to **data pipelines** and **data lakes** that ingest from hundreds of sources, integrate in real time, and serve downstream ML models, dashboards, and data products. This week bridges theory and production architecture.

---

### 2. Formal Introduction — Research Article

> **Kreps, Narkhede & Rao (2011):** *"Kafka: A Distributed Messaging System for Log Aggregation."* LinkedIn Engineering.

Apache Kafka became the backbone of real-time data integration. Its **log-structured storage** model (append-only, immutable) enables high-throughput ingestion and replay.

> **Kleppmann (2017):** *Designing Data-Intensive Applications.* O'Reilly. *(Graduate-level systems bible at MIT, CMU, and Stanford)*

Key concepts from Kleppmann:
- **Batch integration:** Sqoop (RDBMS→HDFS), Flume (logs→HDFS)
- **Stream integration:** Kafka, Kinesis (AWS)
- **Lambda architecture:** Kappa architecture

---

### 3. Integration Tools Ecosystem

| Tool | Direction | Type | Use Case |
|------|-----------|------|----------|
| **Sqoop** | RDBMS ↔ HDFS | Batch | Nightly database dumps |
| **Flume** | Log sources → HDFS | Batch/micro-batch | Web server log ingestion |
| **Kafka** | Any → Any | Stream | Real-time event streaming |
| **NiFi** | Any → Any | Visual pipeline | Data routing with UI |
| **Spark Streaming** | Kafka → HDFS/DB | Stream processing | Stateful stream analytics |

**Lambda Architecture (Nathan Marz):**
```
          Raw Data
         /        \
    Batch Layer   Speed Layer (Kafka + Spark Streaming)
    (Hadoop/Spark) (real-time views)
         \        /
          Serving Layer (merged views → applications)
```

**Kappa Architecture (Jay Kreps):** Eliminate the batch layer; reprocess historical data by replaying Kafka logs through the stream processing system.

---

### 4. Case Study — Netflix's Data Pipeline

Netflix ingests **500 billion events per day** (playback events, errors, recommendations). Their integration stack:
1. Kafka: real-time event bus (thousands of topics)
2. Flink / Spark Streaming: real-time enrichment and aggregation
3. S3 (data lake) + Iceberg (table format): historical storage
4. Spark + Hive: batch analytics for A/B testing reports

(Source: Netflix Tech Blog — "Keystone Real-time Stream Processing Platform")

---

### 5. Textbook Reference

- **[TW]** Chapter 15 — Sqoop; Chapter 14 — Flume
- **[SA]** Chapter 8 — Data Integration Tools
- **[TE]** Chapter 10 — Big Data Integration

---

### 6. Student Assessment Pool — Week 8

**MCQ**

1. Which tool is used to transfer data between RDBMS (e.g., MySQL) and HDFS in bulk?
   - a) Flume b) Kafka c) **Sqoop** d) NiFi

2. Apache Kafka's data model is based on:
   - a) B-tree indexes b) Column-family storage c) **Append-only immutable logs** d) Document storage

3. In the Lambda architecture, which layer handles real-time, low-latency views?
   - a) Batch Layer b) Serving Layer c) **Speed Layer** d) Ingestion Layer

4. The Kappa architecture differs from Lambda by:
   - a) Adding a third processing layer
   - b) Using only relational databases
   - c) **Eliminating the batch layer and using stream replay for reprocessing**
   - d) Replacing Hadoop with Spark

**True / False**

| Statement | Answer |
|-----------|--------|
| Sqoop is designed for real-time streaming ingestion. | **False** |
| Kafka retains messages for a configurable period, allowing replay. | **True** |
| The Lambda architecture requires maintaining two separate code paths. | **True** |
| Flume is primarily used for collecting and aggregating log data into HDFS. | **True** |

**Descriptive Questions**

1. Explain the Lambda architecture with a diagram. What are its advantages and drawbacks compared to the Kappa architecture?
2. Describe how Apache Kafka achieves high throughput and fault tolerance using its log-based storage model.
3. What is a data lake? How does it differ from a data warehouse in terms of schema, storage, and use cases?

**Analytical / CLO4 Questions**

1. Design a data integration pipeline for a bank that needs to: (a) sync 10 million customer records nightly from Oracle to Hadoop, (b) detect fraud in real time from card swipe events, (c) serve risk dashboards with data no older than 5 minutes. Which tools would you use at each stage? Justify your choices.
2. A team using the Lambda architecture complains that maintaining two code paths (batch + stream) doubles development cost. Their CTO suggests switching to Kappa. What are the trade-offs of this migration? Under what conditions is Kappa architecture not suitable?

---
---

# WEEK 9
## Topic: Data Visualization — Principles, Techniques, and Big Data Visualization Tools

**CLO Addressed:** CLO3
**PLO Alignment:** PLO(e)

---

### 1. Basic Introduction

"A picture is worth a thousand words" — but a misleading visualization is worth a thousand bad decisions. As big data matures, the ability to communicate insights visually has become a core data science skill. Traditional static charts fail at petabyte scale — big data visualization requires interactive, scalable, and streaming-aware tools.

---

### 2. Formal Introduction — Research Article

> **Edward Tufte (1983):** *The Visual Display of Quantitative Information.* Graphics Press. *(The foundational text — required at Harvard, Yale, and Stanford data courses)*

Tufte's principles:
- **Data-ink ratio:** Maximize the proportion of ink devoted to data. Remove chart junk.
- **Small multiples:** Repeat the same graph structure across subsets for comparison.
- **Sparklines:** Small, word-sized graphics embedded in text.

> **Shneiderman (1996):** *"The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations."* IEEE Visual Languages.

Shneiderman's **visualization mantra:** *"Overview first, zoom and filter, then details on demand."*

> **Bostock, Ogievetsky & Heer (2011):** *"D³: Data-Driven Documents."* IEEE TVCG. — D3.js: the most influential web visualization library.

---

### 3. Visualization Techniques by Data Type

| Data Type | Recommended Visualizations |
|-----------|---------------------------|
| **Temporal** | Line chart, area chart, heatmap calendar |
| **Categorical** | Bar chart, grouped bar, treemap |
| **Geographical** | Choropleth map, bubble map |
| **Relational** | Network graph, chord diagram |
| **Distribution** | Histogram, box plot, violin plot |
| **High-dimensional** | Parallel coordinates, t-SNE scatterplot, heatmap |

**Big Data Specific Challenges:**
- **Overplotting:** Millions of points on a scatterplot → use hexbin or density contour
- **Latency:** Large datasets cannot be re-queried interactively → pre-aggregation, data cubes
- **Streaming visualization:** Charts that update in real time (D3.js + WebSockets, Grafana)

---

### 4. Tools Landscape

| Tool | Best For | Scale |
|------|----------|-------|
| **Tableau** | Business dashboards | Millions of rows |
| **Power BI** | Microsoft ecosystem | Millions of rows |
| **D3.js** | Custom web visualizations | Flexible |
| **Grafana** | Real-time metrics/time-series | Streaming |
| **Apache Superset** | Open-source BI on data lakes | Billions of rows |
| **Kibana** | Elasticsearch log analytics | Streaming |

---

### 5. Case Study — New York Times Graphics Desk

The NYT Upshot team used D3.js to build interactive visualizations of 2016–2020 election results, showing county-level vote swings with real-time data streaming as results came in. Their work demonstrated how visualization can communicate uncertainty — showing probability distributions rather than point estimates. This is now taught in Harvard's CS171 (Visualization).

---

### 6. Textbook Reference

- **[SA]** Chapter 10 — Data Visualization
- **[TE]** Chapter 12 — Big Data Analysis and Visualization
- Tufte, *The Visual Display of Quantitative Information* (supplementary)

---

### 7. Student Assessment Pool — Week 9

**MCQ**

1. Edward Tufte's "data-ink ratio" principle states that:
   - a) Use more colors to highlight data
   - b) **Maximize the proportion of ink used to represent actual data, removing decorative elements**
   - c) Use ink sparingly to reduce printing costs
   - d) Data labels should always use different ink colors

2. Which visualization is most appropriate for showing the distribution of a continuous variable?
   - a) Pie chart b) Line chart c) **Histogram** d) Treemap

3. Shneiderman's visualization mantra begins with:
   - a) "Details first, then overview"
   - b) **"Overview first, zoom and filter, then details on demand"**
   - c) "Filter first, then zoom"
   - d) "Details on demand, then overview"

4. Which tool is best suited for real-time streaming metric visualization in a production operations context?
   - a) Tableau b) D3.js c) Power BI d) **Grafana**

**True / False**

| Statement | Answer |
|-----------|--------|
| A pie chart is recommended for comparing more than 5 categories. | **False** |
| Hexbin plots are useful for reducing overplotting in large scatterplots. | **True** |
| D3.js generates static image files as its output. | **False** |
| Choropleth maps are used for visualizing geographic distributions. | **True** |

**Descriptive Questions**

1. Explain Tufte's data-ink ratio principle. Provide a "before and after" example of applying it to a cluttered bar chart.
2. What is overplotting? Describe three techniques to address it when visualizing millions of data points.
3. What is a data cube? How does pre-aggregation in a data cube enable interactive visualization of big data?

**Analytical Questions**

1. A public health dashboard needs to show (a) COVID-19 case counts by district over 24 months, (b) real-time hospitalization rates, (c) demographic breakdown of affected populations. Choose the appropriate visualization type for each and justify using Shneiderman's taxonomy.
2. Design a visualization strategy for a streaming Twitter sentiment analysis system. How would you handle the velocity challenge (10,000 tweets/second) in your visualization layer? What tools would you use?

---
---

# WEEK 10
## Topic: Big Data in Real Applications — Social Media, Time Series, and Health Data

**CLO Addressed:** CLO4
**PLO Alignment:** PLO(f)

---

### 1. Basic Introduction

Theory becomes power only when applied. This week bridges the full technical stack to three major real-world application domains where big data creates tangible impact: social media analytics, time series forecasting, and healthcare informatics. Each domain presents unique data characteristics, scale challenges, and ethical considerations.

---

### 2. Formal Introduction — Research Article

**Social Media Analytics:**
> **Kwak et al. (2010):** *"What is Twitter, a Social Network or a News Media?"* WWW 2010.
Analyzed 41.7 million Twitter users and found Twitter is a news medium where 85% of topics are headline news. Foundational for social influence analysis.

**Time Series:**
> **Taylor & Letham (2018):** *"Forecasting at Scale."* The American Statistician. — Facebook's **Prophet** library, designed for business time series with strong seasonality and holiday effects at scale.

**Healthcare:**
> **Obermeyer & Emanuel (2016):** *"Predicting the Future — Big Data, Machine Learning, and Clinical Medicine."* NEJM. — Argues clinical prediction models trained on EHR big data outperform physician heuristics for ICU mortality, readmission, and diagnosis.

---

### 3. Domain Deep Dives

#### Domain A: Social Media Analytics

**Data characteristics:** Graph-structured (followers/following), temporal (tweet timestamps), text (NLP), multimedia.

**Key tasks:**
- **Community detection:** Identify clusters of connected users (Louvain algorithm)
- **Influence maximization:** Which nodes to seed for maximum information spread (Kempe et al., 2003 — KDD Best Paper)
- **Sentiment analysis:** VADER (Valence Aware Dictionary for Sentiment Reasoning) for social media text
- **Trend detection:** Twitter's trending topics use locality-sensitive hashing on n-grams

**Tools:** GraphX (Spark), NetworkX, Neo4j, Twitter API v2

#### Domain B: Time Series Analysis

**Data characteristics:** Ordered, temporal, often seasonal, noisy.

**Key techniques:**
- **ARIMA:** Classic statistical forecasting
- **Prophet:** Facebook's decomposable model (trend + seasonality + holidays)
- **LSTM (Long Short-Term Memory):** Deep learning for sequential patterns
- **Anomaly detection:** Isolation Forest, STL decomposition

**Big data challenge:** Forecasting 10,000 product SKUs simultaneously → **vectorized batch forecasting** in Spark

#### Domain C: Healthcare / Medical Big Data

**Data sources:** EHR records, genomic data, wearables (IoT), medical imaging (DICOM)
**Key challenges:** Privacy (HIPAA, GDPR), small labeled datasets, class imbalance

**Landmark project:** Google DeepMind's AlphaFold (2020) — solved 50-year protein folding problem using big data + deep learning. Deposited 200 million protein structures in public database.

---

### 4. Case Study — Epidemic Intelligence at CDC

The US CDC uses Twitter and Google Flu Trends-style analysis for **syndromic surveillance** — detecting disease outbreaks before hospital reports arrive. Big data integration from pharmacy sales, emergency room chief complaints, and social media posts provides 1–2 week early warning of flu outbreaks. Lesson: big data supplements, but does not replace, ground-truth clinical surveillance.

---

### 5. Textbook Reference

- **[SA]** Chapter 11 — Big Data Use Cases
- **[TE]** Chapter 13 — Big Data in Practice
- **[LRU]** Chapter 10 — Social-Network Graphs

---

### 6. Student Assessment Pool — Week 10 (CLO4 — Application)

**MCQ**

1. Facebook's Prophet library is designed for:
   - a) Graph analytics on social networks
   - b) Real-time stream processing
   - c) **Time series forecasting with strong seasonality and holiday effects**
   - d) Text sentiment classification

2. Which algorithm is commonly used for community detection in social network graphs?
   - a) K-Means b) PageRank c) **Louvain algorithm** d) ARIMA

3. HIPAA in the USA primarily regulates:
   - a) Financial data privacy b) **Healthcare data privacy** c) Social media data usage d) Government data retention

4. AlphaFold (DeepMind) used big data and deep learning to solve:
   - a) Real-time fraud detection b) Social network analysis c) **The protein structure prediction problem** d) Time series anomaly detection

**True / False**

| Statement | Answer |
|-----------|--------|
| Google Flu Trends successfully replaced traditional CDC flu surveillance permanently. | **False** (it had accuracy problems and was discontinued as primary source) |
| Time series data is order-sensitive — shuffling records changes the analysis result. | **True** |
| Social network graphs are typically sparse (most nodes connected to few others). | **True** |
| Medical imaging data (MRI, CT scans) is classified as structured data. | **False** |

**Descriptive Questions**

1. Describe three types of analysis commonly performed on social media data. What are the ethical risks of each?
2. What is the difference between ARIMA and Facebook's Prophet for time series forecasting? When would you prefer Prophet?
3. Identify three data integration and privacy challenges specific to healthcare big data analytics.

**Analytical / Project Questions (CLO4)**

1. You are building a flu outbreak early-warning system for Bangladesh using Twitter data and pharmacy purchase records. (a) How would you collect, store, and integrate these data sources? (b) What features would you extract for a prediction model? (c) What are the ethical considerations?
2. A retail chain wants to forecast daily sales for 5,000 store-product combinations for the next 90 days. Describe an end-to-end big data pipeline: data ingestion, storage, forecasting model choice, and serving the results to a dashboard. Identify bottlenecks.

---
---

# WEEK 11
## Topic: Next Steps — Emerging Trends, Big Data Ethics, and Course Synthesis

**CLO Addressed:** CLO4
**PLO Alignment:** PLO(f)

---

### 1. Basic Introduction

Big data is not a destination — it is an evolving frontier. The tools we taught in Weeks 1–10 (Hadoop, Spark, Hive) represent the current mainstream. But the field is shifting rapidly: cloud-native architectures replace on-premise Hadoop clusters, AI/ML is embedded into every data pipeline, and edge computing pushes analytics to the source of data generation. This final week synthesizes the course, examines what comes next, and positions students for lifelong learning in the field.

---

### 2. Formal Introduction — Research Article

> **Armbrust et al. (2020):** *"Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores."* VLDB 2020. — The next evolution of data lakes: ACID transactions on S3/Azure Blob using Apache Spark.

> **Zaharia et al. (2021):** *"Lakehouse: A New Generation of Open Platforms That Unify Data Warehousing and Advanced Analytics."* CIDR 2021.

The **Lakehouse** paradigm (Databricks) unifies the flexibility of data lakes with the reliability of data warehouses:
```
Data Lake (S3/ADLS) + Delta Lake / Apache Iceberg + Spark SQL
= Lakehouse (ACID + schema enforcement + BI + ML on the same platform)
```

> **On AI Integration:**
> **Sculley et al. (2015):** *"Hidden Technical Debt in Machine Learning Systems."* NeurIPS 2015. — "Only a small fraction of real-world ML systems is composed of the ML code."

---

### 3. Emerging Trends

| Trend | Description | Representative Technology |
|-------|-------------|--------------------------|
| **Cloud-Native Big Data** | Move from on-premise Hadoop to managed cloud services | AWS EMR, Google Dataproc, Azure HDInsight |
| **Lakehouse Architecture** | Unified platform for BI + ML | Delta Lake, Apache Iceberg, Apache Hudi |
| **Real-Time Streaming** | Batch → micro-batch → streaming | Apache Flink, Kafka Streams |
| **MLOps & Data Pipelines** | Operationalizing ML at scale | MLflow, Airflow, Kubeflow |
| **Edge Analytics** | Processing data at the source (IoT) | AWS Greengrass, Azure IoT Edge |
| **Generative AI on Big Data** | LLMs for data querying, summarization | Text-to-SQL, RAG over data lakes |
| **Data Mesh** | Decentralized domain-oriented data ownership | Zhamak Dehghani (2019) |
| **Privacy-Preserving Analytics** | Compute on encrypted data | Federated Learning, Differential Privacy |

**Data Mesh (Dehghani, 2019):**
A sociotechnical paradigm shift — instead of a centralized data team, each business domain owns its own data as a **data product**. Harvard Business Review called it "the future of enterprise data."

---

### 4. Career Pathways from This Course

| Role | Skills from This Course | Additional Skills Needed |
|------|------------------------|--------------------------|
| **Data Engineer** | Hadoop, Spark, Kafka, Hive | Python, SQL, cloud (AWS/GCP) |
| **Data Analyst** | HiveQL, visualization, SQL | Statistics, Tableau/Power BI |
| **Data Scientist** | Spark MLlib, data pipelines | ML/DL (PyTorch/TF), statistics |
| **Big Data Architect** | Ecosystem design, integration | Cloud architecture, security |
| **ML Engineer** | Spark, data pipelines, integration | MLOps, model deployment |

---

### 5. Course Synthesis — CLO Coverage Map

| Week | Topic | CLO |
|------|-------|-----|
| 1 | 3Vs, Types of data | CLO1 |
| 2 | Integration challenges | CLO2 |
| 3 | HDFS, Hadoop Ecosystem | CLO1 |
| 4 | MapReduce, Pig, Hive, HBase | CLO1 |
| 5 | YARN, File formats | CLO3 |
| 6 | Spark, RDDs | CLO3 |
| 7 | HiveQL, SQL-on-Hadoop | CLO3, CLO4 |
| 8 | Data integration pipelines | CLO3, CLO4 |
| 9 | Visualization | CLO3 |
| 10 | Real applications | CLO4 |
| 11 | Emerging trends, synthesis | CLO4 |

---

### 6. Case Study — Google's Dataflow / Apache Beam (2015)

> **Akidau et al. (2015):** *"The Dataflow Model: A Practical Approach to Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-Order Data Processing."* VLDB 2015.

Google unified batch and stream processing in a single programming model (Apache Beam), eliminating the Lambda architecture's dual code path. Beam jobs run on multiple backends (Spark, Flink, Google Dataflow). This represents the convergence of all the technologies studied in this course.

---

### 7. Student Assessment Pool — Week 11

**MCQ**

1. The Lakehouse architecture primarily combines:
   - a) MapReduce and Hive
   - b) **Data lake storage with data warehouse reliability (ACID, schema enforcement)**
   - c) Streaming and batch processing
   - d) Cloud storage with edge computing

2. Apache Iceberg and Delta Lake address which fundamental limitation of traditional data lakes?
   - a) Poor compression ratios
   - b) Lack of SQL support
   - c) **Absence of ACID transactions and schema enforcement**
   - d) Inability to store unstructured data

3. The "Data Mesh" concept was proposed to solve:
   - a) Storage cost problems in HDFS
   - b) Streaming latency issues
   - c) **Bottlenecks caused by centralized data teams owning all organizational data**
   - d) Security vulnerabilities in Hadoop

4. Federated Learning is primarily used for:
   - a) Distributed SQL queries across clusters
   - b) Real-time stream processing
   - c) **Training ML models on distributed data without sharing raw data (privacy-preserving)**
   - d) Graph analytics on social networks

**True / False**

| Statement | Answer |
|-----------|--------|
| Apache Beam allows the same code to run on both Spark and Flink backends. | **True** |
| Cloud-managed services like AWS EMR require you to manage Hadoop cluster hardware yourself. | **False** |
| Differential privacy guarantees that individual records cannot be identified from aggregate results. | **True** |
| The Data Mesh approach centralizes all data ownership in a single platform team. | **False** |

**Descriptive Questions**

1. Explain the Lakehouse architecture. What problems does it solve that neither a pure data lake nor a pure data warehouse solved individually?
2. What is federated learning? Give a healthcare example where it is preferable to centralizing all patient data.
3. Reflect on the full course: explain how HDFS → MapReduce → Hive → Spark forms a coherent technology stack for big data analytics.

**Capstone Analytical / Project Questions (CLO4)**

1. **System Design:** Design a complete big data analytics platform for a nationwide mobile payment company in Bangladesh handling 50 million transactions per day. Your design must include: (a) data ingestion layer, (b) storage architecture (HDFS or cloud), (c) batch analytics (for monthly reports), (d) real-time fraud detection (< 2-second latency), (e) visualization dashboard. Identify every tool from this course you would use and justify each choice.

2. **Critical Thinking:** A colleague claims: *"Hadoop is dead — we should just use Spark on cloud object storage and forget HDFS."* Write a 300-word critical evaluation: Under what conditions is this claim correct? Under what conditions would you still recommend HDFS? What does this evolution tell us about the lifecycle of big data technologies?

3. **Ethics:** A researcher uses 5 years of social media posts from 2 million Bangladeshi users (scraped without explicit consent) to train a mental health prediction model. The model achieves 90% accuracy in predicting depression. (a) What are the privacy and ethical concerns? (b) How could federated learning or differential privacy mitigate these concerns? (c) Should this model be deployed in a hospital setting? Justify your answer.

---

---

## Appendix A: Assessment Weightage (OBE Aligned)

| Assessment Component | Weight | CLOs Assessed |
|---------------------|--------|---------------|
| Written Tests/Quizzes (3×) | 20% | CLO1, CLO2 |
| Mid-Term Examination | 25% | CLO1, CLO2, CLO3 |
| Final Examination | 30% | CLO1, CLO2, CLO3, CLO4 |
| Lab Reports / Assignments | 10% | CLO3 |
| Final Project + Exhibition | 10% | CLO4 |
| Final Viva / Oral Exam | 5% | CLO4 |

---

## Appendix B: Recommended Online Courses (Free)

| Course | Platform | Alignment |
|--------|----------|-----------|
| Mining Massive Datasets | Stanford Online (YouTube) | Weeks 1, 4, 10 |
| Big Data Specialization | Coursera (UC San Diego) | Weeks 3–7 |
| Data Engineering with Google Cloud | Coursera (Google) | Weeks 5, 8, 11 |
| Apache Spark with Python | DataCamp | Week 6 |
| Visualization with D3.js | Observable / YouTube | Week 9 |

---

## Appendix C: Key Research Articles Chronologically

| Year | Paper | Relevance |
|------|-------|-----------|
| 2001 | Laney — 3Vs of Big Data | Week 1 |
| 2003 | Ghemawat et al. — GFS | Week 3 |
| 2004 | Dean & Ghemawat — MapReduce | Weeks 4, 6 |
| 2006 | Chang et al. — Bigtable | Week 4 |
| 2009 | Thusoo et al. — Hive | Week 7 |
| 2010 | Zaharia et al. — Spark | Week 6 |
| 2011 | Manyika et al. — McKinsey Big Data | Week 1 |
| 2011 | Kreps et al. — Kafka | Week 8 |
| 2013 | Vavilapalli et al. — YARN | Week 5 |
| 2015 | Akidau et al. — Dataflow Model | Week 11 |
| 2018 | Taylor & Letham — Prophet | Week 10 |
| 2020 | Armbrust et al. — Delta Lake | Week 11 |
| 2021 | Zaharia et al. — Lakehouse | Week 11 |

---

*Prepared for CSE 4345 — Big Data Analytics | Department of CSE, Premier University*
*Document version: 2026-06-13*
