from multiprocessing import Pool
import json

def element(index, A, B):
    i, j = index
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
    for i in range(len(matrix1)):
        a = []
        for j in range(len(matrix2[0])):
            b = Pool().starmap(element, [[(i, j), matrix1, matrix2]])[0]
            a.append(b)
        matrix.append(a)
    Pool().close()
    
print("Матрица")
for i in range(len(matrix)):
    print(matrix[i])
    
    with open('matrix.json', 'w') as f:
        json.dump(matrix, f)