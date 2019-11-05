import json
from multiprocessing import Pool, cpu_count


def multiplier(params):
    row, line, place = params
    if len(row) != len(line):
        raise ValueError
    return place, sum([row[i] * line[i] for i in range(len(row))])


if __name__ == '__main__':
    with open('matrix.json') as file:
        one_two = json.load(file)
    one, two = one_two['one'], one_two['two']
    result_matrix_size = len(one)
    lst = [(
        one[i],
        [two[x][j] for x in range(len(two))],
        (i, j)
    ) for i in range(result_matrix_size) for j in range(result_matrix_size)]

    processes_pool = Pool(cpu_count())
    pool_results = processes_pool.map(multiplier, lst)

    result = [[[] for _ in range(result_matrix_size)] for __ in range(result_matrix_size)]
    for i in pool_results:
        (row, line), res_c = i
        result[row][line] = res_c
    for i in result:
        print(' '.join(map(str, i)))
