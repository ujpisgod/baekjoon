b1=[]
b2=[]
for i in range(3):
    a1,a2=map(int,input().split())
    if a1 not in b1 :
        b1.append(a1)
    else:
        b1.remove(a1)
    if a2 not in b2:
        b2.append(a2)
    else:
        b2.remove(a2)
print(b1[0],b2[0])
        
        