def element(index, A, B):
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[2, 0], [1, 2]]

print(element((1, 0), matrix1, matrix2))


import numpy as np  
 
a = np.random.randint(0, 100, (2, 2, 2))
b = np.random.randint(0, 100, (2, 2, 2))
print('a==', a)
print('b==', b)

from itertools import starmap
from operator import mul
 
A = a
B = b
 
def matrixmul(A, B):
 
    if len(B) != len(A[0]):
        print("Облом!")
        return
 
    tmp = tuple(zip(*B))
 
    for row in A:
        yield [sum(starmap(mul, zip(row, column))) for column in tmp]
 
if "__main__" == __name__:
    print(list(matrixmul(A, B)))
