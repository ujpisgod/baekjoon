from collections import deque

# a: 정점(사람) 수, b: 간선(관계) 수
a, b = map(int, input().split())

# 1. 인접 리스트 초기화 (방 미리 만들기)
adj = [[] for _ in range(a + 1)]

# 2. 관계 입력 받기 (보통 관계 수 b만큼 반복)
for _ in range(b):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    # 각 노드까지의 거리를 저장 (-1은 미방문)
    dist = [-1] * (a + 1)
    queue = deque([start])
    dist[start] = 0
    
    while queue:
        curr = queue.popleft()
        
        for neighbor in adj[curr]:
            if dist[neighbor] == -1: # 아직 안 가본 친구라면
                dist[neighbor] = dist[curr] + 1
                queue.append(neighbor)
    
    # 0보다 큰 거리값(도착 가능한 모든 거리)의 합 반환
    return sum(d for d in dist if d > 0)

# 3. 각 정점별로 점수 계산
scores = []
for i in range(1, a + 1):
    scores.append(bfs(i))

# 4. 가장 작은 점수를 가진 인덱스 출력 (1부터 시작하므로 +1)
# 점수가 같다면 가장 작은 번호를 출력하기 위해 index() 사용
print(scores.index(min(scores)) + 1)