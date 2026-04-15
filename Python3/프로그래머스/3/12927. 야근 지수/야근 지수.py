import heapq
def solution(n, works):
    new=[-x for x in works]
    heapq.heapify(new)
    if sum(works)<=n:
        return 0
    while n>0:
        a=heapq.heappop(new)
        a+=1
        n-=1
        heapq.heappush(new,a)
    new2=[x**2 for x in new]
    answer=sum(new2)
    return answer
