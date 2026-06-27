# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository contains two parallel course-authoring projects for **CSE 4345 — Big Data Analytics** at the Department of CSE, Premier University:

1. **`lectures/`** — 22 standalone LaTeX Beamer slide decks (W01–W11, Part 1 & 2 each)
2. **`book/`** — A professional B5 LaTeX textbook *"Data Engineering: Distributed Systems, Scalable Processing, and Modern Architectures"*

**Instructor:** rufaruqui@cu.ac.bd (Rokan Uddin Faruqui, Professor, University of Chittagong)

## Compile Commands

**Lectures** (each `.tex` is standalone, compile from `lectures/`):
```
cd lectures && pdflatex W01_Part1.tex
```

**Book** (run from `book/`; biber required for bibliography):
```
cd book && pdflatex main.tex && biber main && pdflatex main.tex && pdflatex main.tex
```

**Clean LaTeX build artifacts:**
```
bash cleanup.sh
```

## Lectures

### File Naming
```
lectures/W01_Part1.tex        ← Week 1, Part 1 (Introduction + Core Content + Assessment)
lectures/W01_Part2.tex        ← Week 1, Part 2 (Seminal Research + Case Study)
lectures/W01_Notes.tex        ← Instructor notes (some weeks)
lectures/W02_Part1.tex        ...and so on through W11_Part2.tex
```

All 22 Part files (W01–W11, Part1 & Part2) are complete. Some weeks also have `_Notes.tex` files. Ignore `_backup` and `_advanced` variants.

### Beamer Design Spec

All lecture `.tex` files share the same design — do not deviate without user approval:
- `\documentclass[aspectratio=169,10pt]{beamer}` + `\usetheme{Madrid}`
- **PUNavy** RGB(10,36,99) as primary; **PUGold** RGB(197,151,37) as accent/alert
- Packages: `booktabs`, `tikz`, `xcolor`, `amsmath`, `enumerate`, `multicol`
- No navigation symbols; custom footline (author | short title | page/total)

### Per-Part Content Template

**Part 1** (Introduction · Core Content · Ivy League Alignment · Assessment · References):
Title → Course Info → ToC → Section: Introduction → Section: Core Content (textbook-sourced, TikZ diagrams, comparison tables) → Section: Ivy League Alignment → Section: Assessment (MCQ Set A, MCQ Set B, True/False, Descriptive, Analytical) → References → Closing slide

**Part 2** (Seminal Research · Case Study):
Title → Seminal Paper (citation block, key insight quote, 2–3 technical contribution slides, impact today) → Case Study (industry scenario, scale numbers, lessons learned, discussion questions) → References → Closing slide

Textbook short codes used throughout: `[TW]`, `[SA]`, `[TE]`, `[LRU]`, `[MMS]`. Always tag CLO on every assessment question.

## Book (`book/`)

### Structure
```
book/
  main.tex          ← master file (\input all chapters)
  preamble.tex      ← all packages, colors, tcolorbox envs, listing styles, macros
  ch01.tex … ch07.tex   (ch01–ch07 complete; ch08–ch11 pending)
  bibliography.bib  ← BibLaTeX/biber entries for all chapters
  BOOK_PLAN.md      ← chapter map, status tracker, research spotlight map
```

### Book Design Spec

| Element | Choice |
|---|---|
| Document class | `\documentclass[11pt,b5paper,twoside,openright]{book}` |
| Colors | DEBlue RGB(0,60,120) · DEAccent RGB(210,120,0) · DEGreen RGB(0,110,70) · DERed RGB(170,30,30) |
| Bibliography | `biblatex` author-year + `biber` |
| Code listings | `listings`: styles `pyspark`, `hiveql`, `pseudocode`, `shell` |

### tcolorbox Environments (defined in `preamble.tex`)

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

### Custom Macros (defined in `preamble.tex`)

- `\term{word}` — bold-italic + auto-indexed
- `\tool{name}` — sans-serif + auto-indexed
- `\code{text}` — monospace inline
- `\KB`, `\MB`, `\GB`, `\TB`, `\PB`, `\EB`, `\ZB` — data-size units

### Exercise Numbering

- `\sq` → **SQ**N.k (Short Question), `\ap` → **AP**N.k (Analytical Problem)
- `\dpr` → **DP**N.k (Design Problem), `\pe` → **PE**N.k (Programming Exercise)

### Chapter Status

| Ch | Title | Status |
|---|---|---|
| 1 | The Big Data Revolution: Scale, Velocity, and Variety | Done |
| 2 | Data Integration: Heterogeneity, Quality, and Provenance | Done |
| 3 | Distributed File Systems: GFS and HDFS | Done |
| 4 | The MapReduce Paradigm and the Hadoop Processing Stack | Done |
| 5 | Resource Management, File Formats, and I/O Optimization | Done |
| 6 | Apache Spark: In-Memory Distributed Computing | Done |
| 7 | SQL at Scale: HiveQL and the SQL-on-Hadoop Ecosystem | Done |
| 8–11 | Data Pipelines · Visualization · Domain Apps · Modern Stack | Pending |

## Course Specifics

- **Credits:** 3 | **Pre-requisite:** CSE 2221 (Database Management System)
- **CLOs:** CLO1 (understand big data characteristics), CLO2 (analyze challenges), CLO3 (explain techniques/tools), CLO4 (solve problems, build project)
- **Key textbooks:** Tom White *Hadoop: The Definitive Guide*; Acharya & Chellappan *Big Data and Analytics*; Erl et al. *Big Data Fundamentals*
- **Ivy League benchmark courses:** Stanford CS246, Harvard CS265, MIT 6.830, CMU 15-721

## Other Files

- `CSE4345_Lecture_Plan.md` — OBE-based 11-week master lecture plan (primary content reference)
- `exercises/fhir.py` — Python exercise script (FHIR healthcare data)
- `local/` — Gitignored: textbook PDFs and course outline images
