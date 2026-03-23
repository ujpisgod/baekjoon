import sys
# 이 문제는 깊이가 깊어질 수 있으므로 재귀 제한 해제 필수!
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b = map(int, input().split())

# 1. 맵 정보 한 번에 깔끔하게 입력받기
graph = []
for _ in range(a):
    graph.append(list(input().strip()))

# 2. 방문 여부를 체크할 2차원 배열 (False로 채움)
visited = [[False] * b for _ in range(a)]

# 상, 하, 좌, 우 방향을 나타내는 리스트 (국룰 테크닉!)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 사람('P')을 만난 횟수를 저장할 글로벌 변수
s = 0

def dfs(x, y):
    global s
    visited[x][y] = True # 현재 위치 방문 도장 쾅!
    
    # 만약 현재 위치에 사람이 있다면 카운트 증가
    if graph[x][y] == 'P':
        s += 1
        
    # for문을 이용해 상하좌우 4방향을 깔끔하게 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 맵의 범위를 벗어나지 않고 (패딩 대신 인덱스 조건 검사)
        if 0 <= nx < a and 0 <= ny < b:
            # 벽('X')이 아니며, 아직 방문하지 않은 곳이라면 깊이 파고든다!
            if graph[nx][ny] != 'X' and not visited[nx][ny]:
                dfs(nx, ny)

# --- 시작점 'I' 찾아서 탐색 시작 ---
for i in range(a):
    for j in range(b):
        if graph[i][j] == 'I':
            dfs(i, j)

# 3. 문제의 출력 조건: 아무도 못 만났으면 'TT' 출력
if s == 0:
    print("TT")
else:
    print(s)