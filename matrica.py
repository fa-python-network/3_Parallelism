from multiprocessing import  Pool
from random import randint

def matrixmult(a, b):
    res_mul = sum(i*j for i, j in zip(a,b))
    write_to_file(res_mul)
    return res_mul  

def write_to_file(a):
    global matrix2, count
    with open('matrixmult.txt','a') as file:
        if count % (len(matrix2[0])) == 0:
            file.write(f'{a}\n')
        else:
            file.write(f'{a} ')
    count+=1

count=1
if __name__ =='__main__':
    matrix1 = [[randint(-10,10) for i in range(2)] for i in range(3)]
    matrix2 = [[randint(-10, 10) for i in range(3)] for i in range(2)]

    with Pool(2) as pool:
    #умножаем каждую строку 1-ой матрицы((1,2,3) и (4,5,6))
    #на каждый столбец 2-ой матрицы ((7, 9, 11) и (8, 10, 12))
    #для этого транспонируем 2-ую матрицу 
        matr = pool.starmap(matrixmult, [(i,j) for i in matrix1 for j in zip(*matrix2)])
    print(matr)

    #делаем матрицу - список списков
    mult = [matr[i:i+len(matrix2[0])] for i in range(0, len(matr), len(matrix2[0]))]
    print("Произведение исходных матриц = ", mult) 
