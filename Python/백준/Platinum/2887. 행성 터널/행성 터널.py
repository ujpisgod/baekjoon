import heapq as hq
import sys
input=sys.stdin.readline
n=int(input().strip())
xl=[]
yl=[]
zl=[]
where={}
pr=list(range(n+1))
def find(x):
    while pr[x]!=x:
        pr[x]=pr[pr[x]]
        x=pr[x]
    return x
def union(a,b):
    aa=find(a)
    bb=find(b)
    if aa>bb:
        pr[bb]=aa
        return True
    elif bb>aa:
        pr[aa]=bb
        return True
    else:
        return False
for i in range(n):
    x,y,z=map(int,input().split())
    xl.append((x,i))
    yl.append((y,i))
    zl.append((z,i))
xl.sort()
yl.sort()
zl.sort()
l=[[] for i in range(n+1)]
q=[]
if n>=3:
    for i in range(1,n-1):
        hq.heappush(q,(abs(xl[i][0]-xl[i+1][0]),xl[i][1],xl[i+1][1]))
        hq.heappush(q,(abs(xl[i][0]-xl[i-1][0]),xl[i][1],xl[i-1][1]))
        hq.heappush(q,(abs(yl[i][0]-yl[i+1][0]),yl[i][1],yl[i+1][1]))
        hq.heappush(q,(abs(yl[i][0]-yl[i-1][0]),yl[i][1],yl[i-1][1]))
        hq.heappush(q,(abs(zl[i][0]-zl[i+1][0]),zl[i][1],zl[i+1][1]))
        hq.heappush(q,(abs(zl[i][0]-zl[i-1][0]),zl[i][1],zl[i-1][1]))
    s=0
    d={}
    while q:
        a,b,c=hq.heappop(q)
        if union(b,c):
            s+=a
        else:
            continue
    print(s)
elif n==1:
    print(0)
elif n==2:
    print(min(abs(xl[1][0]-xl[0][0]),abs(yl[1][0]-yl[0][0]),abs(zl[1][0]-zl[0][0])))
    