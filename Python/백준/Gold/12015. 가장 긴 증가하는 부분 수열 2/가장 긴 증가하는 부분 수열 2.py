from bisect import bisect_left, bisect_right
n=int(input())
l=list(map(int,input().split()))
low=[]
for i in range(n):
    if low:
        if low[-1]>l[i]:
            low[bisect_left(low, l[i])]=l[i]
        elif low[-1]<l[i]:
            low.append(l[i])
    else:
        low.append(l[i])
print(len(low))