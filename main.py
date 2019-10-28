from multiprocessing import Process, Pool
import json
matrix = []
with open('matrix.json', 'r+') as f:
    matrix = json.load(f)

matrix1, matrix2 = matrix['m1'], matrix['m2']




def matmult(m1,m2):
    zip_b = list(m2)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b]
            for row_a in m1]

def element(ele1, ele2):
    for h in zip(ele1,ele2):
        element = sum(ele_a*ele_b for ele_a, ele_b in zip(ele1, ele2))
    return element


results = []
preresult = []
preresults = []

print(f'Proverka: {matmult(matrix1, matrix2)}')


if __name__ == '__main__':
    pool = Pool(processes=len(matrix2)*len(matrix1[0]))
    for i in matrix1:
        if i != matrix1[0]:
            results += [[preresult.get() for preresult in preresults]]
            preresults = []
        for j in matrix2:
            preresults += [pool.apply_async(element, (i,j))]
    results += [[preresult.get() for preresult in preresults]]
    print(results)

    with open('result.json', 'w') as f:
        f.write(json.dumps(results))






