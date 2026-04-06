n=int(input())
k=set()
k.add('ChongChong')
for i in range(n):
    a,b=input().split()
    if a in k:
        k.add(b)
    if b in k:
        k.add(a)
print(len(k))