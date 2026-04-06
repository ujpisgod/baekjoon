n=int(input())
dp=[0]*13
dp[0]=1
dp[1]=1
for i in range(2,13):
    dp[i]=i*dp[i-1]
print(dp[n])