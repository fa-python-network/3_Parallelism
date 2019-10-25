from multiprocessing import Pool,Process,Queue

def element(index, m1, m2,q=0):
    """Поэлементное умножение матриц """
    i, j = index
    res = 0
    N = len(m1[0]) or len(m2)
    for k in range(N):
        res += m1[i][k] * m2[k][j]
    if not q:
        return res
    return q.put(res) #реализация очереди
    
def mp_multiply(m1,m2):
    """Параллельное умножение матриц """
    p=Pool()
    q=Queue()
    m3=[]
    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            p=Process(target=element,args=((i,j),m1,m2,q,))
            p.start()
            m3.append(q.get())
            p.join()
    return m3
    
def read_matrix(f,sep=";"):
    """Читает матрицу из файла с заданным разделителем """
    strm=[] #матрица в строковом представлении
    matrix=[] #матрица в целых числах
    
    with open(f) as file_handler:
        for line in file_handler:#читаем строки из файла и добавляем в список
            strm.append(line)
            
    for i in range(len(strm)):#добавляем в список спличенные по разделителю строки
        matrix.append(strm[i].split(sep))
        
    for i in range(len(matrix)):#преобразуем значения в int
        for j in range(len(matrix[i])):
            matrix[i][j]=int(matrix[i][j])
    return matrix

def write_matrix(matrix,f="m.txt",sep=";",output=True):
    """Записывает матрицу в файл с заданным разделителем"""
    strm=str(matrix)
    mod=str()
    
    try:
        file=open(f)
        file.close()
    except IOError as e:
        mod="a+" #a+ создаёт файл, если он не существует
    else:
        mod="w" #открывает файл на запись
    finally:
        with open(f,mod) as file_handler:
            for i in range(len(strm)):
                file_handler.write(sep.join(strm[i])) #записывает числа, соединённые разделителем
        if output:
            print(matrix)

def reshape(matrix,n,m):
    """Преобразует одномерный массив в двумерный заданной размерности """
    reshaped=[[0 for i in range(n)] for j in range(m)] #пустая матрица заданной размерности
    if len(matrix)==n*m: 
        for i in range(n):
           for j in range(m):
               reshaped[i][j]=matrix[m*i+j]
        return reshaped
    return -1 #возвращает, если размерность не соответствует заданной

if __name__=="__main__":
    m1=read_matrix("m1.txt") #i*j
    m2=read_matrix("m2.txt") #j*m 
    # результирующая матрица i*m
    print("Матрица 1:{} Матрица 2:{}".format(m1,m2))
    write_matrix(reshape(mp_multiply(m1,m2),len(m1),len(m2[0])),"m3.txt")

            