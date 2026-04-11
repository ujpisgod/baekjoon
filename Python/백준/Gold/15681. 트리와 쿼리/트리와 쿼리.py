import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
v,r,n=map(int,input().split())
l=[[] for i in range(v+1)]
for i in range(v-1):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)
dp=[0]*(v+1)
visit=[False]*(v+1)
def solve(x):
    visit[x]=True
    if len(l[x])==1 and x!=r:
        dp[x]=1
        return dp[x]
    dp[x] = 1
    for i in l[x]:
        if visit[i]==False:
            dp[x]+=solve(i)
    return dp[x]
solve(r)
for i in range(n):
    print(dp[int(input())])