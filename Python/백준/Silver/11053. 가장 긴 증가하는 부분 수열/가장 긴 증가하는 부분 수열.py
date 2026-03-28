n=int(input())
l=list(map(int,input().split()))
low=[1]*n
for i in range(1,n):
    for j in range(i):
        if l[j]<l[i]:
            low[i]=max(low[i],low[j]+1)
print(max(low))