from multiprocessing import Process


def elemresult(indexes,A,B):
	global matrixresult
	res = 0
	i,k = indexes
	try:
		for stage in range(len(A)):
			res+=A[i][stage]*B[stage][k]
	except:
		for stage in range(len(B)):
			res+=A[i][stage]*B[stage][k]
	matrixresult[i][k] = res
	
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