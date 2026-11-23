"""Part-level award/demand alignment for connected selected Cambridge items.

Each tuple is original label, question PDF page, marks, response, direct demands.
NSSCO geometry components remain explicit prior assessment, not AS coverage.
"""
PARTS={
 ('9709_s15_qp_13',8):[
  ('i',3,3,'symbolic','1.8.2.1 1.8.2.2'),('ii',3,1,'explanation','1.8.3.2')],
 ('9709_s17_qp_11',2):[
  ('i',3,2,'numeric','1.7.4.2 1.7.5.2'),
  ('ii',3,4,'symbolic','1.7.2.1 1.7.2.2 1.7.3.1 1.7.3.2 1.7.4.1')],
 ('9709_m16_qp_12',9):[
  ('a.i',4,2,'proof/show-that','NSSCO.circle-geometry'),
  ('a.ii',4,2,'symbolic','1.5.2.2 1.5.2.3')],
 ('9709_w16_qp_12',6):[
  ('i',2,2,'proof/show-that','NSSCO.right-triangle-trig'),
  ('ii',2,3,'numeric','1.5.2.1'),('iii',2,3,'numeric','1.5.2.2 1.5.2.3')],
 ('9709_w22_qp_11',5):[
  ('a',6,4,'numeric','1.5.2.1'),('b',7,2,'numeric','1.5.2.2 1.5.2.3')],
 ('9709_m16_qp_12',7):[
  ('i',3,2,'proof/show-that','1.7.1.1 1.7.1.2 1.7.2.2 1.7.2.3 1.7.3.2 1.7.4.1'),
  ('ii',3,2,'symbolic','1.7.2.1 1.7.3.2 1.7.3.3'),
  ('iii',3,4,'numeric','1.7.4.1 1.7.4.2 1.7.5.1')],
 ('9709_w21_qp_22',6):[
  ('a',8,2,'sketch','2.2.2.2 2.6.1.1'),('b',8,2,'proof/show-that','2.6.1.2'),
  ('c',9,1,'proof/show-that','2.2.2.1 2.6.3.1 2.6.3.2'),('d',9,3,'numeric','2.6.2.1 2.6.4.1 2.6.4.2')],
}
