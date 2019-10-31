from multiprocessing import Process, current_process, Manager, Pool


def element(A, B, index_row, index_col, final_path, final_matrix, rows, cols):
    row = A[index_row]
    col = [i[index_col] for i in B]
    element_sum = sum([row[i]*col[i] for i in range(len(row))])
    proc_name = current_process().name
    print(f'c{index_row}{index_col} -> {element_sum} by: {proc_name}')
    final_matrix[index_row+index_col] = element_sum
    with open(final_path, 'w') as f:
        full_string = ''
        for i in range(rows):
            for j in range(cols):
                if final_matrix[i+j] == 0:
                    full_string += f'None '
                else:
                    full_string += f'{final_matrix[i + j]} '
            full_string = full_string[:-1] + '\n'
        f.write(full_string)


def read_matrix(file_matrix):
    try:
        with open(file_matrix, 'r') as f:
            matrix_list_string = f.readlines()
            for i, e in enumerate(matrix_list_string):
                matrix_list_string[i].replace('\n', '')
            full_matrix = [[int(i) for i in j.split()] for j in matrix_list_string]
        return full_matrix
    except FileNotFoundError:
        print(f'Файла {file_matrix} не существует')
        return None


def check_matrix(matrix, num=1):
    for row in matrix[1:]:
        if len(matrix[0]) != len(row):
            print(f"Количество столбцов в строках в матрице {num} не совпадает")
            return False
    else:
        print_matrix(matrix, num)
        return True


def print_matrix(matrix, num=1):
    if num == 1:
        print("Первая матрица")
    else:
        print("Вторая матрица")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f'|{matrix[i][j]:>5}', end=' ')
        print('|')


if __name__ == '__main__':
    matrix1 = input("Введите путь к первому файлу с матрицей (По умолчанию matrix1.txt): ")
    matrix1 = matrix1 if matrix1 != '' else 'matrix1.txt'
    matrix2 = input("Введите путь ко второму файлу с матрицей (По умолчанию matrix2.txt): ")
    matrix2 = matrix2 if matrix2 != '' else 'matrix2.txt'
    final_path = input("Введите путь к файлу, куда сохранить результат (По умолчанию final.txt): ")
    final_path = final_path if final_path != '' else 'final.txt'
    A = read_matrix(matrix1)
    print()
    B = read_matrix(matrix2)
    if A is None or B is None:
        print("Какой-то из файлов не прочтен")
        exit()
    A_bool = check_matrix(A)
    B_bool = check_matrix(B, 2)
    if not A_bool or not B_bool:
        print("проверьте матрицы")
        exit()
    if len(A[0]) != len(B):
        print("Количество столбцов первой матрицы не равно количеству строк второй матрицы! Умножение невозможно!")
        exit()
    with Manager() as manager:
        procs = []
        row_new = len(A)
        col_new = len(B[0])
        final_matrix = manager.list([0 for _ in range(row_new*col_new)])
        with Pool(4) as pool:
            lst = []
            for i in range(row_new):
                for j in range(col_new):
                    lst.append((A, B, i, j, final_path, final_matrix, row_new, col_new))
            pool.starmap(element, lst)
            #         proc = Process(target=element, args=(A, B, i, j, final_matrix))
            #         procs.append(proc)
            #         proc.start()
            # for proc in procs:
            #     proc.join()
        print("Итог")
        for i in range(row_new):
            for j in range(col_new):
                print(f'|{final_matrix[i+j]:>5}', end=' ')
            print('|')

