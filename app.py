from multiprocessing import Process, Pool, cpu_count, Queue


def multiplier(q: Queue, res_q: Queue):
    while q.qsize():
        row, line, place = q.get()
        if len(row) - len(line):
            raise ValueError
        res_q.put((place, sum([row[i] * line[i] for i in range(len(row))])))


if __name__ == '__main__':
    matrix = ((1, 2, 3),
              (4, 5, 6))
    another_matrix = ((1, 3),
                      (4, 6),
                      (7, 9))

    q = Queue()
    res_q = Queue()
    for i in range(len(matrix)):
        for j in range(len(another_matrix[0])):
            q.put((matrix[i], [another_matrix[x][j] for x in range(len(another_matrix))], (i, j)))

    res = [[[] for _ in range(len(matrix))] for __ in range(len(matrix))]
    processes = [Process(target=multiplier, args=(q, res_q)) for _ in range(2)]
    [i.start() for i in processes]
    [i.join() for i in processes]
    for i in range(res_q.qsize()):
        place, res_c = res_q.get()
        res[place[0]][place[1]] = res_c

    print(res)
