import sys
from collections import deque
input = sys.stdin.readline
def solve():
    n, rule = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for _ in range(rule):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1 
    target = int(input())
    dp = cost[:]
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
    while q:
        current = q.popleft()
        if current == target:
            print(dp[target])
            return
        for next_building in graph[current]:
            dp[next_building] = max(dp[next_building], dp[current] + cost[next_building])
            in_degree[next_building] -= 1
            if in_degree[next_building] == 0:
                q.append(next_building)
t = int(input())
for _ in range(t):
    solve()