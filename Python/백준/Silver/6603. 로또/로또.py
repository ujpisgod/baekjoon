ans=[]
k=[]
def solve(start):
    if len(ans)==6:
        print(*ans)
        return
    for i in range(start,len(k)):
        ans.append(k[i])
        solve(i+1)
        ans.pop()
while True:
    ans=[]
    k=list(map(int,input().split()))
    if k[0]==0:
        break
    k.pop(0)
    solve(0)
    print()