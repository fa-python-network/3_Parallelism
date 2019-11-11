from multiprocessing import Process, Pool, Queue




	
q=Queue()    
def main():
	res=0
	A=[[1,2],[1,2]]
	B=[[4,5],[4,5]]
	global C
	C=[]
	size=[]
	procs=[]
	indexes=[]

	#q=Queue()
	
	if len(A[0])!=len(B):
		print("введены не правильные матрицы")
	
	else:
		 							
		size.append(len(A))		
		size.append(len(B[0]))			
		
		for i in range(size[0]):	
			C.append([])
			for n in range(size[1]):
				C[i].append(".")

		for i in range(size[0]):  	
			for n in range(size[1]):
				indexes.append([i,n])
		
		print(indexes)
		
		
		


		for i in range(0,len(indexes)):
			
			proc = Process(target=jeff, args=(indexes[i][0],indexes[i][1],A,B,C,res,q))
			procs.append(proc)
			proc.start()
			
		for proc in procs:
			proc.join()
		
		data2=[]
		count=0
		
		while count!=len(indexes):
			count+=1
			
			data2.append(q.get())
			
			
				
		print("!!@")
		
		q.close()
		print("data2= ",data2)
		print("C=", C)
		for i in range (len(indexes)):
			C[data2[i][0]][data2[i][1]]=data2[i][2]
		#for i in range(len(C)):	
			
			
		for i in C:
			print(i)
		
			


def jeff(i, j, A, B,C, res,q):
	  
	res=0
	N = len(A[0]) or len(B)
	for k in range(N):
		
		res += A[i][k] * B[k][j]
	C[i][j]=res
	print([i,j,res])
	q.put([i,j,res])

	
	
	return res

	


if __name__ == '__main__':
	main()









