n=int(input())
p=[[] for i in range(n)]
for i in range(n):
    k=list(map(int,input().split()))
    p[i]=k
INF=float('inf')
ans=INF
for kk in range(3):
    dp=[[0,0,0] for _ in range(n)]
    for i in range(3):
        if i==kk:
            dp[0][i]=p[0][i]
        else:
            dp[0][i]=INF
    for i in range(1,n):
        k=[(0,1,2,0),(1,0,2,1),(2,0,1,2)]
        for j in k:
            dp[i][j[0]]=min(dp[i-1][j[1]],dp[i-1][j[2]])+p[i][j[3]]
    for i in range(3):
        if i!=kk:
            ans=min(ans, dp[n-1][i])
print(ans)