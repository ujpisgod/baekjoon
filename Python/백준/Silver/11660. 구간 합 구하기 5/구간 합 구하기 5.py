import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 1. 원본 배열 입력
arr = [list(map(int, input().split())) for _ in range(n)]

# 2. '0'으로 테두리가 둘러진 (N+1) x (N+1) 누적 합 배열(dp) 생성!
dp = [[0] * (n + 1) for _ in range(n + 1)]

# 3. 0행과 0열은 '0'이므로 무시하고, 1부터 n까지 예쁘게 채워줍니다.
for r in range(1, n + 1):
    for c in range(1, n + 1):
        # 현재 값 = 위쪽 누적합 + 왼쪽 누적합 - 대각선 중복 제거 + '내 원본 값'
        dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + arr[r-1][c-1]

# 4. 좌표 계산 (마이너스 인덱스 걱정 끝!)
for _ in range(m):
    r1, c1, r2, c2 = map(int, input().split())
    # 질문자님이 완벽하게 구상하셨던 그 수식 그대로입니다!
    ans = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]
    print(ans)