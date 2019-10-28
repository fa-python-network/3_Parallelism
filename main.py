from multiprocessing import Pool
from random import randint
import json


def mult(x, y, z, r):
    result = (sum(i * j for i, j in zip(x, y)), z)
    r.append(result)
    return result

def datarec(file, result):
    with open(file, 'w') as f:
        json.dump(result, f)

if __name__ =='__main__':
    with open('data.json','r') as f:
        matrices = json.load(f)
        m1, m2 = matrices['m1'], matrices['m2']
    print(*m1, '\n', *m2, sep='\n', end='\n\n')

    results = []
    with Pool(5) as p:
        results = p.starmap_async(mult, [(i, j, (ix * len(m2[0]) + jy + 1), results) for ix, i in enumerate(m1) for jy, j in enumerate(zip(*m2))]).get()

    results.sort(key=lambda x: x[1])
    results = [[*map(lambda x: x[0], results[i:i + len(m2[0])])] for i in range(0, len(results), len(m2[0]))]

    print(*results, sep='\n')
    datarec('result.json', results)