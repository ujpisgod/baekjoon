a,b=map(int,input().split())
c=[]
t=0
for i in range(a):
    c.append(int(input()))
for i in range(a - 1, -1, -1):
    if b == 0: 
        break
    t += b // c[i]
    b %= c[i]       
print(t)