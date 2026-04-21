import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
g=int(input().strip())
p=int(input().strip())
l=[]
check=[False]*(g+1)
for i in range(p):
    l.append(int(input().strip()))
c=0
pr=list(range(g+1))
def find(x):
    if pr[x]!=x:
        pr[x]=find(pr[x])
        return pr[x]
    return x
def union(a,b):
    aa=find(a)
    bb=find(b)
    if aa>bb:
        pr[aa]=bb
    elif bb>aa:
        pr[bb]=aa
def solve(x):
    f=0
    if  x<=0:
        return f
    elif check[x]:
        l=solve(find(x)-1)
        union((find(x)-1),x)
        return l
    elif not check[x]:
        check[x]=True
        f=1
        return f
tak=True
for i in l:
    k=solve(i)
    if k:
        c+=k
    else:
        print(c)
        tak=False
        break
if tak:
    print(c)