from multiprocessing import Pool,Process,Queue
import numpy
def q_element(q,index, A, B):#реализация с очередью
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return q.put(res)
    #print(res)
    
def element(index, A, B):#реализация без очереди
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res

def read_matrix(f,sep=";"):
    """Прочитать матрицу из файла с заданным разделителем """
    strm=[] #матрица в строковом представлении
    matrix=[] #матрица в целых числах
    
    with open(f) as file_handler:
        for line in file_handler:#читаем строки из файла и добавляем в список
            strm.append(line)
            
    for i in range(len(strm)):#добавляем в список спличенные по разделителю строки
        matrix.append(strm[i].split(sep))
        
    for i in range(len(matrix)):#преобразуем значения в int
        for j in range(len(matrix[i])):
            matrix[i][j]=int(matrix[i][j])
    return matrix

def write_matrix(matrix,f="m.txt",sep=";"):
    strm=str(matrix)
    with open(f) as file_handler:
        for i in range(len(strm)):
            file_handler.write(sep.join(strm[i]))

def shape_matrix(matrix,n,m):#преобразует одномерный список в двумерный
    reshaped=[] #доделать
    if len(matrix)==n*m: 
       for i in range(n):
           for j in range(m):
               reshaped[i][j]=matrix[i+i*j]
    return reshaped
    return -1

#matrix1 = [[1, 2], [3, 4]]
#matrix2 = [[2, 0], [1, 2]]

if __name__=="__main__":
    m1=read_matrix("m1.txt") #i*j
    m2=read_matrix("m2.txt") #j*m
    m3=[]#i*m
    print("Матрица 1:{} Матрица 2:{}".format(m1,m2))
    p=Pool()
    q=Queue()
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            print(element((i,j),m1,m2))
    print("\n")
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            p=Process(target=q_element,args=(q,(i,j),m1,m2,))
            p.start()
            m3.append(q.get())
            p.join()
    print(m3)
    #print(shape_matrix(m3,2,2))
    #write_matrix(shape_matrix(m3,2,2),"m3.txt")
            