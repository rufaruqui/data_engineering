# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a course materials repository for **CSE 4345 — Big Data Analytics** at the Department of CSE, Premier University. It contains no executable code — all files are course documents (Markdown, images).

**Instructor:** rufaruqui@cu.ac.bd

## Contents

| File / Directory | Description |
|-----------------|-------------|
| `course_outline_page_1.jpeg` | Official course outline (page 1): CLOs, PLO mapping, course content table |
| `course_outline_page_2.jpeg` | Official course outline (page 2): textbooks, teaching-learning strategy   |
| `CSE4345_Lecture_Plan.md`    | OBE-based 11-week detailed lecture plan (master reference document)       |
| `lectures/`                  | LaTeX Beamer slide files — one `W<NN>_Part<P>.tex` per lecture             |

### Lecture File Naming
```
lectures/W01_Part1.tex   ← Week 1, Part 1 (Introduction + Core Content + Assessment)
lectures/W01_Part2.tex   ← Week 1, Part 2 (Seminal Research + Case Study)
lectures/W02_Part1.tex   ...and so on through W11_Part2.tex
```

Each week generates **two standalone Beamer files** (22 total). See memory file `project_lecture_structure.md` for the full generation tracker and per-part content templates.

## Course Specifics

- **Credits:** 3 | **Pre-requisite:** CSE 2221 (Database Management System)
- **CLOs:** CLO1 (understand big data characteristics), CLO2 (analyze challenges), CLO3 (explain techniques/tools), CLO4 (solve problems, build project)
- **Key textbooks:** Tom White *Hadoop: The Definitive Guide*; Acharya & Chellappan *Big Data and Analytics*; Erl et al. *Big Data Fundamentals*
- **Ivy League benchmark courses:** Stanford CS246, Harvard CS265, MIT 6.830, CMU 15-721

## Beamer Slide Design Spec

All `.tex` files share the same design language — do not deviate without user approval:
- `\documentclass[aspectratio=169,10pt]{beamer}` + `\usetheme{Madrid}`
- **PUNavy** RGB(10,36,99) as primary; **PUGold** RGB(197,151,37) as accent/alert
- Packages: `booktabs`, `tikz`, `xcolor`, `amsmath`, `enumerate`, `multicol`
- No navigation symbols; custom footline (author | short title | page/total)

## Lecture Slide Per-Part Content Template

**Part 1** (Introduction · Core Content · Ivy League Alignment · Assessment · References):
Title → Course Info → ToC → Section: Introduction → Section: Core Content (textbook-sourced, TikZ diagrams, comparison tables) → Section: Ivy League Alignment → Section: Assessment (MCQ Set A, MCQ Set B, True/False, Descriptive, Analytical) → References → Closing slide

**Part 2** (Seminal Research · Case Study):
Title → Seminal Paper (citation block, key insight quote, 2–3 technical contribution slides, impact today) → Case Study (industry scenario, scale numbers, lessons learned, discussion questions) → References → Closing slide

Textbook short codes used throughout: `[TW]`, `[SA]`, `[TE]`, `[LRU]`, `[MMS]`. Always tag CLO on every assessment question.
