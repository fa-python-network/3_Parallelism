from multiprocessing import Pool,Process,Queue

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
    
def mp_multiply(m1,m2,mp_write = False,file = "",sep=";",output = True):
    """Параллельное умножение матриц """
    q = Queue()
    m3 = []
    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            p = Process(target = element,args = ((i,j),m1,m2,q,))
            p.start()
            res=q.get()
            if mp_write:
                element_write_matrix(res,(i,j),(len(m1),len(m2[0])),file,sep,output)
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

def write_matrix(matrix,f = "m.txt",sep = ";", output = True):
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
        if output:
            print(matrix)

def element_write_matrix(num,index,size,f = "m.txt",sep = ";",output = True):
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
            if output:
                print(num)

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

if __name__ == "__main__":
    m1=read_matrix("m1.txt") #i*j
    m2=read_matrix("m2.txt") #j*m 
    # результирующая матрица i*m
    print("Матрица 1:{} Матрица 2:{}".format(m1,m2))
    m3=reshape(mp_multiply(m1,m2,mp_write=True,file="m3.txt",output=False),(len(m1),len(m2[0])))
    print(m3)
            