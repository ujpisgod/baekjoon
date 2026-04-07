from collections import deque as dq
n,m=map(int,input().split())
if n==1 and m==1:
    print(1)
    exit()
INF=int(1e9)
l=[[-1]*(m+2)]
for i in range(n):
    l.append([-1]+list(map(int, input().rstrip()))+[-1])
l.append([-1]*(m+2))
visit=[[[INF]*(m+2) for i in range(n+2)] for i in range(2)]
q=dq()
q.append((1,1,1))
visit[1][1][1]=1
dy=[0,0,1,-1]
dx=[1,-1,0,0]
while q:
    y,x,power=q.popleft()
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if l[ny][nx]==1:
            if power>=1 and visit[power-1][ny][nx]>(visit[power][y][x]+1):
                visit[power-1][ny][nx]=visit[power][y][x]+1
                q.append((ny,nx,power-1))

        elif l[ny][nx]==0 and visit[power][ny][nx]>(visit[power][y][x]+1):
            visit[power][ny][nx]=visit[power][y][x]+1
            if ny==n and nx==m:
                print(visit[power][n][m])
                exit()
            q.append((ny,nx,power))
print(-1)