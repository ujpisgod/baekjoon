import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    adj = [list(input().strip()) for _ in range(N)]
    dist = [[51] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0
            elif adj[i][j] == 'Y':
                dist[i][j] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    max_2friends = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if i == j:
                continue
            if dist[i][j] <= 2:
                count += 1
        if count > max_2friends:
            max_2friends = count
    print(max_2friends)
if __name__ == "__main__":
    solve()