import math

n, k = map(int, input().split())
divisors = set() 
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        divisors.add(i)        # 내 값 넣고!
        divisors.add(n // i)   # 짝꿍 값도 넣고!
ans = sorted(divisors)
if len(ans) < k:
    print(0)
else:
    print(ans[k - 1])