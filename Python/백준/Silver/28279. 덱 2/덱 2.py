from collections import deque as dq
import sys
input=sys.stdin.readline
n=int(input())
q=dq()
def a1(x):
    q.appendleft(x)
def a2(x):
    q.append(x)
def a3():
    if q:
        print(q.popleft())
    else: print(-1)
def a4():
    if q:
        print(q.pop())
    else: print(-1)
def a5():
    if q:
        print(len(q))
    else: print(0)
def a6():
    if q:
        print(0)
    else:
        print(1)
def a7():
    if q:
        print(q[0])
    else: print(-1)
def a8():
    if q:print(q[-1])
    else:print(-1)
f=['a',a1,a2,a3,a4,a5,a6,a7,a8]
for i in range(n):
    k=input().split()
    if len(k)>1:
        f[int(k[0])](int(k[1]))
    else:
        f[int(k[0])]()