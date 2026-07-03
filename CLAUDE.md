# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository contains two parallel course-authoring projects for **CSE 4345 — Big Data Analytics** at the Department of CSE, University of Chittagong:

1. **`lectures/`** — 22 standalone LaTeX Beamer slide decks (W01–W11, Part 1 & Part 2 each)
2. **`book/`** — A professional B5 LaTeX textbook *"Data Engineering: Distributed Systems, Scalable Processing, and Modern Architectures"*

**Instructor:** rufaruqui@cu.ac.bd (Rokan Uddin Faruqui, Professor, University of Chittagong)

---

## Compile Commands

**Book** (run from `book/`; requires `biber` on PATH — install via `brew install biber` if missing):
```
cd book
pdflatex main.tex && biber main && pdflatex main.tex && pdflatex main.tex
```

**Cover** (standalone; compile before or independently of main):
```
cd book && pdflatex cover.tex
```
`cover.pdf` is included by `main.tex` via `\includepdf`. Always recompile `cover.tex` first if the cover changes.

**Lectures** (each `.tex` is standalone):
```
cd lectures && pdflatex W01_Part1.tex
```

**Clean build artifacts:**
```
bash cleanup.sh
```

---

## Book — Complete Status

All 11 chapters are written and the book compiles to **~450 pages**. `main.pdf` and `cover.pdf` are committed outputs.

| Ch | Title | Status |
|---|---|---|
| 1 | The Big Data Revolution: Scale, Velocity, and Variety | Done |
| 2 | Data Integration: Heterogeneity, Quality, and Provenance | Done |
| 3 | Distributed File Systems: GFS and HDFS | Done |
| 4 | The MapReduce Paradigm and the Hadoop Processing Stack | Done |
| 5 | Resource Management, File Formats, and I/O Optimization | Done |
| 6 | Apache Spark: In-Memory Distributed Computing | Done |
| 7 | SQL at Scale: HiveQL and the SQL-on-Hadoop Ecosystem | Done |
| 8 | Data Pipelines, Data Lakes, and Real-Time Integration | Done |
| 9 | Data Visualization at Scale | Done |
| 10 | Domain Applications: Social Networks, Time Series, and Healthcare | Done |
| 11 | The Lakehouse, MLOps, and Emerging Architectures | Done |

### Book File Roles

- `main.tex` — master file; `\input`s all chapters and `cover.pdf` via `\includepdf`
- `preamble.tex` — all packages, color definitions, tcolorbox environments, listing styles, exercise macros
- `cover.tex` — standalone TikZ cover; must be compiled separately to produce `cover.pdf`
- `bibliography.bib` — BibLaTeX/biber entries for all 11 chapters; add new entries here
- `BOOK_PLAN.md` — chapter map, status tracker, research spotlight map

---

## Book Design Spec

### Colors (`preamble.tex`)
```
DEBlue   RGB(0,60,120)    — primary headings, frames, defbox borders
DEAccent RGB(210,120,0)   — alerts, accent rules, keyinsight boxes
DEGreen  RGB(0,110,70)    — systemdesign boxes, code comment color
DERed    RGB(170,30,30)   — caution boxes
DEGray   RGB(80,80,80)    — techdebt boxes, secondary text
DEPurple RGB(80,0,120)    — casestudy boxes
```
Light tints (`DELightBlue`, `DELightAccent`, etc.) are defined for box backgrounds.

### tcolorbox Environments

| Environment | Color | Purpose |
|---|---|---|
| `researchspotlight` | DEBlue | Seminal paper summary (one per chapter) |
| `keyinsight` | DEAccent | Critical conceptual highlight |
| `systemdesign` | DEGreen | Architecture note + diagram context |
| `caution` | DERed | Common misconception |
| `techdebt` | DEGray | Industry/production lesson |
| `defbox` | white + DEBlue border | Formal definition |
| `casestudy` | DEPurple | End-of-section industry case |
| `chapterlearning` | DEBlue fill | 10 learning objectives at chapter start |

### Code Listing Styles (all defined in `preamble.tex`)
- `pyspark` — Python/PySpark (blue keywords, green comments, red strings)
- `hiveql` — SQL/HiveQL (amber background)
- `pseudocode` — Gray background, no language highlighting
- `shell` — White-on-dark terminal output

**Critical:** Em dashes (`—`) and non-ASCII characters (Greek letters, arrows) inside `lstlisting` environments cause `Invalid UTF-8 byte` errors. Use ASCII equivalents inside code blocks: `--` for em dash, `epsilon`/`alpha` for Greek letters, `->` for arrows.

### Custom Macros
- `\term{word}` — bold-italic + auto-indexed
- `\tool{name}` — sans-serif + auto-indexed
- `\code{text}` — monospace inline
- `\KB`, `\MB`, `\GB`, `\TB`, `\PB`, `\EB`, `\ZB` — data-size units

### Exercise Macros (use `\exercisesection{}` as section heading, never `\subsection*`)
- `\sq` → **SQ**N.k (Short Question)
- `\ap` → **AP**N.k (Analytical Problem)
- `\dpr` → **DP**N.k (Design Problem)
- `\pe` → **PE**N.k (Programming Exercise)

Sub-questions within exercises use `\begin{enumerate}[label=(\alph*)]` — **not** `[(a)]` (incompatible with `enumitem`).

---

## Known LaTeX Pitfalls (fix before compiling)

These issues were encountered and fixed during development — avoid reintroducing them:

1. **`cm` as a TikZ style name is reserved** — `cm` is a PGF transformation key requiring a value. If a TikZ diagram defines a custom style named `cm`, rename it (e.g., `cmanager`).

2. **`\\` in TikZ nodes requires `align=`** — Any `\node[...]` that uses `\\` for a line break must have `align=center` (or `align=left`) in its style, or the style it inherits must include it. Bare `\node[font=...]` without `align` will fail with `Not allowed in LR mode`.

3. **`\Bbbk` conflict** — `newpxmath` defines `\Bbbk`; `amssymb` redefines it. In `preamble.tex` the fix is `\let\Bbbk\relax` placed **before** `\usepackage{amssymb}`, and `\let\openbox\relax` placed before `\usepackage{amsthm}`.

4. **`microtype` font expansion** — The installed font set is not fully scalable. `preamble.tex` uses `\usepackage[expansion=false]{microtype}`. Do not remove the `expansion=false` option.

5. **`tcolorbox` version** — The user's TeX Live 2025 basic install requires tcolorbox ≤ v5.x. Version 6+ introduced LaTeX tagging APIs not present in TL2025 basic. The installed version is v5.0.2 at `~/Library/texmf/tex/latex/tcolorbox/`.

6. **`shadows.blur` TikZ library** — Not included in the TL2025 basic install. It has been removed from `preamble.tex`. Do not add it back.

---

## Locally Installed Packages (non-system)

The TeX Live 2025 basic install is minimal. The following packages are installed in `~/Library/texmf/` (user texmf tree) and are available without system-level changes:

`inconsolata`, `tcolorbox` (v5.0.2), `environ`, `trimspaces`, `varwidth`, `listingsutf8`, `emptypage`, `csquotes`, `enumitem`, `titlesec`, `nextpage`, `imakeidx`, `pdfpages`, `newpx` (full, with font metrics), `newtx` (enc + vf files), `txfonts` (for `txsya`/`txsyb` math symbols), `pgfplots`, `biblatex`, `epigraph`, `boondox`, `xstring`, `fontaxes`.

If a new package is needed and `tlmgr` fails (TL2025 vs 2026 repo mismatch), download the `.tar.xz` from the TL2021 historic archive at `https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2021/tlnet-final/archive/` and extract into `~/Library/texmf/`.

---

## Lectures

### Design Spec (do not deviate without approval)
- `\documentclass[aspectratio=169,10pt]{beamer}` + `\usetheme{Madrid}`
- **PUNavy** RGB(10,36,99) primary; **PUGold** RGB(197,151,37) accent/alert — distinct from book colors
- Packages: `booktabs`, `tikz`, `xcolor`, `amsmath`, `enumerate`, `multicol`
- No navigation symbols; custom footline: author | short title | page/total

### Per-Part Content Template

**Part 1** — Title → Course Info → ToC → Introduction → Core Content (TikZ diagrams, comparison tables, textbook-sourced) → Ivy League Alignment → Assessment (MCQ Set A, MCQ Set B, True/False, Descriptive, Analytical) → References → Closing

**Part 2** — Title → Research Article (citation block, key insight quote, 2–3 contribution slides, impact today) → Case Study (industry scenario, scale numbers, lessons learned, discussion questions) → References → Closing

Tag every assessment question with its CLO. Textbook short codes used throughout: `[TW]`, `[SA]`, `[TE]`, `[LRU]`, `[MMS]`.

---

## Content Policy: International Audience

The book targets an international audience. Case studies and examples in ch01–ch07 have been updated accordingly. **Ch08–ch11 still contain Bangladesh-specific scenarios (bKash, Pathao, DGHS, Dhaka coordinates) that are pending revision.** When editing these chapters:
- Replace `bKash` → M-Pesa / PayPal / MobilePay and scale figures
- Replace `Pathao` → Uber / Grab
- Replace `DGHS` / Bangladesh hospitals → CDC / NHS / generic regional hospital network
- Replace Dhaka GPS coordinates (90.41, 23.81) → New York (−74.0, 40.7) or London (−0.12, 51.5)
- Replace `amount_bdt` / `BDT` → `amount_usd` / `USD`
- Replace Bangladesh Bank / PDPA references → GDPR / HIPAA / EU PSD2 / Basel III
- Replace `district` (64 Bangladesh districts) → `region` or `state`

---

## Course Specifics

- **Credits:** 3 | **Pre-requisite:** CSE 2221 (Database Management System)
- **CLOs:** CLO1 (big data characteristics), CLO2 (analyze challenges), CLO3 (explain techniques/tools), CLO4 (solve problems, build project)
- **Key textbooks:** Tom White *Hadoop: The Definitive Guide*; Acharya & Chellappan *Big Data and Analytics*; Erl et al. *Big Data Fundamentals*
- **Ivy League benchmark courses:** Stanford CS246, Harvard CS265, MIT 6.830, CMU 15-721
- `CSE4345_Lecture_Plan.md` — OBE-based 11-week master lecture plan (primary content reference for writing new material)
- `local/` — Gitignored: textbook PDFs and course outline images
