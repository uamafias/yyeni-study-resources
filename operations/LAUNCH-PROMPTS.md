# Launch prompts — Hermes Agent and OpenCode

One prompt starts one subject. Open the harness with this repository (YYeni Study Resources) as its project folder, paste the prompt for the subject, and send. The prompt only points the agent at its brief; the handover in the workspace is the full instruction.

**Before you start**

- OpenCode: use the **Build** agent, not Plan (Plan cannot write files).
- Both harnesses: allow file edits and shell commands for this project, or the run stops at every file to ask.
- One subject per session. Never run two sessions on the same workspace; two different subjects at once is fine.
- Commit the repository first, so everything the run changes can be reviewed or reverted.
- If a run stops part-way, open a new session in the same harness and paste that subject's resume prompt.

## 9618 Cambridge International AS Level Computer Science — first paper 9 October 2026

**Start**

```
You are the AUTHOR for Cambridge International AS Level Computer Science, syllabus code 9618. Your workspace is work/cie-9618-as-2026/ in this repository.

1. Read AGENTS.md, then standard/v0.2.0-draft/roles/AUTHOR.md.
2. Read work/cie-9618-as-2026/HANDOVER-9618-as-computer-science.md. Everything below its first "---" line is your full instruction for this run. Where it differs from AUTHOR.md, the handover wins.
3. Before writing anything, read every file the handover's "Start here" section lists, in order, and the structural exemplar in work/cie-9618-as-2026/exemplar/.
4. Check the tools run: python3 -c "import jsonschema, yaml". If that fails, run: pip3 install -r standard/v0.2.0-draft/tests/requirements.txt
5. Write only inside work/cie-9618-as-2026/topics/. (publish_subject.py writes its own output; that is expected.) Do not edit standard/, work/cie-9618-as-2026/curriculum/, work/cie-9618-as-2026/exemplar/ or any other workspace.
6. Author the whole subject in one run, topic by topic in the handover's order. After each topic, render the notes and loop on the checks until what_to_fix.py is clean. Do not stop to ask what is next.
7. When every topic is clean, run publish_subject.py and give the report the handover asks for.

Begin with step 1.
```

**Resume**

```
Continue the 9618 authoring run in work/cie-9618-as-2026/. Re-read work/cie-9618-as-2026/HANDOVER-9618-as-computer-science.md, then run standard/v0.2.0-draft/checks/what_to_fix.py work/cie-9618-as-2026 <T> for each topic in the handover's order. Resume at the first topic that has no learning items or is not clean, keep every topic that is already clean as it is, and carry on to the end exactly as the handover says.
```

## 9702 Cambridge International AS Level Physics — first paper 14 October 2026

**Start**

```
You are the AUTHOR for Cambridge International AS Level Physics, syllabus code 9702. Your workspace is work/cie-9702-as-2025-2027/ in this repository.

1. Read AGENTS.md, then standard/v0.2.0-draft/roles/AUTHOR.md.
2. Read work/cie-9702-as-2025-2027/HANDOVER-9702-as-physics.md. Everything below its first "---" line is your full instruction for this run. Where it differs from AUTHOR.md, the handover wins.
3. Before writing anything, read every file the handover's "Start here" section lists, in order, and the structural exemplar in work/cie-9702-as-2025-2027/exemplar/.
4. Check the tools run: python3 -c "import jsonschema, yaml". If that fails, run: pip3 install -r standard/v0.2.0-draft/tests/requirements.txt
5. Write only inside work/cie-9702-as-2025-2027/topics/. (publish_subject.py writes its own output; that is expected.) Do not edit standard/, work/cie-9702-as-2025-2027/curriculum/, work/cie-9702-as-2025-2027/exemplar/ or any other workspace.
6. Author the whole subject in one run, topic by topic in the handover's order. After each topic, render the notes and loop on the checks until what_to_fix.py is clean. Do not stop to ask what is next.
7. When every topic is clean, run publish_subject.py and give the report the handover asks for.

Begin with step 1.
```

**Resume**

```
Continue the 9702 authoring run in work/cie-9702-as-2025-2027/. Re-read work/cie-9702-as-2025-2027/HANDOVER-9702-as-physics.md, then run standard/v0.2.0-draft/checks/what_to_fix.py work/cie-9702-as-2025-2027 <T> for each topic in the handover's order. Resume at the first topic that has no learning items or is not clean, keep every topic that is already clean as it is, and carry on to the end exactly as the handover says.
```

## 0460 Cambridge IGCSE Geography — first paper 14 October 2026

**Start**

```
You are the AUTHOR for Cambridge IGCSE Geography, syllabus code 0460. Your workspace is work/cie-0460-igcse-2025-2026/ in this repository.

1. Read AGENTS.md, then standard/v0.2.0-draft/roles/AUTHOR.md.
2. Read work/cie-0460-igcse-2025-2026/HANDOVER-0460-igcse-geography.md. Everything below its first "---" line is your full instruction for this run. Where it differs from AUTHOR.md, the handover wins.
3. Before writing anything, read every file the handover's "Start here" section lists, in order, and the structural exemplar in work/cie-0460-igcse-2025-2026/exemplar/.
4. Check the tools run: python3 -c "import jsonschema, yaml". If that fails, run: pip3 install -r standard/v0.2.0-draft/tests/requirements.txt
5. Write only inside work/cie-0460-igcse-2025-2026/topics/. (publish_subject.py writes its own output; that is expected.) Do not edit standard/, work/cie-0460-igcse-2025-2026/curriculum/, work/cie-0460-igcse-2025-2026/exemplar/ or any other workspace.
6. Author the whole subject in one run, topic by topic in the handover's order. After each topic, render the notes and loop on the checks until what_to_fix.py is clean. Do not stop to ask what is next.
7. When every topic is clean, run publish_subject.py and give the report the handover asks for.

Begin with step 1.
```

**Resume**

```
Continue the 0460 authoring run in work/cie-0460-igcse-2025-2026/. Re-read work/cie-0460-igcse-2025-2026/HANDOVER-0460-igcse-geography.md, then run standard/v0.2.0-draft/checks/what_to_fix.py work/cie-0460-igcse-2025-2026 <T> for each topic in the handover's order. Resume at the first topic that has no learning items or is not clean, keep every topic that is already clean as it is, and carry on to the end exactly as the handover says.
```

## 9093 Cambridge International AS Level English Language — first paper 16 October 2026

**Start**

```
You are the AUTHOR for Cambridge International AS Level English Language, syllabus code 9093. Your workspace is work/cie-9093-as-2024-2026/ in this repository.

1. Read AGENTS.md, then standard/v0.2.0-draft/roles/AUTHOR.md.
2. Read work/cie-9093-as-2024-2026/HANDOVER-9093-as-english-language.md. Everything below its first "---" line is your full instruction for this run. Where it differs from AUTHOR.md, the handover wins.
3. Before writing anything, read every file the handover's "Start here" section lists, in order, and the structural exemplar in work/cie-9093-as-2024-2026/exemplar/.
4. Check the tools run: python3 -c "import jsonschema, yaml". If that fails, run: pip3 install -r standard/v0.2.0-draft/tests/requirements.txt
5. Write only inside work/cie-9093-as-2024-2026/topics/. (publish_subject.py writes its own output; that is expected.) Do not edit standard/, work/cie-9093-as-2024-2026/curriculum/, work/cie-9093-as-2024-2026/exemplar/ or any other workspace.
6. Author the whole subject in one run, topic by topic in the handover's order. After each topic, render the notes and loop on the checks until what_to_fix.py is clean. Do not stop to ask what is next.
7. When every topic is clean, run publish_subject.py and give the report the handover asks for.

Begin with step 1.
```

**Resume**

```
Continue the 9093 authoring run in work/cie-9093-as-2024-2026/. Re-read work/cie-9093-as-2024-2026/HANDOVER-9093-as-english-language.md, then run standard/v0.2.0-draft/checks/what_to_fix.py work/cie-9093-as-2024-2026 <T> for each topic in the handover's order. Resume at the first topic that has no learning items or is not clean, keep every topic that is already clean as it is, and carry on to the end exactly as the handover says.
```

## 0500 Cambridge IGCSE First Language English

**Start**

```
You are the AUTHOR for Cambridge IGCSE First Language English, syllabus code 0500. Your workspace is work/cie-0500-igcse-2024-2026/ in this repository.

1. Read AGENTS.md, then standard/v0.2.0-draft/roles/AUTHOR.md.
2. Read work/cie-0500-igcse-2024-2026/HANDOVER-0500-igcse-first-language-english.md. Everything below its first "---" line is your full instruction for this run. Where it differs from AUTHOR.md, the handover wins.
3. Before writing anything, read every file the handover's "Start here" section lists, in order, and the structural exemplar in work/cie-0500-igcse-2024-2026/exemplar/.
4. Check the tools run: python3 -c "import jsonschema, yaml". If that fails, run: pip3 install -r standard/v0.2.0-draft/tests/requirements.txt
5. Write only inside work/cie-0500-igcse-2024-2026/topics/. (publish_subject.py writes its own output; that is expected.) Do not edit standard/, work/cie-0500-igcse-2024-2026/curriculum/, work/cie-0500-igcse-2024-2026/exemplar/ or any other workspace.
6. Author the whole subject in one run, topic by topic in the handover's order. After each topic, render the notes and loop on the checks until what_to_fix.py is clean. Do not stop to ask what is next.
7. When every topic is clean, run publish_subject.py and give the report the handover asks for.

Begin with step 1.
```

**Resume**

```
Continue the 0500 authoring run in work/cie-0500-igcse-2024-2026/. Re-read work/cie-0500-igcse-2024-2026/HANDOVER-0500-igcse-first-language-english.md, then run standard/v0.2.0-draft/checks/what_to_fix.py work/cie-0500-igcse-2024-2026 <T> for each topic in the handover's order. Resume at the first topic that has no learning items or is not clean, keep every topic that is already clean as it is, and carry on to the end exactly as the handover says.
```

## 0450 Cambridge IGCSE Business Studies

**Start**

```
You are the AUTHOR for Cambridge IGCSE Business Studies, syllabus code 0450. Your workspace is work/cie-0450-igcse-2026/ in this repository.

1. Read AGENTS.md, then standard/v0.2.0-draft/roles/AUTHOR.md.
2. Read work/cie-0450-igcse-2026/HANDOVER-0450-igcse-business-studies.md. Everything below its first "---" line is your full instruction for this run. Where it differs from AUTHOR.md, the handover wins.
3. Before writing anything, read every file the handover's "Start here" section lists, in order.
4. Check the tools run: python3 -c "import jsonschema, yaml". If that fails, run: pip3 install -r standard/v0.2.0-draft/tests/requirements.txt
5. Write only inside work/cie-0450-igcse-2026/topics/. (publish_subject.py writes its own output; that is expected.) Do not edit standard/, work/cie-0450-igcse-2026/curriculum/, work/cie-0450-igcse-2026/exemplar/ or any other workspace.
6. Author the whole subject in one run, topic by topic in the handover's order. After each topic, render the notes and loop on the checks until what_to_fix.py is clean. Do not stop to ask what is next.
7. When every topic is clean, run publish_subject.py and give the report the handover asks for.

Begin with step 1.
```

**Resume**

```
Continue the 0450 authoring run in work/cie-0450-igcse-2026/. Re-read work/cie-0450-igcse-2026/HANDOVER-0450-igcse-business-studies.md, then run standard/v0.2.0-draft/checks/what_to_fix.py work/cie-0450-igcse-2026 <T> for each topic in the handover's order. Resume at the first topic that has no learning items or is not clean, keep every topic that is already clean as it is, and carry on to the end exactly as the handover says.
```

## 0455 Cambridge IGCSE Economics

**Start**

```
You are the AUTHOR for Cambridge IGCSE Economics, syllabus code 0455. Your workspace is work/cie-0455-igcse-2026/ in this repository.

1. Read AGENTS.md, then standard/v0.2.0-draft/roles/AUTHOR.md.
2. Read work/cie-0455-igcse-2026/HANDOVER-0455-igcse-economics.md. Everything below its first "---" line is your full instruction for this run. Where it differs from AUTHOR.md, the handover wins.
3. Before writing anything, read every file the handover's "Start here" section lists, in order.
4. Check the tools run: python3 -c "import jsonschema, yaml". If that fails, run: pip3 install -r standard/v0.2.0-draft/tests/requirements.txt
5. Write only inside work/cie-0455-igcse-2026/topics/. (publish_subject.py writes its own output; that is expected.) Do not edit standard/, work/cie-0455-igcse-2026/curriculum/, work/cie-0455-igcse-2026/exemplar/ or any other workspace.
6. Author the whole subject in one run, topic by topic in the handover's order. After each topic, render the notes and loop on the checks until what_to_fix.py is clean. Do not stop to ask what is next.
7. When every topic is clean, run publish_subject.py and give the report the handover asks for.

Begin with step 1.
```

**Resume**

```
Continue the 0455 authoring run in work/cie-0455-igcse-2026/. Re-read work/cie-0455-igcse-2026/HANDOVER-0455-igcse-economics.md, then run standard/v0.2.0-draft/checks/what_to_fix.py work/cie-0455-igcse-2026 <T> for each topic in the handover's order. Resume at the first topic that has no learning items or is not clean, keep every topic that is already clean as it is, and carry on to the end exactly as the handover says.
```

## Notes

- **0455:** its plan is 8 points off the syllabus AO weights (the others are within 5). Fix the plan before launching it.
- **9609:** its workspace holds a repair handover (HANDOVER-9609-command-word-repair.md), not an authoring run; it is not listed here.
