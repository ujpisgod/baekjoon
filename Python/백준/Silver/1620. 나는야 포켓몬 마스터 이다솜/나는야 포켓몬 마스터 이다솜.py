a,b=map(int,input().split())
d1={}
d2={}
for i in range(1,a+1):
    u=input()
    d1[i]=u
    d2[u]=i
for i in range(b):
    c=input()
    if c.strip().isdigit()==True:
        print(d1[int(c)])
    else:
        print(d2[c])