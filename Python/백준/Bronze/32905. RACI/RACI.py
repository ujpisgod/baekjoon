a,b=map(int,input().split())
m=0
c=[]
for i in range(a):
    c.append(input().split())

for i in range(a):        
    if 'A' in c[i]:
        c[i].remove('A')
        m+=1
        if 'A'in c[i]:
            print('No')
            exit()
if m==a:
    print('Yes')
else:
    print('No')