a,b=map(int,input().split())
m=[True]*(b+1)
m[0]=False
m[1]=False
for i in range(b+1):
    if m[i]==False:
        continue
    else:
        for j in range(2*i,b+1,i):
            m[j]=False
for i in range(a,b+1):
    if m[i]==True:
        print(i)
        