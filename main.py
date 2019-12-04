from multiprocessing import Pool

def element(index, A, B):
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[2, 0], [1, 2]]
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