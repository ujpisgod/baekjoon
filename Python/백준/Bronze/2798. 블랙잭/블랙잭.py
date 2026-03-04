n,p=map(int,input().split())
a=list(map(int,input().split()))    
a.sort()
b=set()
for i in range(n):
    t1=a[n-1-i]
    ind1=n-1-i
    for j in range(n):
        t2=a[n-1-j]
        ind2=n-1-j
        if ind1==ind2:
            continue
        for k in range(n):
            t3=a[n-1-k]
            ind3=n-1-k
            if ind2==ind3 or ind1==ind3:
                continue
            if t1+t2+t3<=p:
                c=t1+t2+t3
                b.add(c)
            else:
                continue
print(max(b))