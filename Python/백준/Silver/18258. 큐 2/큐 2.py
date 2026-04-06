from collections import deque as dq
import sys
input=sys.stdin.readline
q=dq()
n=int(input())
def push(x):
    q.append(x)
def pop():
    if q:
        print(q.popleft())
    else:
        print(-1)
def size():
    print(len(q))
def empty():
    if q:
        print(0)
    else:
        print(1)
def front():
    if q:
        print(q[0])
    else:
        print(-1)
def back():
    if q:
        print(q[-1])
    else:
        print(-1)
f=[push,pop,size,empty,front,back]
d={'push':push,'pop':pop,'size':size,'empty':empty,'front':front,'back':back}
for i in range(n):
    a=input().split()
    if len(a)>1:
        c,l=a
        d[c](int(l))
    else:
        d[a[0]]()