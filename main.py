import threading
from multiprocessing import Pool

def f(vector1):
    sum = 0
    for p in range(len(vector1[0])):
        sum = sum + vector1[0][p] * vector1[1][p]
    return (vector1[2], vector1[3], sum)

i = int(input('Введите кол во строк: '))
j = int(input('Введите кол во сталбцов: '))

mat1 = []
mat2 = []
procs = []

newmat = []
maaap = []
print('Матрица 1')
for g in range(i):
    mat1.append(list(map(int, input('введите строку №' + str(g) +' матрицы через пробел: ').split())))
    newmat.append([])
    for e in range(i):
        newmat[g].append(0)

print('Матрица 2')
for g in range(j):
    mat2.append(list(map(int, input('введите строку №' + str(g) +' матрицы через пробел: ').split())))

for g in range(i):
    for r in range(i):
        vect = []
        for b in range(j):
            vect.append(mat2[b][r])

        maaap.append([mat1[g], vect, g, r])

pool = Pool(len(maaap))

a = list(pool.map(f, maaap))

for n in a:
    newmat[n[0]][n[1]] = n[2]

print(newmat)
