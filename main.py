from multiprocessing import Process, Pool, Array


def multiply_matrix(m1,m2,linenum,matrix_result):

	temp = []
	sum = 0
	
	if len(m2) != len(m1[0]):
		print('error! incorrent input!')
		return "error!"
	else:
		cols1 = len(m1[0])
		lines1 = len(m1)
		cols2 = len(m2[0])
		lines2 = len(m2)
		
		for line1 in range(linenum,linenum+1):
			for col2 in range(0,cols2):
				for col1 in range(0,cols1):
					sum+=m1[line1][col1]*m2[col1][col2]
				temp.append(sum)
				sum = 0
			for elem in range(0,len(temp)):
				matrix_result[linenum*len(temp)+elem] = temp[elem]
			temp = []
	
#start data point

m1file = 'matrix1.txt'
m2file = 'matrix2.txt'
mrfile = 'matrix-result.txt'
strresult = ''

matrix1 = []
matrix2 = []

#read data from files

with open(m1file,'r') as f:
	str = f.read()
	str = str.replace('[[','')
	str = str.replace(']]','')
	str = str.split('],[')
	for line in range(0,len(str)):
		matrix1.append([])
		linenow = str[line].split(',')
		for elem in range(0,len(linenow)):
			matrix1[line].append(int(linenow[elem]))
			
			
with open(m2file,'r') as f:
	str = f.read()
	str = str.replace('[[','')
	str = str.replace(']]','')
	str = str.split('],[')
	for line in range(0,len(str)):
		matrix2.append([])
		linenow = str[line].split(',')
		for elem in range(0,len(linenow)):
			matrix2[line].append(int(linenow[elem]))
	
	

validmatrix = matrix2
if len(matrix1) < len(matrix2):
	validmatrix = matrix1

matrix_result = Array('i',[0 for i in range(0,len(validmatrix)*len(validmatrix[0]))])


if __name__ == '__main__':
	for line in range(0,len(matrix1)):
		p1 = Process(target=multiply_matrix,args=(matrix1,matrix2,line,matrix_result))
		p1.start()
		p1.join()


	#print result
	now = 0
	for line in range(0,len(validmatrix)):
		print('[',end='')
		strresult+='['
		for elem in range(0,len(validmatrix[line])-1):
			strresult+=f'{matrix_result[now]},'
			print(f'{matrix_result[now]},',end='')
			now+=1
		print(f'{matrix_result[now]}',end='')
		strresult+=f'{matrix_result[now]}'
		now+=1
		print(']\n',end='')
		strresult+=']\n'
		
	with open(mrfile,'w') as f:
		f.write(strresult)
