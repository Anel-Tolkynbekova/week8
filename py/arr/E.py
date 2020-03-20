import math
a = int(input())
r = False
b = []
sum = 0
for i in range(a):
    b.append(int(input()))
for i in range(1, len(b)):
    if b[i]/math.fabs(b[i])== b[i-1]/math.fabs(b[i-1]):
        r = True
        break
if r:
    print('YES')
else:
    print('NO')