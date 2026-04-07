n=int(input())
hp=list(map(int,input().split()))
happy=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append((hp[i],happy[i]))
dp=[0]*101
for i in range(n):
    a,b=l.pop()
    for j in range(99,a-1,-1):
        dp[j]=max(dp[j], dp[j-a]+b)
print(dp[99])