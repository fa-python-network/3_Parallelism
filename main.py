from multiprocessing import Pool

def element(*args, **kwargs):
    elem = args[0]
    index = list(args[1])	
    res = (sum(i*j for i,j in zip(elem, index)))
    return res
def dop1(m1,m2):
    x = len(m1[0])
    y = len(m2)
    return x*y 
def matrix_search(file):
    res = []
    with open(file,"r") as f:
        for elem in f:
            res.append(list(map(int, elem.split())))
    return res
def output(res):
    with open("result.txt","w") as f:
        for lines in res:
            print(" ".join(str(i) for i in lines), file=f)
            
m1 = matrix_search("matrix1.txt")
m2 = matrix_search("matrix2.txt")
print('\n---First matrix---\n', m1)
print('\n---Second matrix---\n', m2)
print('\n---Second modificated matrix---\n', list(zip(*m2)))

result = []
if __name__ == '__main__':
    pool = Pool(processes=dop1(m1,m2))
    multiplues = pool.starmap(element, [(i,j) for i in m1 for j in list(zip(*m2))]) #m2 modificated
    result = [multiplues[i:i+len(m1[0])] for i in range(0, len(multiplues), len(m1[0]))]
    output(result)
    print('\n---Final matrix---\n')
    for i in range(len(result)):
        print(' '.join(map(str, result[i])))
            
    
