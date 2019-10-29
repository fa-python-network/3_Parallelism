
from multiprocessing import Pool

def element(index):
    global A
    global B
    i, j = index
    res = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res

def dlina(m1,m2) -> int:
    x = len(m1[0])
    y = len(m2)
    return x*y 

def read_matrix_from_file(file):
    with open(file) as f :
        result=[]
        str=''

        for line in f:
            line=line[:-2]
        #print(line)
        for i in line:
            
            if i.isdigit() or i==']':
                str+=i
                str+=' '
        result=str.split(']')
        #print(result)
        r=[]
        for i in result:
            r.append(list(map(int,i.split())))
    return r

        
        
A = read_matrix_from_file("Amatrix")
B = read_matrix_from_file("Bmatrix")
print(A)
print(B)


pool = Pool(processes=dlina(A,B))

k = pool.map(element, [(i,j) for i in range(len(A[0])) for j in range(len(B))])
new_matrix = []
for i in range(len(A[0])):
    new_matrix.append([])
    for j in range(len(B)):
        new_matrix[-1].append(k[0])
        k.remove(k[0])


print(new_matrix)
open("new_matrix",'w').close()
with open('new_matrix','a') as f:
    f.write(str(new_matrix))