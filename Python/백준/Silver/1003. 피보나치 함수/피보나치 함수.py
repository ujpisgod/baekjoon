import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = int(input())
    
    # 0과 1이 나오는 횟수를 담을 리스트 (초기값 세팅)
    zero_count = [1, 0]
    one_count = [0, 1]
    
    # 2부터 a까지, 피보나치 규칙대로 앞의 두 숫자를 더해나갑니다!
    for i in range(2, a + 1):
        zero_count.append(zero_count[i-1] + zero_count[i-2])
        one_count.append(one_count[i-1] + one_count[i-2])
        
    print(zero_count[a], one_count[a])