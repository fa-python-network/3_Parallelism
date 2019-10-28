import os
from multiprocessing import Pool

c =[]
 
mat1=[]
mat2=[]
with open ('matrix1.txt', 'r') as matrix1:
	for i,line in enumerate(matrix1):
		mat1.append([])
		for k in (line.split()):
				mat1[i].append(int(k))

with open ('matrix2.txt', 'r') as matrix2:
	for i,line in enumerate(matrix2):
		mat2.append([])
		for k in (line.split()):
				mat2[i].append(int(k))

n1=len(mat1)

n = n1*n1

print(n)
print(mat1)
print(mat2)

open('promez.txt','w').close()

def q(k):
	with open('promez.txt', 'a') as file:
		l=0
		for i in range(len(mat1[0])):
			l+=mat1[k//n1][i]*mat2[i][k%n1]
		print(l, os.getpid())
		file.write(str(l)+' ')
		return(l)
		
    
    
for i in range(n):
	c.append(i)
print(c)
pool = Pool(processes=5)
h=(pool.map(q,c))

with open('promez.txt', 'r') as file2:
	for line in file2:
		o = line.split(' ')
		rez=''
		for i in range(n1):
			for j in range(n1):
				rez= rez + o[j+i*n1] + ' '
			rez+='\n'
with open ('matrix3.txt', 'w') as matrix3:
		matrix3.write(rez)