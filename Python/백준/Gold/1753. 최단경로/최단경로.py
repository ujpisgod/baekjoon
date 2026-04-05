import sys
import heapq
input = sys.stdin.readline
v,e=map(int,input().split())
start=int(input())
INF=int(1e6)
k=[INF]*(v+1)
q=[]
l=[[] for i in range(v+1)]
for i in range(e):
    u,vv,w=map(int,input().rstrip().split())
    l[u].append((vv,w))
def solve(x):
    heapq.heappush(q,(0,x))
    k[start]=0
    while q:
        d,n=heapq.heappop(q)
        if d>k[n]:
            continue
        for i,j in l[n]:
            c=d+j
            if c<k[i]:
                k[i]=c
                heapq.heappush(q,(c,i))
solve(start)
for i in range(1,v+1):
    if k[i]!=INF:
        print(k[i])
    else:
        print('INF')