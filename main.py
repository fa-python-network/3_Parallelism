from multiprocessing import Process, Pool, Manager

m1_file = 'matrix_1.txt'
m2_file = 'matrix_2.txt'

matrix_1 = []
matrix_2 = []


def matrix_product(m1,m2,num_line,glob):
    result = glob.result
    dop = []
    sum = 0
    
    if len(m2) != len(m1[0]):
        print('Ошибка.Некорректные данные')
        return "ошибка"
    else:
        columns1 = len(m1[0])
        lines1 = len(m1)
        columns2 = len(m2[0])
        lines2 = len(m2)
		
        for line1 in range(num_line, num_line+1):
            for col2 in range(0,columns2):
                for col1 in range(0,columns1):
                    sum += m1[line1][col1]*m2[col1][col2]
                dop.append(sum)
                sum = 0
            str_res = "["
            for el in range(0,len(dop)-1):
                result[num_line*len(dop)+el] = dop[el]
                str_res+=f'{dop[el]},'
            result[num_line*len(dop)+(len(dop)-1)] = dop[len(dop)-1]
            str_res += f'{dop[len(dop)-1]}]'
            with open('result.txt','a') as f:
                f.write(str_res + '\n')
            dop = []

        glob.result = result

with open('result.txt','w') as f:
    f.write('')


with open(m1_file,'r') as f:
    str = f.read()
    str = str.replace('[[','')
    str = str.replace(']]','')
    str = str.split('],[')
    for line in range(0,len(str)):
        matrix_1.append([])
        l = str[line].split(',')
        for el in range(0,len(l)):
            matrix_1[line].append(int(l[el]))
			
			
with open(m2_file,'r') as f:
    str = f.read()
    str = str.replace('[[','')
    str = str.replace(']]','')
    str = str.split('],[')
    for line in range(0,len(str)):
        matrix_2.append([])
        l = str[line].split(',')
        for el in range(0,len(l)):
            matrix_2[line].append(int(l[el]))

print('-----Результат произведения матриц:')
	
mat = matrix_2
if len(matrix_1) > len(matrix_2):
    mat = matrix_1
if __name__ == '__main__':
    manager = Manager()
    Global = manager.Namespace()
    Global.result = [0 for i in range(0,len(mat)*len(mat[0]))]
    
    pool = Pool(len(matrix_1))
	
    pool.starmap(matrix_product,[(matrix_1, matrix_2, lin, Global) for lin in range(0,len(matrix_1))])
    result = Global.result
    n = 0
    for line in range(0,len(mat)):
        print('[',end='')
        for el in range(0,len(mat[line])-1):
            print(f'{result[n]},',end='')
            n += 1
        print(f'{result[n]}',end='')
        n += 1
        print(']\n',end='')

