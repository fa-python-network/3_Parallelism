from multiprocessing import Process, Pool

A = []
B = []
project_path = '/Users/alexandr/PycharmProjects/fa-parallelism/'


def open_file(array, path):
    with open(path, 'r') as filehandle:
        for line in filehandle:
            if '\n' in line:
                line = line[:-1]
            array.append(line.split(','))


def write_file(array, path):
    with open(path, "w") as txt_file:
        for item in array:
            txt_file.write("{} ".format(str(item)) + "\n")


open_file(A, project_path + 'Array A.txt')
open_file(B, project_path + 'Array B.txt')

ai, aj, bi, bj = len(A), len(A[0]), len(B), len(B[0])
C = [[0 for j in range(bj)] for i in range(ai)]


def calculate(index):
    i, j = index
    res = 0
    for k in range(len(A[0])):
        res += A[i][k] * B[k][j]
    C[i][j] = int(res)
    return C


if aj != bi:
    print("Умножение невозможно")
    exit(1)

for i in range(ai):
    for j in range(aj):
        A[i][j] = int(A[i][j])

for i in range(bi):
    for j in range(bj):
        B[i][j] = int(B[i][j])

if __name__ == '__main__':
    pool = Pool(4)
    result = pool.map(calculate, [(0, 0), (0, 1), (1, 0), (1, 1)])
    write_file(result[ai + 1], project_path + "Result.txt")
