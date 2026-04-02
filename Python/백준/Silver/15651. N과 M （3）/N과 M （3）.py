n,m=map(int,input().split())
ans=[]
c=[]
def solve():
    if len(ans)==m:
        print(*ans)
        return
    for i in range(1,n+1):
        ans.append(i)
        solve()
        ans.pop()
solve()
