n=int(input())
isp=[True]*(n+1)
isp[0]=False
isp[1]=False
p=[]
for i in range(n):
    if isp[i]==True:
        for j in range(2*i,n+1,i):
            isp[j]=False
for i,j in enumerate(isp):
    if j:
        p.append(i)
c=0
l=0
r=0
cs= 0
lp=len(p)
while True:
    if cs==n:
        c+=1
    if cs>=n:
        cs-=p[l]
        l+= 1
    elif r==lp:
        break
    else:
        cs+=p[r]
        r+=1
print(c)