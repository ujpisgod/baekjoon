a=list(map(int,input().split()))
s=sum(a)-max(a)
if (s-1)<max(a):
    print(2*s-1)
else:
    print(sum(a))