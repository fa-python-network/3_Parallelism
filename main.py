# -*- coding: utf-8 -*-
from multiprocessing import Process, Pool

def element(*args):
    '''
    Функция перемножения элементов.
    '''
    i, j = args[0]
    A = args[1]
    B = args[2]
    res = 0
    f = open("log.txt", "a")
    
    for k in range(len(A[i])):
        res += int(A[i][k]) * int(B[k][j])  
    f.write("Added " + str(res) + "\n")
    f.close()
    
    return res

def ch_mtrx(A, B):
    '''
    Функция проверки матриц.
    '''
    try:
        for i in range(len(A)):
            assert len(A[i])==len(B)                

        for i in range(1, len(A[0])):
            assert len(B[i])==len(B[i-1])
            
    except AssertionError:
        print("Wrong matrix")
        exit(0)
        
def extract(f):
    '''
    Функция вытаскивания матрицы из файла в список.
    '''
    mtrx = []
    for line in f:
        mtrx.append(list(line.split()))
    return mtrx

def involve(f, C, ln, st):
    '''
    Функция втаскивания матрицы в файл.
    '''
    s = ""
    for i in range(ln):
        s = ""
        for j in range(st):
            s += str(C[i+j]) + " "
        f.write(s + "\n")
 
def main():
    # Вытаскиваем первую матрицу.
    f = open("m1.txt")
    mtrx1 = extract(f)
    # Вытаскиваем вторую матрицу.
    f = open("m2.txt")
    mtrx2 = extract(f)
    # Сравниваем.
    ch_mtrx(mtrx1, mtrx2)
    
    ln = len(mtrx2[0])
    st = len(mtrx1)
    
    mtrx3 = []
    # ПУУУУЛЛЛ!!!
    with Pool(ln*st) as p:
        mtrx3 = (p.starmap(element, [((i,j), mtrx1, mtrx2) for i in range(ln) for j in range(st) ] ))
    # Втаскиваем.
    f = open("m3.txt", "w")    
    involve(f, mtrx3, ln, st)
    f.close()         


if __name__ == '__main__':
        __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
        main()
