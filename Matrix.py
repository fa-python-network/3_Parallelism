import os
from multiprocessing import Pool
from multiprocessing import cpu_count
from multiprocessing import RLock
from functools import partial
from random import randint

lock = RLock()


# Подсчёт эл-та матрицы
def element(index, a, b):
    global lock
    i, j = index[0], index[1]
    res = 0
    n = len(a[0])
    for k in range(n):
        res += a[i][k] * b[k][j]
    # Запись в промежуточный файл
    lock.acquire()
    with open("Matrix.txt", "a+") as mat:
        print(f"{res};{index}", file=mat)

    lock.release()


def mult(a, b, index):
    # Хотя быстрее было бы сделать всё в 1 поток
    # И ошибок, когда в матрице 0 остаются не было бы
    pool = Pool(processes=cpu_count())
    pool.map_async(partial(element, a=a, b=b), index)
    pool.close()
    pool.join()


class Matrix:
    def __init__(self, matrix=None, a=None, b=None, file=None, random=False):
        """Вызов различных конструкторов матрицы"""
        if matrix is not None:
            self.__matrix = matrix
        elif a is not None and b is not None:
            if not random:
                self.__matrix = self.new_matrix(a, b)
            else:
                self.__matrix = self.random_matrix(a, b)
        elif file is not None:
            self.read_matrix(file)
        else:
            self.__matrix = []

        # Количество строк и столбцов
        self.__count_line = len(self.__matrix)
        self.__count_column = len(self.__matrix[0])

    @staticmethod
    def new_matrix(a, b):
        """Создание новой матрицы и заполнение её нулями"""
        matrix = []
        for i in range(a):
            t = []
            for j in range(b):
                t.append(0)
            matrix.append(t)
        return matrix

    @staticmethod
    def random_matrix(a, b):
        """Создание матрицы из случайных чисел"""
        matrix = []
        for i in range(a):
            t = []
            for j in range(b):
                t.append(randint(0, 101))
            matrix.append(t)
        return matrix

    def read_matrix(self, file):
        """Чтение матрицы из файла"""
        with open(file, 'r') as f:
            self.__matrix = eval(f.readline())

    def __str__(self):
        """__str__"""
        return str(self.__matrix)

    def build_matrix(self, file, matrix, index):
        """Сброка матрицы из файла"""
        with open(file, "r") as f:
            while True:
                s = f.readline().split(";")  # Считываем строку и делием её по ;
                try:
                    i, j = eval(s[1])  # Получаем индекс эелемента матрицы
                except IndexError:
                    break  # Если ошибка - файл кончился, выходим из цикла
                matrix[i][j] = int(s[0])  # Изменяем элемент матрицы на подсчитанное значение
                t = [i, j]

                index.remove(t)  # Удаляем индекс этого эл-та из списка
        os.remove(file)  # Удаление промежуточного файла

        # Из-за ошибки в потоках, может получиться, что некоторые значения не будут записанны в файл, в таком случае
        # список индексов будет непустой, поэтому для этих индексов снова запустим умножение
        return index, matrix

    def creating_index(self, other, rmul=False):  # rmul - флаг того, что происходит умножение rmul
        """Получение индексов всех элементов в перемножаемой матрице"""
        # Создаётся список, в котором содержатся индексы перемноженной матрицы
        index = []
        if rmul:
            for i in range(len(other.__matrix)):
                for j in range(len(self.__matrix[0])):
                    index.append([i, j])
        else:
            for i in range(len(self.__matrix)):
                for j in range(len(other.__matrix[0])):
                    index.append([i, j])
        return index

    def __mul__(self, other):
        """Умножение матриц"""
        if self.__count_column != other.__count_line:
            raise IOError("Невозможно перемножить матрицы")
        index = self.creating_index(other)  # Получаем все индексы будущей матрицы
        mult(self.__matrix, other.__matrix, index)  # Выполняем умножение
        matrix = self.new_matrix(self.__count_line, other.__count_column)  # Создаём пустую матрицу, в которую запишем
        # результат
        index, matrix = self.build_matrix("Matrix.txt", matrix, index)  # Получаем незаписавшиеся индексы и
        # получившуюся матрицу
        while index:
            mult(self.__matrix, other.__matrix, index)
            index, matrix = self.build_matrix("Matrix.txt", matrix, index)
        return Matrix(matrix=matrix)  # Если все индексы посчитаны - выводим результат

    def __rmul__(self, other):
        """Отражённое умножение матриц"""
        if self.__count_line != other.__column:
            raise IOError("Невозможно перемножить матрицы")
        index = self.creating_index(other)
        mult(other.__matrix, self.__matrix, index)
        matrix = self.new_matrix(self.__count_column, other.__count_line)
        index, matrix = self.build_matrix("Matrix.txt", matrix, index)
        while index:
            mult(other.__matrix, self.__matrix, index)
            index, matrix = self.build_matrix("Matrix.txt", matrix, index)
        return Matrix(matrix=matrix)

    def __imul__(self, other):
        """Умножение с присваиванием"""
        if self.__count_column != other.__count_line:
            raise IOError("Невозможно перемножить матрицы")
        index = self.creating_index(other)
        mult(self.__matrix, other.__matrix, index)
        matrix = self.new_matrix(self.__count_line, other.__count_column)
        index, matrix = self.build_matrix("Matrix.txt", matrix, index)
        while index:
            mult(self.__matrix, other.__matrix, index)
            index, matrix = self.build_matrix("Matrix.txt", matrix, index)
        self.__matrix = matrix
        return self
