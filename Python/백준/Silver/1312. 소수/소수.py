a,b,n=map(int,input().split())
if a%b==0:
    print(0)
    exit()
else:
    a%=b
num=0
while num<n:
    a*=10
    t=a//b
    a%=b
    num+=1
print(t)