def solution(A, B):
    from collections import Counter
    from bisect import bisect_right
    b=max(B)
    nb=set(B)
    nB=sorted(list(nb))
    answer = 0
    pr=list(range(len(nB)+1))
    cnt=Counter(B)
    def find(x):
        while pr[x]!=x:
            pr[x]=pr[pr[x]]
            x=pr[x]
        return x
    def union(a,b):
        aa=find(a)
        bb=find(b)
        if bb<aa:
            pr[bb]=aa
        elif aa<bb:
            pr[aa]=bb
    sc=0
    for i in A:
        if i<= b:
            c=bisect_right(nB,i)
            x=find(c)
            if x==len(nB):
                continue
            if cnt.get(nB[x],0)>=1:
                cnt[nB[x]]-=1
                sc+=1
                if cnt.get(nB[x],0)==0 and i!=b:
                    union(x,x+1)
    answer=sc
    return answer