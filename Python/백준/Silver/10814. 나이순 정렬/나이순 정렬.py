n=int(input())
m=1
t=[]
for i in range(n):
    a,b=input().split()
    t.append((int(a),m,b))
    m+=1
t.sort()
for (p,q,r) in t:
    print(p,r)