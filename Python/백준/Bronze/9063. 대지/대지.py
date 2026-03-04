import sys
input = sys.stdin.readline
n = int(input())
x_list = []
y_list = []
for _ in range(n):
    a, b = map(int, input().split())
    x_list.append(a)
    y_list.append(b)
print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))