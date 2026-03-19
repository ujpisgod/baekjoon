import sys
sys.setrecursionlimit(10**6)

n1=int(input())
def chase(lis,a1,b1):
    if lis[a1][b1]==1:
        lis[a1][b1]=0
        chase(lis,a1-1,b1)            
        chase(lis,a1+1,b1)
        chase(lis,a1,b1-1)
        chase(lis,a1,b1+1)
    else:
        return
for _ in range(n1):
    x,y,n2=map(int,input().split())
    m=max(x,y)
    count=0
    a=[]
    for i in range(m+2):
        a.append([0]*(m+2))
    for i in range(n2):
        nx,ny=map(int,input().split())
        a[nx+1][ny+1]=1
    for i in range(1,m+2):
        for j in range(1,m+2):
            if a[i][j]==1:
                chase(a,i,j)
                count+=1
    print(count)