import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
l=[]
for i in range(m):
    a,b,c=map(int,input().split())
    l.append((c,a,b))
l.sort(reverse=True)
pr=list(range(n+1))
def find(x):
    if pr[x]!=x:
        pr[x]=find(pr[x])
    return pr[x]
def union(a,b):
    aa=find(a)
    bb=find(b)
    if aa>bb:
        pr[bb]=aa
        return True
    elif aa<bb:
        pr[aa]=bb
        return True
    else:
        return False
tc=0
ma=0
while l:
    money,start,end=l.pop()
    if union(start,end):
        tc+=money
        ma=money
print(tc-ma)