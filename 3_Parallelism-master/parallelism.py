from multiprocessing import Process, cpu_count, Queue


def umnoj(q, res_q):
    while q.qsize():
        row, line, place = q.get()
        if len(row) - len(line):
            raise ValueError
        else:
            res_q.put((place, sum([row[i] * line[i] for i in range(len(row))])))

if __name__ == '__main__':
    matrix1 = ((1, 2, 3, 4),
              (5, 6, 7, 8))
    matrix2 = ((1, 3),
               (4, 6),
                (7, 9),
                (11, 13))

    q = Queue()
    res_q = Queue()
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            q.put([matrix1[i], [matrix2[x][j] for x in range(len(matrix2))], [i, j]])

    res = [[ [] for i in range(len(matrix1))] for j in range(len(matrix1))]

    processes = [Process(target = umnoj, args=(q, res_q)) for i in range(2)]
    [i.start() for i in processes]
    [i.join() for i in processes]
    for i in range(res_q.qsize()):
        place, res_prom= res_q.get()
        res[place[0]][place[1]] = res_prom

    print(res)
	
#nikitin
