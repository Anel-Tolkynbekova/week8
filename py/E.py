a = 109
v = int(input())
t = int(input())
if v <0:
    print(a-(-v*t)%109)
else:
    print((v*t)%109)