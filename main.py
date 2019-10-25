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


def generate_map(matrix1, matrix2):
    args = []
    for i in range(matrix1.shape[0]):
        for j in range(matrix2.shape[1]):
            args.append(((i, j), matrix1, matrix2))
    return args

def to_file(matrix, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in matrix:
            for elem in line:
                f.write(f'{elem}\t')
            f.write('\n')



if __name__ == "__main__":
    # Читаем 2 матрицы из исходных файлов
    with open('matrix1.json', encoding='utf-8') as f:
        matrix1 = np.matrix(load(f))

    with open('matrix2.json', encoding='utf-8') as f:
        matrix2 = np.matrix(load(f))

    p = Pool(matrix1.shape[0] * matrix2.shape[1])  # Определение кол-ва потоков
    args = generate_map(matrix1, matrix2)
    result = np.array(p.map(element, args))
    matrix = result.reshape(matrix1.shape[0], matrix2.shape[1])
    print(matrix)
    to_file(matrix, 'result.txt')
