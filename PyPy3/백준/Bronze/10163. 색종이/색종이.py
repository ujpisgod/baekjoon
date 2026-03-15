n=int(input())
p=set()
pp=[0]*n
for i in range(n-1,-1,-1):
    a,b,s,t=map(int,input().split())
    for j in range(s):
        for k in range(t):
            if (a+j,b+k) not in p:
                p.add((a+j,b+k))
                pp[i]+=1
            else:
                continue
for i in pp:
    print(i)