from collections import deque as dq
import sys
input=sys.stdin.readline

a,b=map(int,input().split())
check=[[False]*b for i in range(a)]
l=[list(map(int,input().split())) for i in range(a)]
ll = [[0]*b for _ in range(a)]
for i in range(a):
    for j in range(b):
        if l[i][j] == 1:
            ll[i][j] = -1
k=dq([])
def bfs(y,x):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    check[y][x]=True
    k.append((y,x))
    ll[y][x]=0
    while k:
        i,j=k.popleft()
        for _ in range(4):
            nx=j+dx[_]
            ny=i+dy[_]
            if 0<=ny<a and 0<=nx<b and l[ny][nx]==1 and check[ny][nx]==False:
                check[ny][nx]=True
                k.append((ny,nx))
                ll[ny][nx]=ll[i][j]+1
for i in range(a):
    for j in range(b):
        if l[i][j]==2:
            bfs(i,j)
for i in ll:
    print(*i)