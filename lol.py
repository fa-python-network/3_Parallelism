from multiprocessing import Process, Manager, Queue


def element(i: int, j: int, A: list, B: list, answer: Queue):
    answer.put((sum(A[i][k] * B[k][j] for k in range(len(A[0]) or len(B))), [i, j]))


if __name__ == '__main__':
    manager = Manager()

    n1 = int(input('Введите число элементов в строке'))
    n2 = int(input('Введите число строк в матрице'))
    matrix1 = [[[] for i in range(n1)] for j in range(n2)]
    matrix1 = [[0 for i in range(n1)] for j in range(n2)]

    n1 = int(input('Введите число элементов в строке'))
    n2 = int(input('Введите число строк в матрице'))
    matrix2 = [[[] for i in range(n1)] for j in range(n2)]
    matrix2 = [[0 for i in range(n1)] for j in range(n2)]

    lol1 = []
    lol2 = []
    k = 0
    kk = 0
    with open('matrix1.txt', 'r') as m1:
        for line in m1.read():
            if line != '[' and line != ']' and line != ',' and line != '\n' and line != ' ':
                lol1 += line
    with open('matrix2.txt', 'r') as m2:
        for line in m2.read():
            if line != '[' and line != ']' and line != ',' and line != '\n' and line != ' ':
                lol2 += line

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            try:
                matrix1[i][j] = int(lol1[k])
                k += 1
            except:
                if k <= len(lol1):
                    i = k
                    k += 1
    print(matrix1)

    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            try:
                matrix2[i][j] = int(lol2[kk])
                kk += 1
            except:
                if kk <= len(lol2):
                    i = kk
                    kk += 1
    print(matrix2)


    matrix3 = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix2[0]))]

    processes = list()
    answer = manager.Queue()

    for i in range(len(matrix3)):
        for j in range(len(matrix3[i])):
            p = Process(target=element, args=(i, j, matrix1, matrix2, answer, ))
            processes.append(p)

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    for i in range(len(matrix3)):
        for j in range(len(matrix3[i])):
            lol, kek = answer.get()
            matrix3[kek[0]][kek[1]] = lol
    with open('matrix3.txt', 'w') as file:
        file.write(str(matrix3))
    print(matrix3)
# 8 15
# 7 13
