import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 사람 수
t = int(input()) # 게임 횟수
# 사람들을 원형 큐(deque)에 넣습니다.
u = deque(map(int, input().split()))
# 각 판마다 외치는 층수들
v = list(map(int, input().split()))

for count in v:
    # 핵심: (count - 1)만큼 왼쪽으로 회전시킵니다.
    # 손을 밑에서 빼서 위로 올리는 동작을 한 번에 처리합니다.
    u.rotate(-(count - 1))
    
    # 이제 맨 앞(가장 아래)에 있는 사람이 당첨자입니다.
    print(u[0], end=' ')