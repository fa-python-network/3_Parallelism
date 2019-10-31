from multiprocessing import Process, current_process, Manager


def element(A, B, index_row, index_col, final_matrix):
    row = A[index_row]
    col = [i[index_col] for i in B]
    element_sum = sum([row[i]*col[i] for i in range(len(row))])
    proc_name = current_process().name
    print(f'c{index_row}{index_col} -> {element_sum} by: {proc_name}')
    final_matrix[index_row+index_col] = element_sum


if __name__ == '__main__':
    with Manager() as manager:
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        B = [[1, 2], [4, 5], [7, 8]]
        procs = []
        row_new = len(A)
        col_new = len(B[0])
        final_matrix = manager.list(range(row_new*col_new))
        for i in range(row_new):
            for j in range(col_new):
                proc = Process(target=element, args=(A, B, i, j, final_matrix))
                procs.append(proc)
                proc.start()
        for proc in procs:
            proc.join()
        print("Итог")
        for i in range(row_new):
            for j in range(col_new):
                print(f'|{final_matrix[i+j]:>5}', end=' ')
            print('|')