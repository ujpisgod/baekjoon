import sys
input=sys.stdin.readline
n=int(input())
l=[[0]*(2*n-1) for i in range(2*n-1)]
tmp=[list(map(int,input().split())) for i in range(n)]
tmpl=[]
check=[[True]*(2*n-1) for i in range(2)]
def calc(rows):
    cand = []
    for r in rows:
        cols = []
        for c in range(2*n - 1):
            if l[r][c] == 1:
                cols.append(c)
        if cols:
            cand.append(cols)
    cand.sort(key=len)
    used_col = [False] * (2*n - 1)
    best = 0
    def dfs(idx, cnt):
        nonlocal best
        if idx == len(cand):
            best = max(best, cnt)
            return
        if cnt + (len(cand) - idx) <= best:
            return
        for c in cand[idx]:
            if not used_col[c]:
                used_col[c] = True
                dfs(idx + 1, cnt + 1)
                used_col[c] = False
        dfs(idx + 1, cnt)
    dfs(0, 0)
    return best
if n==1:
    if tmp==[[1]]:
        print(1)
    elif tmp==[[0]]:
        print(0)
else:
    for i in range(n):
        for j in range(i+1):
            tmpl.append(tmp[i-j][j])
    for i in range(1,n):
        for j in range(0,n-i):
            tmpl.append(tmp[n-j-1][i+j])
    for i in range(2*n-1):
        for j in range(-1*abs(i-n+1)+(n-1),-1*(-1*abs(i-n+1)+(n-1))-1,-2):
            l[i][n-1-j]=tmpl.pop(0)
    even_rows = [i for i in range(2*n - 1) if i % 2 == 0]
    odd_rows = [i for i in range(2*n - 1) if i % 2 == 1]
    print(calc(even_rows) + calc(odd_rows))