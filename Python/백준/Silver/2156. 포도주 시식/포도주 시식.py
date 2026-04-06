n=int(input())
l=[0]
for i in range(n):
    l.append(int(input()))
dp=[0]*(n+1)
dp[1]=l[1]
if n==1:
    print(dp[1])
    exit()

dp[2]=dp[1]+l[2]
if n==2:
    print(dp[2])
    exit()
dp[3]=max(l[1]+l[3],l[2]+l[3],dp[2])
if n==3:
    print(dp[3])
    exit()
for i in range(4,n+1):
    dp[i]=max(dp[i-2]+l[i],dp[i-3]+l[i-1]+l[i],dp[i-1])
print(dp[n])
