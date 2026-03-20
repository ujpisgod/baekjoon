from collections import deque as dq
a, b = map(int, input().split())
k = dq(range(1, a + 1))
ans = []
while k:
    for _ in range(b - 1):
        k.append(k.popleft())
    ans.append(str(k.popleft()))
print("<" + ", ".join(ans) + ">")