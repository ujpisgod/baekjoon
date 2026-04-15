from collections import deque as dq
def solution(begin, target, words):
    q=dq()
    answer=0
    q.append((begin,0))
    visit=[[False,0] for i in range(len(words)+1)]
    finish=False
    while not finish and q:
        a,b=q.popleft()
        for i,word in enumerate(words,start=1):
            if issame(a,word) and visit[i][0]==False:
                q.append((word,i))
                visit[i][0]=True
                visit[i][1]=visit[b][1]+1
                if word==target:
                    answer=visit[i][1]
                    finish=True
                    break
    return answer
def issame(a,b):
    c=0
    aa=list(a.strip())
    bb=list(b.strip())
    for i in range(len(aa)):
        if aa[i]==bb[i]:
            c+=1
    if c==len(aa)-1:
        return True
    else:
        return False