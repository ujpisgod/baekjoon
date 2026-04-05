import sys
import heapq
input = sys.stdin.readline
INF=int(1e9)
n,e=map(int,input().split())
l=[[] for i in range(n+1)]
for i in range(e):
    v1,v2,bias=map(int,input().split())
    l[v1].append((v2,bias))
    l[v2].append((v1,bias))
m1,m2=map(int,input().split())
def dijk(start_node):
    hq=[]
    k=[INF]*(n+1)
    k[start_node] = 0
    heapq.heappush(hq, (0, start_node))
    while hq:
        dist,now=heapq.heappop(hq)
        if k[now]<dist:
            continue
        for next_node, weight in l[now]:
            cost=dist+weight
            if cost<k[next_node]:
                k[next_node]=cost
                heapq.heappush(hq, (cost, next_node))
    return k
k=dijk(1)
a=(k[m1],k[m2])
k=dijk(m1)
b=k[m2]
t=k[n]
k=dijk(m2)
c=min(a[0]+b+k[n],a[1]+b+t)
if c>=INF:
    print(-1)
else:
    print(c)