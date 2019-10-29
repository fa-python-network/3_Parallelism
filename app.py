import json
from multiprocessing import Pool, cpu_count


def multiplier(params):
    row, line, place = params
    if len(row) - len(line):
        raise ValueError
    return place, sum([row[i] * line[i] for i in range(len(row))])


if __name__ == '__main__':
    with open('matrix.json') as j_file:
        both_matrix = json.load(j_file)
    matrix, another_matrix = both_matrix['one'], both_matrix['two']

    q = []
    for i in range(len(matrix)):
        for j in range(len(another_matrix[0])):
            q.append((matrix[i], [another_matrix[x][j] for x in range(len(another_matrix))], (i, j)))

    res = [[[] for _ in range(len(matrix))] for __ in range(len(matrix))]

    processes_pool = Pool(cpu_count())
    results = processes_pool.map(multiplier, q)
    for i in results:
        place, res_c = i
        res[place[0]][place[1]] = res_c

    print(res)
