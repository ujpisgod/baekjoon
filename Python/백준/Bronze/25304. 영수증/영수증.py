tot=int(input())
num=int(input())
c=[]
q=0
w=0
for i in range(num):
    (a,b)=map(int,input().split())
    c.append((a,b))
for i in range(num):
    a1,b1=c[i]
    w += a1*b1
if w == tot:
    print("Yes")
else:
    print("No")
