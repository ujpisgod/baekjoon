from collections import deque as dq
a,b=map(int,input().split())
k=dq([])
l=[-1]*100001
if a==b:
    print(0)
    exit()
k.append(a)
l[a]=0
while k:
    n=k.popleft()
    tt=[n-1,n+1,2*n]
    for i in tt:
        if 0<=i<=100000:
            if i==b:
                print(l[n]+1)
                exit()
            if l[i]==-1:
                l[i]=l[n]+1
                k.append(i)
           