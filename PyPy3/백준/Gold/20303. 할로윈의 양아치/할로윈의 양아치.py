from collections import deque as dq
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
candy=list(map(int,input().split()))
fr=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    fr[a].append(b)
    fr[b].append(a)
visit=[False]*(n+1)
group_candy=[]
for i in range(1,n+1):
    c=0
    num=0
    q=dq()
    if visit[i]==False:
        q.append(i)
        visit[i]=True
        while q:
            a=q.popleft()
            c+=candy[a-1]
            num+=1
            for j in fr[a]:
                if not visit[j]:
                    visit[j]=True
                    q.append(j)
                    
        group_candy.append((num,c))
bag=[0]*k
for i,j in group_candy:
    for p in range(k-1,i-1,-1):
        bag[p]=max(bag[p],bag[p-i]+j)
print(max(bag))