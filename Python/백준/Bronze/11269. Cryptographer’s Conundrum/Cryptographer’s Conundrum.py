a=input()
k=len(a)
n=1
p=3*n-2
q=3*n-1
r=3*n-3
while len(a)>max(p,q,r):
    if a[p]=='E':
        k-=1
    if a[r]=='P':
        k-=1
    if a[q]=='R':
        k-=1
    n+=1
    p=3*n-2
    q=3*n-1
    r=3*n-3
    
print(k)