import heapq as hq
n,m=map(int,input().split())
q=[]
pr=list(range(n+1))
for i in range(m):
    a,b,c=map(int,input().split())
    hq.heappush(q,(-c,a,b))
start,end=map(int,input().split())
def find(x):
    if pr[x]!=x:
        pr[x]=find(pr[x])
    return pr[x]
def union(a,b):
    aa=find(a)
    bb=find(b)
    if aa>bb:
        pr[bb]=aa
    elif aa<bb:
        pr[aa]=bb
while q:
    i,j,k=hq.heappop(q)
    union(j,k)
    if find(end)==find(start):
        print(-i)
        exit()