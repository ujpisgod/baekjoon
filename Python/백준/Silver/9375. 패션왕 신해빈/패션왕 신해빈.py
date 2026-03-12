n=int(input())
wear=[0]*30

for i in range(n):
    d={}
    m=int(input())
    for j in range(m):
        a,b=input().split()
        if b in d:
            d[b]+=1
        else:
            d[b]=1
    l=1
    for i in list(d.values()):
        l*=(i+1)
    print(l-1)