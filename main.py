from multiprocessing import Pool
import json

matrix = []

with open('matrices.json', 'r') as f:
    matrix = json.load(f)

m1, m2 = matrix['m1'], matrix['m2']

def mult(elem1, elem2, elem3, elem4):
    result = (sum(i * j for i, j in zip(elem1, elem2)), elem3)
    elem4.append(result)
    return result


if __name__ == '__main__':

    results = []

    with Pool(5) as p:
        results = p.starmap_async(mult, [(i, j, (ix * len(m2[0]) + jy + 1), results) for ix, i in enumerate(m1) for jy, j in enumerate(zip(*m2))]).get()

    results.sort(key=lambda x: x[1])
    results = [[*map(lambda x: x[0], results[i:i + len(m2[0])])] for i in range(0, len(results), len(m2[0]))]

    with open('mult.json', 'w') as f:
        json.dump(results, f)
