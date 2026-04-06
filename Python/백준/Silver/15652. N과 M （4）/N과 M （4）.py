n,m=map(int,input().split())
ans=[]
def solve(start):
    if len(ans)==m:
        print(*ans)
        return
    for i in range(start,n+1):
        ans.append(i)
        solve(i)
        ans.pop()
solve(1)