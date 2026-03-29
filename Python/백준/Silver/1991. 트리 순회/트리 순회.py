n=int(input())
d={}
for i in range(n):
    a,b,c=input().split()
    d[a]=(b,c)
order=[(0,1,2),(1,0,2),(1,2,0)]
def pr(x,i):
    result.append(x)
def right(x,i):
    nx=d[x][1]
    re(nx,i)
def left(x,i):
    nx=d[x][0]
    re(nx,i)
f=[pr,left,right]
def re(x,i):
    if x=='.':
        return
    f[order[i][0]](x,i)
    f[order[i][1]](x,i)
    f[order[i][2]](x,i)
for i in range(3):
    result=[]
    re('A',i)
    print("".join(result))