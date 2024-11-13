from itertools import*
def Func(x,y,z,w):
    return (not(x<=w)) or (y==z) or y

 for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
     t = {(a1,1,a2,0), (a3,0,1,a4), (a5,a6,0,a7)}
     for j in permutations('xyzw'):
         if [Func(**dict(zip(j,r))) for r in t] == [0,0,0]:
             print(*j)


def Func1(x,y,z,w):
    return not(y<=x) or (z<=w) or not(z)

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
     t = {(a1,0,a2,a3), (0,1,a4,a5), (1,a6,a7,0)}
     for j in permutations('xyzw'):
         if [Func1(**dict(zip(j,r))) for r in t] == [0,0,0]:
             print(*j)

def Func2(x,y,z,w):
    return (x and not(y)) or (y==z) or not(w)

for a1,a2,a3,a4 in product([0,1], repeat=4):
     t = {(0,a1,a2,0), (0,1,0,1), (a3,1,0,a4)}
     for j in permutations('xyzw'):
         if [Func2(**dict(zip(j,r))) for r in t] == [0,0,0]:
             print(*j)

def Func3(x,y,z,w):
    return ((x<=(z==w))) or not(y<=w)

for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
     t = {(a1,1,a2,a3), (0,a4,0,a5), (a6,0,0,a7)}
     for j in permutations('xyzw'):
         if [Func3(**dict(zip(j,r))) for r in t] == [0,0,0]:
             print(*j)
