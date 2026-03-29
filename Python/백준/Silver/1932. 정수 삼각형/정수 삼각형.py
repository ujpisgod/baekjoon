n=int(input())
k=[[0] for i in range(1,n+1)]
r=[[0]*i for i in range(1,n+1)]
for i in range(n):
    k[i]=list(map(int,input().split()))
for _ in range(n):
    r[n-1][_]=k[n-1][_]
for i in range(n-2,-1,-1):
    for j in range(i+1):
        r[i][j]=max(r[i+1][j],r[i+1][j+1])+k[i][j]
print(r[0][0])