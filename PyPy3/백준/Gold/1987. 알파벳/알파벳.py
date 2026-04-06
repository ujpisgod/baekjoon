a,b=map(int,input().split())
l=[list(input()) for i in range(a)]
ans=[[0]*(b+2) for i in range(a+2)]
for i in range(a+2):
    ans[i][0]=-1
    ans[i][b+1]=-1
for i in range(b+2):
    ans[0][i]=-1
    ans[a+1][i]=-1
ans[1][1]=1
alpha=[False]*26
dx=[1,-1,0,0]
dy=[0,0,1,-1]
max_strike = 1
def solve(sy,sx,strikes):
    global max_strike
    idx=ord(l[sy][sx])-65
    if alpha[idx]:
        return
    max_strike = max(max_strike, strikes)
    alpha[idx]=True
    for i in range(4):
        ny=sy+dy[i]
        nx=sx+dx[i]
        if ans[ny+1][nx+1]!=-1:
            solve(ny,nx,strikes+1)
    alpha[idx]=False
solve(0,0,1)
print(max_strike)