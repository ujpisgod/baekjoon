from collections import deque as dq
def solution(n, computers):
    answer=0
    visit=[False]*n
    for i in range(n):
        if visit[i]==False:
            q=dq()
            visit[i]=True
            answer+=1
            q.append(computers[i])
            while q:
                a=q.popleft()
                for k,j in enumerate(a):
                    if j and visit[k]==False:
                        q.append(computers[k])
                        visit[k]=True
                
    return answer