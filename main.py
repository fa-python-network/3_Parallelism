from multiprocessing import Process


def elemresult(index, A, B, res):
    glodal res
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res
	
#start data point

matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
matrix2 = [[3,3],[3,3],[3,3]]
matrixresult = []
	
#convert result matrix with correct length
	
for smth in range(len(matrix1)):
		matrixresult.append([])
		
for line in range(len(matrixresult)):
	for smth in range(len(matrix2[0])):
		matrixresult[line].append(0)
		
#call function

if len(matrix1) == len(matrix2[0]) or len(matrix1[0]) == len(matrix2):
	for line in range(len(matrix1)):
				for elem in range(len(matrix1[0])):
					elemresult((line,elem),matrix1,matrix2)

	#print result
	print(matrixresult)
else:
	print('invalid input data')