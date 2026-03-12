m=int(input())
b=[0]*105
for i in range(1,4):
    b[i]=1
b[4]=2
b[5]=2
for i in range(6,105):
    b[i]=b[i-1]+b[i-5]
for j in range(m):
    n=int(input())
    print(b[n])