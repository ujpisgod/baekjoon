b=[0]*1001
b[1]=1
b[2]=2
for i in range(1,999):
    b[i+2]=b[i]+b[i+1]
c=int(input())
d=b[c]%10007
print(d)