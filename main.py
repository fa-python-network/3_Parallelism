from multiprocessing import Process, Pool

def element(*args):
	elemen = args[0]
	index = list(args[1])	
	result = (sum(i*j for i,j in zip(elemen, index)))
	return result

matrix1 = [[1, 1, 2] , [2, 2, 1], [3, 3, 3]]
matrix2 = [[2, 3,1] , [3, 1, 4], [0,3,3]]
print('Первая матрица\n', matrix1)
print('\nВторая матрица\n', matrix2)

C1 = matrix1
C2 = list(zip(*matrix2))
result = []

if __name__ == '__main__':
	pool = Pool()
	result = pool.starmap(element, [(i,j) for i in C1 for j in C2])
	res = [result[i:i+len(C1[0])] for i in range(0, len(result), len(C1[0]))]
	print('\nКонечная матрица\n')
	for i in range(len(res)):
		print(res[i])