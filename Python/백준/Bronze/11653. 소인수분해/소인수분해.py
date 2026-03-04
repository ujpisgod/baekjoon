n=int(input())
d=2
if n!=1:
    while d**2<=n:
        while n%d==0:
            n=n//d
            print(d)
        d+=1
    if n>1:
        print(n)