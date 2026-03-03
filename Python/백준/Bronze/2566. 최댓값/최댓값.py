a=[list(map(int,input().split())) for i in range(9)]
maxi=0
maxj=0
maxn=-1
for i in range(9):
    for j in range(9):
        if a[i][j]>maxn:
            maxn=a[i][j]
            maxi=i+1
            maxj=j+1
print(maxn)
print(maxi,maxj)