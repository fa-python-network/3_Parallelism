def multiply_matrix(m1,m2):

	m3 = []
	temp = []
	sum = 0
	
	if len(m1) == len(m2[0]) or len(m1[0]) == len(m2):
		cols1 = len(m1[0])
		lines1 = len(m1)
		cols2 = len(m2[0])
		lines2 = len(m2)
		
		for line1 in range(0,lines1):
			for col2 in range(0,cols2):
				for col1 in range(0,cols1):
					sum+=m1[line1][col1]*m2[col1][col2]
				temp.append(sum)
				sum = 0
			m3.append(temp)
			temp = []
			
	else:
		return "error!"
		
		
	return m3
	
#start data point

matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
matrix2 = [[3,3,3],[3,3,3],[2,3,3]]

print(multiply_matrix(matrix1,matrix2))
