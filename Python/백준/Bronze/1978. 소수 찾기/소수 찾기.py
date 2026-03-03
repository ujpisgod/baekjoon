n=int(input())
a=list(map(int,input().split()))
for i in a:
    d=2
    if i==1:
        n-=1
    while d**2<=i:
        if i%d==0:
            n-=1
            break
        elif i%d!=0:
            d+=1
print(n)