# Plan — Cambridge International AS Level Computer Science 9618

The brief an authoring agent works to. Generated 29 September 2026 from `work/cie-9618-as-2026/curriculum/` and the topic work orders; regenerate rather than edit. The analysis it rests on is `operations/analysis/9618-as-computer-science-corpus-analysis.md`.

## 0. What the syllabus says

Transcribed from the syllabus, every value with its page (`curriculum/syllabus-facts.json`).

| AO | definition | weight | Paper 1 | Paper 2 |
|---|---|---:|---:|---:|
| AO1 | Demonstrate knowledge and understanding of the principles and concepts of computer science, including abstract | 30% | 60% | 0% |
| AO2 | Apply knowledge and understanding of the principles and concepts of computer science, including to analyse pro | 40% | 40% | 40% |
| AO3 | Design, program and evaluate computer systems to solve problems, making reasoned judgements about these. | 30% | 0% | 60% |

- **Paper 1, Theory Fundamentals.** 75 marks, 90 minutes, 50% of the qualification. Assesses syllabus sections 1 to 8. Short and longer answers testing knowledge and understanding of the principles of computer science and their application to solving problems.
- **Paper 2, Fundamental Problem-solving and Programming Skills.** 75 marks, 120 minutes, 50% of the qualification. Assesses syllabus sections 9 to 12. Tests programming knowledge and skills. Candidates are not required to write programming code; an insert of pseudocode built-in functions and operators is provided.

The command-word table on page 41 lists 27 words for AS and A Level together. Paper 2 is answered in pseudocode, never programming code, with an insert of built-in functions and operators (page 40). The syllabus numbers its AOs without naming them; the plan calls them knowledge (AO1), application (AO2) and design and programming (AO3).

## 1. What the corpus says

60 AS papers, 60 mark schemes and 60 examiner-report sections, June 2021 to November 2025; 1,534 parts, 4,497 marks. The whole corpus is under the current syllabus.

- **Two papers, two kinds of topic.** Paper 1 (sections 1-8) is knowledge applied to a scenario that runs through the whole question: most parts are 1-4 marks, Describe, Explain and Complete carry half the marks. Paper 2 (sections 9-12) is design and programming: Write and Complete carry 62% of its marks, and 21% of its parts are 5-8 marks.
- **Point-marked, with development.** A 2-mark Describe or Explain is usually two points from a longer list; at 3-4 marks the scheme often marks the development of a point separately. State, Identify and Convert at 1 mark want the bare item.
- **Algorithms are marked element by element**: the loop and its bounds, the value returned, the selection inside the loop, the heading and ending with parameters, declarations. A structurally complete answer scores even where one step of its logic is wrong.
- **The failures that recur in every series:** answers not applied to the scenario; imprecise terms (memory for storage, package for packet); OUTPUT where RETURN is required; missing end statements; file-handling detail; + for & and misused string functions; the wrong loop for the problem.
- **86 examiner-evidenced misconceptions**, curated by hand from 1,865 error statements, each with a test that separates the two ideas.

## 2. Command words and tariffs

Use only these to open a prompt. The tariff is the one the work-order slot names; every slot tariff is one the papers set for that word.

| command word | in the syllabus table | parts | modal tariff | tariffs seen |
|---|---|---:|---:|---|
| Complete | yes | 242 | 4 | 1, 2, 3, 4, 5, 6, 7, 8 |
| Write | yes | 235 | 7 | 1, 2, 3, 4, 5, 6, 7, 8 |
| Describe | yes | 218 | 2 | 1, 2, 3, 4, 5, 6, 7 |
| Explain | yes | 185 | 2 | 1, 2, 3, 4, 5 |
| Identify | yes | 163 | 2 | 1, 2, 3, 4, 6 |
| State | yes | 136 | 1 | 1, 2, 3, 4 |
| Give | yes | 78 | 2 | 1, 2, 3, 6 |
| Draw | yes | 49 | 2 | 1, 2, 3, 4, 5, 6 |
| Convert | no (observed) | 37 | 1 | 1, 2, 3 |
| Show | no (observed) | 23 | 1 | 1, 2, 3 |
| Calculate | yes | 10 | 2 | 2, 3 |
| Suggest | yes | 10 | 2 | 1, 2 |
| Add | no (observed) | 9 | 4 | 1, 2, 3, 4, 6 |
| Outline | yes | 7 | 2 | 2, 3, 5 |
| Define | yes | 6 | 2 | 1, 2, 6 |
| Perform | no (observed) | 5 | 2 | 1, 2 |
| Trace | no (observed) | 5 | 3 | 3, 4, 5 |

**Never open a prompt with:** Analyse, Assess, Comment, Compare, Consider, Contrast, Demonstrate, Develop, Discuss, Evaluate, Examine, Justify, Predict, Sketch, Summarise, Tick. The table lists them for A Level too; none opens an AS question in 2021-2025. Justification is asked with "Explain why" or "Describe the reasons why". Tick is a response format for a printed grid, and Evaluate, Comment, Consider and Examine open fewer than five AS parts in five years.

- **Definitions** open with "State what is meant by" (1-2 marks) or "Describe what is meant by" (2); "Define" is rare.
- **Write has two forms.** A flashcard models the short form: a statement, a query, a shift instruction, a record definition, 3-4 marks. A worked example models the 6-8 mark module.
- **Convert and Show** open conversions and results on Paper 1; **Perform** opens binary arithmetic.

## 3. Answer shapes

From the mark schemes’ award rules (`curriculum/answer-shapes.json`). Write each answer to the shape its tariff carries.

| command, marks | how it is marked |
|---|---|
| State 1, Identify 1, Convert 1, Show 1 | one correct element; nothing else earns credit |
| Describe 2, Explain 2, Identify 2, Give 2 | two creditable points from a longer list; a repeated point earns nothing |
| Describe 3-4, Explain 3-4 | points from a longer list, and a point earns its second mark only when it is developed ("... so the file takes less time to transmit") |
| Complete 2-5 | one mark per correct gap, row or statement |
| Write 3-4 (flashcard) | one mark per correct statement or clause |
| Write 6-8 (worked example) | numbered mark points, one per element: heading and ending with parameters and return type, declarations and initialisation, the loop and its condition, the selection, the operation inside the loop, the value returned or output |

## 4. Card types, assessment objectives and Bloom levels

Each slot declares its subtype, its AOs (narrowed from the permitted set below by objective type and paper) and its Bloom level.

| subtype | tests | permitted AOs | Bloom level |
|---|---|---|---|
| DEF | Precise meaning of one term | AO1, AO2 | Remember |
| FEATURE | Features or characteristics | AO1, AO2 | Remember |
| DIST | The difference between two confusable ideas | AO1, AO2 | Understand |
| PROC | An ordered sequence: the stages of a process, or an algorithm written as pseudocode statements | AO1, AO2, AO3 | Apply |
| WHY | Purpose or need | AO1, AO2 | Understand |
| MECH | How something works | AO1, AO2 | Understand |
| BEN | A benefit, taken to its consequence | AO1, AO2 | Understand |
| LIM | A drawback, taken to its consequence | AO1, AO2 | Understand |
| APP | Knowledge applied to the scenario given, or code written for it | AO2, AO3 | Apply |
| CHAIN | A change traced to its effect (for example sampling rate to file size to transmission time) | AO2 | Analyse |
| EVAL | A justified choice between options for a stated situation | AO2, AO3 | Evaluate |
| CALC | A conversion or calculation with working | AO2 | Apply |
| INTERP | Reading given code, a circuit, a table or a trace: what it does or outputs | AO2, AO3 | Analyse |
| MISCON | Telling a concept from the one it is confused with | AO1, AO2 | Understand |
| SYNTH | Joining two objectives into one design | AO2, AO3 | Create |

Performance tasks: data_response = Analyse; short_answer = Apply; worked_example = Create.

## 5. The topics

| topic | title | paper | objectives | items | notes words |
|---|---|---|---:|---:|---|
| 1.1 | Data Representation | 1 | 5 | 36 | 1,540–2,200 |
| 1.2 | Multimedia | 1 | 7 | 50 | 2,200–3,140 |
| 1.3 | Compression | 1 | 3 | 20 | 860–1,230 |
| 2.1 | Networks including the internet | 1 | 15 | 53 | 4,260–6,110 |
| 3.1 | Computers and their components | 1 | 8 | 31 | 2,360–3,380 |
| 3.2 | Logic Gates and Logic Circuits | 1 | 6 | 35 | 1,580–2,260 |
| 4.1 | Central Processing Unit (CPU) Architecture | 1 | 8 | 32 | 2,460–3,520 |
| 4.2 | Assembly Language | 1 | 5 | 29 | 1,460–2,090 |
| 4.3 | Bit manipulation | 1 | 2 | 18 | 630–900 |
| 5.1 | Operating Systems | 1 | 4 | 17 | 1,220–1,740 |
| 5.2 | Language Translators | 1 | 4 | 25 | 1,140–1,640 |
| 6.1 | Data Security | 1 | 6 | 23 | 1,680–2,410 |
| 6.2 | Data Integrity | 1 | 3 | 14 | 930–1,330 |
| 7.1 | Ethics and Ownership | 1 | 5 | 29 | 1,460–2,090 |
| 8.1 | Database Concepts | 1 | 7 | 42 | 1,980–2,830 |
| 8.2 | Database Management Systems (DBMS) | 1 | 2 | 10 | 630–900 |
| 8.3 | Data Definition Language (DDL) and Data Manipulation Language (DML) | 1 | 5 | 34 | 1,370–1,960 |
| 9.1 | Computational Thinking Skills | 2 | 2 | 12 | 660–940 |
| 9.2 | Algorithms | 2 | 9 | 39 | 2,510–3,600 |
| 10.1 | Data Types and Records | 2 | 2 | 13 | 660–940 |
| 10.2 | Arrays | 2 | 4 | 22 | 1,160–1,660 |
| 10.3 | Files | 2 | 2 | 14 | 560–800 |
| 10.4 | Introduction to Abstract Data Types (ADT) | 2 | 4 | 20 | 1,150–1,650 |
| 11.1 | Programming Basics | 2 | 3 | 21 | 910–1,300 |
| 11.2 | Constructs | 2 | 2 | 14 | 560–800 |
| 11.3 | Structured Programming | 2 | 7 | 32 | 1,970–2,820 |
| 12.1 | Program Development Life cycle | 2 | 4 | 20 | 1,100–1,580 |
| 12.2 | Program Design | 2 | 2 | 12 | 630–900 |
| 12.3 | Program Testing and Maintenance | 2 | 8 | 34 | 2,330–3,330 |

**29 topics, 751 items, 41,960–60,050 words of notes.**

## 6. AO balance, in marks

| AO | planned | syllabus weight | gap |
|---|---:|---:|---:|
| AO1 | 30% | 30% | +0 |
| AO2 | 44% | 40% | +4 |
| AO3 | 26% | 30% | -4 |

Sections 1-8 are examined only on Paper 1, which assesses no AO3; sections 9-12 only on Paper 2, which assesses no AO1 (syllabus page 13). So each topic is balanced against its own paper’s split, a recall card on a Paper 2 topic is credited as application, and a scenario or design card on Paper 2 as AO3. The subject total answers to 30/40/30. Paper 2 topics carry more practice per objective (two pseudocode cards per programming objective, three worked modules per topic) because the papers weigh equally and Paper 2 has fewer objectives.

## 7. Misconceptions, glossary and scope

- **86 examiner-evidenced misconceptions** in `curriculum/misconceptions.json`, each on its objective with a `test`. Every entry has its own MISCON slot in the work order (`misconception_entry`).
- **55 glossary terms** in `curriculum/glossary.json`, each with its settled sense.
- **15 scope patterns** in `curriculum/scope-scan.json`, carried by every contract as `excluded_constructs`; C-11 fails any learner-facing match:
  - memorising particular character codes (syllabus, page 14, topic 1.1)
  - a logic gate with more than two inputs (syllabus, page 18, topic 3.2)
  - more than one general purpose register (syllabus, pages 21-22, topics 4.2 and 4.3)
  - writing pseudocode to implement a stack, queue or linked list (syllabus, page 29, topic 10.4)
  - program code in a programming language on Paper 2 (syllabus, page 40, Paper 2)
  - floating-point representation (A Level 13.3) (syllabus, page 32, A Level content)
  - file organisation and access methods (A Level 13.2) (syllabus, page 32, A Level content)
  - user-defined types beyond records (A Level 13.1) (syllabus, page 32, A Level content)
  - protocols and switching (A Level 14) (syllabus, page 33, A Level content)
  - processor design, parallel processing and virtual machines (A Level 15.1) (syllabus, page 33, A Level content)
  - Boolean algebra, De Morgan and Karnaugh maps (A Level 15.2) (syllabus, page 33, A Level content)
  - encryption protocols and digital certificates (A Level 17) (syllabus, page 34, A Level content)
  - graph and machine-learning algorithms (A Level 18) (syllabus, page 35, A Level content)
  - algorithms and recursion beyond AS (A Level 19) (syllabus, page 35, A Level content)
  - programming paradigms and exception handling (A Level 20) (syllabus, page 36, A Level content)

## 8. Rules particular to this subject

- **Cambridge pseudocode only**, as the Paper 2 insert defines it: keywords in capitals, the assignment arrow ←, & to join strings, the insert’s functions only. Never Python, Java or Visual Basic: C-11 scans for their syntax.
- **Code in a labelled fence.** Code shown in a prompt or a note goes in a fence labelled ```pseudocode (or ```sql). This subject has no chart renderer, so any other fence fails C-41: truth tables, trace tables and data go in markdown tables; circuits are written as logic expressions or gate-by-gate tables; flowcharts and structure charts are described box by box.
- **Every model algorithm is complete and closed**: heading and ending, declarations, initialisation, every end statement. A function RETURNs; a module takes its values as parameters, never by INPUT inside it.
- **Binary is written in groups of four bits**, working is shown, and the result is in the width the question asks for. C-32 checks binary sums in base 2, and a fixed-width result modulo its width.
- **Every scenario card answers for its scenario.** Where natural, the stem gives one example and asks for others.
- **No brand names** for hardware or software.
