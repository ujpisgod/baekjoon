n=int(input())
m=[]
m2=[]
m=list(map(int,input().split()))
m2=list(input())
m3=[0]*n
for i in range(n):
    if m2[i]==' ':
        continue
    else:
        if ord(m2[i])>96:
            m3[i]=ord(m2[i])-70
        else:
            m3[i]=ord(m2[i])-64
if sorted(m3)==sorted(m):
    print('y')
else:
    print('n')