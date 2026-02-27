w=input().upper()
a=list(set(w))
b=[]
for c in a:
    b.append(w.count(c))
m=max(b)
if b.count(m)>=2:
    print("?")
else:
    d=b.index(m)
    print(a[d])
    