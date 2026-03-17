b=[0]*1001
b[1]=1
b[2]=3
for i in range(1,999):
    b[i+2]=(b[i+1]+2*b[i])%10007
print(b[int(input())])
 