m,n=map(int,input().split())
a=m
b=n

while b>0:
    a,b=b,(a%b)
print(m*n//a)