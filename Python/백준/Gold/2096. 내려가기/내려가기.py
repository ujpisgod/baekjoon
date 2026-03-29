n= int(input())
a1=[0,0,0]
a2=[0,0,0]
r1=[[0,0],[0,0],[0,0]]
r2=[[0,0],[0,0],[0,0]]
c=[(0,max),(1,min)]
def num1(x):
    if x==1:
        return a1
    elif x==0:
        return a1[0:2]
    elif x==2:
        return a1[1:3]
def num2(x,k):
    if x==1:
        return r1[0][k],r1[1][k],r1[2][k]
    elif x==0:
        return r1[0][k],r1[1][k]
    elif x==2:
        return r1[1][k],r1[2][k]
new=True
count=0
if n==1:
    c=list(map(int,input().split()))
    print(max(c),min(c))
    exit()
while count<n:
    if new:
        a1[0],a1[1],a1[2]=map(int,input().split())
        a2[0],a2[1],a2[2]=map(int,input().split())
        for j in range(3):
            for i in c:
                r1[j][i[0]]=a2[j]+i[1](num1(j))
        new=False
        count+=2
    else:
        a2[0],a2[1],a2[2]=map(int,input().split())
        for j in range(3):
            for i in c:
                r2[j][i[0]]=a2[j]+i[1](num2(j,i[0]))
        for i in range(3):
            for j in range(2):
                r1[i][j]=r2[i][j]
        count+=1
r1.sort(key=lambda x:x[0])
print(r1[2][0],end=" ")
r1.sort(key=lambda x:x[1])
print(r1[0][1])