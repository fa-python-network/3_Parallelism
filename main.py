from multiprocessing import Process, Pool, Queue, Lock, Value
import random
import time

def element(index, matrix1, matrix2):
    """получаем элемент произведения строки и столбца"""
    i, j = index
    res = 0
    # get a middle dimension
    N = len(matrix1[0]) or len(matrix2)
    for k in range(N):
        res += matrix1[i][k] * matrix2[k][j]
    return res

def read_matrix(filename):
    """читаем матрицу из файла в список списков с типом элементов float"""
    try:
        with open (filename, "r") as matrix_file:
            matrix = []
            for line in matrix_file.readlines():
                matrix.append([float(el) for el in line.split()])
    except:
        matrix = []
    return matrix

def write_matrix(filename, matrix):
    """Записываем матрицу в файл"""

    with open (filename, "w") as matrix_file:
        matrix = "\r".join([' '.join(row) for row in [[str(element) for element in row] for row in matrix]])
        matrix_file.write(matrix)
    return 

def write_element(filename, index, value, lock):
    """Записываем отдельный элемент по индексу в файл матрицы"""
    i, j = index
    with lock:
        matrix = read_matrix(filename)
        if len(matrix) <= i:
            for _ in range(i - len(matrix) + 1):
                matrix.append([])
        if len(matrix[i]) <= j:
            for _ in range(j - len(matrix[i]) + 1):
                matrix[i].append(0)
        matrix[i][j] = value
        write_matrix(filename, matrix)
    return 
        
def write_immediately(args):
    """вычисление текущего элемента и его немедленная запись в файл"""
    filename, index, matrix1, matrix2 = args
    value = element(index, matrix1, matrix2)
    write_element(filename, index, value, lock)
    return value

def create_arguments(filename, matrix1, matrix2):
    """создание аргументов для pool'а процессов"""
    indexes = []
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            indexes.append([filename, (i, j), matrix1, matrix2])
    return indexes

def generate_matrix(size, start, end):
    """генерация случайной целочисленной матрицы"""
    return [[random.randint(start, end) for _ in range(size)] for _ in range(size)]

def queue_creating(que, matrix_size = 2, start = 0, end = 5):
    while True:
        matrix = generate_matrix(matrix_size, start, end)
        filename = f"matrix{time.time()}.txt"
        write_matrix(filename, matrix)
        que.put(filename)
        time.sleep(5)
    
def init(l):
    global lock
    lock = l

def matrix_multiplier(que, run):
    while True:
        if run.value:
            matrix1 = read_matrix(que.get())
            matrix2 = read_matrix(que.get())
            filename = f"mul_matrix{time.time()}.txt"
            indexes = create_arguments(filename, matrix1, matrix2)

            l = Lock()
            proc_count = len(matrix1) + len(matrix2[0])
            pool = Pool(processes = proc_count, initializer = init,  initargs=(l,))

            pool.map(write_immediately, indexes)
            pool.close()
            pool.join()

            que.put(filename)


if __name__ == '__main__':
    matrix_q = Queue()
    run = Value('i', 1)
    queue_process =  Process(target=queue_creating, args=[matrix_q])
    queue_process.start()
    multiplier_process = Process(target=matrix_multiplier, args=[matrix_q, run])
    multiplier_process.start()
    proc_list = [queue_process, multiplier_process]

    print("stop - stop multiplication\nexit - to shutdown")
    while True:
        cmd = input()
        if cmd == "stop":
            run.value = not run.value
        elif cmd == "exit":
            for proc in proc_list:
                proc.terminate()
            break
        else:
            pass
