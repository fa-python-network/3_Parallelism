from multiprocessing import Process, Pool


def element(index, A, B, res):
    global d
    i, j = index
    b=[]
    # get a middle dimension
    N = len(A[0]) or len(B)
    print (N)
    for k in range(N):
        res += A[i][k] * B[k][j]
        print (res)
    return ''


if __name__ == '__main__':
    res = 0
    m1 = open('matrix1.txt', 'r')
    matrix1 = []
    for line in m1.readlines():
        cut = line.find('\n')
        if cut != -1:
            c = line[:cut]
            l = c.split(' ')
            result = [int(item) for item in l]
            matrix1.append(result)
        else:
            a = line.split(' ')
            result = [int(item) for item in a]
            matrix1.append(result)
    m1.close()
    m1 = open('matrix1.txt', 'r')
    mm = len(m1.readline().split(' '))
    m1.close()
    m2 = open('matrix2.txt', 'r')
    matrix2 = []
    for line in m2.readlines():
        cut = line.find('\n')
        if cut != -1:
            c=line[:cut]
            l = c.split(' ')
            result = [int(item) for item in l]
            matrix2.append(result)

        else:
            li = line.split(' ')
            result = [int(item) for item in li]
            matrix2.append(result)
    m2.close()
    m2 = open('matrix2.txt', 'r')
    mn = len(m2.readline().split(' '))
    m2.close()
    print (matrix1, len(matrix1), mm)

    print (matrix2, len(matrix2), mn)

    d = 0

    p1 = Process(target=element, args=[(0, 0), matrix1, matrix2, res])
    p1.start()
    p1.join()

