from collections import deque as dq
n = int(input())
visit=[False]*(n+1)
q=dq()
q.append(n)
ll=[0]*(n+1)
def is1():
    global t
    if t<=1:
        return 1
    else:
        return 0
t=0
visit[n]=True
fin=False
while q:
    t=q.popleft()
    k=[(t//3,t%3),(t//2,t%2),(t-1,is1())]
    for i in k:
        if i[1]==0 and visit[i[0]]==False:
            q.append(i[0])
            visit[i[0]]=True
            ll[i[0]]=ll[t]+1
            if i[0]==1:
                fin=True
    if fin==True:
        break
print(ll[1])