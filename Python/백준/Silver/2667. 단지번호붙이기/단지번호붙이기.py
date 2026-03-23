n=int(input())
li=[list(map(int,input()))for i in range(n)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]
num=0
def dfs(a,b):
    li[a][b]=0
    global home
    home+=1
    for i in range(4):
        if -1<a+dx[i]<n and -1<b+dy[i]<n:
            if li[a+dx[i]][b+dy[i]]==1:
                dfs(a+dx[i],b+dy[i])
nn=[]
for i in range(n):
    for j in range(n):
        if li[i][j]==1:
            home=0
            dfs(i,j)
            nn.append(home)
            num+=1
nn.sort()
print(num)
for i in nn:
    print(i)