from multiprocessing import Pool

def el(*args):
	m=args[0]
	ind = list(args[1])
	res=sum(i*j for i,j in zip(m,ind))
	return res

m1=[[1,1],
	[2,2]]

m2=[[3,4],
	[3,4]]

m22=list(zip(*m2))

res=[]
M=[]
pool=Pool(3)
for i in range(len(m1[0])):
	for j in range(len(m22)):
		res = pool.starmap(el, [(i,j) for i in m1 for j in m22])
	
print(res)