n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
s=[]
t=[]
g=1e6
ll=list(range(1,n+1))
def solve(player):
    global g
    if len(s)==n//2:
        t=list(set(ll) - set(s))
        sc1,sc2 = 0,0
        for i in s:
            for j in s:
                sc1+=l[i-1][j-1]
        for i in t:
            for j in t:
                sc2+=l[i-1][j-1]
        g=min(g,abs(sc1-sc2))
        return
    for i in range(player,n+1):
        s.append(i)
        solve(i+1)
        s.pop()
solve(1)
print(g)