n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

white = 0 # 0의 개수
blue = 0  # 1의 개수

# 현재 구역의 시작점 x, y 그리고 한 변의 길이 n
def divide(x, y, n):
    global white, blue
    
    # 현재 구역의 첫 번째 칸 색깔을 기준점으로 잡습니다.
    color = a[x][y] 
    
    # 현재 구역 전체를 순회하면서 첫 번째 칸과 색이 같은지 확인!
    for i in range(x, x + n):
        for j in range(y, y + n):
            
            if color != a[i][j]: 
                # 앗! 색깔이 하나라도 다른 칸을 발견했다! -> 바로 4등분 시작
                divide(x, y, n // 2)                 # 1. 왼쪽 위
                divide(x, y + n // 2, n // 2)        # 2. 오른쪽 위
                divide(x + n // 2, y, n // 2)        # 3. 왼쪽 아래
                divide(x + n // 2, y + n // 2, n // 2) # 4. 오른쪽 아래
                
                return # 4등분으로 쪼개서 넘겼으니, 현재 구역 탐색은 여기서 즉시 종료!
                
    # for문을 무사히 다 돌았다면? -> 구역 전체가 모두 같은 색이라는 뜻!
    if color == 0:
        white += 1
    else:
        blue += 1

# 처음에는 전체 종이의 시작점 (0, 0)과 전체 길이 n을 넣고 시작합니다.
divide(0, 0, n)

print(white)
print(blue)