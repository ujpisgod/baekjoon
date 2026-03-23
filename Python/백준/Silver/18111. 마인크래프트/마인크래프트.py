import sys

# 빠른 입력을 위한 세팅
input = sys.stdin.readline

# N: 세로, M: 가로, B: 초기 인벤토리 블록 수
N, M, B = map(int, input().split())

# 1. 2차원 배열을 굳이 다 저장하지 않고, '높이별 개수'만 딕셔너리에 압축해서 저장합니다!
height_counts = {}
for _ in range(N):
    for h in map(int, input().split()):
        # 방금 물어보셨던 get()을 활용한 딕셔너리 카운팅
        height_counts[h] = height_counts.get(h, 0) + 1

# 정답을 저장할 변수 (최소 시간은 무한대로, 높이는 0으로 초기화)
min_time = float('inf')
best_height = 0

# 2. 목표 높이(target_h)를 0층부터 256층까지 전부 다 해봅니다. (브루트포스)
for target_h in range(257):
    remove_blocks = 0
    place_blocks = 0
    
    # 3. 500x500 배열을 다 도는 게 아니라, 딕셔너리에 있는 종류(최대 257개)만 봅니다.
    for h, count in height_counts.items():
        if h > target_h:
            # 목표보다 높으면 깎아야 함
            remove_blocks += (h - target_h) * count
        elif h < target_h:
            # 목표보다 낮으면 채워야 함
            place_blocks += (target_h - h) * count
            
    # 4. 블록이 충분한지 확인 (기존 인벤토리 + 깎아서 얻은 블록 >= 채우는 데 쓴 블록)
    if remove_blocks + B >= place_blocks:
        # 걸린 시간 계산: 깎는 건 2초, 채우는 건 1초
        time = (remove_blocks * 2) + place_blocks
        
        # 5. 최소 시간 갱신 (시간이 같다면 더 높은 땅을 선택해야 하므로 <= 사용)
        if time <= min_time:
            min_time = time
            best_height = target_h

# 최종적으로 걸린 최소 시간과 그때의 땅 높이를 출력
print(min_time, best_height)