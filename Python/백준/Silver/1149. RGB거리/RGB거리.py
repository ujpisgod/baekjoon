n=int(input())
p=[[] for i in range(n)]
for i in range(n):
    k = list(map(int, input().split()))
    p[i]=k#빨강0 초록 1 파랑 2

dp=[[0,0,0]for i in range(n)]
dp[0]=p[0]
for i in range(1,n):
    k=[(0,1,2,0),(1,0,2,1),(2,0,1,2)]
    for j in k:
        dp[i][j[0]]=min(dp[i-1][j[1]],dp[i-1][j[2]])+p[i][j[3]]
print(min(dp[n-1]))