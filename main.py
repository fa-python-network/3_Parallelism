from multiprocessing import Process, Pool, Manager      #импортируем библиотеки для работы с процессами, пулом процессов, менеджером общего пространства


def multiply_matrix(m1,m2,linenum,glb):     #функция, вычисляющая произведение матриц ПО ОДНОЙ ОТДЕЛЬНОЙ СТРОКЕ. Каждый процесс вычисляет отдельную строку итоговой матрицы!
	
	matrix_result = glb.matrix_result       #берем итоговую матрицу из общего пространства
	
	temp = []       #строка, временная переменная, которая потом последует в итоговую матрицу
	sum = 0         #переменная, куда складывается сумма произведений элементов матрицы
	
	if len(m2) != len(m1[0]):       #проверка на корректность исходных матриц
		print('error! incorrent input!')
		return "error!"
	else:
		cols1 = len(m1[0])          #кол-во столбцов матрицы 1
		lines1 = len(m1)            #кол-во строк матрицы 1
		cols2 = len(m2[0])          #кол-во столбцов матрицы 2
		lines2 = len(m2)            #кол-во строк матрицы 2
		
		for line1 in range(linenum,linenum+1):          #процесс перемножения и суммирования элементов матриц
			for col2 in range(0,cols2):
				for col1 in range(0,cols1):
					sum+=m1[line1][col1]*m2[col1][col2]
				temp.append(sum)            #добавляем элемент во временную переменную, которая затем последует в итоговую матрицу
				sum = 0
			strresult = '['                 #мгновенный ввод результата в файл, собираем сначала строку - результат, строку затем целой частью записываем за раз в файл
			for elem in range(0,len(temp)-1):
				matrix_result[linenum*len(temp)+elem] = temp[elem]      #добавляем временную переменную - строку матрицы в итоговую матрицу - результат
				strresult+=f'{temp[elem]},'
			matrix_result[linenum*len(temp)+(len(temp)-1)] = temp[len(temp)-1]
			strresult+=f'{temp[len(temp)-1]}]'
			with open('matrix-result.txt','a') as f:        #записываем результат в файл (делает каждый процесс отдельно для своей строки через append)
				f.write(strresult + '\n')
			temp = []
			
		glb.matrix_result = matrix_result       #обновляем матрицу результат в общем пространстве памяти
	
#start data point

m1file = 'matrix1.txt'
m2file = 'matrix2.txt'
with open('matrix-result.txt','w') as f:        #очищаем предыдущий результат вычисления произведения
	f.write('')

matrix1 = []        #будут содержать матрицы исходные из файлов
matrix2 = []

#read data from files

with open(m1file,'r') as f:     #читаем сложной схемой матрицу 1 из файла
	str = f.read()
	str = str.replace('[[','')
	str = str.replace(']]','')
	str = str.split('],[')
	for line in range(0,len(str)):
		matrix1.append([])
		linenow = str[line].split(',')
		for elem in range(0,len(linenow)):
			matrix1[line].append(int(linenow[elem]))
			
			
with open(m2file,'r') as f:         #читаем сложной схемой матрицу 2 из файла
	str = f.read()
	str = str.replace('[[','')
	str = str.replace(']]','')
	str = str.split('],[')
	for line in range(0,len(str)):
		matrix2.append([])
		linenow = str[line].split(',')
		for elem in range(0,len(linenow)):
			matrix2[line].append(int(linenow[elem]))
	
	

validmatrix = matrix2           #определяем размерность итоговой матрицы для правильности границ списков в циклах
if len(matrix1) > len(matrix2):
	validmatrix = matrix1


if __name__ == '__main__':      #если запускается непосредственно данный файл, не в составе подключенной библиотеки. Для работы процессов.

	manager = Manager()     #менеджер общего пространства памяти процессов

	Global = manager.Namespace()        #область имен
	Global.matrix_result = [0 for i in range(0,len(validmatrix)*len(validmatrix[0]))]       #генерируем размеры итоговой матрицы
	
	
	pool = Pool(len(matrix1))       #создаем пул
	
	pool.starmap(multiply_matrix,[(matrix1,matrix2,linehere,Global) for linehere in range(0,len(matrix1))])     #используем starmap, так как нужно передать несколько аргументов

	matrix_result = Global.matrix_result        #обновляем переменную в главном процессе

	#print result
	now = 0
	for line in range(0,len(validmatrix)):      #выводим результат в консоль
		print('[',end='')
		for elem in range(0,len(validmatrix[line])-1):
			print(f'{matrix_result[now]},',end='')
			now+=1
		print(f'{matrix_result[now]}',end='')
		now+=1
		print(']\n',end='')
