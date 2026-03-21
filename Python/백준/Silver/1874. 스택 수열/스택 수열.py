from collections import deque as dq
import sys
imput=sys.stdin.readline
n=int(input())
num=0
k=dq([0])
r=[]
for i in range(n):
    a=int(input())
    while num<=n:
        if k[-1]<a:
            num+=1
            k.append(num)
            r.append('+')
        elif k[-1]==a:
            k.pop()
            r.append('-')
            break
        elif k[-1]>a:
            print('NO')
            exit()
for i in r:
    print(i)