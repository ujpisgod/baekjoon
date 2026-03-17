import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 1. 누적 합 배열을 n + 1 크기로 만듭니다. (인덱스 에러 방지!)
b = [0] * (n + 1)

# 2. 1번째 인덱스부터 차곡차곡 누적 합을 채웁니다.
for i in range(n):
    b[i + 1] = b[i] + a[i]

for _ in range(m):
    p, q = map(int, input().split())
    # 3. p번째부터 q번째까지의 구간 합을 구합니다.
    print(b[q] - b[p - 1])