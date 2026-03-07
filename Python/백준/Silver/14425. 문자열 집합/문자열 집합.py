a,b=map(int,input().split())
l=[input() for i in range(a)]
li=set(l)
c=0
w=[input() for i in range(b)]
for i in w:
    if i in li:
        c+=1
print(c)