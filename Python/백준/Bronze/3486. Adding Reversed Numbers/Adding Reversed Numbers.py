n=int(input())
for i in range(n):
    a,b=input().split()
    a,b=a[::-1],b[::-1]
    a=int(a)+int(b)
    a=str(a)[::-1]
    print(int(a))
    