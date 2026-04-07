import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    grid = input_data[1:6]
    
    # 1. 2차원 입력을 1차원 상태(col_state)로 압축
    # 0: 하양(.), 1: 검정(X), -1: 모름(?)
    col_state = []
    for j in range(N):
        has_x = False
        has_dot = False
        for i in range(5):
            if grid[i][j] == 'X':
                has_x = True
            elif grid[i][j] == '.':
                has_dot = True
                
        # 한 열에 X와 .이 동시에 있으면 절대 불가능한 바코드 오류
        if has_x and has_dot:
            print("UNDETERMINABLE")
            return
            
        if has_x:
            col_state.append(1)
        elif has_dot:
            col_state.append(0)
        else:
            col_state.append(-1)
            
    # 2. DP 테이블 초기화
    # dp[현재 열(i)][현재 색깔(c)][연속된 칸 수(l)]
    dp = [[[0] * 3 for _ in range(2)] for _ in range(N)]
    
    # 0번째 열의 초기 세팅 (거름망 역할의 시작점)
    if col_state[0] in (1, -1):
        dp[0][1][1] = 1
    if col_state[0] in (0, -1):
        dp[0][0][1] = 1
        
    # 3. 점화식을 통한 경우의 수 누적
    for i in range(1, N):
        for c in range(2):
            # 현재 열의 색이 이미 고정되어 있는데, c와 다르다면 불가능한 상태이므로 패스
            if col_state[i] != -1 and col_state[i] != c:
                continue
                
            # 조건 1. 길이 2 (이전 열과 동일한 색깔 유지)
            dp[i][c][2] = dp[i-1][c][1]
            
            # 조건 2. 길이 1 (이전 열과 다른 색깔에서 새로 시작)
            # 총 가짓수가 2 이상인지만 알면 되므로, 불필요하게 숫자가 커지는 것을 막기 위해 min(2, ...) 처리
            dp[i][c][1] = min(2, dp[i-1][1-c][1] + dp[i-1][1-c][2])
            
    # 마지막 열까지 도달했을 때, 가능한 모든 올바른 바코드의 경우의 수 합산
    total_ways = 0
    end_c, end_l = -1, -1
    
    for c in range(2):
        for l in range(1, 3):
            if dp[N-1][c][l] > 0:
                total_ways += dp[N-1][c][l]
                end_c = c
                end_l = l
                
    # 완성된 바코드 경우가 정확히 1개가 아니라면(0개거나 여러 개) 복원 불가
    if total_ways != 1:
        print("UNDETERMINABLE")
        return
        
    # 4. 역추적 (Backtracking)을 통해 맨 뒤에서부터 원래 픽셀 색상 복원
    pixels = [-1] * N
    cur_i = N - 1
    cur_c = end_c
    cur_l = end_l
    
    while cur_i >= 0:
        pixels[cur_i] = cur_c
        if cur_l == 2:
            cur_i -= 1
            cur_l = 1
        else: # cur_l == 1
            if cur_i == 0:
                break
            prev_c = 1 - cur_c
            
            # 이전 색상(prev_c)의 길이가 1이었는지 2였는지 확인하여 확정된 길을 따라 거슬러 올라감
            if dp[cur_i-1][prev_c][1] == 1:
                cur_l = 1
            else:
                cur_l = 2
                
            cur_c = prev_c
            cur_i -= 1
            
    # 5. 복원된 픽셀 덩어리를 문제 규칙에 맞게 0(얇은 바)과 1(두꺼운 바)로 최종 변환
    result = []
    i = 0
    while i < N:
        color = pixels[i]
        length = 0
        
        # 같은 색상이 몇 칸 연속되는지 센다
        while i < N and pixels[i] == color:
            length += 1
            i += 1
            
        if length == 1:
            result.append('0')
        elif length == 2:
            result.append('1')
            
    print("".join(result))

if __name__ == '__main__':
    solve()