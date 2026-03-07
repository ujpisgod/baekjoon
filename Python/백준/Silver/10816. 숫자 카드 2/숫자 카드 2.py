n=int(input())
d={}
c=list(map(int,input().split()))
for i in range(n):
    if c[i] in d:
        d[c[i]]+=1
    else:
        d[c[i]]=1
n2=int(input())
c2=list(map(int,input().split()))
for i in c2:
       print(d.get(i, 0))