from collections import deque as dq
import sys
input=sys.stdin.readline
q=dq()
n=int(input())
nn=[[] for i in range(n+1)]
m=[]
visit=[False]*(n+1)
for i in range(n-1):
    a,b=map(int,input().split())
    nn[a].append(b)
    nn[b].append(a)
q.append(1)
d={}
visit[1]=True
while q:
    t=q.popleft()
    for i in nn[t]:
        if visit[i]==False:
            q.append(i)
            d[i]=t
            visit[i]=True
for i in range(2,n+1):
    print(d[i])