a = int(input())
if a < 10:
    a *= 10
num = 0
a4 = a

while True:
    a2 = (a // 10) + (a % 10)           # 자리수 합
    a = (a % 10) * 10 + (a2 % 10)       # 새로운 수
    num += 1
    if a == a4:
        break

print(num)