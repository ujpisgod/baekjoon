import sys
input = sys.stdin.readline

n = int(input())
# 1. 삼각형을 입력받으면서 리스트의 리스트로 바로 만듭니다.
k = [list(map(int, input().split())) for _ in range(n)]

# 2. 맨 밑에서 두 번째 줄(n-2)부터 꼭대기(0)까지 거꾸로 올라갑니다.
for i in range(n - 2, -1, -1):
    # 3. 현재 층(i)에 있는 숫자의 개수는 i + 1개입니다.
    for j in range(i + 1): 
        # 4. 내 바로 밑의 양쪽 중 큰 값을 고르고, 내 값을 더해서 덮어씌웁니다.
        k[i][j] = max(k[i+1][j], k[i+1][j+1]) + k[i][j]

# 5. 꼭대기 도착! 모든 최대 누적합이 여기에 모여있습니다.
print(k[0][0])