import sys
input = sys.stdin.readline

n = int(input())

# 1. 가로 1001, 세로 1001 크기의 빈 도화지(2차원 배열)를 0으로 생성
# 메모리 제한(64MB) 안에서 아주 안전하고 가벼운 방식이야!
board = [[0] * 1001 for _ in range(1001)]

# 2. 색종이 덮어쓰기
for i in range(1, n + 1):
    x, y, w, h = map(int, input().split())
    # 입력받은 영역을 현재 색종이 번호(i)로 덮어씀
    for row in range(x, x + w):
        for col in range(y, y + h):
            board[row][col] = i

# 3. 각 번호별 면적을 저장할 리스트 (인덱스 1부터 n까지 사용하기 위해 n+1 크기로 만듦)
area = [0] * (n + 1)

# 4. 도화지 전체를 딱 한 번만 훑으면서 면적 세기 (시간 단축의 핵심!)
for row in board:
    for cell in row:
        if cell > 0:  # 0(빈칸)이 아니라면
            area[cell] += 1  # 해당 색종이 번호의 면적 1 증가

# 5. 정답 출력
for i in range(1, n + 1):
    print(area[i])