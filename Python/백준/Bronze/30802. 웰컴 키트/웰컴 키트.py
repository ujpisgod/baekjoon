num=int(input())
n=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
for i in n:
    if i==0:
        continue
    else:
        k+=(i-1)//a+1
print(k)
print(num//b,num%b)