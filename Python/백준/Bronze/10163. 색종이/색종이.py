import sys
input = sys.stdin.readline

n = int(input())

# 1. 도화지 생성
board = [[0] * 1001 for _ in range(1001)]

# 2. 색종이 덮어쓰기 (슬라이싱 최적화!)
for i in range(1, n + 1):
    x, y, w, h = map(int, input().split())
    
    # x부터 x+w-1 줄까지 반복
    for row in range(x, x + w):
        # 안쪽 for문 없이 y부터 y+h-1 칸까지 한 방에 i로 덮어쓰기
        board[row][y:y+h] = [i] * h

# 3. 면적 세기 (count 함수 최적화!)
area = [0] * (n + 1)

for row in board:
    for i in range(1, n + 1):
        # 각 줄(row)에서 i번 색종이가 몇 개 있는지 한 번에 세서 더함
        area[i] += row.count(i)

# 4. 정답 출력
for i in range(1, n + 1):
    print(area[i])