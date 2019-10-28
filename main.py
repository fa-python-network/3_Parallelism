import numpy as np
from multiprocessing import Process, Pool

m1=[]
with open("matrix.txt") as f:
	for line in f:
		m1.append([int(x) for x in line.split()])

m2=[]
with open("matrix2.txt") as f:
	for line in f:
		m2.append([int(x) for x in line.split()])
print(m1)
print(m2)
m3=[]
r1=len(m1)
c1=len(m1[0])
r2=c1
c2=len(m2[0])
def proizvedenie(m1,m2):
    k=0
    d=[]
    c=[]
    for z in range(0,r1):
        for j in range(0,c2):
            for i in range(0,c1):
                k=k+m1[z][i]*m2[i][j]
            d.append(k)
            k=0
        c.append(d)
        d=[]    
    return c
m3 = proizvedenie(m1,m2)

print(m3)
    
    