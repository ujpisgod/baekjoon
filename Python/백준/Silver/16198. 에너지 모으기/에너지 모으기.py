import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
max_energy = 0

def solve(current_list, current_sum):
    global max_energy
    
    # 1. 종료 조건: 구슬이 2개만 남으면 끝!
    if len(current_list) == 2:
        max_energy = max(max_energy, current_sum)
        return
    
    # 2. 첫 번째와 마지막 구슬은 못 고르니까 1부터 len-2까지
    for i in range(1, len(current_list) - 1):
        # 에너지 계산: 양옆의 곱 (문제에서 곱하기라고 했어!)
        energy = current_list[i-1] * current_list[i+1]
        
        # 3. i번째 구슬을 뺀 '새 리스트'를 만들어서 다음 재귀로 토스!
        # current_list 자체는 변하지 않아서 for문이 꼬이지 않아.
        solve(current_list[:i] + current_list[i+1:], current_sum + energy)

solve(l, 0)
print(max_energy)