n=int(input())
if n==1:
    print(1)
    exit()
if n==2:
    print(2)
    exit()
if n==3:
    print(3)
    exit()
INF=int(1e6)
dp=[INF]*(n+1)
dp[2]=2
dp[3]=3
nn=int(n**(1/2))
for i in range(1,nn+1):
    dp[i**2]=1
for i in range(1,n+1):
    for j in range(1,nn+1):
        if (i-j**2)<=0:
            continue
        dp[i]=min(dp[i],dp[i-j**2]+1)
print(dp[n])