from collections import deque as dq
a,b=map(int,input().split())
if a==b:
    print(0)
    print(1)
    exit()
visit=[-1]*(10**5+1)
INF=int(1e9)
dp=[0]*(10**5+1)
dp[a]=1
q=dq([])
q.append(a)
visit[a]=0
limit=INF
while q:
    t=q.popleft()
    m=[t-1,t+1,2*t]
    for i in m:
        if 0<=i<=100000:
            if visit[i]==-1 and visit[t]+1<limit:
                visit[i]=visit[t]+1
                dp[i]=dp[t]
                if i!=b:
                    q.append(i)
                else:
                    limit=visit[i]
            elif visit[i]==visit[t]+1:
                dp[i]+=dp[t]
print(visit[b])
print(dp[b])