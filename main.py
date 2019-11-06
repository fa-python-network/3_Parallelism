def compute_matrix_element(args):
    s1, s2, filename = args

    elem = 0
    for i in range(len(s1)):
        elem += s1[i] * s2[i]

    with open(filename, 'w') as f:
        f.write(str(elem))


def multiply_matrices(m1, m2, filename='result.txt'):
    from multiprocessing import Pool
    from os import remove

    m2_columns = []
    for i in range(len(m2[0])):
        m2_columns.append([st[i] for st in m2])

    for st1 in m1:
        assert len(st1) == len(m2), 'Кол-во столбцов первой матрицы не равно кол-ву строк второй.'

    pool = Pool(processes=8)  # чаще всего 4 ядра, а из-за hyper-threading - 4*2
    elem_filenames = []
    for st_index, st in enumerate(m1):
        loc_filenames = [f'element_{chr(ord("a") + col_index)}{st_index}' for col_index in range(len(m2_columns))]
        elem_filenames.extend(loc_filenames)
        pool.map(compute_matrix_element, zip([st] * len(m2_columns), m2_columns, loc_filenames))

    with open(filename, 'w') as res_file:
        for loop in range(len(m1)):
            for col_index in range(len(m2_columns)):
                elem_filename_index = loop * len(m2_columns) + col_index
                with open(elem_filenames[elem_filename_index]) as elem_file:
                    res_file.write(elem_file.read() + (' ' if col_index != len(m2_columns) - 1 else ''))
                remove(elem_filenames[elem_filename_index])
            res_file.write('\n')


def read_matrix(filename):
    with open(filename) as f:
        result = []
        line = f.readline().split()
        normal_len = len(line)

        while line:
            if len(line) != normal_len:
                raise ValueError('Строки матрицы имеют разную длину')

            for i in range(len(line)):
                line[i] = int(line[i])
            result.append(line)

            line = f.readline().split()

    return result


if __name__ == '__main__':
    m1, m2 = read_matrix('m1.txt'), read_matrix('m2.txt')
    multiply_matrices(m1, m2)
