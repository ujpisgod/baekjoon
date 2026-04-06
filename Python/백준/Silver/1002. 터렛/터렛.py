import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # 두 원 중심 거리
    
    # 두 원이 완전히 일치
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    # 만나지 않음 (멀리 떨어짐 or 한 원이 다른 원 안에 들어감)
    elif d > r1 + r2 or d < abs(r1 - r2):
        print(0)
    # 내접 또는 외접
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
    # 두 점에서 만남
    else:
        print(2)