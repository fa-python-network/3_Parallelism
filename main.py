from multiprocessing  import Pool
from random import randint

def matx( x, y):

	s = sum(i*n for i, n in zip(x,y))
     
	return s


if __name__ =='__main__':

	m1=[[randint(-100, 100) for i in range(3)] for n in range(4)]

	m2=[[randint(-100, 100) for i in range(4)] for n in range(3)]

	with Pool(2) as pool:
		mat = pool.starmap(matx, [(i,n) for i in m1 for n in zip(*m2)])
	print(mat)

	summ = [mat[i:i+len(m2[0])] for i in range(0, len(mat), len(m2[0]))]
	print("Произведение  матриц = ", summ) 

