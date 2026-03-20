from collections import deque
a, n, start = map(int, input().split())
graph = [[] for _ in range(a + 1)]
for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, a + 1):
    graph[i].sort()
visit = [False] * (a + 1)
def dfs(graph, visit, current_node):
    visit[current_node] = True
    print(current_node, end=' ')
    for neighbor in graph[current_node]:
        if visit[neighbor] == False: 
            dfs(graph, visit, neighbor) 
dfs(graph, visit,start)
visit = [False] * (a + 1)
print()
def bfs(graph, start, visit):
    queue = deque([start])
    visit[start] = True
    while queue:
        current = queue.popleft() 
        print(current, end=' ')
        for i in graph[current]:
             if visit[i] == False:
                visit[i] = True  
                queue.append(i)
bfs(graph, start, visit)