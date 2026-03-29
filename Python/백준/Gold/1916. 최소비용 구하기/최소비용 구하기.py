import sys
input = sys.stdin.readline
import heapq
INF=int(1e9)
n=int(input())
m=int(input())
k=[INF]*(n+1)
l=[[] for i in range(n+1)]
d={}
for i in range(m):
    a,b,c=map(int,input().split())
    l[a].append((b,c))
sc,ec = map(int, input().split())
k[sc]=0
def dijk(x):
    hq=[]
    heapq.heappush(hq, (0, x))
    while hq:
        dist,now=heapq.heappop(hq)
        if k[now]<dist:
            continue
        for next_node, weight in l[now]:
            cost=dist+weight
            if cost<k[next_node]:
                k[next_node]=cost
                heapq.heappush(hq, (cost, next_node))
dijk(sc)
print(k[ec])