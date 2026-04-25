from bisect import bisect_left, bisect_right
import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int, input().split()))
low=[]
table={}
k=0
t=0
last_k=-1
row=[]
def put(t,k,value):
    table[(t,k)]=value
    while len(row)<=k:
        row.append([])
    if not row[k] or row[k][-1]!=t:
        row[k].append(t)
for i in range(n):
    x=l[i]
    if not low:
        low.append(x)
        k=0
        put(t,k,x)
        last_k=k
        continue
    if low[-1] < x:
        low.append(x)
        k=len(low) - 1
        put(t,k,x)
        last_k=k
    elif low[-1]>x:
        k=bisect_left(low,x)
        if last_k>=k:
            t+=1
        last_k=k
        low[k]=x
        put(t,k,x)
    else:
        continue
print(len(low))
start=(row[len(low)-1][-1],len(low)-1)
result=[]
while True:
    result.append(table[start])
    col=start[1]-1
    if col<0:
        break
    n_start=(start[0],col)
    if n_start not in table:
        idx=bisect_right(row[col],start[0]) - 1
        if idx<0:
            break
        n_start=(row[col][idx], col)
    start=n_start
print(*result[::-1])