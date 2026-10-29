"""Semantic decisions after reading all 772 card prompts/rubrics and 236 parts.
Selections are review decisions, not predicates on Bloom labels. Partial values count
separable recall credit; full-credit conservative decisions cover inseparable mixtures.
"""
# Every actual DEF/FEATURE card in the reviewed snapshot asks for familiar factual content;
# count all its credit conservatively, including occasional explanatory second points.
# Actual subtype, not the legacy ID suffix, was reviewed.
ADDITIONAL={
1:'013 040 046 050 057 059 061 063 065 071',
2:'026 055 058 065 079 080 111 112 113 114 115 116 117 118 119 120 137 138 139',
3:'015 034',5:'009 028',6:'001 008',7:'005 006 014 018 032 051',
8:'001 002 003 005 007 009 011 012 013 014 016 022 024 025 026 027 028 029 030 031 032 033 035 036 040 042 044 046 048',
9:'001 003 005 021 023 027 029 031',
10:'028 029 031 035 042 044 045 053 055 057 066 072 073 074',
11:'013 015 016 026 033 034 035 039 068 072 074 077',12:'001 007 011 019 029'}
MECH={2:'077 087 134',5:'002 008 019',6:'004 006 023 029',7:'003 008 013 015 017 021 023',10:'021 027 041 048',11:'058 061'}
PART_RECALL={
1:{'P01:6':1,'P01:9':1,'P02:a':1,'P03:b':2},
2:{'P01:1':1,'P01:3':1,'P01:8':1,'P01:10':1,'P01:12':1,'P02:b':2},
3:{'P01:6':1,'P01:10':1,'P01:12':1,'P02:credit-group-1':2,'P02:credit-group-2':1},
4:{'P01:1':1,'P01:2':1,'P01:3':1,'P01:4':1,'P01:5':1,'P01:6':1,'P02:a':1,'P03:a':1,'P04:a':1},
5:{'P01:1':1,'P01:3':1,'P01:6':1,'P01:8':1,'P01:10':1,'P01:11':1,'P02:a':1,'P02:b':2,'P03:a':3,'P03:b':2,'P03:c':1,'P03:d':2},
6:{'P01:1':1,'P01:2':1,'P01:6':1,'P01:8':1,'P01:9':1,'P01:12':1,'P02:a':1,'P03:c':1,'P04:a':1},
7:{'P01:1':1,'P01:4':1,'P01:5':1,'P01:11':1,'P01:12':1,'P02:credit-group-1':2,'P03:a':3},
8:{**{f'P01:{n}':1 for n in [1,4,5,6,8,10,11,12]},'P02:a':1,'P02:b':2,'P02:c':1,'P03:e':2},
9:{**{f'P01:{n}':1 for n in [2,3,4,5,6,11,12]},'P02:a':1},
10:{'P01:3':1,'P01:7':1,'P01:8':1,'P01:11':1,'P02:a':1,'P02:b':2,'P02:c':2},
11:{'P01:2':1,'P01:6':1,'P01:9':1,'P01:10':1,'P01:11':1,'P02:credit-group-1':2,'P02:credit-group-2':1},
12:{'P01:c':1}}
PARTIAL_CARDS={ '2-034':2,'2-062':1,'3-038':1,'5-030':1,'8-020':1,'8-038':1,'11-028':2,'11-037':1,'11-059':1,'12-013':1 }

MIXED_CREDIT_DETAILS={'ITEM-6117-2-034-FEATURE': 'Recall: isotope definition and known contrasting nuclear stability (2). Non-recall: explaining that isotope is broader than radioactive isotope (1).', 'ITEM-6117-2-062-MECH': 'Recall: helium is non-flammable (1). Non-recall: link lower density to balloon lift (1).', 'ITEM-6117-3-038-LIM': 'Recall: soap forms scum in hard water (1). Non-recall: link soap loss to reduced cleaning efficiency (1).', 'ITEM-6117-5-030-APP': 'Recall: name concentrated aqueous NaCl as the feed (1). Non-recall: explain why water is needed for hydroxide formation (1).', 'ITEM-6117-11-028-LIM': 'Conservatively count familiar health and crop consequences (2); the proposed practical response requires a feasible response to the stated shortage (1).', 'ITEM-6117-11-059-LIM': 'Recall: removing leaded fuel removes that lead source (1). Non-recall: connect this to toxicity and explain the remaining pollution limitation (2).', 'ITEM-6117-3-P02:credit-group-2': 'Recall: biodegradation means microbial breakdown (1). Non-recall: link breakdown to persistence under suitable conditions (1).', 'ITEM-6117-5-P03:b': 'Recall: glowing-splint test and relighting observation (2). Non-recall: choose collection that avoids air contamination or mixing gases (1).', 'ITEM-6117-8-P02:c': 'Conservatively count stating the familiar relighting observation (1), even though the prompt mentions it. Credit linking oxygen to combustion separately as understanding (1).', 'ITEM-6117-11-P02:credit-group-2': 'Recall: SO2 is an acidic oxide (1). Non-recall: connect acid formation in atmospheric water to lower rain pH (1).'}
