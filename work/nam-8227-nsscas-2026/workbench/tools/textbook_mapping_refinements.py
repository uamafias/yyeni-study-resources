"""R3 second author pass: minimum direct demands, never a union of group topics.

Used after compact input expansion. Missing secondary links are not full coverage;
prerequisites and solution sophistication must not inflate directly assessed counts.
"""
# book | chapter or exercise | set (Goldie '-') | items | replacement direct aliases
REFINEMENTS = r'''
Goldie|1B|-|6|2.1.4.2,1.3.5.1
Goldie|1B|-|17,19-20|2.1.4.2,2.1.4.3
Goldie|2A|-|3-5|2.2.2.1
Goldie|2A|-|3,5|2.2.2.1,2.2.2.2
Goldie|2B|-|20|2.1.4.2,2.1.4.4,2.2.3.1
Goldie|2D|-|8|2.2.1.1,2.2.1.2
Goldie|3B|-|6|2.3.2.2,2.3.2.5
Goldie|3B|-|11|2.3.2.1,2.3.2.2,2.3.2.5
Goldie|3C|-|5,7|2.3.2.3,2.3.2.5
Goldie|3C|-|8|2.3.2.2,2.3.2.5
Goldie|3C|-|10|2.3.2.2,2.3.2.3,2.3.2.5
Goldie|3C|-|11-12|2.3.1.1,2.3.2.3,1.6.6.1,1.6.6.2
Goldie|3D|-|9|2.3.2.4,1.6.2.3
Goldie|4A|-|3|2.4.2.1,1.8.4.1,1.8.4.2,1.3.5.1
Goldie|4A|-|4|2.4.2.2,1.8.3.1,1.8.4.1,1.3.5.1
Goldie|4A|-|8|1.8.2.2,2.4.2.1,1.8.4.1,2.4.3.3
Goldie|4B|-|4-5|2.4.1.1,2.4.2.1,1.8.4.1
Goldie|4C|-|4|2.4.1.2
Goldie|4C|-|9|2.4.1.1,2.4.1.2
Goldie|4C|-|10|2.4.1.1,1.8.4.1,1.8.4.2
Goldie|4D|-|9|2.4.3.1,2.4.3.3
Goldie|4D|-|11|2.4.3.1,1.8.3.1
Goldie|4D|-|12|2.4.3.1,1.8.4.1
Goldie|4E|-|2-4|2.4.3.2,2.4.3.3,1.8.3.1
Goldie|4E|-|10|2.4.3.2,2.3.2.2
Goldie|4E|-|12,14|2.4.3.2,2.3.2.3
Goldie|4E|-|11|2.4.3.2,2.4.3.3
Goldie|5B|-|1|2.5.1.2
Goldie|5B|-|3|2.5.2.1,2.5.1.2,1.9.3.1
Goldie|5B|-|11|2.3.2.3,2.5.2.1,1.9.3.1
Goldie|6A|-|2,4-5|2.6.1.2
Goldie|6B|-|1,3|2.6.1.2,2.6.4.1,2.6.4.2
Goldie|6B|-|14|2.6.1.2,2.6.4.1,2.6.4.2
Goldie|10C|-|1,3|1.7.4.2,1.7.5.1
Goldie|10C|-|2|1.7.4.2,1.7.5.2
Goldie|10C|-|7|1.7.4.2,1.7.3.1,1.7.4.1
Goldie|10C|-|9|1.7.4.2,1.7.5.1,1.7.4.1
YM|1|Exercise 1|2|1.1.4.2,1.1.4.3
YM|1|Exercise 1|3|2.1.4.2,2.1.4.3,2.1.4.4
YM|1|Exercise 1|16|1.4.2.1
YM|1|Exercise 1|21|1.4.1.1
YM|2|Exercise 2.2|2|
YM|3|Exercise 3.1|4|1.3.2.2,1.3.3.1,1.3.4.1
YM|4|Revision Exercise 4|2|1.2.3.1,1.2.3.2,1.2.5.2,1.6.5.2,1.6.6.1
YM|4|Exercise 4.2|2|1.6.1.1,1.6.2.3,2.6.1.1
YM|4|Exercise 4.2|8|1.6.5.1
YM|5|Exercise 5|2|1.7.4.2,1.7.5.1,1.7.5.2
YM|6|Try Now|37|1.8.3.1
YM|6|Exercise 6|1|1.8.2.1
YM|6|Exercise 6|8|1.8.4.1,1.8.4.2
YM|7|Exercise 7|9|1.1.4.1,1.1.4.2,1.1.4.3,1.9.1.2,1.9.2.1,1.9.2.2
YM|8|Revision Exercise 8|5|1.1.3.2,2.1.3.3,2.1.4.2
YM|8|Revision Exercise 8|6|2.1.4.2,2.1.4.3,1.1.2.2
YM|8|Exercise 8|12|2.1.3.2,2.1.3.3
YM|8|Exercise 8|14|2.1.4.2,2.1.4.3
YM|8|Exercise 8|15|2.1.4.1,2.1.4.4
YM|8|Exercise 8|16|2.1.4.1,2.1.4.3
YM|8|Exercise 8|17|2.1.4.1,2.1.4.2,2.1.4.4
YM|8|Exercise 8|18|2.1.4.2,2.1.4.3,2.1.4.4,1.6.6.1,1.6.6.2
YM|9|Try Now 35|2|2.2.1.2,2.2.3.1
YM|9|Exercise 9|1-2|2.2.1.2
YM|9|Exercise 9|3-4|2.2.1.1
YM|9|Exercise 9|9|2.2.1.2
YM|12|Exercise 12|2|2.5.1.2,1.9.3.1
'''
SKETCH_OVERRIDES={('Goldie','2A','-',4):False}
NOTE_OVERRIDES={('YM','7','Exercise 7',9):"First derivative f'(x), not f''(x), is supplied: solve 3sqrt(x)-2/sqrt(x)=-1, then integrate once and use the point. Source inspected at larger scale to settle prime and half-power notation."}
REFINEMENTS += r'''
YM|2|Try Now 2|1|1.2.3.2
YM|5|Try Now 7|2|1.7.3.2
YM|5|Try Now 7|3|1.7.2.1
YM|6|Try Now 31|3|1.8.4.1
YM|6|Try Now 35|3|1.8.4.1
YM|7|Try Now 34|2|1.9.4.1,1.9.4.2
'''
REPRESENTATION_OVERRIDES={('YM','1','Try Now 36',1):'text'}

# R4 item-specific corrections, checked on rendered question pages.
REFINEMENTS += r'''
Goldie|1B|-|17|2.1.3.1,2.1.4.2,2.1.4.3
Goldie|3C|-|6|1.6.2.3,2.3.2.1,2.3.2.3,1.6.6.1,1.6.6.2
Goldie|4A|-|2|2.4.2.2,1.8.4.1
Goldie|4A|-|8|1.8.2.2,2.4.2.1,1.8.4.1
YM|7|Exercise 7|1|1.9.1.1,1.9.1.2
YM|13|Try Now 5|2|2.6.1.1,2.6.1.2,2.6.4.1,2.6.4.2
YM|4|Try Now 55|3|1.3.2.2,1.3.3.2,1.6.2.2
YM|6|Try Now 15|2|1.8.2.2,1.8.3.1
'''
NOTE_OVERRIDES.update({
 ('YM','3','Example',15):'Piecewise line/reciprocal inverse and domains. Valid original; QUAL01 is specific to modulus graphs and does not apply.',
 ('YM','3','Try Now',15):'Piecewise quadratic/line graph and range. Valid original; range answer uses wrong variable in PDF600; QUAL01 does not apply.',
 ('YM','4','Exercise 4.2',3):'Part(a) establishes a trigonometric equation in cosine; part(b) lacks specified finite interval, so requires a bounded adaptation.',
 ('YM','7','Try Now',27):'Three simple improper integrals. In(c) upper bound is infinity, integral1/30. Key(a) sign is wrong; see recorded correction.',
 ('YM','8','Exercise 8',7):'Remainder theorem with degree-five polynomial. LIMIT05 division-domain limit does not exclude remainder evaluation; calibration caution only.'
})

REFINEMENTS += r'''
YM|3|Example|22|1.4.2.1,1.4.2.2,1.1.2.1,1.1.2.2,1.1.2.3
'''
