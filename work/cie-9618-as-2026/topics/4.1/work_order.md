# Work order — 4.1 Central Processing Unit (CPU) Architecture

*build/make_work_order.py — regenerate, never edit*

8 assessable objectives · 32 planned items · 2 content units

## Planned AO mix by item count (reported, not targeted)

| AO | planned | item-count target |
|---|---:|---:|
| AO1 | 70% | 30% |
| AO2 | 30% | 40% |
| AO3 | 0% | 30% |

## Planned AO mix in marks-equivalent — the measure the syllabus uses

| AO | planned | syllabus weight |
|---|---:|---:|
| AO1 | 56% | 30% |
| AO2 | 44% | 40% |
| AO3 | 0% | 30% |

75 marks-equivalent of practice in this topic.

> The syllabus states its AO weights as a share of MARKS, so planned_ao_mix_by_marks is the one that answers "does this resource match the exam". It values each card at the tariff of the question it models, split across the AOs the card declares, and values each performance task at the marks of the paper part it models. The count-based mix below is reported only because it is what a reader expects to see; do not balance against it. AO shares by ITEM COUNT: Every objective needs one recall anchor, so AO1 has a structural floor of about 27% in this topic (8 objectives against 30 slots) and cannot reach the 30% target by count however many other cards are added - padding the bank to chase it makes the resource worse. The framework already measures the AO4 share in practice time rather than by count for the same reason. Treat AO1 above target as expected, and AO2/AO3/AO4 below target as the thing worth fixing.

## Content units

**CU-9618-4.1.1** — sub-topic 4.1.1, 4 objectives, 1230–1760 words
- `OBJ-9618-4.1.1-01` tier 2 — Show understanding of the basic Von Neumann model for a computer system and the stored program concept
- `OBJ-9618-4.1.1-02` tier 2 — Show understanding of the purpose and role of registers, including the difference between general purpose and special purpose registers
- `OBJ-9618-4.1.1-03` tier 2 — Show understanding of the purpose and roles of the Arithmetic and Logic Unit (ALU), Control Unit (CU) and system clock, Immediate Access Store (IAS)
- `OBJ-9618-4.1.1-04` tier 2 — Show understanding of how data are transferred between various components of the computer system using the address bus, data bus and control bus

**CU-9618-4.1.2** — sub-topic 4.1.2, 4 objectives, 1230–1760 words
- `OBJ-9618-4.1.2-01` tier 3 — Show understanding of how factors contribute to the performance of the computer system
- `OBJ-9618-4.1.2-02` tier 2 — Understand how different ports provide connection to peripheral devices
- `OBJ-9618-4.1.2-03` tier 2 — Describe the stages of the Fetch-Execute (F-E) cycle
- `OBJ-9618-4.1.2-04` tier 2 — Show understanding of the purpose of interrupts

## Item slots

| Slot | Objective | Subtype | AO | Command word | Tariff | Why |
|---|---|---|---|---|---:|---|
| `001-DEF` | Show understanding of the basic Von Neumann model for a computer system and the stored program concept | DEF | AO1 | State | 1 | instructs with State, which this objective carries |
| `002-WHY` | Show understanding of the basic Von Neumann model for a computer system and the stored program concept | WHY | AO1 | Explain | 2 | instructs with Explain, which this objective carries |
| `003-APP` | Show understanding of the basic Von Neumann model for a computer system and the stored program concept | APP | AO2 | Explain | 2 | instructs with Explain, which this objective carries |
| `004-DEF` | Show understanding of the purpose and role of registers, including the difference between general purpose and special purpose registers | DEF | AO1 | State | 1 | instructs with State, which this objective carries |
| `005-DIST` | Show understanding of the purpose and role of registers, including the difference between general purpose and special purpose registers | DIST | AO1 | Describe | 2 | instructs with Describe, which this objective carries |
| `006-APP` | Show understanding of the purpose and role of registers, including the difference between general purpose and special purpose registers | APP | AO2 | Write | 3 | instructs with Write, which this objective carries |
| `025-MISCON` | Show understanding of the purpose and role of registers, including the difference between general purpose and special purpose registers | MISCON | AO1 | Explain | 2 | discriminates misconception MC-9618-4.1-01 (3 examiner statements): the program counter counts the instructions executed |
| `007-DEF` | Show understanding of the purpose and roles of the Arithmetic and Logic Unit (ALU), Control Unit (CU) and system clock, Immediate Access Store (IAS) | DEF | AO1 | State | 1 | instructs with State, which this objective carries |
| `008-WHY` | Show understanding of the purpose and roles of the Arithmetic and Logic Unit (ALU), Control Unit (CU) and system clock, Immediate Access Store (IAS) | WHY | AO1 | Explain | 2 | instructs with Explain, which this objective carries |
| `009-APP` | Show understanding of the purpose and roles of the Arithmetic and Logic Unit (ALU), Control Unit (CU) and system clock, Immediate Access Store (IAS) | APP | AO2 | Explain | 2 | instructs with Explain, which this objective carries |
| `026-MISCON` | Show understanding of the purpose and roles of the Arithmetic and Logic Unit (ALU), Control Unit (CU) and system clock, Immediate Access Store (IAS) | MISCON | AO1 | Explain | 2 | discriminates misconception MC-9618-4.1-02 (3 examiner statements): describing the whole CPU when the control unit was asked for |
| `010-PROC` | Show understanding of how data are transferred between various components of the computer system using the address bus, data bus and control bus | PROC | AO1 | Describe | 2 | instructs with Describe, which this objective carries |
| `011-MECH` | Show understanding of how data are transferred between various components of the computer system using the address bus, data bus and control bus | MECH | AO1 | Explain | 2 | instructs with Explain, which this objective carries |
| `012-APP` | Show understanding of how data are transferred between various components of the computer system using the address bus, data bus and control bus | APP | AO2 | Complete | 4 | instructs with Complete, which this objective carries |
| `027-MISCON` | Show understanding of how data are transferred between various components of the computer system using the address bus, data bus and control bus | MISCON | AO1 | Explain | 2 | discriminates misconception MC-9618-4.1-03 (4 examiner statements): saying that data or instructions travel on the control bus |
| `030-DEF` | Show understanding of how data are transferred between various components of the computer system using the address bus, data bus and control bus | DEF | AO1 | State | 1 | added to reach the framework AO1 target of 60% |
| `013-DEF` | Show understanding of how factors contribute to the performance of the computer system | DEF | AO1 | State | 1 | instructs with State, which this objective carries |
| `014-CHAIN` | Show understanding of how factors contribute to the performance of the computer system | CHAIN | AO2 | Explain | 2 | instructs with Explain, which this objective carries |
| `015-APP` | Show understanding of how factors contribute to the performance of the computer system | APP | AO2 | Explain | 2 | instructs with Explain, which this objective carries |
| `016-PROC` | Understand how different ports provide connection to peripheral devices | PROC | AO1 | Describe | 2 | instructs with Describe, which this objective carries |
| `017-MECH` | Understand how different ports provide connection to peripheral devices | MECH | AO1 | Explain | 2 | instructs with Explain, which this objective carries |
| `018-APP` | Understand how different ports provide connection to peripheral devices | APP | AO2 | Complete | 4 | instructs with Complete, which this objective carries |
| `019-PROC` | Describe the stages of the Fetch-Execute (F-E) cycle | PROC | AO1 | Describe | 2 | instructs with Describe, which this objective carries |
| `020-MECH` | Describe the stages of the Fetch-Execute (F-E) cycle | MECH | AO1 | Explain | 2 | instructs with Explain, which this objective carries |
| `021-APP` | Describe the stages of the Fetch-Execute (F-E) cycle | APP | AO2 | Complete | 4 | instructs with Complete, which this objective carries |
| `028-MISCON` | Describe the stages of the Fetch-Execute (F-E) cycle | MISCON | AO1 | Explain | 2 | discriminates misconception MC-9618-4.1-04 (14 examiner statements): copying the MAR’s own value into the MDR during the fetch |
| `022-DEF` | Show understanding of the purpose of interrupts | DEF | AO1 | State | 1 | instructs with State, which this objective carries |
| `023-WHY` | Show understanding of the purpose of interrupts | WHY | AO1 | Explain | 2 | instructs with Explain, which this objective carries |
| `024-APP` | Show understanding of the purpose of interrupts | APP | AO2 | Explain | 2 | instructs with Explain, which this objective carries |
| `029-MISCON` | Show understanding of the purpose of interrupts | MISCON | AO1 | Explain | 2 | discriminates misconception MC-9618-4.1-05 (4 examiner statements): one interrupt service routine handles every interrupt |

## Performance tasks

- **short_answer** — A Paper 1 style scenario question: three or four linked parts that identify, describe and explain, every answer applied to the scenario, about 8 marks in all.
- **data_response** — A given table, diagram, circuit, register trace or SQL task to read and complete, with the reason for each entry; about 6 marks.

## Excluded from this topic

Limits the syllabus states, enforced by C-11 in everything a learner reads: memorising particular character codes (syllabus, page 14, topic 1.1); a logic gate with more than two inputs (syllabus, page 18, topic 3.2); more than one general purpose register (syllabus, pages 21-22, topics 4.2 and 4.3); writing pseudocode to implement a stack, queue or linked list (syllabus, page 29, topic 10.4); program code in a programming language on Paper 2 (syllabus, page 40, Paper 2); floating-point representation (A Level 13.3) (syllabus, page 32, A Level content); file organisation and access methods (A Level 13.2) (syllabus, page 32, A Level content); user-defined types beyond records (A Level 13.1) (syllabus, page 32, A Level content); protocols and switching (A Level 14) (syllabus, page 33, A Level content); processor design, parallel processing and virtual machines (A Level 15.1) (syllabus, page 33, A Level content); Boolean algebra, De Morgan and Karnaugh maps (A Level 15.2) (syllabus, page 33, A Level content); encryption protocols and digital certificates (A Level 17) (syllabus, page 34, A Level content); graph and machine-learning algorithms (A Level 18) (syllabus, page 35, A Level content); algorithms and recursion beyond AS (A Level 19) (syllabus, page 35, A Level content); programming paradigms and exception handling (A Level 20) (syllabus, page 36, A Level content)

## Owned by another topic

Name in passing if you must; teach there.

- Multimedia — taught in topic 1.2
