a,b=map(int,input().split())
m=1
for i in range(a,0,-1):
    m*=i
k=m
m=1
for i in range(a-b,0,-1):
    m*=i
n=m
m=1
for i in range(b,0,-1):
    m*=i
c=m
print(k//(n*c))