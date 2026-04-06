from collections import deque as dq
a,b=map(int,input().split())
k=[list(map(int, input())) for i in range(a)]
c = [[-1] * b for _ in range(a)]
for i in range(a):
    for j in range(b):
        if k[i][j]==1:
            c[i][j]=-1
        elif k[i][j]==0:
            c[i][j]=False
c[0][0]=1
ll=dq([(0,0)])
while ll:
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    h=ll.popleft()
    for i in range(4):
        if -1< h[0]+dx[i]<a and -1<h[1]+dy[i]<b:
            if c[h[0]+dx[i]][h[1]+dy[i]]==-1:
                if (h[0]+dx[i],h[1]+dy[i])==(a-1,b-1):
                    print(c[h[0]][h[1]]+1)
                    exit()
                c[h[0]+dx[i]][h[1]+dy[i]]=c[h[0]][h[1]]+1
                ll.append((h[0]+dx[i],h[1]+dy[i]))
                