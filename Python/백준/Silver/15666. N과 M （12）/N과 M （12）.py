n,m=map(int,input().split())
j=list(map(int,input().split()))
l=[False]*n
ans=[]
j.sort()
d={}

def solve(start):
    if len(ans) == m:
        if tuple(ans) not in d:       
            print(*ans)
            d[tuple(ans)] = True
        return
    for i in range(start,n):
        ans.append(j[i])
        solve(i)
        ans.pop()
solve(0)