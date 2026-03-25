import sys
from collections import deque as dq
input=sys.stdin.readline

x,y,z=map(int,input().split())
al=[[list(map(int,input().split())) for i in range(y)] for i in range(z)]
day=[[[-1]*x for i in range(y)] for i in range(z)]
q=dq()
for i in range(z):
    for j in range(y):
        for k in range(x):
            if al[i][j][k]==1:
                q.append((i,j,k))
                day[i][j][k]=0
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
while q:
    num=1
    m=q.popleft()
    for i in range(6):
        nz,ny,nx=m[0]+dz[i],m[1]+dy[i],m[2]+dx[i]
        if 0<=nz<z and 0<=ny<y and 0<=nx<x and al[nz][ny][nx]==0:
            al[nz][ny][nx]=1
            q.append((nz,ny,nx))
            day[nz][ny][nx]=day[m[0]][m[1]][m[2]]+1
m1=0
lll=0
for i in range(z):
    for j in range(y):
        for k in range(x):
            m1=max(m1,day[i][j][k])
            if al[i][j][k]==0:
                lll=-1
if lll!=-1:
    print(m1)
else:
    print(-1)
    