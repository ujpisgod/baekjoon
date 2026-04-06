import sys
input = sys.stdin.readline
q=[]
def a1(x):
    q.append(x)
    return
def a2():
    if q:
        print(q.pop())
        return
    else:
        print(-1)
        return
def a3():
    print(len(q))
    return
def a4():
    if q:
        print(0)
        return
    else:
        print(1)
        return
def a5():
    if q:
        print(q[-1])
        return
    else:
        print(-1)
        return
f=[a1,a2,a3,a4,a5]
n=int(input())
for i in range(n):
    c = input().split()
    if len(c)==2:
        a1(int(c[1]))
    else:
        f[int(c[0])-1]()