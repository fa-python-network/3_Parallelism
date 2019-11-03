# -*- coding: utf-8 -*-
import random
from multiprocessing import Process, Pool

def gen(i):
    '''
    Функция генерирования матриц.
    '''
    n = random.randint(2, 5)
    ls1 = [[random.randint(1,10) for i in range(n)] for j in range(n)]
    ls2 = [[random.randint(1,10) for i in range(n)] for j in range(n)]            
    return ls1, ls2
            
    
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

def involve(f, C, ln):
    '''
    Функция втаскивания матрицы в файл.
    '''
    s = ""
    for i in range(ln):
        s = ""
        for j in range(ln):
            s += str(C[i+j]) + " "
        f.write(s + "\n")
    f.write("\n\n")
 
def main():
    # Генерируем матрицы.
    n = 5
    with Pool(n) as p:
        mls = (p.map(gen, range(n)))
        
        # Производим вычисления.
        for i in mls:
            ln = len(i[0])
            with Pool(ln) as p1:
                mtrx3 = (p1.starmap(element, [((j,k), i[0], i[1]) for j in range(ln) for k in range(ln) ] ))
        # Втаскиваем.
            f = open("m3.txt", "a")    
            involve(f, mtrx3, ln)
            f.close()         


if __name__ == '__main__':
        __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)" # Без этой строчки 
                                                                                                     # на домашнеи компе ничего 
                                                                                                     # не работает.
        main()
