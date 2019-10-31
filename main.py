from multiprocessing import Process, Pool

def element(*args):
    i, j = args[0]
    A = args[1]
    B = args[2]
    res = 0
    for k in range(len(A[i])):
        res += int(A[i][k]) * int(B[k][j])
    return res

def ch_mtrx(A, B):
    try:
        for i in range(len(A)):
            assert len(A[i])==len(B)                

        for i in range(1, len(A[0])):
            assert len(B[i])==len(B[i-1])
    except AssertionError:
        print("Wrong matrix")
        exit(0)
        
def extract(f):
    mtrx = []
    for line in f:
        mtrx.append(list(line.split()))
    return mtrx

def involve(f, C, ln, st):
    s = ""
    for i in range(ln):
        s = ""
        for j in range(st):
            s += str(C[i+j]) + " "
        f.write(s + "\n")
    
        
f = open("m1.txt")
mtrx1 = extract(f)
f = open("m2.txt")
mtrx2 = extract(f)
ch_mtrx(mtrx1, mtrx2)

ln = len(mtrx2[0])
st = len(mtrx1)

mtrx3 = []

if __name__ == '__main__':
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    with Pool(ln*st) as p:
        mtrx3 = (p.starmap(element, [((i,j), mtrx1, mtrx2) for i in range(ln) for j in range(st) ] ))
        
    f = open("m3.txt", "w")    
    involve(f, mtrx3, ln, st)
    f.close()         
