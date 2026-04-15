import heapq
def solution(operations):
    answer = []
    q1=[]
    q2=[]
    check={}
    for i in operations:
        a,b=i.split()
        bb=int(b)
        if a=='I':
            heapq.heappush(q1,bb)
            heapq.heappush(q2,-bb)
            check[bb]=check.get(bb,0)+1
        elif a=='D' and bb==-1 and q1:
            while q1:
                k1=heapq.heappop(q1)
                if check.get(k1,0)!=0:
                    check[k1]-=1
                    break
                elif check.get(k1,0)==0:
                    continue
        elif a=='D' and bb==1 and q2 :
            while q2:
                k2=-1*heapq.heappop(q2)
                if check.get(k2,0)!=0:
                    check[k2]-=1
                    break
                elif check.get(k2,0)==0:
                    continue
    ans=[]
    for i in q1:
        if check.get(i,0)!=0:
            ans.append(i)
    if ans:
        answer.append(max(ans))
        answer.append(min(ans))
    else:
        answer=[0,0]
    return answer