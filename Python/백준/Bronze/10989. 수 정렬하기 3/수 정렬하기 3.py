import sys
count = [0] * 10001
input=sys.stdin.readline
n=int(input())
for i in range(n):
    a=int(input())
    count[a]+=1
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            sys.stdout.write(str(i) + '\n')