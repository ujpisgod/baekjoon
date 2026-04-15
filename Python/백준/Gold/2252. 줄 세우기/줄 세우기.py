from collections import deque as dq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
front=[0]*(n+1)
l=[[]for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    front[b]+=1
q=dq()
for i in range(1, n + 1):
    if front[i] == 0:
        q.append(i)
ans=[]
while q:
    t=q.popleft()
    ans.append(t)
    for i in l[t]:
        front[i]-=1
        if front[i]==0:
            q.append(i)
print(*ans)