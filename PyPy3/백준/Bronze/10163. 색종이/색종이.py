n=int(input())
p=set()
pp=[0]*n
papers = []
for _ in range(n):
    papers.append(tuple(map(int, input().split())))
for i in range(n-1,-1,-1):
    a,b,s,t=papers[i]
    for j in range(s):
        for k in range(t):
            if (a+j,b+k) not in p:
                p.add((a+j,b+k))
                pp[i]+=1
            else:
                continue
for i in pp:
    print(i)