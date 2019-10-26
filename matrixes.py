
from multiprocessing import Process, Pool
import csv

def new_matrix (name, reader):
    matrix = []
    with open (name, reader, newline="") as f1:
        f1_reader = csv.reader(f1)
        i = 0
        for row in f1_reader:
            matrix.append([])
            for items in row:
                for item in items:
                    matrix[i].append(int(item))
            i += 1
    return(matrix)
            
def element(A, B, index):
    i, j = index
    res  = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    print(res)
    return res
            
matrix1 = new_matrix("matrix1.csv", 'r')
matrix2 = new_matrix("matrix2.csv", 'r')
matrix = []
k = 0
key_item = 0

if __name__ == "__main__":
    n, m = len(matrix1), len(matrix2[0])
    items = [(i,j) for i in range(n) for j in range(m)] 
    pool = Pool(2)
    #args = [
    #        matrix1, matrix2, (0,0),
    #        matrix1, matrix2, (0,1),
    #        matrix1, matrix2, (1,0),
    #        matrix1, matrix2, (1,1)
    #        ]
    args = [(matrix1,matrix2, item) for item in items]
    result = pool.starmap(element, args)
    while key_item < len(result):
            matrix.append([])
            for i in range(n):
                matrix[k].append(result[key_item])
                key_item += 1
            k += 1
    f = open("new_matrix.csv", 'w', newline='')
    f.close()
    with open ("new_matrix.csv", 'a', newline='') as f1:
        f1_writer = csv.writer(f1, delimiter=',')
        for line in matrix:
            f1_writer.writerow(line)
    print(matrix)        
    print(result)    
    input()