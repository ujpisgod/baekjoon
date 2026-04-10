import sys
input=sys.stdin.readline
n=int(input())
k=input().rstrip() 
t=0
a=0
for i in k:
    if i.isdigit():
        a=a*10+int(i)
    else:
        t+=a
        a=0
t+=a
print(t)