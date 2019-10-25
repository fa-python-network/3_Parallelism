from multiprocessing import Pool, cpu_count


class Matrix(object):

    def __init__(self, A: list = None, B: list = None, A_file_name: str = None, B_file_name: str = None):
        """
        Конструктор

        :param A: первая матрица
        :param B: вторая матарица
        :param A_file_name: название файла с первой матрицей
        :param B_file_name: название файла второй матрицы
        """

        if A is None:
            A = list()
        if B is None:
            B = list()
        self.A = A
        self.B = B
        if A_file_name is not None:
            self.A = self.matrix_open(file_name=A_file_name)
        if B_file_name is not None:
            self.B = self.matrix_open(file_name=B_file_name)
        self.__C = list()

    def matrix_multiply(self, max_processes: int = None, file_name: str = None) -> list:
        """
        Перемножает элементы матрицы используя пул процессов

        :param file_name: название файла, куда сохранить матрицу
        :param max_processes: максимально допустимое кол-во процессов
        :return: матрица
        """

        self.__C = [[0 for _ in range(len(self.A))] for _ in range(len(self.A))]
        with Pool(processes=cpu_count() if max_processes is None else max_processes) as pool:
            self.__C = [pool.starmap(self._element, [(i, j) for j in range(len(self.A))]) for i in range(len(self.A))]
        return self.matrix_save("C.txt" if file_name is None else file_name, self.__C)

    def _element(self, i: int, j: int) -> int:
        """
        Вычисляет значение элемента матрицы

        :param i: индекс строки
        :param j: индекс элемента строки
        :return: значение элемента матрицы
        """

        return sum(self.A[i][k] * self.B[k][j] for k in range(len(self.A[0]) or len(self.B)))

    @staticmethod
    def matrix_open(file_name: str) -> list:
        """
        Открывает файл

        :param file_name: название открываемого файла
        :return: матрица
        """

        with open(file_name) as file_m:
            return [[int(i) for i in line.rstrip().split(" ")] for line in file_m]

    @staticmethod
    def matrix_save(file_name: str, matrix: list) -> list:
        """
        Сохраняет матрицу в файл

        :param file_name: название открываемого файла
        :param matrix: матрица
        :return: матриа
        """

        with open(file_name, "w") as file_m:
            print("\n".join([" ".join(map(str, line)) for line in matrix]), file=file_m)
        return matrix


if __name__ == '__main__':
    matrix = Matrix(A_file_name="A.txt", B_file_name="B.txt").matrix_multiply()
    print(matrix)

