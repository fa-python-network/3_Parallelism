global v
global n

with open("matrs.txt", "r") as f:

    matrix1 = f.readline().strip()
    matrix2 = f.readline().strip()



f.close()


prom_1 = []
prom_2 = []
d = []
v = 0
for i in matrix1:
    if i == '[':
        v += 1

n = v-1

for x in matrix1:
    if x.isdigit() == True:
        d.append(int(x))

for i in range(0, len(d), n):
    prom_1.append(d[i:i + n])

d = []

for y in matrix2:
    if y.isdigit() == True:
        d.append(int(y))

for i in range(0, len(d), n):
    prom_2.append(d[i:i + n])





mat1 = prom_1
mat2 = prom_2











