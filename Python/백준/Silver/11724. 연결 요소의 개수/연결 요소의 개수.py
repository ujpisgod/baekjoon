import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check=[]
def dfs(start):  
    visited[start]=True
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(next_node)
ct=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        ct+=1
print(ct)