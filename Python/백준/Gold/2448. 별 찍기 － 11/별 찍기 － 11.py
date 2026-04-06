n=int(input())
l=[[' ']*(n*2) for i in range(n)]
h=n
def solve(hi,y,x):
    if hi==3:
        l[y][x],l[y+1][x-1],l[y+1][x+1],l[y+2][x-1],l[y+2][x-2],l[y+2][x],l[y+2][x+1],l[y+2][x+2]='*','*','*','*','*','*','*','*'
        return
    solve(hi//2,y,x)
    solve(hi//2,y+hi//2,x-hi//2)
    solve(hi//2,y+hi//2,x+hi//2)
solve(h,0,n-1)
for i in l:
    print("".join(i))