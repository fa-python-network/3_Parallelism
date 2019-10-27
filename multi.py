import os
from multiprocessing import Pool

c =[]

n1 = int(input('Введите количество строк в 1 матрице: '))
m1 = int(input('Введите количество столбцов в 1 матрице: '))
n2 = int(input('Введите количество строк во 2 матрице: '))
m2 = int(input('Введите количество столбцов во 2 матрице: '))
 
mat1 = [[int(input('элементы 1 матрицы ')) for i in range(m1)] for j in range(n1)]
mat2 = [[int(input('элементы 2 матрицы ')) for k in range(m2)] for l in range(n2)]

n = n1*m2
print(n)
print(mat1)
print(mat2)

def q(k):
	l=0
	for i in range(m1):
		l+=mat1[k//n1][i]*mat2[i][k%n1]
	print(l, os.getpid())
	return(l)
	
    
    
for i in range(n):
	c.append(i)
print(c)
pool = Pool(processes=5)
h=(pool.map(q,c))
o=[]
print(n1)
print(h)
for i in range(n1):
	o.append([])
	for j in range(n1):
		o[i].append(h[j+i*n1])

print(o)
