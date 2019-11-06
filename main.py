def read_matrix_from_file(filename, elem_type='int'):
    types_dict = {
        'int': int,
        'float': float
    }

    with open(filename) as file:
        result = []
        new_line = file.readline().split()
        st_len = len(new_line)

        while new_line:
            assert len(new_line) == st_len, 'Строки матрицы имеют разную длину.'

            for i in range(len(new_line)):
                new_line[i] = types_dict[elem_type](new_line[i])
            result.append(new_line)

            new_line = file.readline().split()

    return result


def multiply_matrix_strings(s1, s2, filename):
    result = 0
    for i in range(len(s1)):
        result += s1[i] * s2[i]

    with open(filename, 'w') as f:
        f.write(str(result))


def multiply_matrices(m1, m2, filename='result.txt', delimiter=' '):
    from multiprocessing import Pool
    from os import remove

    m2_columns = []
    for i in range(len(m2[0])):
        m2_columns.append([st[i] for st in m2])

    for st1 in m1:
        assert len(st1) == len(m2), 'Кол-во столбцов первой матрицы не равно кол-ву строк второй.'

    pool = Pool(processes=8)  # чаще всего 4 ядра, а из-за hyper-threading - 4*2
    fragment_filenames = []
    for st_index, st in enumerate(m1):
        for col_index, col in enumerate(m2_columns):
            fragment_filenames.append(f'element_{chr(ord("a") + col_index)}{st_index}')
            pool.apply_async(multiply_matrix_strings, (st, col, fragment_filenames[-1])).get()

    with open(filename, 'w') as res_file:
        for loop in range(len(m1)):
            for col_index in range(len(m2_columns)):
                with open(fragment_filenames[loop * len(m2_columns) + col_index]) as fragment_file:
                    res_file.write(fragment_file.read() + (delimiter if col_index != len(m2_columns) - 1 else ''))
                remove(fragment_filenames[loop * len(m2_columns) + col_index])
            res_file.write('\n')


if __name__ == '__main__':
    m1, m2 = read_matrix_from_file('m1.txt'), read_matrix_from_file('m2.txt')
    multiply_matrices(m1, m2)
