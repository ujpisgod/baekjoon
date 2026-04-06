from collections import deque as dq
import sys
input=sys.stdin.readline
q=dq()
a,b=map(int,input().split())
m=[-1]*(100001)
m[a]=0
q.append(a)
def ad(x):return x+1
def mi(x):return x-1
def mul(x):return 2*x
k=[(mul,0),(ad,1),(mi,1)]
while q:
    c=q.popleft()
    if b==c:
        print(m[c])
        break
    for i in k:
        ll=i[0](c)
        if 0<=ll<100001 and (m[ll]>(m[c]+i[1]) or m[ll]==-1):
            m[ll]=m[c]+i[1]
            if i[1] == 0:
                q.appendleft(ll)
            else:
                q.append(ll)