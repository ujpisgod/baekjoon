n=int(input())
p=list(map(int,input().split()))
a = sorted(list(set(p)))
b=[]
d={v: i for i,v in enumerate(a)}
for i in range(n):
    b.append(str(d[p[i]]))
print(" ".join(b))
    