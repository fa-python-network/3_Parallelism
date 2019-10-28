
from multiprocessing import Process, Pool




	
    
def main():
	res=0
	A=[[1,2,3],[4,5,6]]
	B=[[7,8],[9,10],[11,12]]
	global C
	C=[]
	size=[]
	procs=[]
	indexes=[]

	if len(A[0])!=len(B):
		print("Матртицы не согласованы")
	#print("перед елсе С=",C)
	else:
		 							#размер итоговой матрицы
		size.append(len(A))		
		size.append(len(B[0]))			
		
		for i in range(size[0]):
			C.append([])
			for n in range(size[1]):
				C[i].append(".")

		for i in range(size[0]):  			#все индексы итоговой матрицы
			for n in range(size[1]):
				indexes.append([i,n])
		
		print(indexes)
		
		
		


		for i in range(0,len(indexes)):
			
			proc = Process(target=jeff, args=(indexes[i][0],indexes[i][1],A,B,C,res))
			procs.append(proc)
			proc.start()
			
		for proc in procs:
			proc.join()


		for i in C:
			print(i)


def jeff(i, j, A, B,C, res):
	  
	res=0
	N = len(A[0]) or len(B)
	for k in range(N):
		
		res += A[i][k] * B[k][j]
	C[i][j]=res
	print("res=",res)
	print(C[i][j])
	print(C)

	return res

	


if __name__ == '__main__':
	main()










