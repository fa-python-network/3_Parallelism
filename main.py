"""
Процесс перемножения завершается нажатием Ctrl C, вместе с ним убивается процесс генерации матриц.
Работает криво, но работает
А первый номер тем способом с помощью таймера решать долго:(
"""

from multiprocessing import Process, Queue, Pool
import random
from functools import partial
from itertools import product
import sys, signal

def signal_handler(signal, frame):
	global sig
	sig=1
	

def creator(r,q):
	while True:
	
		m=[[random.randint(-10,10) for i in range(r)] for j in range(r)]
		q.put(m)
		
sig=0

if __name__=='__main__':
	q=Queue()
	n1=int(input('Razmernost: '))
	process_one = Process(target=creator,args=(n1,q))
	process_one.start()



	def my_(k):
		l=0
		for i in range(n1):
			l+=mat1[k//n1][i]*mat2[i][k%n1]
		return(l)
		
	while True:
		mat1=q.get()
		mat2=q.get()
		c=[]
		for i in range(n1*n1):
			c.append(i)
		pool = Pool(processes=5)
		h=(pool.map(my_,c))
		o=[]
		for i in range(n1):
			o.append([])
			for j in range(n1):
				o[i].append(h[j+i*n1])
		print('REZ',o)

		signal.signal(signal.SIGINT,signal_handler)
		if sig==1:
			process_one.terminate()
			break

	q.close()
	q.join_thread()
	process_one.join()

	print("VSE")
