n,k=map(int,input().split())
nk=(2*k)%10
b=[k%10,nk]
l=[]
for i in range(1,n+1):
    if i%10 not in b:
        l.append(i)
print(len(l))
if l:
    print(*l)