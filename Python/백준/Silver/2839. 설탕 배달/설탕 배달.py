n = int(input())
r = 0

while True:
    if n % 5 == 0:  # 5로 나누어 떨어지면 끝!
        r += n // 5
        print(r)
        break
    elif n < 0:     # 3씩 빼다가 음수가 되면 못 만드는 숫자니까 끝!
        print(-1)
        break
    else:           # 둘 다 아니면 일단 3을 빼고 본다!
        n -= 3
        r += 1
        