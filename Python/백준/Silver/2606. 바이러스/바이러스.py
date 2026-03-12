n=int(input())
m=int(input())
if m==0:
    print(0)
    exit()
k=[]
c=[1]
for i in range(m):
    a,b=map(int,input().split())
    k.append([a,b])
t=0
l=0
p=0
while True:
    if k[t][0]==c[l] and k[t][1] not in c:
        c.append(k[t][1])
    elif k[t][1]==c[l] and k[t][0] not in c:
        c.append(k[t][0])
    t+=1
    if t==m:
        l+=1
        t=0
    if l>=len(c):
        break
c1=set(c)
print(len(c1)-1)