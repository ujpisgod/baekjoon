import sys
input = sys.stdin.readline

# 1. 입력 받기 (표준 0-based 인덱스로 깔끔하게)
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

# 2. 공기청정기 위치 찾기 (위쪽: up, 아래쪽: down)
up = -1
down = -1
for i in range(R):
    if board[i][0] == -1:
        up = i
        down = i + 1
        break

# 3. 확산 함수 (네가 짰던 로직 그대로 + 깔끔한 경계 조건)
def spread():
    # 확산량 저장할 빈 도화지
    tmp = [[0] * C for _ in range(R)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                amount = board[i][j] // 5
                if amount == 0:
                    continue # 5 미만이면 퍼질 게 없으니 패스 (최적화)
                
                spread_cnt = 0
                for k in range(4):
                    ni, nj = i + dy[k], j + dx[k]
                    # 패딩 대신 '맵 범위 안'이고 '공기청정기(-1)'가 아닌 곳만!
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] != -1:
                        tmp[ni][nj] += amount
                        spread_cnt += 1
                
                # 본인 칸에서 퍼져나간 만큼 빼기
                board[i][j] -= (amount * spread_cnt)
    
    # 임시 도화지(tmp)에 모인 먼지를 원본에 합치기
    for i in range(R):
        for j in range(C):
            board[i][j] += tmp[i][j]

# 4. 공기청정기 순환 (인덱스 꼬임 제로 로직)
def clean():
    # [위쪽 순환] 반시계 방향
    for i in range(up - 1, 0, -1): board[i][0] = board[i - 1][0]    # 1. 왼쪽
    for j in range(0, C - 1): board[0][j] = board[0][j + 1]         # 2. 위쪽
    for i in range(0, up): board[i][C - 1] = board[i + 1][C - 1]    # 3. 오른쪽
    for j in range(C - 1, 1, -1): board[up][j] = board[up][j - 1]   # 4. 아래쪽
    board[up][1] = 0 # 청정기에서 나온 바람

    # [아래쪽 순환] 시계 방향
    for i in range(down + 1, R - 1): board[i][0] = board[i + 1][0]  # 1. 왼쪽
    for j in range(0, C - 1): board[R - 1][j] = board[R - 1][j + 1] # 2. 아래쪽
    for i in range(R - 1, down, -1): board[i][C - 1] = board[i - 1][C - 1] # 3. 오른쪽
    for j in range(C - 1, 1, -1): board[down][j] = board[down][j - 1] # 4. 위쪽
    board[down][1] = 0 # 청정기에서 나온 바람

# 5. T초 동안 반복
for _ in range(T):
    spread()
    clean()

# 6. 먼지 총합 계산
ans = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            ans += board[i][j]

print(ans)