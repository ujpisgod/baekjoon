n,m=map(int,input().split())
j=list(map(int,input().split()))
l=[False]*n
ans=[]
j.sort()
d={}

def solve():
    if len(ans) == m:
        if tuple(ans) not in d:       
            print(*ans)
            d[tuple(ans)] = True
        return
    for i in range(n):
        if not l[i]:
            ans.append(j[i])
            l[i]=True
            solve()
            ans.pop()
            l[i]=False
solve()