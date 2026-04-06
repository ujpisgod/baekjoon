a,b,c=map(int,input().split())
if b<=a//2:
    b=a-b
if c<=a//2:
    c=a-c
print(4*(b*c))