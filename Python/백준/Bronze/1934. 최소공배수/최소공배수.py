n=int(input())

def gcd(a, b):
     while b > 0:
        a, b = b, a % b
     return a

# 2. 공식을 이용해 최소공배수(LCM) 구하기
def lcm(a, b):
    return (a * b) // gcd(a, b)
for i in range(n):
    a,b=map(int,input().split())
    c=lcm(a,b)
    print(c)