from collections import deque as dq
def solution(m, n, puddles):
    if m==1 and n==1:
        return 1
    visit=[[[False,0,0] for i in range(m)]for i in range(n)]
    q=dq()
    path=0
    q.append((0,0))
    visit[0][0][0]=True
    visit[0][0][1]=1
    visit[0][0][2]=1
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    while q:
        y,x=q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<m and [nx+1,ny+1] not in puddles:
                if visit[ny][nx][0]==False:
                    visit[ny][nx][0]=True
                    visit[ny][nx][1]=visit[y][x][1]
                    visit[ny][nx][2]=visit[y][x][2]+1
                    q.append((ny,nx))
                elif visit[ny][nx][0]==True and (visit[ny][nx][2]-1)==visit[y][x][2]:
                    visit[ny][nx][1]=(visit[ny][nx][1]+visit[y][x][1])%1000000007
    answer=visit[n-1][m-1][1] 
    return answer