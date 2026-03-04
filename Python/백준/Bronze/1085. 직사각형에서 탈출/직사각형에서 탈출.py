x, y, a, b = map(int, input().split())
print(min(x, y, a - x, b - y))
