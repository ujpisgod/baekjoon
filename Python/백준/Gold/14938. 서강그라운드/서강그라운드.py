import heapq
n,m,r=map(int,input().split())
itm=list(map(int,input().split()))
l=[[] for i in range(n+1)]
INF=int(1e9)

for i in range(r):
    a,b,c=map(int,input().split())
    l[a].append((b,c))
    l[b].append((a, c))
q=[]
def solve(start):
    global m
    v=[INF]*(n+1)
    v[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if dist>v[now]:
            continue
        for i,j in l[now]:
            new=dist+j
            if new<=m:
                if v[i]>new:
                    v[i]=new
                    heapq.heappush(q,(new,i))
    return v
maxi=0
for i in range(1,n+1):
    k=solve(i)
    total=0
    for num,j in enumerate(k):
        if j<=m:
            total+=itm[num-1]
    maxi=max(maxi,total)
print(maxi)