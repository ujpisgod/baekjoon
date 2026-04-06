n=int(input())
dp=[1]*31
for i in range(1,31):
    dp[i]=i*dp[i-1]
for i in range(n):
    a,b=map(int,input().split())
    print(dp[b]//(dp[b-a]*dp[a]))