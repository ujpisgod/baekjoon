from collections import deque as dq
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
testcase=int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(testcase):
    l=[]
    h,w=map(int,input().split())
    l.append(['.']*(w+2))
    for i in range(h):
        l.append(['.']+list(input().strip())+['.'])
    l.append(['.']*(w+2))
    keys=list(map(ord,input().strip()))
    key=[False]*26
    if keys!=[48]:
        for i in keys:
            key[i-97]=True
    s=set()
    for i in range(1,h+1):
        for j in range(1,w+1):
            if 96<ord(l[i][j])<123:
                s.add(l[i][j])
    cnt=0
    for i in range(len(s)+1):
        stop=0
        visit=[[False]*(w+2) for i in range(h+2)]
        q=dq()
        q.append((0,0))
        visit[0][0]=True
        while q:
            y,x=q.popleft()
            for j in range(4):
                ny=y+dy[j]
                nx=x+dx[j]
                if 0<=ny<(h+2) and 0<=nx<(w+2) and visit[ny][nx]==False:
                    c=ord(l[ny][nx])
                    if -1<c-65<26 and key[c-65]:
                        q.append((ny,nx))
                        visit[ny][nx]=True
                    elif 96<c<123:
                        stop-=1
                        q.append((ny,nx))
                        visit[ny][nx]=True
                        l[ny][nx]='.'
                        key[c-97]=True
                    elif c==36:
                        q.append((ny,nx))
                        visit[ny][nx]=True
                        l[ny][nx]='.'
                        cnt+=1
                    elif c==46:
                        q.append((ny,nx))
                        visit[ny][nx]=True
        if stop==0:
            break
    print(cnt)