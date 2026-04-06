import sys
input=sys.stdin.readline
n=int(input())
k=[]
for i in range(n):
    c=list(input().split())
    aa=c[0]
    if aa=='push':
        k.append(int(c[1]))
    if aa=='pop':
        if k:
            print(k.pop(0))
        else:
            print(-1)
    if aa=='size':
        print(len(k))
    if aa=='empty':
        if k:
            print(0)
        else:
            print(1)
    if aa=='front':
        if k:
            print(k[0])
        else:
            print(-1)
    if aa=='back':
        if k:
            print(k[-1])
        else:
            print(-1)