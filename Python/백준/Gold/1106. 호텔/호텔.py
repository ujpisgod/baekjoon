c,n=map(int,input().split())
ll=[]
k=set()
for i in range(n):
    cost,people=map(int,input().split())
    mean=people/cost
    k.add(cost)
    ll.append((mean,people,cost))
ll.sort(key= lambda x:(x[1],-x[0],x[2]))
INF=int(1e9)
dp=[INF]*(c+1)
dp[0]=0
for _ in range(1,c+1):
    for i in ll:
        kl=max(0,_-i[1])
        dp[_]=min(dp[_],dp[kl]+i[2])
print(dp[c])