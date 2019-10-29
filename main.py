from multiprocessing import Pool
from random import randint


def matrix_multiplier(a, b):
    s = sum(i * j for i, j in zip(a, b))
    writing_into_file(s)
    return s


def writing_into_file(a):
    global matrix_b, quantity
    with open('matrix_multiplier.txt', 'a') as file:

        if quantity % (len(matrix_b[0])) == 0:
            file.write(f'{a}\n')

        else:
            file.write(f'{a} ')
    quantity += 1

quantity = 1

if __name__ == '__main__':
    matrix_a = [[randint(-50, 50) for i in range(2)] for i in range(2)]
    matrix_b = [[randint(-50, 50) for i in range(2)] for i in range(2)]

    with Pool(2) as pool:

        mat = pool.starmap(matrix_multiplier, [(i, j) for i in matrix_a for j in zip(*matrix_b)])
    print(mat)

    result = [mat[i:i + len(matrix_b[0])] for i in range(0, len(mat), len(matrix_b[0]))]
    print("Произведение матриц = ", result)
