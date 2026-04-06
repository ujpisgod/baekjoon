n,m=map(int,input().split())
l=list(map(int,input().split()))
ans=[]
l.sort()
def solve():
    if len(ans)==m:
        print(*ans)
        return
    for i in l:
        if i not in ans:
            ans.append(i)
            solve()
            ans.pop()
solve()