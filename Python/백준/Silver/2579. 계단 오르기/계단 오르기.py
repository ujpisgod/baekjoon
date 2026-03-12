n=int(input())
a=[0]
b=[]
stack=0
c=0
for i in range(n):
    a.append(int(input()))
a.append(0)
b.append(a[0])
b.append(a[1])
b.append(a[1]+a[2])
for i in range(3,len(a)):
    g=max((b[i-2]+a[i]),(b[i-3]+a[i-1]+a[i]))
    b.append(g)

print(b[n])