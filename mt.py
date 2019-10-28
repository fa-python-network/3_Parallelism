from multiprocessing import Process, Pool
import numpy as np
from json import load, dump

def element(args):
    index, A, B = args[0], args[1], args[2]
    i, j = index
    res = 0
    N = A.shape[1] or B.shape[0]
    for k in range(N):
        res += A[i, k] * B[k, j]
    return res


def generate_map(mt1, mt2):
    args = []
    for i in range(mt1.shape[0]):
        for j in range(mt2.shape[1]):
            args.append(((i, j), mt1, mt2))
    return args



def to_file(matrix, filename):
    with open(filename, 'w') as f:
        for line in matrix:
            for elem in line:
                f.write(f'{elem}\t')
            f.write('\n')


if __name__ == "__main__":
    with open('mt1.json') as f:
        mt1 = np.matrix(load(f))

    with open('mt2.json') as f:
        mt2 = np.matrix(load(f))

    p = Pool(mt1.shape[0] * mt2.shape[1])
    args = generate_map(mt1, mt2)
    result = np.array(p.map(element, args))
    matrix = result.reshape(mt1.shape[0], mt2.shape[1])
    print(matrix)
    to_file(matrix, 'result.txt')
