import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
ma=[list(input().rstrip()) for _ in range(n)]
visit=[[False]*m for _ in range(n)]
stack=[]
def u(x,y):
    if y>0:
        return True
    else:
        return False
def d(x,y):
    global n
    if y<n-1:
        return True
    else:
        return False
def r(x,y):
    global m
    if x<m-1:
        return True
    else:
        return False
def l(x,y):
    if x>0:
        return True
    else:
        return False
stack=[]
ans=0
stt=[[0]*m for i in range(n)]
st=0
def dfs(y,x):
    global stemp
    global ans
    global st
    stt[y][x]=st
    visit[y][x]=True
    stack.append((y,x))
    k=[('U',u(x,y),y-1,x),('D',d(x,y),y+1,x),('L',l(x,y),y,x-1),('R',r(x,y),y,x+1)]
    for i in k:    
        if ma[y][x]==i[0]:
            if i[1] and visit[i[2]][i[3]]==False:
                dfs(i[2],i[3])
                break
            elif i[1] and visit[i[2]][i[3]]==True and stt[i[2]][i[3]]==st:
                ans+=1
                break
            elif not i[1]:
                ans+=1
                break
            else:
                return
for i in range(n):
    for j in range(m):
        if visit[i][j]==False:
            st+=1
            dfs(i,j)
print(ans)