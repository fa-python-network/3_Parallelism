from random import randint
from multiprocessing import Pool

def write(a):
    with open('result.txt', 'a') as f:
        f.write(str(a) + " ") 

def multiplication(x, y):
    rez = sum(i*k for i, k in zip(x, y))
    return rez

matrix1 = [[randint(0, 15) for i in range(3)] for i in range(3)]
print(f'Первая матрица = {matrix1}')

matrix2 = [[randint(0, 10) for i in range(3)] for i in range(3)]
print(f'Вторая матрица = {matrix2}')

with Pool(4) as pool:
    matric = pool.starmap(multiplication, [(i, k) for i in matrix1 for k in zip(*matrix2)])
    print(matric, 'result.txt')
    write(matric)
