import sys
n=int(input())
input = sys.stdin.readline

for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)
