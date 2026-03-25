n=int(input())
c=[]
l=[]
for i in range(n):
    a,b=map(int,input().split())
    c.append((b,a))
c.sort()
l.append(c[0])
t=1
while t<n:
    if l[-1][0]<=c[t][1]:
        l.append(c[t])
        t+=1
    else:
        t+=1
print(len(l))