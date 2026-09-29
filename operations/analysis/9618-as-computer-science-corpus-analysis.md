# Corpus analysis — Cambridge International AS Level Computer Science 9618

What the syllabus and the AS assessment corpus say about this subject: what the skills are, and what a learner has to do to succeed on each paper. Step one of the pipeline, written after the syllabus (step zero) and before any plan. 29 September 2026. First exam for this cohort: 9 October 2026 (Paper 1).

## 0. The syllabus, first

Transcribed from the 9618 syllabus for 2026 into `curriculum/syllabus-facts.json`, every value carrying its page. The AS route is Papers 1 and 2, sections 1 to 12 of the subject content.

| AO | definition (page 13) | AS weight | Paper 1 | Paper 2 |
|---|---|---:|---:|---:|
| AO1 | Demonstrate knowledge and understanding of the principles and concepts of computer science | 30% | 60% | 0% |
| AO2 | Apply knowledge and understanding of the principles and concepts of computer science | 40% | 40% | 40% |
| AO3 | Design, program and evaluate computer systems to solve problems, making reasoned judgements | 30% | 0% | 60% |

The syllabus numbers and defines its objectives but does not name them. The names used in the plan (knowledge, application, design and programming) are our labels for the definitions.

- **Paper 1, Theory Fundamentals.** 75 marks, 90 minutes, 50%. Sections 1 to 8. No AO3.
- **Paper 2, Fundamental Problem-solving and Programming Skills.** 75 marks, 120 minutes, 50%. Sections 9 to 12. No AO1. Candidates are not required to write programming code: answers are in pseudocode, with an insert of built-in functions and operators (page 40).
- **Command words, page 41:** 27 words, for AS and A Level together.

## 1. The corpus

| source | held | used |
|---|---:|---|
| Question papers, AS (11, 12, 13, 21, 22, 23) | 60 | every series June 2021 to November 2025 |
| Mark schemes | 60 | the same papers |
| Principal Examiner Reports | 10 | AS sections only (60 paper sections); A Level sections removed first |

9618 was first examined in 2021, so the whole corpus sits under the current syllabus. There is no regime break to correct for.

- **1,534 question parts carrying 4,497 marks.** The part list and the tariffs are read from the mark schemes, which are more reliable than the papers: 58 of 60 papers sum to exactly 75, and the other two are within 2 marks.
- **The command word** is read from the matching question-paper part, found for 1,472 parts (96%).
- **6,816 examiner-report sentences,** of which 5,364 are located to the question part they discuss. 1,865 of them state an error.

## 2. The two papers are different subjects

| | Paper 1 | Paper 2 |
|---|---|---|
| parts | 891 | 642 |
| marks per part | mostly 1-4 (95%) | 1-8; 21% of parts are 5-8 marks |
| largest share of marks | Describe 19%, Explain 16%, Complete 16% | Write 39%, Complete 23% |
| what earns marks | a correct, developed point about the scenario in the stem | a correct, complete pseudocode or design element |

**Paper 1 is knowledge applied to a scenario.** A question usually opens with a context: a video doorbell, a school network, a database of horse riders. The context then holds for every part of the question. Most marks come from Describe, Explain and Complete at 2 to 4 marks, one mark per creditable point.

**Paper 2 is design and programming on paper.** Write and Complete carry 62% of its marks. A Paper 2 question gives a scenario and the modules that serve it, then asks the candidate to:

- write or complete pseudocode for a module;
- trace code or complete a trace table;
- draw a flowchart or structure chart;
- choose test data;
- explain a design choice.

## 3. Command words: what the papers actually use

| command word | parts | modal tariff | tariffs seen | Paper 1 / Paper 2 |
|---|---:|---:|---|---|
| Complete | 242 | 4 | 1-8 | 120 / 122 |
| Write | 235 | 7 | 1-8, bimodal: 1-4 for a statement, query or instruction, 6-8 for a module | 73 / 162 |
| Describe | 218 | 2 | 1-7 | 152 / 66 |
| Explain | 185 | 2 | 1-5 | 129 / 56 |
| Identify | 163 | 2 | 1-6 | 91 / 72 |
| State | 136 | 1 | 1-4 | 67 / 69 |
| Give | 78 | 2 | 1-6 | 44 / 34 |
| Draw | 49 | 2 | 1-6 | 36 / 13 |
| Convert\* | 37 | 1 | 1-3 | 37 / 0 |
| Tick\* | 24 | 2 | 1-6 | 21 / 3 |
| Show\* | 23 | 1 | 1-3 | 23 / 0 |
| Calculate | 10 | 2 | 2-3 | 10 / 0 |
| Suggest | 10 | 2 | 1-2 | 0 / 10 |
| Add\*, Outline, Define, Perform\*, Trace\* | 5-9 each | 2-4 | | |

\* observed in the papers, not in the syllabus table.

- **Listed but never used on an AS paper, 2021-2025:** Analyse, Assess, Compare, Contrast, Demonstrate, Develop, Discuss, Justify, Predict, Sketch, Summarise. The table serves A Level too.
- **Justification is still examined.** "Justify the use of a bitmap or a vector graphic for a given task" is a syllabus outcome. It is asked as "Explain the reasons why …" (23 parts) or "Describe the reasons why …" (5), never with Justify.
- **How definitions are asked:** "State what is meant by" (15), "Describe what is meant by" (13), "Explain the meaning of" (6), "Define" (6).
- **Tick** answers a printed grid of statements. It is modelled inside tasks, not as a card instruction.

## 4. What a creditable answer looks like

From the mark schemes' own award rules. Structure only; no scheme wording is reproduced.

| command, marks | parts | how it is marked |
|---|---:|---|
| Describe 2 | 98 | one mark per creditable point from a list longer than the tariff (55%); a third of schemes mark a development separately |
| Explain 2 | 82 | the same pattern: points from a longer list (57%), development marked separately (29%) |
| Explain 3 | 50 | points from a longer list (80%); development marked separately (56%) |
| Describe 4 | 43 | points from a longer list (77%); development marked separately (72%) |
| Complete 2-5 | 209 | one mark per correct gap, row or statement (59-78%) |
| State 1, Identify 1, Convert 1 | 143 | one correct element; nothing else earns credit |
| Write 6-8 | 101 | numbered mark points, each naming one element of the solution (73-90%) |

**Two things follow for every card.**

- **At 3 marks and above, a point has to be developed to earn its second mark.** "It is faster" is a point. "… so the file takes less time to transmit to the phone" is the development. State and Identify cards want the bare item.
- **An algorithm is marked element by element.** Across 160 Paper 2 Write and Complete parts of 5 marks or more, the mark points most often name:
  - a loop with the right bounds or terminating condition (72%);
  - the value returned or the output produced (71%);
  - selection inside the loop (64%);
  - the heading and ending, with parameters and return type (52%);
  - calling another module or using parameters (50%);
  - declarations (47%);
  - counting or totalling (44%);
  - array access (42%).

  So a structurally complete answer scores even where one step of its logic is wrong. A heading, a correct loop and a RETURN are marks in their own right.

## 5. Where the marks fall

Share of the corpus's marks by syllabus section. Each part is matched to one objective, so these figures are approximate.

| section | share | section | share |
|---|---:|---|---:|
| 1 Information representation | 8.2% | 7 Ethics and ownership | 2.1% |
| 2 Communication | 6.0% | 8 Databases | 9.1% |
| 3 Hardware | 6.5% | 9 Algorithm design | 5.3% |
| 4 Processor fundamentals | 9.5% | 10 Data types and structures | 18.2% |
| 5 System software | 5.2% | 11 Programming | 17.9% |
| 6 Security, privacy, integrity | 3.5% | 12 Software development | 8.6% |

**The most-examined outcomes** appear in all 10 series:

- defining and using procedures and functions, with parameters (11.3);
- text-file handling (10.3);
- arrays (10.2), and stacks, queues and linked lists implemented with arrays (10.4);
- registers and the fetch-execute cycle (4.1);
- SQL DDL and DML (8.3);
- flowcharts (9.2);
- number systems (1.1).

**Paper 2 needs rules, not word-matching.** A Paper 2 part that asks for a module usually combines a file, a loop, a test and a return. So Paper 2 parts are filed by what they ask the candidate to produce (a structure chart, a trace table, test data, a module), and word-matching decides only what those rules leave. 26 outcomes are never the best match for any part. Some of them are examined only inside a neighbour (truth tables inside logic-circuit questions, assembly tracing inside addressing questions). Exposure calibrates emphasis. It never removes coverage (RS-05).

## 6. How candidates lose marks on every question (the systemic failures)

Counted over the 60 AS report sections: statements that state an error or give general advice and match each failure. **Spread** is the number of report sections, out of 60, that make the point; **series** is out of 10.

| paper | failure | statements | spread | series | what the resource does about it |
|---|---|---:|---:|---:|---|
| 1 | answered in general, not applied to the scenario in the question | 118 | 30 | 10 | every scenario card has an answer written for that scenario; guidance says a generic answer earns nothing |
| 1 | imprecise or wrong technical term (memory for storage, package for packet, database for table) | 107 | 30 | 10 | the glossary settles each term; MISCON cards drill the pairs |
| 1 | a statement where a description or explanation was asked for | 44 | 19 | 7 | Describe and Explain cards model a point plus its development; State and Identify cards model the bare item |
| 1 | working or final answer not clearly shown | 35 | 21 | 8 | every conversion card shows working and marks the final answer |
| 1 | repeating the question, or giving the example the stem excludes | 30 | 18 | 9 | scenario cards state an example and ask for others |
| 1 | more answers than asked, or two points that say the same thing | 37 | 15 | 5 | guidance names how many points are credited; a repeated point earns nothing |
| 2 | wrong operator or function (+ for &, no NUM_TO_STR, MID and LENGTH misused) | 105 | 29 | 10 | model answers use & and the insert's functions exactly |
| 2 | file handling detail (mode, CLOSEFILE, EOF(file), quotation marks) | 69 | 26 | 10 | every file answer opens with a mode, tests EOF(file) and closes by name |
| 2 | OUTPUT where RETURN was required, or INPUT instead of parameters | 55 | 25 | 10 | functions RETURN; modules take their values as parameters |
| 2 | a missing end statement (ENDIF, ENDWHILE, NEXT, ENDFUNCTION) | 53 | 23 | 10 | every answer is complete and closed; the end statements are a mark point |
| 2 | the wrong loop or selection structure for the problem | 49 | 25 | 10 | design cards ask which structure fits and why, before any code |
| 2 | a keyword, data type or function name used as an identifier | 38 | 17 | 8 | no model answer uses a reserved word as an identifier |
| 2 | count and total confused; inclusive boundaries; empty string; increment | 37 | 16 | 10 | MISCON cards on 11.1 and 11.2 |
| 2 | programming-language syntax, or functions not in the insert | 35 | 21 | 9 | all code is Cambridge pseudocode; C-11 scans for programming-language syntax |
| 2 | ADTs: pointers shown as data values, or the behaviour described when the array implementation was asked for | 32 | 12 | 7 | 10.4 cards separate behaviour from implementation |
| 2 | pseudocode questions left blank, though their first marks are accessible | 31 | 17 | 7 | worked examples mark each element separately |

The counts come from pattern matches over the report sentences, so treat them as indicative. The spread is the robust figure. Every failure above is reported in at least five of the ten series.

## 7. Examiner-evidenced misconceptions

**86 confusions, curated by hand** from the 1,865 error statements, restated in our words and attached to the objective they concern (`curriculum/misconceptions.json`). Each entry carries:

- the wrong idea;
- the correct idea;
- a test that tells them apart;
- the count of supporting statements (573 in all).

Every entry has at least one. Three examples:

- **Memory and storage** used interchangeably, and data and information. In 11 statements across 4 series, in topics 3.1, 5.1 and 8.2.
- **Validation and verification make data correct.** Neither does. Validation checks data is reasonable; verification checks it was copied accurately. 19 statements in topic 6.2, in 8 of the 10 series.
- **OUTPUT where RETURN is required.** 38 statements in 10 series, on module-writing parts across topics 10.2, 10.3 and 11.3.

By topic, the most confusions are in:

- 2.1 networks (6): public and private IP, IPv6 format, packet, star and mesh, the WNIC and the MAC address;
- 1.1 and 1.2 data and multimedia (5 each): binary prefixes, BCD, two's complement, the three resolutions, drawing list;
- 3.1 hardware (5) and 4.1 the CPU (5): the program counter, CU and CPU, bus roles, register transfer notation.

## 8. Scope

The AS route is sections 1 to 12. The syllabus states four limits inside that content (`curriculum/syllabus-exclusions.json`):

- no memorising of particular character codes;
- gates have at most two inputs (NOT has one);
- one general-purpose register, the accumulator;
- no writing pseudocode to implement a stack, queue or linked list (adding, editing and deleting data in them is required).

A fifth limit is on page 40: no programming code on Paper 2.

A Level content (sections 13-20) is out of scope. `curriculum/scope-scan.json` carries 15 patterns, one per limit and one per A Level section, each tested against text it must catch and in-scope text it must leave alone. For example, it catches "binary search" and "recursion" and allows "linear search" and "bubble sort". It catches "packet switching" and allows "data is sent in packets". An examiner report records candidates importing packet switching from the A Level paper.

## 9. What this means for the plan

- **Two kinds of topic.** Sections 1-8 are Paper 1 topics. Their cards are knowledge applied to a scenario, credited as AO1 and AO2. Sections 9-12 are Paper 2 topics. Their cards are pseudocode, traces and design decisions, credited as AO2 and AO3. A Paper 2 recall card is credited as application, because Paper 2 assesses no AO1.
- **Command words from section 3 only,** at the tariffs they carry.
  - Write has two forms. A flashcard models the short form (a statement, a query, an instruction, up to 4 marks). A worked example models the 6-8 mark module.
  - Justification cards use "Explain why".
- **Answers are developed at 3 marks and above.** Algorithm answers are complete and closed. Their guidance names each mark-point element.
- **Every card that sets a scenario answers for that scenario.**
- **Pseudocode is Cambridge pseudocode** as the insert defines it. Never a programming language.

## Derivation policy

Official assessment material is `mine_do_not_reproduce`. The analysis extracted structure, frequency and examiner-stated failure. No question, mark-scheme or examiner-report wording reaches learner-facing output, and every scenario, program and answer in the resource is original.
