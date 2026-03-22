n,m=map(int,input().split())
li=list(map(int,input().split()))
end=max(li)
start=0
result=0
while end>=start:
    to=0
    mid=(end+start)//2
    a=[i-mid for i in li if i>mid]
    to=sum(a)
    if to>=m:
        result=mid 
        start=mid+1
    else:
        end = mid - 1
print(result)