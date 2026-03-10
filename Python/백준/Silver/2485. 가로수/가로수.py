# 아까 완벽하게 이해하신 그 유클리드 호제법 함수!
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())

# 1. 심어진 가로수 위치 모두 입력받기
trees = []
for _ in range(n):
    trees.append(int(input()))

# 2. 가로수들 사이의 간격 구하기
intervals = []
for i in range(1, n):
    intervals.append(trees[i] - trees[i-1])

# 3. 모든 간격의 최대공약수(GCD) 구하기
# 첫 번째 간격을 초기값으로 잡고, 다음 간격들과 계속 GCD를 갱신해 나갑니다.
g = intervals[0]
for i in range(1, len(intervals)):
    g = gcd(g, intervals[i])

# 4. 정답 계산 (선생님의 공식 적용!)
# (마지막 나무 위치 - 처음 나무 위치) // 최대공약수 + 1 - (기존 나무 개수)
total_trees = (trees[-1] - trees[0]) // g + 1
print(total_trees - n)