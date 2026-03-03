m = int(input()) # 문제에서는 M, N으로 주어집니다
n = int(input())

# --- 회원님의 완벽한 에라토스테네스의 체 (변경 없음!) ---
sieve = [True] * (n + 1)
if n >= 0: sieve[0] = False
if n >= 1: sieve[1] = False

d = 2
while d**2 <= n:
    if sieve[d] == True:
        for j in range(d * 2, n + 1, d):
            sieve[j] = False
    d += 1
# --------------------------------------------------------

# 🌟 변경된 부분: 개수를 세지 말고, 진짜 소수들을 주머니(리스트)에 담습니다!
primes = []
for i in range(m, n + 1):  # m 이상 n 이하 (m 포함!)
    if sieve[i] == True:
        primes.append(i)

# 🌟 백준이 원하는 깐깐한 출력 조건 맞추기
if len(primes) == 0:
    print(-1)  # 소수가 하나도 없으면 -1 출력
else:
    print(sum(primes))  # 첫째 줄: 소수들의 합 (파이썬 내장 함수 sum 활용!)
    print(primes[0])    # 둘째 줄: 최솟값 (작은 수부터 차례대로 넣었으니 당연히 0번 방이 제일 작음!)