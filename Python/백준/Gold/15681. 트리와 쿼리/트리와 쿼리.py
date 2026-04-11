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
def solve(x,p):
    dp[x]=1
    for i in l[x]:
        if i!=p:
            dp[x]+=solve(i,x)
    return dp[x]
solve(r,0)
for i in range(n):
    print(dp[int(input())])