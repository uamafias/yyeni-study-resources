# -*- coding: utf-8 -*-
"""The 0500 plan, as data. Read by build_0500.py.

Three kinds of value live here, and each says which it is:

  syllabus   transcribed from the 0500 syllabus (2024-2026, v1); every objective's text is verified
             against the page it cites before anything is written.
  corpus     counted from the 84 question papers, 84 mark schemes and 17 examiner reports held for
             2020-2025 (see operations/analysis/0500-igcse-first-language-english-corpus-analysis.md).
  judgement  our design: how the resource is cut into topics, which cards each objective gets.

0500 is examined by task and skill, not by topic. So a "topic" here is one paper task (or one skill
that runs across Paper 2), and its objectives are the syllabus's own statements of what that task
assesses. Nothing below reproduces question, insert, mark-scheme or examiner-report wording.
"""

CODE = '0500'
SLUG = 'igcse-first-language-english'
WS_NAME = 'cie-0500-igcse-2024-2026'

UNITS = {'1': 'Paper 1 Reading', '2': 'Paper 2 Directed Writing and Composition'}

# ------------------------------------------------------------------------------------------ topics
# Each objective: key, sub_topic, syllabus_text (verbatim), page, sub_objectives, command_words,
# learner_objective (our plain restatement), depth_tier.
TOPICS = [
 {'id': '1.1', 'title': 'Comprehension: explicit and implicit meaning', 'paper': 'P1',
  'task': 'Paper 1 Question 1, comprehension task on Text A (15 marks)',
  'container': ('Comprehension task: this question requires candidates to respond to Text A.', 13),
  'sub_topics': {'1.1.1': 'Finding and restating what a text states', '1.1.2': 'Reading implied meanings and attitudes'},
  'objectives': [
   ('A', '1.1.1', 'R1 demonstrate understanding of explicit meanings', 13, ['R1'], ['Give', 'Explain'],
    'Find what a text states directly and restate it accurately, in your own words where asked', 1),
   ('B', '1.1.1', 'R5 select and use information for specific purposes.', 13, ['R5'], ['Give', 'Identify'],
    'Select exactly the information a question asks for, and no more', 2),
   ('C', '1.1.2', 'R2 demonstrate understanding of implicit meanings and attitudes', 13, ['R2'], ['Explain'],
    'Work out what a text suggests without stating it, including the attitudes of the writer or the people in it', 3),
  ]},
 {'id': '1.2', 'title': 'Selective summary', 'paper': 'P1',
  'task': 'Paper 1 Question 1, summary task on Text B (15 marks: 10 reading, 5 writing)',
  'container': ('Summary task: this question requires candidates to respond to Text B.', 13),
  'sub_topics': {'1.2.1': 'Selecting the points', '1.2.2': 'Writing the summary'},
  'objectives': [
   ('A', '1.2.1', 'Candidates answer a selective summary task in their own words.', 13, ['R1', 'R2', 'R5'], [],
    'Select every idea on the stated focus of a summary and restate it in your own words', 3),
   ('B', '1.2.1', 'Summarise and use material for a specific context', 11, ['R5'], [],
    'Keep a summary to the exact focus the task sets, adding nothing of your own', 2),
   ('C', '1.2.2', 'Candidates write their summary as continuous writing of no more than 120 words.', 13, ['W2'], [],
    'Organise the selected ideas into continuous prose of no more than 120 words', 3),
   ('D', '1.2.2', 'W3 use a range of vocabulary and sentence structures appropriate to context.', 13, ['W3'], [],
    'Use precise vocabulary and compact sentence structures so that each idea takes few words', 3),
  ]},
 {'id': '1.3', 'title': 'Words and phrases in context', 'paper': 'P1',
  'task': 'Paper 1 Question 2, short-answer questions on Text C: the word-and-phrase items',
  'container': ('Short-answer questions: this question requires candidates to respond to Text C.', 14),
  'sub_topics': {'1.3.1': 'Finding the word or phrase', '1.3.2': 'Explaining a word in its context'},
  'objectives': [
   ('A', '1.3.1', 'Demonstrate understanding of written texts, and of the words and phrases within them', 11, ['R1'], ['Identify'],
    'Find the exact word or phrase in a text that carries a given meaning', 2),
   ('B', '1.3.2', 'R2 demonstrate understanding of implicit meanings and attitudes', 14, ['R1', 'R2'], ['Explain'],
    'Explain in your own words what a word means in the sentence where the writer uses it', 2),
  ]},
 {'id': '1.4', 'title': 'How writers achieve effects', 'paper': 'P1',
  'task': 'Paper 1 Question 2: explaining one example, and the language task on Text C (15 marks)',
  'container': ('Language task: this question requires candidates to respond to Text C.', 14),
  'sub_topics': {'1.4.1': 'Language, imagery and their effects', '1.4.2': 'Writing the language analysis'},
  'objectives': [
   ('A', '1.4.1', 'Recognise and respond to linguistic devices, figurative language and imagery.', 11, ['R4'], ['Explain'],
    'Recognise figurative language and imagery and explain what it adds, not just what it is called', 3),
   ('B', '1.4.1', 'R4 demonstrate understanding of how writers achieve effects and influence readers.', 14, ['R4'], ['Explain'],
    'Explain how a writer’s choice of words makes a reader see, feel or understand something', 3),
   ('C', '1.4.2', 'Candidates write about 200–300 words.', 14, ['R1', 'R2', 'R4'], [],
    'Write a language analysis of about 200–300 words on the choices a writer makes across two paragraphs', 4),
  ]},
 {'id': '1.5', 'title': 'Extended response to reading', 'paper': 'P1',
  'task': 'Paper 1 Question 3, extended response on Text C (25 marks: 15 reading, 10 writing)',
  'container': ('Question 3 Extended response to reading (25 marks)', 14),
  'sub_topics': {'1.5.1': 'Reading for the response: developing and inferring', '1.5.2': 'Writing in role: form, voice and register'},
  'objectives': [
   ('A', '1.5.1', 'R3 analyse, evaluate and develop facts, ideas and opinions, using appropriate support from the text.', 14,
    ['R1', 'R2', 'R3'], [], 'Develop ideas from a text beyond what it states, supported by its details, without inventing', 4),
   ('B', '1.5.2', 'Candidates write about 250–350 words, responding in one of the following text types: letter, report, journal, speech, interview and article.', 14,
    ['W2', 'W3'], [], 'Write about 250–350 words in the text type the task names, using its conventions', 3),
   ('C', '1.5.2', 'W4 use register appropriate to context.', 14, ['W4'], [],
    'Match register to the role, the audience and the purpose the task sets', 3),
   ('D', '1.5.2', 'W1 articulate experience and express what is thought, felt and imagined', 14, ['W1'], [],
    'Write in role with a consistent, convincing voice that expresses what that person thinks and feels', 4),
  ]},
 {'id': '2.1', 'title': 'Directed writing: evaluating the texts', 'paper': 'P2',
  'task': 'Paper 2 Section A, directed writing: the reading marks (15)',
  'container': ('Section A Directed Writing (40 marks)', 15),
  'sub_topics': {'2.1.1': 'Fact, opinion, perspective and bias', '2.1.2': 'Evaluating ideas across two texts'},
  'objectives': [
   ('A', '2.1.1', 'Candidates should study how influence may include fact, ideas, perspectives, opinions and bias.', 11,
    ['R1', 'R2'], [], 'Tell facts from opinions and recognise the perspective and any bias behind a text', 2),
   ('B', '2.1.2', 'R3 analyse, evaluate and develop facts, ideas and opinions, using appropriate support from the text', 15,
    ['R3'], [], 'Judge how convincing the ideas and views in two texts are, not just report them', 4),
   ('C', '2.1.2', 'R5 select and use information for specific purposes.', 15, ['R5'], [],
    'Select the ideas from both texts that a task needs, and use them in your own words', 3),
  ]},
 {'id': '2.2', 'title': 'Directed writing: arguing and persuading in form', 'paper': 'P2',
  'task': 'Paper 2 Section A, directed writing: the writing marks (25)',
  'container': ('Candidates use, develop and evaluate the information in the text(s) to create a discursive/argumentative/persuasive speech, letter or article.', 15),
  'sub_topics': {'2.2.1': 'Building an argument of your own', '2.2.2': 'Speech, letter and article'},
  'objectives': [
   ('A', '2.2.1', 'Organise and convey facts, ideas and opinions effectively', 11, ['W1', 'W2'], [],
    'Organise a response by argument, not by the order of the source texts', 3),
   ('B', '2.2.2', 'Demonstrate an understanding of audience, purpose and form', 11, ['W3', 'W4'], [],
    'Write a speech, letter or article that reads as one, in the register its audience and purpose need', 3),
  ]},
 {'id': '2.3', 'title': 'Descriptive writing', 'paper': 'P2',
  'task': 'Paper 2 Section B, composition: descriptive titles (40 marks)',
  'container': ('Section B Composition (40 marks)', 15),
  'sub_topics': {'2.3.1': 'What a description needs', '2.3.2': 'Shaping a description'},
  'objectives': [
   ('A', '2.3.1', 'Express what is thought, felt and imagined', 11, ['W1'], ['Describe'],
    'Build a convincing picture of a place, moment or experience from precise, well-chosen detail', 3),
   ('B', '2.3.1', 'Candidates answer one question from a choice of four titles: two descriptive and two narrative.', 15,
    ['W1', 'W2'], [], 'Choose a title you can develop, and know what a descriptive title asks for', 2),
   ('C', '2.3.2', 'Candidates write about 350–450 words.', 15, ['W2', 'W3'], [],
    'Structure a description of about 350–450 words for deliberate effect', 4),
  ]},
 {'id': '2.4', 'title': 'Narrative writing', 'paper': 'P2',
  'task': 'Paper 2 Section B, composition: narrative titles (40 marks)',
  'container': ('Section B Composition (40 marks)', 15),
  'sub_topics': {'2.4.1': 'What a narrative needs', '2.4.2': 'Structuring a story for effect'},
  'objectives': [
   ('A', '2.4.1', 'Candidates use the title to develop and write a composition.', 15, ['W1'], [],
    'Develop a credible, contained story from a title', 3),
   ('B', '2.4.1', 'As developing writers themselves, candidates should be introduced to a range of writing skills, including the ability to create and compose texts with a variety of forms and purposes, e.g. descriptive, narrative, discursive, argumentative and persuasive.', 11,
    ['W1', 'W3'], [], 'Use the features of fiction — characterisation, setting, convincing detail — to make a story work', 3),
   ('C', '2.4.2', 'W2 organise and structure ideas and opinions for deliberate effect', 15, ['W2'], [],
    'Shape a story with an opening, rising tension, a climax and a resolution', 4),
  ]},
 {'id': '2.5', 'title': 'Vocabulary, sentences and accuracy', 'paper': 'P2',
  'task': 'Paper 2, both sections: vocabulary, sentence structures and accuracy (W3, W5)',
  'container': ('AO2 Writing', 9),
  'sub_topics': {'2.5.1': 'Vocabulary and sentence structures', '2.5.2': 'Spelling, punctuation and grammar'},
  'objectives': [
   ('A', '2.5.1', 'Demonstrate a varied vocabulary appropriate to the context', 11, ['W3'], [],
    'Choose the precise word rather than the general or the showy one', 2),
   ('B', '2.5.1', 'Demonstrate an effective use of sentence structures', 11, ['W3'], [],
    'Vary sentence structures deliberately, for clarity and for effect', 3),
   ('C', '2.5.2', 'Demonstrate accuracy in spelling, punctuation and grammar.', 11, ['W5'], [],
    'Write accurately: sentence boundaries, apostrophes, agreement, tense and commonly confused words', 2),
  ]},
]

# --------------------------------------------------------------------------------- flashcard slots
# (objective key, subtype, what the card teaches, command word or None, tariff or None, misconception id or None)
# The command word and tariff are set only where the card models a real paper item; a technique
# card models none and carries None for both.
F = {}
F['1.1'] = [
 ('A', 'DEF', 'explicit meaning: what a text states in its own words', None, None, None),
 ('A', 'DEF', 'restating in your own words: keeping the idea, replacing the text’s key words', None, None, None),
 ('A', 'PROC', 'locating an answer: go to the paragraph the question names, find the sentence, check it answers exactly what is asked', None, None, None),
 ('A', 'APP', 'give one reason stated in a supplied three-sentence original extract', 'Give', 1, None),
 ('A', 'APP', 'explain a supplied two-part phrase in your own words so that both parts are covered', 'Explain', 2, None),
 ('A', 'DIST', 'quoting the text versus restating it: when the text’s words are acceptable and when own words are required', None, None, None),
 ('A', 'MISCON', 'copying a sentence is not explaining it when the task asks for your own words', None, None, 'MC-0500-1.1-01'),
 ('A', 'MISCON', 'a two-part idea explained by one part only', None, None, 'MC-0500-1.1-02'),
 ('B', 'DEF', 'selecting information for a purpose: taking only what the question asks for', None, None, None),
 ('B', 'PROC', 'matching points to marks: count the marks, find that many separate points', None, None, None),
 ('B', 'DIST', 'a point that answers the question versus an example or detail around it', None, None, None),
 ('B', 'WHY', 'why an answer stops once the point is made: added material can blur or contradict it', None, None, None),
 ('B', 'APP', 'identify the two details in a supplied short original extract that answer a stated question', 'Identify', 2, None),
 ('B', 'MISCON', 'adding material beyond the point can undo a correct answer', None, None, 'MC-0500-1.1-04'),
 ('B', 'MISCON', 'a correct idea taken from outside the paragraph the question names does not answer it', None, None, 'MC-0500-1.1-05'),
 ('C', 'DEF', 'implicit meaning: what a text suggests without stating', None, None, None),
 ('C', 'DEF', 'attitude: a view or feeling shown through what someone says or does, not named', None, None, None),
 ('C', 'DIST', 'explicit versus implicit meaning, and the test that tells them apart', None, None, None),
 ('C', 'DIST', 'an inference the text supports versus a personal opinion about the topic', None, None, None),
 ('C', 'PROC', 'making an inference: detail, what it suggests, check it fits the rest of the text', None, None, None),
 ('C', 'INTERP', 'what a supplied action or detail suggests about a person’s attitude', 'Explain', 2, None),
 ('C', 'INTERP', 'what a writer’s choice of a single word in a supplied sentence suggests about their view', 'Explain', 2, None),
 ('C', 'MISCON', 'reading only what is stated and missing what the text implies', None, None, 'MC-0500-1.1-03'),
]
F['1.2'] = [
 ('A', 'DEF', 'a selective summary: the ideas on one stated focus, not a retelling of the whole text', None, None, None),
 ('A', 'PROC', 'selecting: mark every idea on the focus, strike out examples and repeats, group what is left', None, None, None),
 ('A', 'DIST', 'an idea versus an example that illustrates it', None, None, None),
 ('A', 'APP', 'write one umbrella phrase that covers three supplied specific details', None, None, None),
 ('A', 'APP', 'write one umbrella phrase for a second set of supplied details from a different context', None, None, None),
 ('A', 'MISCON', 'lifting: stringing together the text’s own sentences', None, None, 'MC-0500-1.2-01'),
 ('A', 'MISCON', 'examples and incidental detail included as if they were points', None, None, 'MC-0500-1.2-02'),
 ('B', 'DEF', 'the focus of a summary task: the exact angle it asks for', None, None, None),
 ('B', 'DIST', 'an idea on the focus versus an idea on the topic but off the focus', None, None, None),
 ('B', 'APP', 'from five supplied statements, sort those on a stated focus from those off it', None, None, None),
 ('B', 'MISCON', 'adding your own opinion or comment to a summary', None, None, 'MC-0500-1.2-04'),
 ('B', 'MISCON', 'answering the topic of the text instead of the focus of the task', None, None, 'MC-0500-1.2-05'),
 ('C', 'DEF', 'continuous writing: connected prose, not notes, bullets or a list', None, None, None),
 ('C', 'DIST', 'a list of points versus an organised overview', None, None, None),
 ('C', 'PROC', 'ordering a summary: group related ideas, sequence the groups, link them', None, None, None),
 ('C', 'WHY', 'why concision matters inside 120 words: shorter points leave room for more of them', None, None, None),
 ('C', 'FEATURE', 'what an organised, concise summary contains', None, None, None),
 ('C', 'MISCON', 'a few ideas explained at length instead of many ideas put concisely', None, None, 'MC-0500-1.2-06'),
 ('C', 'MISCON', 'a summary that reads as a list rather than an overview', None, None, 'MC-0500-1.2-03'),
 ('D', 'DIST', 'paraphrase versus swapping single words and keeping the text’s sentence', None, None, None),
 ('D', 'APP', 'rewrite a supplied wordy sentence concisely in your own words', None, None, None),
 ('D', 'FEATURE', 'sentence structures that compress several ideas into one sentence', None, None, None),
]
F['1.3'] = [
 ('A', 'DEF', 'synonym: a word with the same meaning in a given context', None, None, None),
 ('A', 'PROC', 'finding the word or phrase: re-read the named paragraph, find the candidate, test it by substitution', None, None, None),
 ('A', 'APP', 'identify the word in a supplied original sentence that means a given idea', 'Identify', 1, None),
 ('A', 'APP', 'identify the phrase in a supplied original sentence that means a given idea', 'Identify', 1, None),
 ('A', 'APP', 'identify the word in a supplied original sentence that suggests a given feeling', 'Identify', 1, None),
 ('A', 'APP', 'identify the phrase in a supplied original sentence that suggests a given quality of a place', 'Identify', 1, None),
 ('A', 'DIST', 'giving the text’s word or phrase versus explaining a meaning in your own words: which task asks for which', None, None, None),
 ('A', 'MISCON', 'copying a whole sentence when one word or phrase is asked for', None, None, 'MC-0500-1.3-01'),
 ('B', 'DEF', 'meaning in context: the sense a word carries in the sentence where it is used', None, None, None),
 ('B', 'DEF', 'denotation: the literal, dictionary meaning of a word', None, None, None),
 ('B', 'DEF', 'connotation: the associations a word carries beyond its literal meaning', None, None, None),
 ('B', 'DIST', 'a word’s dictionary sense versus the sense a sentence gives it', None, None, None),
 ('B', 'PROC', 'explaining a word: read the whole sentence, settle the sense used, give an own-words equivalent that fits', None, None, None),
 ('B', 'APP', 'explain in your own words a supplied verb as used in an original sentence', 'Explain', 1, None),
 ('B', 'APP', 'explain in your own words a supplied adjective as used in an original sentence', 'Explain', 1, None),
 ('B', 'APP', 'explain in your own words a supplied word that has several senses, as used in an original sentence', 'Explain', 1, None),
 ('B', 'APP', 'explain in your own words a supplied adverb as used in an original sentence', 'Explain', 1, None),
 ('B', 'MISCON', 'guessing a meaning from the look of a word without checking the sentence', None, None, 'MC-0500-1.3-02'),
 ('B', 'MISCON', 'repeating the word, or a form of it, instead of explaining it', None, None, 'MC-0500-1.3-03'),
]
F['1.4'] = [
 ('A', 'DEF', 'simile', None, None, None),
 ('A', 'DEF', 'metaphor', None, None, None),
 ('A', 'DEF', 'personification', None, None, None),
 ('A', 'DEF', 'imagery: language that creates a picture or sensation in the reader’s mind', None, None, None),
 ('A', 'DEF', 'figurative versus literal language', None, None, None),
 ('A', 'DEF', 'onomatopoeia and the sound of words', None, None, None),
 ('A', 'DEF', 'hyperbole', None, None, None),
 ('A', 'MECH', 'how a supplied original metaphor creates its effect: literal picture first, then what it suggests', 'Explain', 3, None),
 ('A', 'MECH', 'how a supplied original simile shapes the reader’s view of a person', 'Explain', 3, None),
 ('A', 'MECH', 'how personification in a supplied original sentence makes a setting feel threatening or welcoming', 'Explain', 3, None),
 ('A', 'DIST', 'reading an image literally versus figuratively, and why both are needed', None, None, None),
 ('A', 'MISCON', 'naming a device is not explaining its effect', None, None, 'MC-0500-1.4-04'),
 ('A', 'MISCON', 'leaving an image unexplained, or explaining it only literally', None, None, 'MC-0500-1.4-05'),
 ('B', 'DEF', 'effect: what a language choice makes the reader see, feel or understand', None, None, None),
 ('B', 'PROC', 'the meaning-then-effect sequence for one language choice', None, None, None),
 ('B', 'DIST', 'meaning versus effect', None, None, None),
 ('B', 'MECH', 'how a supplied verb choice in an original sentence conveys movement or mood', 'Explain', 3, None),
 ('B', 'MECH', 'how supplied adjectives in an original sentence build an impression of a place', 'Explain', 3, None),
 ('B', 'APP', 'choose one example from a supplied original extract and explain how it suggests a feeling', 'Explain', 3, None),
 ('B', 'MISCON', 'discussing several examples when the task asks for one', None, None, 'MC-0500-1.4-01'),
 ('B', 'MISCON', 'explaining what words mean and stopping before their effect', None, None, 'MC-0500-1.4-03'),
 ('C', 'PROC', 'planning a language analysis: about three short choices from each named paragraph, balanced', None, None, None),
 ('C', 'DIST', 'a short, precise quotation versus a long one', None, None, None),
 ('C', 'WHY', 'why short quotations let you examine the individual words inside them', None, None, None),
 ('C', 'FEATURE', 'what one strong paragraph of language analysis contains', None, None, None),
 ('C', 'MISCON', 'long quotations that leave no single word examined', None, None, 'MC-0500-1.4-02'),
 ('C', 'MISCON', 'one paragraph analysed and the other neglected', None, None, 'MC-0500-1.4-06'),
 ('C', 'MISCON', 'general comments about atmosphere with no specific words attached', None, None, 'MC-0500-1.4-07'),
]
F['1.5'] = [
 ('A', 'DEF', 'developing an idea: saying why, or what follows, beyond what the text states', None, None, None),
 ('A', 'PROC', 'planning the route: for each of the three bullets, the text material, the explicit and implicit ideas, the developments', None, None, None),
 ('A', 'APP', 'develop a supplied detail from an original extract into a point made in role', None, None, None),
 ('A', 'DIST', 'developing an idea versus repeating it', None, None, None),
 ('A', 'DIST', 'using the text’s details in your own words versus copying them', None, None, None),
 ('A', 'WHY', 'why the three bullets are the structure of the answer', None, None, None),
 ('A', 'MISCON', 'one bullet covered well and another thinly or not at all', None, None, 'MC-0500-1.5-01'),
 ('A', 'MISCON', 'repeating the text’s ideas without developing or inferring from them', None, None, 'MC-0500-1.5-02'),
 ('A', 'MISCON', 'copying the text’s details instead of using them in your own words', None, None, 'MC-0500-1.5-03'),
 ('A', 'MISCON', 'inventing material the text does not support', None, None, 'MC-0500-1.5-04'),
 ('B', 'FEATURE', 'the conventions of a letter', None, None, None),
 ('B', 'FEATURE', 'the conventions of a report', None, None, None),
 ('B', 'FEATURE', 'the conventions of a journal or diary entry', None, None, None),
 ('B', 'FEATURE', 'the conventions of a speech', None, None, None),
 ('B', 'FEATURE', 'the conventions of an interview', None, None, None),
 ('B', 'FEATURE', 'the conventions of an article', None, None, None),
 ('B', 'DIST', 'a journal entry versus a letter: who the reader is changes what is said and how', None, None, None),
 ('C', 'DEF', 'register', None, None, None),
 ('C', 'DIST', 'formal versus informal register, and what decides which fits', None, None, None),
 ('C', 'APP', 'rewrite a supplied informal sentence for a named formal audience', None, None, None),
 ('C', 'MISCON', 'a register that does not fit the role or the audience', None, None, 'MC-0500-1.5-05'),
 ('D', 'DEF', 'voice: the sense of a particular person speaking', None, None, None),
 ('D', 'PROC', 'building a voice: who you are, what you know, how you feel, who you are addressing', None, None, None),
 ('D', 'DIST', 'a plain factual account versus a convincing voice in role', None, None, None),
]
F['2.1'] = [
 ('A', 'DEF', 'fact', None, None, None),
 ('A', 'DEF', 'opinion', None, None, None),
 ('A', 'DEF', 'perspective', None, None, None),
 ('A', 'DEF', 'bias', None, None, None),
 ('A', 'DIST', 'fact versus opinion, and the test that tells them apart', None, None, None),
 ('A', 'DIST', 'an opinion versus a biased account', None, None, None),
 ('A', 'APP', 'classify three supplied original statements as fact, opinion or biased claim, with the reason', None, None, None),
 ('A', 'INTERP', 'what a supplied original sentence implies about its writer’s attitude to a proposal', None, None, None),
 ('B', 'DEF', 'evaluating a view: judging how convincing, complete or consistent it is', None, None, None),
 ('B', 'DIST', 'summarising the texts’ ideas versus evaluating them', None, None, None),
 ('B', 'PROC', 'evaluating one view: its claim, its support, what it overlooks, how the other text tests it', None, None, None),
 ('B', 'EVAL', 'judge how convincing a supplied original claim is, given the evidence offered for it', None, None, None),
 ('B', 'EVAL', 'judge which of two supplied original views on the same proposal is better supported', None, None, None),
 ('B', 'EVAL', 'judge what a supplied original argument leaves out, and whether that weakens it', None, None, None),
 ('B', 'APP', 'use a point from one supplied original text to question a point in another', None, None, None),
 ('B', 'MISCON', 'paraphrasing and listing the texts’ ideas as if that were evaluation', None, None, 'MC-0500-2.1-01'),
 ('C', 'DEF', 'selecting for the task: the ideas your argument and your audience need', None, None, None),
 ('C', 'PROC', 'gathering from two texts: collect from both, sort for and against, keep what the task needs', None, None, None),
 ('C', 'MISCON', 'drawing on one text and ignoring the other', None, None, 'MC-0500-2.1-02'),
 ('C', 'MISCON', 'lifting the texts’ sentences instead of using their ideas in your own words', None, None, 'MC-0500-2.1-03'),
]
F['2.2'] = [
 ('A', 'DIST', 'discursive, argumentative and persuasive writing: what each sets out to do', None, None, None),
 ('A', 'PROC', 'organising by argument: position, grouped points, the other side answered, conclusion', None, None, None),
 ('A', 'DIST', 'organising by argument versus following the order of the source texts', None, None, None),
 ('A', 'FEATURE', 'what a developed argument paragraph contains', None, None, None),
 ('A', 'APP', 'combine two supplied original source points into one evaluated sentence of your own', None, None, None),
 ('A', 'PROC', 'answering the second bullet: turning the evaluation into advice, a response or a recommendation', None, None, None),
 ('A', 'MISCON', 'following the order of the source texts, so the argument comes out disconnected', None, None, 'MC-0500-2.2-01'),
 ('A', 'MISCON', 'a second bullet handled in a sentence at the end', None, None, 'MC-0500-2.2-03'),
 ('B', 'DEF', 'audience and purpose', None, None, None),
 ('B', 'FEATURE', 'the conventions of a speech', None, None, None),
 ('B', 'FEATURE', 'the conventions of a formal letter', None, None, None),
 ('B', 'FEATURE', 'the conventions of an article', None, None, None),
 ('B', 'DIST', 'a speech versus an article: listeners in the room versus readers on the page', None, None, None),
 ('B', 'DEF', 'rhetorical question', None, None, None),
 ('B', 'DEF', 'direct address', None, None, None),
 ('B', 'MECH', 'how direct address draws an audience into agreeing', None, None, None),
 ('B', 'APP', 'write the opening of a speech for a supplied audience and occasion', None, None, None),
 ('B', 'MISCON', 'a form named but not written: a letter or speech that reads as an essay', None, None, 'MC-0500-2.2-02'),
]
F['2.3'] = [
 ('A', 'DEF', 'descriptive writing: a picture built from detail, not a sequence of events', None, None, None),
 ('A', 'DIST', 'describing versus narrating', None, None, None),
 ('A', 'DEF', 'sensory detail', None, None, None),
 ('A', 'DEF', 'atmosphere', None, None, None),
 ('A', 'PROC', 'building a description: fix a moment and a place, gather the senses, choose the precise details, shift focus', None, None, None),
 ('A', 'APP', 'rewrite a supplied flat original sentence with precise sensory detail', None, None, None),
 ('A', 'APP', 'rewrite a second supplied flat original sentence so that it creates a mood', None, None, None),
 ('A', 'MISCON', 'a description that turns into a story of events', None, None, 'MC-0500-2.3-01'),
 ('A', 'MISCON', 'cliché in place of observed detail', None, None, 'MC-0500-2.3-02'),
 ('B', 'PROC', 'reading a descriptive title: what it names, what it leaves open, what you could build from it', None, None, None),
 ('B', 'WHY', 'why the choice between titles should rest on the material you can describe', None, None, None),
 ('C', 'PROC', 'structuring a description: a frame, a movement of focus, a change in time or light, a return', None, None, None),
 ('C', 'MECH', 'how moving from a wide view to a close detail structures a description', None, None, None),
 ('C', 'MECH', 'how varied sentence lengths build atmosphere', None, None, None),
 ('C', 'FEATURE', 'what a convincing, well-shaped description contains', None, None, None),
 ('C', 'DIST', 'precise vocabulary versus showy vocabulary', None, None, None),
]
F['2.4'] = [
 ('A', 'DEF', 'plot', None, None, None),
 ('A', 'PROC', 'developing a story from a title: one central event, one or two characters, one conflict', None, None, None),
 ('A', 'DIST', 'a contained plot versus a chain of events', None, None, None),
 ('A', 'MISCON', 'too many events and no credible shape', None, None, 'MC-0500-2.4-01'),
 ('B', 'DEF', 'characterisation', None, None, None),
 ('B', 'DEF', 'setting', None, None, None),
 ('B', 'MECH', 'how one well-chosen detail makes a character credible', None, None, None),
 ('B', 'APP', 'rewrite a supplied original sentence that tells a feeling so that it shows it', None, None, None),
 ('B', 'DIST', 'first-person versus third-person narration, and what each makes possible', None, None, None),
 ('B', 'FEATURE', 'what a well-developed narrative contains', None, None, None),
 ('C', 'DEF', 'climax', None, None, None),
 ('C', 'DEF', 'resolution', None, None, None),
 ('C', 'PROC', 'structuring a story: opening, complication, rising tension, climax, resolution', None, None, None),
 ('C', 'MECH', 'how slowing the pace at the climax builds tension', None, None, None),
 ('C', 'DIST', 'an open ending versus an unfinished one', None, None, None),
 ('C', 'MISCON', 'a story that stops rather than ends', None, None, 'MC-0500-2.4-02'),
]
F['2.5'] = [
 ('A', 'DIST', 'the precise word versus the general word', None, None, None),
 ('A', 'APP', 'replace the general words in a supplied original sentence with precise ones', None, None, None),
 ('A', 'APP', 'choose between three supplied near-synonyms for a supplied context, with the reason', None, None, None),
 ('A', 'MISCON', 'an ambitious word used in the wrong sense', None, None, 'MC-0500-2.5-01'),
 ('B', 'DEF', 'simple sentence', None, None, None),
 ('B', 'DEF', 'compound sentence', None, None, None),
 ('B', 'DEF', 'complex sentence', None, None, None),
 ('B', 'MECH', 'how a short sentence after longer ones creates emphasis', None, None, None),
 ('B', 'APP', 'combine two supplied simple sentences into one complex sentence', None, None, None),
 ('B', 'DIST', 'a sentence fragment versus a deliberate minor sentence', None, None, None),
 ('C', 'DEF', 'comma splice', None, None, None),
 ('C', 'APP', 'correct a supplied comma splice in three different ways', None, None, None),
 ('C', 'DIST', 'its versus it’s', None, None, None),
 ('C', 'DIST', 'their, there and they’re', None, None, None),
 ('C', 'DIST', 'apostrophe for possession versus apostrophe for omission', None, None, None),
 ('C', 'FEATURE', 'how direct speech is punctuated', None, None, None),
 ('C', 'PROC', 'proofreading: one read for each kind of error', None, None, None),
 ('C', 'APP', 'correct the subject–verb agreement errors in a supplied original sentence', None, None, None),
 ('C', 'APP', 'correct the tense shifts in a supplied original passage of three sentences', None, None, None),
 ('C', 'MISCON', 'comma splices: two sentences joined by a comma', None, None, 'MC-0500-2.5-02'),
 ('C', 'MISCON', 'tense that drifts between past and present in a narrative', None, None, 'MC-0500-2.5-03'),
]

# ---------------------------------------------------------------------------- performance tasks
# The paper architecture (syllabus) with its corpus-measured sub-layout. A text a task is answered from
# is an ORIGINAL written for the purpose (RS-48); its length is the syllabus's.
TEXTS = {
 '1.1': [('TXT-0500-1.1-%02d' % n, 700, 750, g) for n, g in
         [(1, 'non-fiction feature article'), (2, 'autobiographical account'), (3, 'informative article with a narrative thread')]],
 '1.2': [('TXT-0500-1.2-%02d' % n, 700, 750, g) for n, g in
         [(1, 'informative article'), (2, 'report-style account of a project or scheme'), (3, 'non-fiction article weighing a change'), (4, 'feature article on a local initiative')]],
 '1.3': [('TXT-0500-1.3-%02d' % n, 500, 650, g) for n, g in
         [(1, 'descriptive or narrative prose'), (2, 'autobiographical prose')]],
 '1.4': [('TXT-0500-1.4-%02d' % n, 500, 650, g) for n, g in
         [(1, 'narrative prose rich in imagery'), (2, 'descriptive travel writing'), (3, 'fiction with a tense moment'), (4, 'memoir of a journey')]],
 '1.5': [('TXT-0500-1.5-%02d' % n, 500, 650, g) for n, g in
         [(1, 'narrative account of an event'), (2, 'autobiographical prose'), (3, 'narrative with two people in it'), (4, 'account of a place and the people who work there'), (5, 'account of a community event')]],
 '2.1': [('TXT-0500-2.1-%02d' % n, 650, 750, g) for n, g in
         [(1, 'two texts, an article and a letter, taking different views of a local proposal'), (2, 'two texts, a speech and a blog post, on a school or youth issue'), (3, 'one article presenting several views of a national issue')]],
 '2.2': [('TXT-0500-2.2-%02d' % n, 650, 750, g) for n, g in
         [(1, 'two texts with opposed views, for a letter task'), (2, 'two texts with opposed views, for a speech task'), (3, 'two texts with mixed views, for an article task')]],
}

# (slot suffix, item_type, text index or None, objective keys, sub_objectives, command word, tariff, bloom, brief)
P = {}
P['1.1'] = []
_LAYOUT = [(1, 'Give', ['A'], ['R1'], 'one explicit detail'),
           (2, 'Explain', ['A'], ['R1'], 'explain a two-part phrase in your own words'),
           (2, 'Explain', ['A', 'C'], ['R1', 'R2'], 'explain a second phrase in your own words'),
           (2, 'Give', ['B'], ['R1', 'R5'], 'two separate points from a named paragraph'),
           (2, 'Explain', ['C'], ['R2'], 'what a detail implies about someone’s attitude'),
           (3, 'Explain', ['B', 'C'], ['R2', 'R5'], 'three reasons, stated or implied, from a named paragraph'),
           (3, 'Explain', ['A', 'B', 'C'], ['R1', 'R2', 'R5'], 'three points from across two named paragraphs')]
for t in range(3):
    for (m, cw, keys, subs, brief) in _LAYOUT:
        P['1.1'].append(('short_answer', t, keys, subs, cw, m, 'Understand',
                         'Text A-style comprehension item, %d mark%s: %s' % (m, '' if m == 1 else 's', brief)))
P['1.2'] = [('writing_task', t, ['A', 'B', 'C', 'D'], ['R1', 'R2', 'R5', 'W2', 'W3'], None, 15, 'Analyse',
             'selective summary of no more than 120 words on a stated focus; the model answer, the list of '
             'content points on that focus, and guidance against both level tables (reading /10, writing /5)')
            for t in range(4)]
P['1.3'] = []
for t in range(2):
    for n in range(4):
        P['1.3'].append(('short_answer', t, ['A'], ['R1'], 'Identify', 1, 'Understand',
                         'word-or-phrase item, 1 mark: the text’s word or phrase for a given idea'))
    for n in range(3):
        P['1.3'].append(('short_answer', t, ['B'], ['R1', 'R2'], 'Explain', 1, 'Understand',
                         'own-words meaning of a single word as used, 1 mark'))
P['1.4'] = []
for t in range(4):
    P['1.4'].append(('source_analysis', t, ['B'], ['R2', 'R4'], 'Explain', 3, 'Analyse',
                     'choose one example from a named short extract and explain how it suggests a feeling, 3 marks'))
    P['1.4'].append(('source_analysis', t, ['A', 'B', 'C'], ['R1', 'R2', 'R4'], None, 15, 'Analyse',
                     'language task on two named paragraphs, about 200–300 words; model answer and guidance against the 15-mark level table'))
P['1.5'] = [('writing_task', t, ['A', 'B', 'C', 'D'], ['R1', 'R2', 'R3', 'W1', 'W2', 'W3', 'W4'], None, 25, 'Create',
             'extended response in role, about 250–350 words, three bullets, in the form: %s; model answer and '
             'guidance against both level tables (reading /15, writing /10)' % f)
            for t, f in enumerate(['interview', 'letter', 'journal entry', 'speech', 'article'])]
P['2.1'] = [('essay_plan', t, ['A', 'B', 'C'], ['R1', 'R2', 'R3', 'R5'], None, 15, 'Evaluate',
             'evaluation plan for a directed-writing task: ideas from both texts, each judged, the writer’s own position; '
             'guidance against the 15-mark reading table')
            for t in range(3)]
P['2.2'] = [('writing_task', t, ['A', 'B'], ['R1', 'R2', 'R3', 'R5', 'W1', 'W2', 'W3', 'W4', 'W5'], None, 40, 'Create',
             'directed writing, about 250–350 words, as a %s, with two bullets, the first asking for evaluation; '
             'model answer and guidance against both tables (writing /25, reading /15)' % f)
            for t, f in enumerate(['letter', 'speech', 'article'])]
P['2.3'] = [('writing_task', None, ['A', 'B', 'C'], ['W1', 'W2', 'W3', 'W4', 'W5'], 'Describe' if n < 2 else None, 40, 'Create',
             'descriptive composition, about 350–450 words, on an original title; a plan, the model answer, and '
             'guidance against both tables (content and structure /16, style and accuracy /24)')
            for n in range(3)]
P['2.4'] = [('writing_task', None, ['A', 'B', 'C'], ['W1', 'W2', 'W3', 'W4', 'W5'], None, 40, 'Create',
             'narrative composition, about 350–450 words, on an original title; a plan, the model answer, and '
             'guidance against both tables (content and structure /16, style and accuracy /24)')
            for n in range(3)]
P['2.5'] = ([('short_answer', None, ['C'], ['W5'], None, None, 'Apply',
              'proofreading task: an original paragraph of about 120 words with a stated number of errors of named kinds, '
              'written into the prompt; the corrected paragraph is the answer')
             for n in range(3)] +
            [('short_answer', None, ['A', 'B'], ['W3'], None, None, 'Apply',
              'rewriting task: an original flat paragraph of about 100 words, written into the prompt, to be rewritten '
              'with precise vocabulary and deliberately varied sentences; a model rewrite is the answer')
             for n in range(2)])

# ------------------------------------------------------------------------------ misconceptions
# (id, topic, objective key, source task in the examiner reports, theme, what learners do, the test that tells it apart)
MISCONCEPTIONS = [
 ('MC-0500-1.1-01', '1.1', 'A', 'P1 Q1(a-e) comprehension', 'restates in own words rather than copying',
  'copy the text’s sentence when the question asks them to explain in their own words',
  'if the key words of the answer are the text’s key words, the idea has been located, not explained'),
 ('MC-0500-1.1-02', '1.1', 'A', 'P1 Q1(a-e) comprehension', 'explains both parts of a two-part idea',
  'explain one half of a phrase that carries two ideas',
  'count the ideas in the phrase before answering; a two-mark explanation that covers one of them is half an answer'),
 ('MC-0500-1.1-03', '1.1', 'C', 'P1 Q1(a-e) comprehension', 'reads implied meaning as well as stated meaning',
  'answer an implicit question with what the text states on the surface',
  'if the question asks what a detail suggests, the answer is something the text does not say in words'),
 ('MC-0500-1.1-04', '1.1', 'B', 'P1 Q1(a-e) comprehension', 'gives only what is asked; extra material can undo a correct answer',
  'add extra material after the point, some of which contradicts or blurs it',
  'stop when the point the marks ask for is made; anything added must be another point, not a padding of this one'),
 ('MC-0500-1.1-05', '1.1', 'B', 'P1 Q1(a-e) comprehension', 'answers from the part of the text the question names',
  'give a correct idea taken from outside the paragraph the question names',
  'an idea from elsewhere in the text can be true and still not answer a question that names its paragraph'),
 ('MC-0500-1.2-01', '1.2', 'A', 'P1 Q1(f) summary', 'own words, not lifted',
  'string together the text’s own sentences and call it a summary',
  'a summary in your own words could be written by someone who had closed the book after reading it'),
 ('MC-0500-1.2-02', '1.2', 'A', 'P1 Q1(f) summary', 'selects only relevant points; no examples or excess',
  'include examples and incidental detail as if each were a separate point',
  'an example answers “like what?”; a point answers the focus. Several examples of one idea are one point'),
 ('MC-0500-1.2-03', '1.2', 'C', 'P1 Q1(f) summary', 'an overview, not a list',
  'write a list of unconnected points instead of an organised overview',
  'an overview groups and links ideas; if the sentences could be shuffled without loss, it is a list'),
 ('MC-0500-1.2-04', '1.2', 'B', 'P1 Q1(f) summary', 'no added opinion or comment',
  'add their own view or comment to the summary',
  'every sentence of a summary should be traceable to the text; a sentence that is not is comment'),
 ('MC-0500-1.2-05', '1.2', 'B', 'P1 Q1(f) summary', 'range of points; answers the focus of the question',
  'summarise the topic of the text rather than the focus the task sets',
  'test each point against the task’s exact words: on the topic is not the same as on the focus'),
 ('MC-0500-1.2-06', '1.2', 'C', 'P1 Q1(f) summary', 'concise; within the word limit',
  'explain a few ideas at length and run out of words for the rest',
  'within a word limit, the number of ideas covered rises as the words per idea fall'),
 ('MC-0500-1.3-01', '1.3', 'A', 'P1 Q2(a) word or phrase with the same meaning', 'the exact word or phrase, not extra text',
  'copy the whole sentence, or explain the meaning, when one word or phrase is asked for',
  'the answer is a word or phrase you could substitute for the given idea; a sentence cannot be substituted'),
 ('MC-0500-1.3-02', '1.3', 'B', 'P1 Q2(b) own-words meaning of single words', 'meaning in this context',
  'guess a meaning from how a word looks without checking the sentence it is in',
  'put your meaning back into the writer’s sentence; if the sentence no longer makes sense, the meaning is wrong'),
 ('MC-0500-1.3-03', '1.3', 'B', 'P1 Q2(b) own-words meaning of single words', 'own words, not the word itself',
  'repeat the word, or a form of it, in the explanation',
  'an explanation that contains the word being explained has not explained it'),
 ('MC-0500-1.4-01', '1.4', 'B', 'P1 Q2(c) one example, explain the effect', 'uses one example only',
  'discuss several examples when the task asks for one',
  'one example fully explained answers the task; three touched on do not answer it three times'),
 ('MC-0500-1.4-02', '1.4', 'C', 'P1 Q2(d) language task', 'selects precise words and phrases, not long quotations',
  'quote long stretches of text, leaving no single word examined',
  'a quotation is short enough when every word in it is one you comment on'),
 ('MC-0500-1.4-03', '1.4', 'B', 'P1 Q2(d) language task', 'explains meaning AND effect, not meaning alone',
  'explain what words mean and stop before saying what they do to the reader',
  'after the meaning, ask: so what does the reader see, feel or understand because of this word?'),
 ('MC-0500-1.4-04', '1.4', 'A', 'P1 Q2(d) language task', 'names devices without explaining them',
  'name a device and treat the label as the analysis',
  'delete the device’s name from the sentence; if nothing about meaning or effect is left, nothing was analysed'),
 ('MC-0500-1.4-05', '1.4', 'A', 'P1 Q2(d) language task', 'tackles imagery',
  'leave an image unexplained, or explain it only literally',
  'an image is explained when both the literal picture and what it suggests about the subject are given'),
 ('MC-0500-1.4-06', '1.4', 'C', 'P1 Q2(d) language task', 'covers both paragraphs, around three choices each',
  'analyse one paragraph and neglect the other',
  'count the choices per paragraph before writing; an answer on one of two paragraphs covers half the task'),
 ('MC-0500-1.4-07', '1.4', 'C', 'P1 Q2(d) language task', 'specific, not general, comment',
  'comment on the atmosphere of a whole paragraph without naming the words that create it',
  'every comment should point at a specific word or phrase; a comment that could fit any paragraph is general'),
 ('MC-0500-1.5-01', '1.5', 'A', 'P1 Q3 extended response to reading', 'covers all three bullets, evenly',
  'cover one bullet fully and another thinly or not at all',
  'the three bullets are the answer’s structure; plan a roughly equal share of the words for each'),
 ('MC-0500-1.5-02', '1.5', 'A', 'P1 Q3 extended response to reading', 'develops and evaluates ideas, not just repeats them',
  'repeat the text’s ideas without developing or inferring from them',
  'a developed point adds a why or a what-follows that the text supports but does not state'),
 ('MC-0500-1.5-03', '1.5', 'A', 'P1 Q3 extended response to reading', 'uses details from the text, not copying',
  'copy the text’s details instead of using them in their own words',
  'the details should come from the text; the sentences they sit in should be yours'),
 ('MC-0500-1.5-04', '1.5', 'A', 'P1 Q3 extended response to reading', 'stays tethered to the text; no invention',
  'invent events or feelings the text gives no grounds for',
  'every development should be traceable to something in the text; an idea with no root there is invention'),
 ('MC-0500-1.5-05', '1.5', 'C', 'P1 Q3 extended response to reading', 'convincing voice, form and register',
  'write in a register that does not fit the role or the audience',
  'ask who is speaking, to whom, and why; the register follows from those three answers'),
 ('MC-0500-2.1-01', '2.1', 'B', 'P2 Section A directed writing', 'evaluates the ideas, not just summarises them',
  'paraphrase and list the texts’ ideas as if that were evaluation',
  'an evaluated point says how convincing an idea is and why; a summarised point only says what it is'),
 ('MC-0500-2.1-02', '2.1', 'C', 'P2 Section A directed writing', 'uses both texts',
  'draw on one text and ignore the other',
  'each text should supply ideas, and each should be used to test the other'),
 ('MC-0500-2.1-03', '2.1', 'C', 'P2 Section A directed writing', 'own words, not lifting',
  'lift the texts’ sentences instead of using their ideas in their own words',
  'the ideas should come from the texts; the sentences should be yours'),
 ('MC-0500-2.2-01', '2.2', 'A', 'P2 Section A directed writing', 'structure and a line of argument',
  'follow the order of the source texts, so the argument comes out disconnected or contradictory',
  'plan by your own line of argument first, then place each source idea where the argument needs it'),
 ('MC-0500-2.2-02', '2.2', 'B', 'P2 Section A directed writing', 'form, register and audience',
  'write a letter, speech or article that reads as a general essay',
  'read the opening and closing lines alone; they should tell a reader which form this is and who it is for'),
 ('MC-0500-2.2-03', '2.2', 'A', 'P2 Section A directed writing', 'addresses both bullets',
  'handle the second bullet in a single sentence at the end',
  'the second bullet is half the task; the evaluation should lead into it, not stop short of it'),
 ('MC-0500-2.3-01', '2.3', 'A', 'P2 Section B composition', 'descriptive: images and detail, not a plot',
  'let a description turn into a story told as a sequence of events',
  'if the paragraphs are ordered by “and then”, it is narrating; a description is ordered by what is noticed'),
 ('MC-0500-2.3-02', '2.3', 'A', 'P2 Section B composition', 'vocabulary: precise, not overwritten',
  'reach for cliché or showy vocabulary in place of observed detail',
  'a precise detail could only belong to this scene; a cliché could belong to any'),
 ('MC-0500-2.4-01', '2.4', 'A', 'P2 Section B composition', 'narrative: a credible, controlled plot',
  'pack in too many events for the length, so the story has no credible shape',
  'in about 400 words one central event, developed, carries a story further than several summarised'),
 ('MC-0500-2.4-02', '2.4', 'C', 'P2 Section B composition', 'narrative: character and tension, a real ending',
  'stop the story rather than end it',
  'an ending resolves or deliberately leaves open the conflict the story set up; a stop just runs out'),
 ('MC-0500-2.5-01', '2.5', 'A', 'P2 Section B composition', 'vocabulary: precise, not overwritten',
  'use an ambitious word in a sense it does not have',
  'a less impressive word used precisely is better than an impressive one used wrongly'),
 ('MC-0500-2.5-02', '2.5', 'C', 'P2 Section B composition', 'varied, accurate sentences',
  'join two complete sentences with a comma',
  'if both sides of the comma could stand alone as sentences, a comma alone cannot join them'),
 ('MC-0500-2.5-03', '2.5', 'C', 'P2 Section B composition', 'varied, accurate sentences',
  'let the tense drift between past and present within a narrative',
  'choose the tense of the telling once, and check each verb against it'),
]

# ------------------------------------------------------------------------------------- glossary
GLOSSARY = [
 ('explicit meaning', 'What a text states in its own words.', None),
 ('implicit meaning', 'What a text suggests without stating it, which the reader works out from the details.', None),
 ('attitude', 'A view or feeling held by a writer or a person in a text, shown through what they say or do rather than named.', None),
 ('inference', 'A conclusion about implicit meaning, drawn from details the text gives.', 'An inference must be supported by the text; a personal opinion about the topic is not an inference.'),
 ('own words', 'The same idea expressed without the text’s key words or sentence structure.', 'Changing one word in a copied sentence is not using your own words.'),
 ('selective summary', 'A summary of only the ideas in a text that fit the focus a task sets.', 'Not a retelling of the whole text.'),
 ('focus', 'The exact angle a summary task asks for, such as the benefits of something or the reasons for it.', 'Distinct from the topic of the text.'),
 ('overview', 'An organised account that groups related ideas and links them, rather than listing them.', None),
 ('lifting', 'Copying stretches of the text’s own wording into an answer.', None),
 ('context', 'The sentence and passage in which a word is used, which settle its meaning.', 'In 1.3 this means the words around a word, not the historical or social context of a text.'),
 ('connotation', 'The associations a word carries beyond its literal meaning.', None),
 ('denotation', 'The literal, dictionary meaning of a word.', None),
 ('effect', 'What a writer’s language choice makes the reader see, feel or understand.', 'Distinct from the meaning of the words.'),
 ('imagery', 'Language that creates a picture or sensation in the reader’s mind, literal or figurative.', None),
 ('figurative language', 'Language that means more than, or other than, its literal sense, such as a metaphor or a simile.', None),
 ('register', 'The level of formality and the choice of language that suit an audience, a purpose and a situation.', None),
 ('voice', 'The sense of a particular person speaking, carried by what they notice, what they feel and how they say it.', None),
 ('text type', 'The form a piece of writing takes: letter, report, journal, speech, interview or article.', 'The six named by the syllabus for Paper 1 Question 3.'),
 ('evaluate', 'In directed writing, to judge how convincing, complete or consistent an idea or view is, and why.', 'Distinct from summarising or listing the ideas.'),
 ('fact', 'A statement that can be checked and shown true or false.', None),
 ('opinion', 'A statement of belief or judgement that cannot be proved true or false.', None),
 ('perspective', 'The position from which someone sees an issue, shaped by who they are and what they stand to gain or lose.', None),
 ('bias', 'A one-sided presentation that favours a view by what it selects, stresses or leaves out.', 'An opinion openly argued is not in itself bias.'),
 ('descriptive writing', 'Writing that builds a picture of a place, moment or experience from detail, not from a sequence of events.', None),
 ('narrative writing', 'Writing that tells a story: characters, a sequence of events and a shape.', None),
 ('plot', 'The sequence of connected events in a story, shaped around a conflict.', None),
 ('characterisation', 'How a writer makes a character real to the reader, through action, speech, thought and detail.', None),
 ('climax', 'The point of greatest tension in a story, where the conflict comes to a head.', None),
 ('resolution', 'How a story’s conflict is settled, or deliberately left open, after the climax.', None),
 ('comma splice', 'Two complete sentences joined by a comma alone.', None),
 ('minor sentence', 'A deliberate sentence without a main verb, used for effect.', 'Distinct from an accidental fragment.'),
]

VARIANT_REGISTER = [
 {'term': 'composition', 'variants': ['descriptive', 'narrative'],
  'consequence': 'The two kinds of title ask for different content: a picture built from detail, or a story with a shape.',
  'teach_as': 'Wherever composition is taught, say which kind is meant and what that kind needs.'},
]

CONDITIONED = [
 {'mechanism_id': 'CM-0500-SHORT-SENTENCE',
  'name': 'Short sentences create tension or emphasis',
  'rationale': 'A short sentence creates emphasis or tension by contrast with the sentences around it. Taught '
               'as a rule on its own, it produces answers that say every short sentence builds tension.',
  'asserted_when': [r'\bshort sentences?\b', r'\b(tension|suspense|emphasis|impact|drama)\b',
                    r'\b(creates?|builds?|adds?|gives?)\b'],
  'required_conditions': [{'name': 'the contrast with the surrounding sentences',
                           'any_of': [r'\bcontrast', r'\blonger\b', r'\blong sentences?\b', r'\bvar(y|ied|iety|ying)\b',
                                      r'\bafter\b', r'\bamong\b', r'\bsurround']}]},
 {'mechanism_id': 'CM-0500-FORMAL-REGISTER',
  'name': 'A formal register is the correct one',
  'rationale': 'Register is right or wrong only for an audience and a purpose. A journal entry or a speech to '
               'classmates written formally is as mismatched as a complaint to a council written casually.',
  'asserted_when': [r'\bformal\b', r'\bregister\b', r'\b(should|must|always|correct|appropriate|right)\b'],
  'required_conditions': [{'name': 'the audience or purpose that decides it',
                           'any_of': [r'\baudience\b', r'\bpurpose\b', r'\breader', r'\blistener', r'\bwho\b', r'\bsituation\b']}]},
]

# Constructs the learner does not sit (their route is components 12 and 22). The strings are scanned
# for in learner-facing text by C-11, so they are short terms, not sentences.
NOT_IN_ROUTE = ['Coursework Portfolio', 'Component 3', 'Component 4', 'Speaking and Listening']
