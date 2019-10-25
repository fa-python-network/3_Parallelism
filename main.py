from multiprocessing import Process, Pool


def forpotok(matrix1, matrix2, ind):
    res = []
    for k in range(0, len(matrix2[0])):
        res.append(element((ind, k), matrix1, matrix2))
    with open ('and.json', 'r') as file:
        mat = json.load(file)
        mat[ind] = res
    with open('and.json', 'a') as file:):
        


def element(index, A, B):
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


if __name__ == '__main__':
    matrix1 = [[2, 0, 1],
               [1, 2, 5]]
    matrix2 = [[1, 2],
               [3, 4],
               [3, 4]]
    procs = []
    an = [[] for i in range(len(matrix1))]

    for i in range(0, len(matrix1)):
        proc = Process(target=forpotok, args=(matrix1, matrix2, i))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    print(an)
