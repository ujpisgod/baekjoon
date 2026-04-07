import sys
from collections import deque

def solve():
    input=sys.stdin.readline
    a,b=map(int, input().split())
    if a==b:
        print(0)
        print(1)
        return
    visit=[-1]*100001
    dp=[0]*100001
    visit[a]=0
    dp[a]=1
    q=deque([a])
    limit=1e9  # INF 값
    while q:
        t = q.popleft()
        for i in (t-1, t+1, t*2):
            if 0 <= i <= 100000:
                if visit[i] == -1 and visit[t] + 1 < limit:
                    visit[i] = visit[t] + 1
                    dp[i] = dp[t]
                    if i != b:
                        q.append(i)
                    else:
                        limit = visit[i]
                elif visit[i] == visit[t] + 1:
                    dp[i] += dp[t]
    print(visit[b])
    print(dp[b])
if __name__ == '__main__':
    solve()