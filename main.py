from multiprocessing import Pool
import json
import numpy as np



def element(args):
    index, A, B = args[0], args[1], args[2]
    i, j = index
    res = 0
    N = A.shape[1] or B.shape[0]
    for k in range(N):
        res += A[i, k] * B[k, j]
    return res


def generate_map(matrix1, matrix2):
    args = []
    for i in range(matrix1.shape[0]):
        for j in range(matrix2.shape[1]):
            args.append(((i, j), matrix1, matrix2))
    return args


def to_file(matrix, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in matrix:
            for digit in line:
                f.write(f'{digit}\t')
            f.write('\n')


if __name__ == "__main__":
    with open('matrix1.json', encoding='utf-8') as f:
        matrix1 = np.matrix(json.load(f))

    with open('matrix2.json', encoding='utf-8') as f:
        matrix2 = np.matrix(json.load(f))

    p = Pool(matrix1.shape[0] * matrix2.shape[1])
    args = generate_map(matrix1, matrix2)
    result = np.array(p.map(element, args))
    matrix = result.reshape(matrix1.shape[0], matrix2.shape[1])
    print(matrix)
    to_file(matrix, 'result.txt')
