
from multiprocessing import Process, Pool
import random

def new_matrix (columns):
    '''
    Созадет матрицу
    '''
    row = []
    for i in range(int(columns)):
        row.append(random.randint(0,10))
    return(row) 
            
def element(A,B,index):
    '''
    Подсчитывает элемент
    '''
    i, j = index
    res  = 0
    A = A
    B = B
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    try:
        with open('final_matrix.txt','a') as f:
            if (j+1) == len(A):
                f.write(str(res)+'\n')
            else:
                f.write(str(res)+' ')
    except:
        with open('final_matrix.txt','w') as f:
            f.write(str(res)+' ')
    return res

def check(lines1, columns1, lines2, columns2):
    '''
    Проверяет матрицы
    '''
    if int(lines1) == int(columns2) and int(columns1) == int(lines2):
        return True
    else:
        return False
    
def inits():
    '''
    Задает базы матриц
    '''
    lines1 = input('Введите количество строк первой матрицы: ')
    columns1 = input('Введите количество cтолбцов первой матрицы: ')
    lines2 = input('Введите количество строк второй матрицы: ')
    columns2 = input('Введите количество cтолбцов второй матрицы: ')
    if check(lines1, columns1, lines2, columns2) == True:
        pass
    else:
       
        return()
    matrix1 = []
    matrix2 = []
    elems1 = []
    elems2 = []
    for i in range(int(lines1)):
        elems1.append(list(columns1))
    for i in range(int(lines2)):
        elems2.append(list(columns2))
    pool_matrix = Pool(2)
    matrix1 = pool_matrix.starmap(new_matrix, elems1)
    matrix2 = pool_matrix.starmap(new_matrix, elems2)
    print('Первая матрица:')
    print(matrix1)
    print('Вторая матрица:')
    print(matrix2)
    return(matrix1, matrix2)
    
def final_matrix(matrix1,matrix2):
    '''
    Подсчитывает финальную матрицу
    '''
    items = [(i,j) for i in range(len(matrix1)) for j in range(len(matrix2[0]))] 
    args = [(matrix1,matrix2, item) for item in items]
    pool = Pool(2)
    matrix = []
    matrix = pool.starmap(element, args)
    matrix3 = []
    k = 0
    print('Финальная матрица:')
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(matrix[k])
            k += 1
        matrix3.append(row)
    print(matrix3)
    
if __name__ == "__main__":
    
    try:
        m1,m2 = inits()
        final_matrix(m1,m2)
    except:
        print('Параметры матриц не допускают их перемножения')
    
    
