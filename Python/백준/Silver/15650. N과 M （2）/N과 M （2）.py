import sys

# N과 M 입력 받기
n, m = map(int, sys.stdin.readline().split())
ans = []

def solve(start):
    if len(ans) == m:
        print(*(ans))
        return
    for i in range(start, n + 1):
        ans.append(i)    # 숫자 선택해서 바구니에 넣기
        solve(i + 1)     # 다음 칸은 '현재 뽑은 숫자 + 1'부터 시작하도록 넘겨줌 (오름차순 보장!)
        ans.pop()        # ★중요★ 다음 경우의 수를 위해 방금 넣었던 숫자를 다시 빼기 (백트래킹)

# 1부터 시작하는 재귀 함수 호출
solve(1)