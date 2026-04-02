import sys
from collections import deque as dq
sys.setrecursionlimit(10**6)
q=dq()
n=int(input())
l=list(map(int,input().split()))
for i,k in enumerate(l,start=1):
    q.append((i,k))
ans=[]
def sign(x):
    if x>0:
        return 1
    else:
        return -1
def solve(m,k):
    ans.append(q.popleft()[0])
    if q:
        if m>0:
            for i in range(k-1):
                q.append(q.popleft())
            if q:
                solve(sign(q[0][1]),q[0][1])
        else:
            for i in range(m*k):
                q.appendleft(q.pop())
            if q:
                solve(sign(q[0][1]),q[0][1])
solve(sign(q[0][1]),q[0][1])
print(*ans)