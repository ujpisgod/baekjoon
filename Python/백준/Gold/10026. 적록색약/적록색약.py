from collections import deque as dq
n=int(input())
color=[list(input().rstrip())for i in range(n)]
xcolor=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if color[i][j]=='B':
            xcolor[i][j]=color[i][j]
        else:
            xcolor[i][j]='R'
visit=[[False]*n for i in range(n)]
xvisit=[[False]*n for i in range(n)]
def bfs(i,j):
    q1=dq()
    q1.append((i,j))
    visit[i][j]=True
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while q1:
        h=q1.popleft()
        y,x=h[0],h[1]
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<n and visit[ny][nx]==False and color[ny][nx]==color[y][x]:
                visit[ny][nx]=True
                q1.append((ny,nx))
def xbfs(i,j):
    q2=dq()
    q2.append((i,j))
    xvisit[i][j]=True
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while q2:
        h=q2.popleft()
        y,x=h[0],h[1]
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<n and xvisit[ny][nx]==False and xcolor[ny][nx]==xcolor[y][x]:
                xvisit[ny][nx]=True
                q2.append((ny,nx))

cansee=0
cantsee=0
for i in range(n):
    for j in range(n):
        if xvisit[i][j]==False:
            xbfs(i,j)
            cantsee+=1
        if visit[i][j]==False:
            bfs(i,j)
            cansee+=1
print(cansee,cantsee)
             
