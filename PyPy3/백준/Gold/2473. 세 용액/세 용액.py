import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
l.sort()
cs=int(1e12)
for i in range(n-1):
    start=i+1
    end=n-1
    while start<end:
        c=l[i]+l[start]+l[end]
        k=min(abs(c),abs(cs))
        if k!=cs:
            ii,st,en=i,start,end
        cs=k
        if c<0:
            start+=1
        elif c>0:
            end-=1
        elif c==0:
            print(l[i],l[start],l[end])
            exit()
print(l[ii],l[st],l[en])