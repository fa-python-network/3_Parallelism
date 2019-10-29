from multiprocessing import Pool, cpu_count


def elem(m):
    res = 0
    m1, m2 = m
    for y in range(len(m1)):
        res += m1[y] * m2[y]
    return res
def read_matr(file_name):
    f = open(file_name, 'r')
    l = [line.strip().split('\t') for line in f]
    f.close()
    return l
def write_matr(ls, u, t):
    f = open('m1_m2.txt', 'w')
    k = 0
    for i in range(u):
        if i != 0:
            f.write('\n')
        for j in range(t):
            f.write(f"{new_ls[k]}\t")
            k += 1


if __name__ == '__main__':
    #A = [[1, 2, 3], [4, 5, 6], [1, 1, 1], [2, 1, 2]]
    #B = [[7, 8, 5, 1], [9, 10, 1, 1], [11, 12, 1, 1]]


    A = read_matr('matr1.txt')
    B = read_matr('matr2.txt')
    res_matr = [[0, 0] for i in range(len(A))]

    ls = []

    for i in range(cpu_count()):
        for j in range(len(B[1])):
            ls.append(([int(o) for o in A[i]], [int(k[j]) for k in B]))

    p = Pool(len(ls))
    new_ls = p.map(elem, ls)
    k = 0
    write_matr(new_ls, len(res_matr), len(res_matr[0]))
    for i in range(len(res_matr)):
        for j in range(len(res_matr[i])):
            res_matr[i][j] = new_ls[k]
            k += 1
    print(res_matr)
