import sys
n = int(sys.stdin.readline())
m=[True]*(10**6+1)
m[0]=False
m[1]=False
for i in range(2,10**6):
    if m[i]==False:
        continue
    else:
        for j in range(2*i,10**6+1,i):
            m[j]=False
for _ in range(n):
    a = int(sys.stdin.readline())
    n1 = 0
    for i in range(2, (a // 2) + 1):
        if m[i] == True and m[a - i] == True:
            n1 += 1        
    print(n1)
