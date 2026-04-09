from collections import deque as dq
n=int(input())
l=[[-999]*(n+2)]
for i in range(n):
    l.append([-999]+list(map(int,input().split()))+[-999])
l.append([-999]*(n+2))
for i in range(1,n+1):
    for j in range(1,n+1):
        if l[i][j]==9:
            y,x=i,j
            l[i][j]=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(level,y,x):
    q=dq()
    ccc=0
    visit=[[-1]*(n+2) for i in range(n+2)]
    visit[y][x]=0
    q.append((y,x))
    ans=[]
    while q:
        a,b=q.popleft()
        for i in range(4):
            ny=a+dy[i]
            nx=b+dx[i]
            if (l[ny][nx]==level or l[ny][nx]==0) and visit[ny][nx]==-1:
                visit[ny][nx]=visit[a][b]+1
                q.append((ny,nx))
            elif 0<l[ny][nx]<level and l[ny][nx]!=0 and visit[ny][nx]==-1:
                visit[ny][nx]=visit[a][b]+1
                ans.append((visit[ny][nx],ny,nx))
                q.append((ny,nx))
    ans.sort()
    return ans
sl=2
time=0
exp=0
while True:
    k=bfs(sl,y,x)
    if k:
        exp+=1
        if exp==sl:
            exp=0
            sl+=1
        time+=k[0][0]
        y, x = k[0][1], k[0][2]
        l[y][x] = 0
    else:
        print(time)
        exit()