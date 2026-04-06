import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

# 중앙값, 최빈값, 범위를 구하기 위해 일단 정렬!
a.sort()

# 1. 산술평균 (round 함수 쓰면 깔끔하게 해결됨)
print(round(sum(a) / n))

# 2. 중앙값 (0부터 시작하니까 n // 2 가 딱 정중앙 인덱스야)
print(a[n // 2])

# 3. 최빈값 (Counter의 마법)
# Counter(a).most_common()은 [(최빈값1, 빈도), (최빈값2, 빈도)] 형태로,
# 빈도수가 높은 순서대로 알아서 예쁘게 묶어줘!
cnt = Counter(a).most_common()

# 최빈값이 여러 개일 때 (두 번째로 작은 값 출력)
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0]) 
else:
    print(cnt[0][0])

# 4. 범위 (max, min 함수보다 그냥 정렬된 리스트의 끝 - 처음이 훨씬 빠름!)
print(a[-1] - a[0])