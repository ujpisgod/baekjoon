n=int(input())
if n==1:
    print(9)
    exit()
dp=[[0]*(n+1) for i in range(10)]
for i in range(1,10):
    dp[i][1]=1
for i in range(2,n+1):
    for j in range(10):
        if j==0:
            dp[j][i]=dp[j+1][i-1]%1000000000
        elif 0<j<9:
            dp[j][i]=(dp[j+1][i-1]+dp[j-1][i-1])%1000000000
        elif j==9:
            dp[j][i]=dp[j-1][i-1]%1000000000
print((sum([dp[i][n] for i in range(10)]))%1000000000)