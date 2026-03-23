import sys
input=sys.stdin.readline
a,b=map(int,input().split())
c=[0]*(a+1)
for i in range(1,a+1):
    c[i]=i
for i in range(b):
    p,q=map(int,input().split())
    c[p],c[q]=c[q],c[p]
c.pop(0)
print(*c)
    