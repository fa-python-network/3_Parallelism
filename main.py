import random
from random import randint
from multiprocessing import Pool

 
def matrixmult(m1,m2):

    result = sum(i*j for i, j in zip(m1,m2))
    return result
 
def creatematrix(l,r):
    t=[]
    m=[]
    for i in range(0,l):
        for j in range(0,r):
            t.append(random.randint(1,10))
        m.append(t)
        t=[]
    return m



if __name__ =='__main__':
    print("Number of rows in 2nd matrix must be the same as number of lines in 1st matrix")
    l1=input ('Insert number of lines in 1st matrix >')
    r1=input ('Insert number of rows in 1st matrix >')
    l2=input ('Insert number of lines in 2nd matrix >')
    r2=input ('Insert number of rows in 2nd matrix >')
    if l1 != r2:
        print ("Matrixes can't be multiplied")
    else:
        m1=creatematrix(int(l1),int(r1))
        m2=creatematrix(int(l2),int(r2))
        print(m1)
        print (m2)
        with Pool(5) as pool:
    
                matr = pool.starmap(matrixmult, [(i,j) for i in m1 for j in zip(*m2)])
        #print(matr)

        matr = [matr[i:i+len(m2[0])] for i in range(0, len(matr), len(m2[0]))]
        print("\nRESULT:   ", matr)
