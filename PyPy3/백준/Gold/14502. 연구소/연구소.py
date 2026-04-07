n,m=map(int,input().split())
l=[[1]*(m+2)]
for i in range(n):
    l.append([1]+list(map(int,input().split()))+[1])
l.append([1]*(m+2))
l2=[]
t0=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if l[i][j]==2:
            l2.append((i,j))
        if l[i][j]==0:
            t0+=1
dy=[0,0,1,-1]
dx=[1,-1,0,0]
cc=0
def solve(x):
    global cc,ct0
    if x==3:
        cl=[row[:] for row in l]
        ct0=t0-3
        for k in l2:
            dfs(k[0],k[1],cl)
        cc=max(cc, ct0)
        return
    for i in range(1,n+1):
        for j in range(1,m+1):
            if l[i][j]==0:
                l[i][j]=1
                solve(x+1)
                l[i][j]=0
def dfs(x,y,cl):
    global ct0
    for j in range(4):
        ny=x+dy[j]
        nx=y+dx[j]
        if cl[ny][nx]==0:
            cl[ny][nx]=2
            ct0-=1
            dfs(ny,nx,cl)
    return ct0
solve(0)
print(cc)