from multiprocessing import  Pool
from random import randint

def f(x,y) -> float:
    rez = sum(i*j for i, j in zip(x,y))
    dump(rez)
    return rez  

def dump(x):
    global c

    with open('file','a') as f:
        if c % 4 == 0:
            f.write(f'{x}\n')
        else:
            f.write(f'{x} ')
            
    c += 1
            
        
c = 1
if __name__ =='__main__':
    m1 = [[randint(-5,5) for i in range(3)] for i in range(4)]
    m2 = [[randint(-5, 5) for i in range(4)] for i in range(3)]
    print(*m1,'\n' , *m2, sep = '\n', end = '\n\n')

    print([(i,j) for i in m1 for j in zip(*m2)], end = '\n\n')
    with Pool(5) as p:
        results = p.starmap_async(f, [(i,j) for i in m1 for j in zip(*m2)]).get()
    print(results, '\n')
    new_m = [results[i:i+4] for i in range(0, len(results), 4)]
    print(*new_m, sep = '\n')


