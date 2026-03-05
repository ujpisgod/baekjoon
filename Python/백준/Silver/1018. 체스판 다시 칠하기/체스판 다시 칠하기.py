n,m=map(int,input().split())
a1=[]
a2=[]
a3=[]
for i in range(n):
    b=list(input())
    a1.append(b)
b=0
w=0
for i in range(n-7):
    for j in range(m-7):
        for k in range(8):
            for r in range(8):
                if (r+k)%2==0:
                    if a1[i+k][j+r]=="W":
                        b+=1
                    if a1[i+k][j+r]=="B":
                        w+=1
                if (r+k)%2==1:
                    if a1[i+k][j+r]=="B":
                        b+=1
                    if a1[i+k][j+r]=="W":
                        w+=1
        a2.append(b)
        a2.append(w)
        b=0
        w=0
print(min(a2))