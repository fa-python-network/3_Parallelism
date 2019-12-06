from multiprocessing import Pool
import json

def element(i, j, A, B):
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res

with open('matrix1.json', 'r') as f:
        mat1 = json.load(f)
        matrix1 = mat1['matrix1']
with open('matrix2.json', 'r') as f:
        mat2 = json.load(f)
        matrix2 = mat2['matrix2']

#matrix1 = [[1, 2], [3, 4]]
#matrix2 = [[2, 0], [1, 2]]
matrix = []


if __name__ == '__main__':
    with Pool(2) as pool:
        data = [[i, j, matrix1, matrix2] for i in range(len(matrix1)) \
                                           for j in range(len(matrix2[0]))]
        data = pool.starmap(element, data)
        
        data = [i for i in [data[x:x + len(matrix1[0])] for x in range (0, len(data), len(matrix1[0]))]]
   
        with open('matrix.json', 'w') as f:
            json.dump(data, f) 
        
        print("Матрица")
        for i in range(len(data)):
            print(data[i])



    
    