import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

target = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
subA = []
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += A[j]
        subA.append(current_sum)
subB = []
for i in range(m):
    current_sum = 0
    for j in range(i, m):
        current_sum += B[j]
        subB.append(current_sum)
subB.sort()
ans = 0
for a_sum in subA:
    find_target = target - a_sum
    left_idx = bisect_left(subB, find_target)
    right_idx = bisect_right(subB, find_target)
    ans += (right_idx - left_idx)
print(ans)