import sys
sys.setrecursionlimit(10**6)
v,e=map(int,input().split())
rp = list(range(v + 1))
def find(x):
    if rp[x] != x:
        rp[x] = find(rp[x])
    return rp[x]
def union(a,b):
    ra = find(a)
    rb = find(b)
    if rb<ra:
        rp[ra]=rb
    else:
        rp[rb]=ra
t=0
kk=[]
for i in range(e):
    a,b,c=map(int,input().split())
    kk.append((a,b,c))
kk.sort(key=lambda x:x[2])

for i in kk:
    if find(i[0])!=find(i[1]):
        union(i[0],i[1])
        t+=i[2]
print(t)