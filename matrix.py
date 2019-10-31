# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:16:42 2019

@author: admin
"""
#import os
from multiprocessing import Pool
def matrixmult (lisst):
    stroka=lisst[0]
    cols_A = len(stroka)
    rows_A=lisst[1]
    B=lisst[2]
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
      print ("Cannot multiply the two matrices. Incorrect dimensions.")
      return
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += stroka[k] * B[k][j]
    with open("result.txt",'a') as f:
        f.write(str(C[0]))
        f.write('\n')         
    return C[0]
 

def reading(file):
    rez = []
    with open(file) as f:
        for line in f:
            line=line.strip()
            rez.append([int(i) for i in line.split()])
    return rez

if __name__=='__main__':
    matr1=reading("file_matr1.txt")
    dlina=len(matr1)
    matr2=reading("file_matr2.txt")
    print('Матрица №1:')
    print(matr1)
    print('Матрица №2:')
    print(matr2)
    sp=[]
    for i in matr1:
        sp1=[i,dlina,matr2]
        sp.append(sp1)
    with Pool(dlina) as pool:
        print(pool.map(matrixmult,[i for i in sp]))
        pool.close()
        pool.join()


