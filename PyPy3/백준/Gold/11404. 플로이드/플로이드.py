import heapq
n=int(input())
m=int(input())
INF=int(1e9)
l=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    l[a].append((b,c))
def solve(x):
    dis=[INF]*(n+1)
    dis[x]=0
    q=[]
    heapq.heappush(q,(0,x))
    while q:
        d,now=heapq.heappop(q)
        if dis[now]<d:
            continue
        for mm,nn in l[now]:
            nd=nn+d
            if nd<dis[mm]:
                dis[mm]=nd
                heapq.heappush(q,(nd,mm))
    for i in range(1,n+1):
        if dis[i]==INF:
            dis[i]=0
    return dis
ans=[]
for i in range(1,n+1):
    dis=solve(i)
    ans.append(dis)
for i in ans:
    print(*i[1:])