import sys
input = sys.stdin.readline
n,a=map(int,input().split())
m=(n+9)//10
a1=[]
for i in range(m):
    a1.extend([1,0,0,1,0,0,1,0,0,0])
a2=a1[0:n]
s=sum(a2)
for i in range(a):
    c=int(input())-1
    if a2[c]==0:
        a2[c]+=1
        s+=1
    else:
        a2[c]-=1
        s-=1
    print(s)
