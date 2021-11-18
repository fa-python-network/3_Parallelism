import multiprocessing
from multiprocessing import Process
from ref import *
import logging
import os
import psutil





res = 0

def element(index, A, B, conn):
    global res

    i, j = index
    res = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    conn.send(res)



if __name__ == '__main__':
    global v
    global p1
    if v == 3:
        inds = [(0, 0), (0, 1),(1, 0),(1, 1)]
    elif v == 4:
       inds = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    procs = []
    res = 0
    fin = []

    l_end, r_end = multiprocessing.Pipe()

    for index, number in enumerate(inds):
        p1 = Process(target=element, args=(number, mat1, mat2, r_end))
        procs.append(p1)
        p1.start()
        res = l_end.recv()
        fin.append(res)
        logging.basicConfig(filename='/Users/Aram/Desktop/matrx.log', level=logging.INFO,
                            format='%(asctime)s - %(message)s')

        logging.info(f'{res}')


    for p1 in procs:
        p1.join()


    sp = []

    for i in range(0, len(fin), n):
            sp.append(fin[i:i + n])

    print(sp)
    f1 = open('neww.txt', 'w')
    f1.write(str(sp))



