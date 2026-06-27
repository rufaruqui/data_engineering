# Data Engineering: Distributed Systems, Scalable Processing, and Modern Architectures

**Subtitle:** From Foundations to Production  
**Author:** Rokan Uddin Faruqui  
**Audience:** Senior undergraduates, graduate students, and early-career practitioners  
**Format:** Professional B5 textbook, ~450–550 pages, pdfLaTeX

---

## File Structure

```
book/
  main.tex            ← master file (\input all chapters)
  preamble.tex        ← shared packages, colors, tcolorbox defs, listings styles
  ch01.tex  … ch11.tex
  appendix.tex
  bibliography.bib    ← ALL paper entries (all chapters), BibLaTeX/biber format
  BOOK_PLAN.md        ← this file
```

Compile with:
```
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

---

## LaTeX Design Decisions

| Element | Choice |
|---|---|
| Document class | `\documentclass[11pt,b5paper,twoside,openright]{book}` |
| Text font | `newpxtext` (Palatino clone, pdfLaTeX) |
| Math font | `newpxmath` |
| Mono font | `inconsolata` |
| Typography | `microtype` |
| Page layout | `geometry`: top 2.5 cm, bottom 2.8 cm, inner 2.8 cm, outer 2.2 cm |
| Colors | DEBlue RGB(0,60,120) · DEAccent RGB(210,120,0) · DEGreen RGB(0,110,70) · DERed RGB(170,30,30) |
| Chapter heads | `titlesec`: large gray chapter number + colored rule |
| Headers | `fancyhdr`: part/chapter name, folio outside |
| Bibliography | `biblatex` author-year + `biber` |
| Code | `listings`: styles `pyspark`, `hiveql`, `pseudocode`, `shell` |
| Boxes | `tcolorbox` — 8 environments (see below) |
| Cross-refs | `hyperref` + `cleveref` |

### tcolorbox Environments

| Environment | Color | Purpose |
|---|---|---|
| `researchspotlight` | DEBlue | Seminal paper summary |
| `keyinsight` | DEAccent | Critical conceptual highlight |
| `systemdesign` | DEGreen | Architecture note + diagram context |
| `caution` | DERed | Common misconception |
| `techdebt` | DEGray | Industry/production lesson |
| `defbox` | white + DEBlue border | Formal definition |
| `casestudy` | DEPurple | End-of-section industry case |
| `chapterlearning` | DEBlue fill | Learning objectives at chapter start |

### Exercise Numbering Scheme

- **SQ** N.k — Short Question (chapter N, item k)
- **AP** N.k — Analytical Problem
- **DP** N.k — Design Problem
- **PE** N.k — Programming Exercise

---

## Part and Chapter Map

### Part I — The Data Engineering Landscape
| Ch | Title | Source weeks | Status |
|---|---|---|---|
| 1 | The Big Data Revolution: Scale, Velocity, and Variety | W01 | **DONE** |
| 2 | Data Integration: Heterogeneity, Quality, and Provenance | W02 | pending |

### Part II — Distributed Storage
| Ch | Title | Source weeks | Status |
|---|---|---|---|
| 3 | Distributed File Systems: GFS and HDFS | W03 | pending |

### Part III — Batch Processing at Scale
| Ch | Title | Source weeks | Status |
|---|---|---|---|
| 4 | The MapReduce Paradigm and the Hadoop Processing Stack | W04 | pending |
| 5 | Resource Management, File Formats, and I/O Optimization | W05 | pending |

### Part IV — In-Memory Processing
| Ch | Title | Source weeks | Status |
|---|---|---|---|
| 6 | Apache Spark: In-Memory Distributed Computing | W06 | pending |
| 7 | SQL at Scale: HiveQL and the SQL-on-Hadoop Ecosystem | W07 | pending |

### Part V — Data Pipelines and Modern Integration
| Ch | Title | Source weeks | Status |
|---|---|---|---|
| 8 | Data Pipelines, Data Lakes, and Real-Time Integration | W08 | pending |

### Part VI — Insight Delivery
| Ch | Title | Source weeks | Status |
|---|---|---|---|
| 9 | Data Visualization at Scale | W09 | pending |
| 10 | Domain Applications: Social Networks, Time Series, and Healthcare | W10 | pending |

### Part VII — The Modern Data Stack
| Ch | Title | Source weeks | Status |
|---|---|---|---|
| 11 | The Lakehouse, MLOps, and Emerging Architectures | W11 | pending |

---

## Research Spotlights Map (all chapters)

| Paper | Chapter |
|---|---|
| Laney (2001) — 3Vs of Big Data | 1 |
| Brewer (2000) — CAP Theorem | 1 |
| Gilbert & Lynch (2002) — CAP formal proof | 1 |
| McKinsey Global Institute (2011) — Big Data frontier | 1 |
| Halevy, Rajaraman & Ordille (2006 VLDB) — Data Integration | 2 |
| Ghemawat, Gobioff & Leung (2003 SOSP) — GFS | 3 |
| Dean & Ghemawat (2004 OSDI) — MapReduce | 4 |
| Chang et al. (2006 OSDI) — Bigtable | 4 |
| Thusoo et al. (2009 VLDB) — Hive | 4, 7 |
| Vavilapalli et al. (2013 SoCC) — YARN | 5 |
| Zaharia et al. (2010 HotCloud) — Spark | 6 |
| Zaharia et al. (2012 NSDI) — RDDs | 6 |
| Venkataraman et al. (2019 ICDE) — Presto | 7 |
| Kreps, Narkhede & Rao (2011) — Kafka | 8 |
| Tufte (1983) — Visual Display | 9 |
| Shneiderman (1996 IEEE VL) — Visualization mantra | 9 |
| Bostock, Ogievetsky & Heer (2011 IEEE TVCG) — D3 | 9 |
| Kwak et al. (2010 WWW) — Twitter as news medium | 10 |
| Taylor & Letham (2018) — Prophet | 10 |
| Obermeyer & Emanuel (2016 NEJM) — ML in clinical medicine | 10 |
| Armbrust et al. (2020 VLDB) — Delta Lake | 11 |
| Zaharia et al. (2021 CIDR) — Lakehouse | 11 |
| Akidau et al. (2015 VLDB) — Dataflow model | 11 |
| Sculley et al. (2015 NeurIPS) — Hidden Technical Debt in ML | 11 |
