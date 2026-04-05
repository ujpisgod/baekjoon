import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

l = []
while True:
    try:
        l.append(int(input()))
    except:
        break
def solve(start, end):
    if start > end:
        return
    root = l[start] 
    cut = end + 1 
    for i in range(start + 1, end + 1):
        if l[i] > root:
            cut = i
            break
    solve(start + 1, cut - 1)
    solve(cut, end)
    print(root)
if l:
    solve(0, len(l) - 1)