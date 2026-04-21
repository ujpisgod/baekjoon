from collections import deque as dq
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
l=[]
l.append([-1]*(m+2))
for i in range(n):
    l.append([-1]+list(map(int,input().strip()))+[-1])
l.append([-1]*(m+2))
dy=[0,0,1,-1]
dx=[1,-1,0,0]
id_=1
m1=[0]*(10**6)
for i in range(1,n+1):
    for j in range(1,m+1):
        if l[i][j]==0:
            id_+=1
            m1[id_]=1
            q=dq()
            q.append((i,j))
            l[i][j]=-1*id_
            while q:
                y,x=q.popleft()
                for k in range(4):
                    ny=y+dy[k]
                    nx=x+dx[k]
                    if l[ny][nx]==0:
                        l[ny][nx]=-1*id_
                        m1[id_]+=1
                        q.append((ny,nx))
ans=[['0']*m for i in range(n)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if l[i][j]==1:
            c=1
            s=set()
            for k in range(4):
                ny=i+dy[k]
                nx=j+dx[k]
                f=l[ny][nx]
                if f<-1 and f not in s:
                    c+=m1[-1*f]
                    s.add(f)
            c=c%10        
            ans[i-1][j-1]=str(c)
for i in ans:
    print("".join(i))