import sys
input = sys.stdin.readline
INF = int(1e9)

def solve():
    tc = int(input())
    for _ in range(tc):
        n, m, w = map(int, input().split())
        edges = []
        for _ in range(m):
            s, e, t = map(int, input().split())
            edges.append((s, e, t))
            edges.append((e, s, t))
        for _ in range(w):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t))
        dist = [INF] * (n + 1)
        negative_cycle = False
        for i in range(n):
            for cur, nxt, cost in edges:
                if dist[cur] + cost < dist[nxt]:
                    dist[nxt] = dist[cur] + cost
                    if i == n - 1:
                        negative_cycle = True
        if negative_cycle:
            print("YES")
        else:
            print("NO")
if __name__ == '__main__':
    solve()