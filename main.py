from multiprocessing import Pool
from random import randint

def matrix_mult(x, y):

	s = sum(i*j for i, j in zip(x,y))
    
	zapis(s)

	return s

def zapis(a):
    global matrix2, count
    with open('matrmulti.txt', 'a') as file:
        if count % (len(matrix2[0])) == 0:
            file.write(f'{a}\n')
        else:
            file.write(f'{a} ')
    count += 1

count = 1


if __name__ =='__main__':

	matrix1=[[randint(-20, 20) for i in range(3)] for j in range(4)]

	matrix2=[[randint(-20, 20) for i in range(4)] for j in range(3)]

	with Pool(2) as pool:
		mat = pool.starmap(matrix_mult, [(i,j) for i in matrix1 for j in zip(*matrix2)])
	print(mat)

	result = [mat[i:i+len(matrix2[0])] for i in range(0, len(mat), len(matrix2[0]))]
	print("Произведение исходных матриц = ", result) 