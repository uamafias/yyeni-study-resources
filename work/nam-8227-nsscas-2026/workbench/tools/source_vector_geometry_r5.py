"""Fixed-source named-point arithmetic for a textbook cuboid/prism."""
import sympy as sp

def named_locations(points,target):
 assert all(len(point)==len(target)for point in points.values())
 return sp.FiniteSet(*(sp.Symbol(name)for name,point in points.items()if all(sp.simplify(v-w)==0 for v,w in zip(point,target))))

def named_displacements(points,target):
 """Return every ordered labelled displacement,from independent coordinates."""
 dimension=len(target)
 assert all(len(name)==1 and len(point)==dimension for name,point in points.items())
 found=[]
 for tail,a in points.items():
  for head,b in points.items():
   if all(sp.simplify(v-u-w)==0 for u,v,w in zip(a,b,target)):
    found.append(sp.Symbol(tail+head))
 return sp.FiniteSet(*found)

def regular_hexagon_prism():
 """An independent exact Cartesian realisation,not printed p/q answer lists."""
 root=sp.sqrt(3)
 front={'A':(0,0,0),'B':(sp.Rational(1,2),root/2,0),'C':(sp.Rational(3,2),root/2,0),'D':(2,0,0),'E':(sp.Rational(3,2),-root/2,0),'F':(sp.Rational(1,2),-root/2,0)}
 # A non-orthogonal extrusion checks that no perpendicularity to the face is
 # accidentally needed for these vector identities.
 extrusion=sp.Matrix([sp.Rational(1,3),sp.Rational(-2,5),2])
 points={k:sp.Matrix(v)for k,v in front.items()}
 for back,face in [('G','B'),('H','C'),('I','D'),('J','E')]:points[back]=points[face]+extrusion
 basis=sp.Matrix.hstack(points['B']-points['A'],points['C']-points['B'],extrusion)
 assert basis.det()!=0
 return points,basis
