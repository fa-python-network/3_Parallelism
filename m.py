from multiprocessing import  Pool
from random import randint


def callback_f(res):
    global dumps
    dumps = res


def f(x, y, z) -> float:
    rez = sum(i*j for i, j in zip(x,y))
    z = z[0] * 4 + z[1] + 1
    
    return (rez, z)


def dump(x, y, z):
    with open('file','a') as f:
        if y % z == 0:
            f.write(f'{x}\n')
        else:
            f.write(f'{x} ')


dumps = []

if __name__ =='__main__':
    rx, ry = 3, 4
    m1 = [[randint(-5, 5) for i in range(rx)] for i in range(ry)]
    m2 = [[randint(-5, 5) for i in range(ry)] for i in range(rx)]
    
    print(*m1,'\n' , *m2, sep = '\n', end = '\n\n')

    print([(i,j, (x, y)) for x, i in enumerate(m1) for y, j in enumerate(zip(*m2))], end = '\n\n')
    
    with Pool(5) as p:
        results = p.starmap_async(f, [(i, j, (x, y)) for x, i in enumerate(m1) for y, j in enumerate(zip(*m2))], callback=callback_f).get()

    print(results, '\n')
    
    new_m = [results[i:i + ry] for i in range(0, len(results), ry)]
    
    print(*new_m, sep = '\n')
    
    dumps.sort(key=lambda x: x[1])
    for i in dumps:
        dump(*i, ry)
