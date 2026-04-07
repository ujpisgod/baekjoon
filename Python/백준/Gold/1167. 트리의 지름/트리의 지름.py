import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

n = int(input())
l = [[] for _ in range(n + 1)]
for _ in range(n):
    line = list(map(int,input().split()))
    node_num = line[0]
    t = []
    for j in range(1, len(line) - 1, 2):
        neighbor = line[j]
        weight = line[j+1]
        t.append((neighbor, weight))
    l[node_num] = t
def solve(now, dist):
    for next_node, weight in l[now]:
        if visit[next_node] == -1:
            visit[next_node] = dist + weight
            solve(next_node, dist + weight)
visit = [-1] * (n + 1)
visit[1] = 0
solve(1, 0)
start_node = 0
max_dist = -1
for i in range(1, n + 1):
    if visit[i] > max_dist:
        max_dist = visit[i]
        start_node = i
visit = [-1] * (n + 1)
visit[start_node] =0
solve(start_node, 0)
print(max(visit))