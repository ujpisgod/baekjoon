import heapq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
l=[[] for i in range(n+1)]
front=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    front[b]+=1
q=[]
for i in range(1, n + 1):
    if front[i] == 0:
        heapq.heappush(q,i)
ans=[]
while q:
    t=heapq.heappop(q)
    ans.append(t)
    for i in l[t]:
        front[i]-=1
        if front[i]==0:
            heapq.heappush(q,i)
print(*ans)