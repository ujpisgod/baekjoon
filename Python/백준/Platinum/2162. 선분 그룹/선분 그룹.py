import sys
input=sys.stdin.readline
n=int(input())
pr=list(range(n+1))
line=[]
def find(x):
    root=x
    while pr[root]!=root:
        root=pr[root]
    while pr[x]!=x:
        nxt=pr[x]
        pr[x]=root
        x=nxt
    return root
def union(a,b):
    aa=find(a)
    bb=find(b)
    if aa>bb:
        pr[aa]=bb
    else:
        pr[bb]=aa
for i in range(n):
    x1,y1,x2,y2=map(int,input().split())
    line.append(((x1,y1),(x2,y2)))
def ccw(a,b,c):
    x1,y1=a
    x2,y2=b
    x3,y3=c
    v=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    if v>0:
        return 1
    if v<0:
        return -1
    return 0
def intersect(a,b,c,d):
    ab = ccw(a,b,c)*ccw(a,b,d)
    cd = ccw(c,d,a)*ccw(c,d,b)
    if ab==0 and cd==0:
        if a>b:
            a,b=b,a
        if c>d:
            c,d=d,c
        return c<=b and a<=d
    return ab<=0 and cd<=0
for i in range(n):
    for j in range(i+1,n):
        if intersect(line[i][0],line[i][1],line[j][0],line[j][1]):
            union(i,j)
g=[0]*(n+1)
for i in range(n):
    g[find(i)]+=1
s=0
for i in g:
    if i>0:
        s+=1
print(s)
print(max(g))