from multiprocessing import Pool, Process, Queue
import random

def element(index, m1, m2,q = 0):
    """Поэлементное умножение матриц """
    i, j = index
    res = 0
    N = len(m1[0]) or len(m2)
    for k in range(N):
        res += m1[i][k] * m2[k][j]
    if not q:
        return res
    return q.put(res) #реализация очереди
    
def mp_multiply(m1,m2,mp_write = False,file = "",sep=";",generate=False):
    """Параллельное умножение матриц """
    q = Queue()
    m3 = []
    randomized=[False for i in range(len(m1[0])) ] #список булевых значений, отражающий, был ли сгенерирован данный столбец случайных чисел
    for i in range(len(m1)):
        if generate: #если генерируем случайную матрицу           
                randomize_row(m1,i) 
        for j in range(len(m1[0])):
            if generate:
                if not randomized[j]:#благодаря этому уже сгенерированные столбцы 
                    randomize_column(m2,j) #не заменяются новыми значениями
                    randomized[j]=True
            p = Process(target = element,args = ((i,j),m1,m2,q,))
            p.start()
            res=q.get()
            if mp_write:
                element_write_matrix(res,(i,j),(len(m1),len(m2[0])),file,sep)
            m3.append(res)
            p.join()
    return m3
    
    
def read_matrix(f,sep = ";"):
    """Читает матрицу из файла с заданным разделителем """
    strm = [] #матрица в строковом представлении
    matrix = [] #матрица в целых числах
    
    with open(f) as file_handler:
        for line in file_handler:#читаем строки из файла и добавляем в список
            strm.append(line)
            
    for i in range(len(strm)):#добавляем в список спличенные по разделителю строки
        matrix.append(strm[i].split(sep))
        
    for i in range(len(matrix)):#преобразуем значения в int
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    return matrix

def generate_empty_square(size):
    """Генерирует пустую квадратную матрицу """
    return [[0 for i in range(size)] for j in range(size)]

def randomize_row(m,row,lower_bound=-10,upper_bound=10):
    """ Рандомизирует row строку матрицы"""
    t=list()
    for n in range(len(m[0])): 
        t.append(random.randint(lower_bound,upper_bound))
    m[row]=t

def randomize_column(m,column,lower_bound=-10,upper_bound=10):
    """ Рандомизирует column столбец матрицы"""
    t=list()
    for n in range(len(m)):
        t.append(random.randint(lower_bound,upper_bound))
    for n in range(len(m)):
        m[n][column]=t[n]

def write_matrix(matrix,f = "m.txt",sep = ";"):
    """Записывает матрицу в файл с заданным разделителем"""
    strm = str(matrix)
    mod = str()
    try:
        file = open(f)
        file.close()
    except IOError as e:
        mod ="a+" #a+ создаёт файл, если он не существует
    else:
        mod = "w" #открывает файл на запись
    finally:
        with open(f,mod) as file_handler:
            for i in range(len(strm)):
                file_handler.write(sep.join(strm[i])) #записывает числа, соединённые разделителем

def element_write_matrix(num,index,size,f = "m.txt",sep = ";"):
    """Записывает матрицу в файл поэлементно """
    mod = str()
    i, j = index
    n, m = size
    exists= True if index != (0,0) else False #проверка на то, существуют ли элементы до этого
    try:
        file = open(f)
        file.close()
    except IOError as e:
        mod = "a" #a+ создаёт файл, если он не существует
    else:
        if not exists:
            mod = "w" #открывает файл на запись (перезапись)
        else:
            mod="a"
    finally:
        with open(f,mod) as file_handler:
            if j == m-1: #если последний элемент на строке, нет разделителя и новая строка
                file_handler.write("{}{}".format(num,"\n")) #записывает числа, соединённые разделителем
            else:
                file_handler.write("{}{}".format(num,sep))

def reshape(matrix,size):
    """Преобразует одномерный массив в двумерный заданной размерности """
    n, m = size
    reshaped = [[0 for i in range(n)] for j in range(m)] #пустая матрица заданной размерности
    if len(matrix) == n*m: 
        for i in range(n):
           for j in range(m):
               reshaped[i][j] = matrix[m*i+j]
        return reshaped
    return -1 #возвращает, если размерность не соответствует заданной

def output(m):
    """ Красивый вывод матрицы"""
    string=str()
    for i in range(len(m)):
        for j in range(len(m[0])):
            string+="{:4d} ".format(m[i][j])
        string+="\n"
    return string

if __name__ == "__main__":
    m1=read_matrix("m1.txt") #i*j
    m2=read_matrix("m2.txt") #j*m 
    print(m1,m2)
    # результирующая матрица i*m
    
    m3=reshape(mp_multiply(m1,m2,mp_write=True,file="m3.txt"),(len(m1),len(m2[0])))

    print(m3)
    #print("Матрица 1:\n{}\n Матрица 2:\n{}\n Матрица 3:\n {}\n".format(output(m1),output(m2),output(m3)))
    
    n=int(input("Введите размерность квадратной матрицы случайных чисел: "))
    m4=generate_empty_square(n) #пустые квадратные матрицы для 
    m5=generate_empty_square(n)
    m6=reshape(mp_multiply(m4,m5,generate=True),(len(m4),len(m4)))
    print("Матрица 4:\n {}\n Матрица 5:\n {} \nМатрица 6:\n {} ".format(output(m4),
          output(m5),output(m6)))
    

    