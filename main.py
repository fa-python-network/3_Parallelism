from multiprocessing import  Pool

def matrix_multiplier(a, b):

     s = sum(i*j for i, j in zip(a,b))
     return s

if __name__ =='__main__':
    matrix_a=[[1,1], [2,2]]
    matrix_b=[[12, 21], [1, 11], [5, 2]]

    with Pool(2) as pool:
        mat = pool.starmap(matrix_multiplier, [(i,j) for i in matrix_a for j in zip(*matrix_b)])
    print(mat)

    result = [mat[i:i+len(matrix_b[0])] for i in range(0, len(mat), len(matrix_b[0]))]
    print("Произведение исходных матриц = ", result)