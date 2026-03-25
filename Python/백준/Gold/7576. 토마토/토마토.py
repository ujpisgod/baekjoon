import sys
from collections import deque as dq
input=sys.stdin.readline

x,y=map(int,input().split())
al=[list(map(int,input().split())) for i in range(y)]
day=[[-1]*x for i in range(y)]
q=dq()
for i in range(y):
    for j in range(x):
        if al[i][j]==1:
            q.append((i,j))
            day[i][j]=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while q:
    num=1
    m=q.popleft()
    for i in range(4):
        ny,nx=m[0]+dy[i],m[1]+dx[i]
        if 0<=ny<y and 0<=nx<x and al[ny][nx]==0:
            al[ny][nx]=1
            q.append((ny,nx))
            day[ny][nx]=day[m[0]][m[1]]+1
m1=0
lll=0
for i in range(y):
    for j in range(x):
        m1=max(m1,day[i][j])
        if al[i][j]==0:
            lll=-1
if lll!=-1:
    print(m1)
else:
    print(-1)
    