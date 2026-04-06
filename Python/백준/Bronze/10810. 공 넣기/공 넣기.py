a,b=map(int,input().split())
c=[0]*(a+1)
for i in range(b):
    p,q,r=map(int,input().split())
    for j in range(p,q+1):
        c[j]=r
c.pop(0)
print(*c)