a=input()
b=len(a)-1
c=0
for i in range(b):
    if a[i]!=a[b-i]:
        c+=1
if c==0:
    print(1)
else:
    print(0)