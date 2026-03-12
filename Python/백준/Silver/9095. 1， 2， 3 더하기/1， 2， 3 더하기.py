n=int(input())
b=[0]*n
for i in range(n):
    b[i]=int(input())
u=[1,2,4]
for j in range(3,12):
    k=u[j-1]+u[j-2]+u[j-3]
    u.append(k)
for i in b:
    print(u[i-1])