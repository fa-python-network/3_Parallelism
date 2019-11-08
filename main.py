from multiprocessing import Pool


def element(lst1, lst2, number, index):
    n = len(lst1)
    value = 0
    for i in range(n):
        value += lst1[number][i] * lst2[i][index]
    return value


def read(file):
    m3 = []
    with open(file, 'r') as f:
        for line in f:
            m3.append(list(map(int, line.split())))
    return m3


def write(m3):
    open('new.txt', 'w').close()    
    with open('new.txt', 'a') as f:
        for line in m3:
            print(" ".join(str(x) for x in line), file=f) 


a = read('matrix1.txt')
b = read('matrix2.txt')

n = len(a)
p = []
for i in range(n):
    for j in range(n):
        p.append([i, j])
p = [[a,b,i[0],i[1]]for i in p]
pool = Pool(len(p))
p = pool.starmap(element, p)

lst = []
new = []
k = 0
for i in p:
    k += 1
    if k%n != 0:
        lst.append(i)
    else:
        lst.append(i)
        new.append(lst)
        lst = []
print(new)
write(new)