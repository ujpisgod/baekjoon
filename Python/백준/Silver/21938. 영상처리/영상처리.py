import sys
sys.setrecursionlimit(10**9)
n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
k=int(input())
newl=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(0,3*m,3):
        if ((l[i][j]+l[i][j+1]+l[i][j+2])//3)>=k:
            newl[i][j//3]=255
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def solve(y,x):
    newl[y][x]=0
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<n and 0<=nx<(m) and newl[ny][nx]!=0:
            solve(ny,nx)
ct=0
for i in range(n):
    for j in range(m):
        if newl[i][j]!=0:
            solve(i,j)
            ct+=1
print(ct)