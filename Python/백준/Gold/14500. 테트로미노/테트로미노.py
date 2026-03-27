m=0
def ismax(x):
    global m
    if x>m:
        m=x
    return m
a,b=map(int,input().split())
map_=[list(map(int,input().split())) for i in range(a)]
def L1(x,y):
    global a
    global b
    if x+1<b and y+2<a:
        return map_[y][x]+map_[y+1][x]+map_[y+2][x]+map_[y+2][x+1]
    else:
        return 0
def L2(x,y):
    global a
    global b
    if x+2<b and y+1<a:
        return map_[y][x]+map_[y+1][x]+map_[y][x+1]+map_[y][x+2]
    else:
        return 0
def L3(x,y):
    global a
    global b
    if x+1<b and y+2<a:
        return map_[y][x]+map_[y+1][x+1]+map_[y+2][x+1]+map_[y][x+1]
    else:
        return 0
def L4(x,y):#a의 인덱스가 1이상일때만 실행할 것
    global a
    global b
    if x+2<b and 0<y:
        return map_[y][x]+map_[y][x+1]+map_[y][x+2]+map_[y-1][x+2]
    else:
        return 0
def l(x,y):
    global a
    global b
    if y+3<a:
        return map_[y][x]+map_[y+1][x]+map_[y+2][x]+map_[y+3][x]
    else:
        return 0
def sq(x,y):
    global a
    global b  
    if x+1<b and y+1<a:
        return map_[y][x]+map_[y+1][x]+map_[y][x+1]+map_[y+1][x+1]
    else:
        return 0
def z1(x,y):
    global a
    global b
    if x+2<b and y+1<a:
        return map_[y][x]+map_[y][x+1]+map_[y+1][x+1]+map_[y+1][x+2]
    else:
        return 0
def z2(x,y):
    global a
    global b
    if 0<x and y+2<a:
        return map_[y][x]+map_[y+1][x]+map_[y+1][x-1]+map_[y+2][x-1]
    else:
        return 0
def t1(x,y):
    global a
    global b
    if 2<=x+1<b and y+1<a:
        return map_[y][x]+map_[y+1][x+1]+map_[y+1][x]+map_[y+1][x-1]
    else:
        return 0
def t2(x,y):
    global a
    global b
    if x+2<b and y+1<a:
        return map_[y][x]+map_[y+1][x+1]+map_[y][x+1]+map_[y][x+2]
    else:
        return 0
k1=[L1,L2,L3,L4,l,sq,z1,z2,t1,t2]
for i in range(a):
    for j in range(b):
        for k in k1:
            ismax(k(j,i))
map_ = [list(row) for row in zip(*map_)]
a,b=b,a
for i in range(a):
    for j in range(b):
        for k in k1:
            ismax(k(j,i))
print(m)        