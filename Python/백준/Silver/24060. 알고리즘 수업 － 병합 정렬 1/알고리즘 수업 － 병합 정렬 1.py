n,m=map(int,input().split())
a=list(map(int,input().split()))
tmp=[0]*n
def merge_sort(a,p,r):
    global m
    global mm
    if p<r:
        q=(p + r)//2 
        merge_sort(a, p, q)     
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
mm=0
def merge(a, p, q, r):
    global m
    global mm
    i,j,t=p,q+1,0
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp[t]=a[i]
            mm+=1
            if mm==m:
                print(tmp[t])
                exit()
            i+=1
            t+=1
            
        else:
            tmp[t]=a[j]
            mm+=1
            if mm==m:
                print(tmp[t])
                exit()
            t+=1
            j+=1

            
    while i <=q:
        tmp[t]=a[i]
        mm+=1
        if mm==m:
            print(tmp[t])
            exit()
        t+=1
        i+=1
        
    while j <= r:
        tmp[t]=a[j]
        mm+=1
        if mm==m:
            print(tmp[t])
            exit()
        t+=1
        j+=1
        
        
    i,t=p,0;
    while i <= r:
        a[i]= tmp[t] 
        i+=1
        t+=1
merge_sort(a,0,n-1)
print(-1)