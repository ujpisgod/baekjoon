from collections import deque as dq
import sys
input = sys.stdin.readline
n=int(input())
for i in range(n):
    k=dq()
    a,b=map(int,input().split())
    li=list(map(int,input().split()))
    for i, p in enumerate(li):
        k.append((i, p))
    count = 0
    while k:
        current = k.popleft()
        if any(current[1] < doc[1] for doc in k):
            k.append(current)
        else:
            count += 1
            if current[0] == b:
                print(count)
                break