a,b=map(int,input().split())
c,d=map(int,input().split())
n=c*b+a*d
m=b*d
while m>0:
    n,m=m,(n%m)
print(((c*b+a*d)//n),(b*d//n))