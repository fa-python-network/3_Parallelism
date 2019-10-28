from multiprocessing import Pool
import json


def f(x, y, z, r) -> float:
    result = (sum(i * j for i, j in zip(x, y)), z)
    r.append(result)
    return result


if __name__ == '__main__':
    with open('entrance.json', 'r') as fl:
        matrices = json.load(fl)
        m1, m2 = matrices['first'], matrices['second']

    print(*m1, '\n', *m2, sep='\n', end='\n\n')

    columns, rows = len(m1[0]), len(m2)
    if columns != rows:
        raise ValueError('Columns != Rows')

    second_columns = len(m2[0])

    results = []


    with Pool(5) as p:
        results = p.starmap_async(f,
                                  [(i, j, (ix * second_columns + jy + 1), results) for ix, i in enumerate(m1) for jy, j
                                   in enumerate(zip(*m2))]).get()

    results.sort(key=lambda x: x[1])
    results = [[*map(lambda x: x[0], results[i:i + second_columns])] for i in range(0, len(results), second_columns)]

    print(*results, sep='\n')

    with open('exitt.json', 'w') as fl:
        json.dump(results, fl)
