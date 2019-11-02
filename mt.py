from multiprocessing import Process, Pool
import numpy as np
from json import load, dump


mt1 = np.random.randint(0, 50, (3, 3))
mt2 = np.random.randint(0, 50, (3, 3))

def to_file(matrix, filename):
    with open(filename, 'w') as f:
        for line in matrix:
            for elem in line:
                f.write(f'{elem}\t')
            f.write('\n')


if __name__ == '__main__':

    print(mt1)
    print(mt2)
    with Pool(5) as pool:
        mtt = np.matmul(mt1,mt2)
        print(mtt)
        to_file(mtt, 'result.txt')
