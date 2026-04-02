from collections import deque as dq
import sys
sys.setrecursionlimit(10**6)
n=int(input())
nn=list(map(int,input().split()))
q=dq()
s=list(map(int,input().split()))
for i,j in enumerate(nn):
    if j==1:
        pass
    else:
        q.append(s[i])
nnn=int(input())
ll=list(map(int,input().split()))
m=len(ll)
ans=[]
for i in ll:
    q.appendleft(i)
for i in range(m):
    ans.append(q.pop())
print(*ans)
