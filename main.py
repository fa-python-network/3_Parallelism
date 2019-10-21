
from multiprocessing import Process, Pool

matrix_1=[]

with open('matrix_1.txt','r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            matrix_1.append([int(n) for n in line.split()])
    print('First matrix: ')
    print(matrix_1)

matrix_2=[]

with open('matrix_2.txt','r') as f2:
    for line in f2:
        line = line.strip()
        if len(line) > 0:
            matrix_2.append([int(n) for n in line.split()])
    print('Second matrix: ')
    print(matrix_2)



def element(index):
    global A
    global B
    #A, B = matrix_1, matrix_2
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


A, B = matrix_1, matrix_2
pool = Pool(processes = 2)

matr = pool.map( element , [(i, j) for i in range (len(A[0])-1) for j in range (len(B)-1)])

res=[]
for i in range(len (A[0])-1):
    res.append([])
    for j in range(len(B)-1):
        res[-1].append(matr[0])
        matr.remove(matr[0])
print(res)
        


with open('res.txt','w') as f3:
    f3.write(str(res))

#write_res(res)





