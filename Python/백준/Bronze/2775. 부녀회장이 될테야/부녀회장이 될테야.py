n=int(input())
b=[[0]*15 for x in range(15)]
for i in range(15):
    b[0][i]=i
for i in range(1,15):
    for j in range(1,15):
        b[i][j]=b[i-1][j]+b[i][j-1]
for _ in range(n):
    n1=int(input())
    k=int(input())
    print(b[n1][k])
        
