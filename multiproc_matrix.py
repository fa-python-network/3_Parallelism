from random import randint as ri
import multiprocessing as mp
from time import time


def element(index, A, B):
    global res
    i, j = index
    res = 0
    N = len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


res = 0
R = []

mat1 = [
    [ri(1, 10), ri(1, 10), ri(1, 10)],
    [ri(1, 10), ri(1, 10), ri(1, 10)],
    [ri(1, 10), ri(1, 10), ri(1, 10)]
]

mat2 = [
    [ri(1, 10), ri(1, 10), ri(1, 10)],
    [ri(1, 10), ri(1, 10), ri(1, 10)],
    [ri(1, 10), ri(1, 10), ri(1, 10)]
]

begin = time()

if __name__ == '__main__':
    pool = mp.Pool()
    for str_i in range(len(mat1)):
        cur_line = []
        for col_i in range(len(mat2[0])):
            cur_elem = pool.starmap(element, [[(str_i, col_i), mat1, mat2]])[0]
            cur_line.append(cur_elem)
        R.append(cur_line)

    print("\nR(esult) = ")
    for z in range(len(R)):
        print(R[z])
    pool.close()

end = time()
print(end-begin)
