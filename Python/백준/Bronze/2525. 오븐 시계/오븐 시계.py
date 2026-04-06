a,b=map(int,input().split())
c=int(input())
d=c%60
c=c//60
if b+d>=60:
    a=a+1
    b=b-60
if a+c>=24:
    a=a-24
print(a+c,b+d)