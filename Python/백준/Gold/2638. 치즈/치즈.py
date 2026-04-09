from collections import deque as dq
n,m=map(int,input().split())
l=[[-2]*(m+2)]
for i in range(n):
    l.append([-2]+list(map(int,input().split())) +[-2])
l.append([-2]*(m+2))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def check(a,b):
    k=0
    for i in range(4):
        if l[a+dy[i]][b+dx[i]]==-1:
            k+=1
    if k>1:
        tmp[a][b]=-2

def bfs(y,x):
    visit=[[False]*(m+2) for i in range(n+2)]
    q=dq()
    q.append((y,x))
    l[y][x]=-1
    visit[y][x]=True
    while q:
        y,x=q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if l[ny][nx]==0 and visit[ny][nx]==False:
                visit[ny][nx]=True
                l[ny][nx]=-1
                q.append((ny,nx))
            elif l[ny][nx]==-1 and visit[ny][nx]==False:
                visit[ny][nx]=True
                q.append((ny,nx))
ans=0
conti = True
while conti:
    tmp=[[0]*(m+2) for i in range(n+2)]
    conti=False
    ans+=1
    bfs(1,1)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if l[i][j]==1:
                check(i,j)  
    for i in range(1,n+1):
        for j in range(1,m+1):
            l[i][j]+=tmp[i][j]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if l[i][j]==1:
                conti=True
print(ans)