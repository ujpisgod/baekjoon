n=int(input())
c=[]
bigger=[]
for i in range(n):
    a,b=map(int,input().split())
    c.append([a,b])
for i in range(n):
    k=0
    for j in range(n):
        if i==j:
            continue
        if c[i][0]<c[j][0] and c[i][1]<c[j][1]:
            k+=1
    bigger.append(k+1)
print(*bigger)