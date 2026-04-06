n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=a
    d=b
    while d>0:
        c,d=d,c%d
    print(a*b//c)