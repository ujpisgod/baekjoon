n = int(input())
m = list(map(ord, input().upper()))

# 1. 글자를 1~26의 숫자로 변환
for i in range(n):
    m[i] -= 64

# 2. 호너의 법칙 적용 (뒤에서부터 거꾸로 계산!)
su = 0
# n-1부터 0까지 1씩 줄어들면서 역순으로 순회
for i in range(n - 1, -1, -1):
    su = (su * 31 + m[i]) % 1234567891

print(su)