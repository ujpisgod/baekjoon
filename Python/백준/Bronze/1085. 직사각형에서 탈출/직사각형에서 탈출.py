x,y,a,b=map(int,input().split())
m=[x,x,y,y]
mm=[a,0,b,0]
_try=0
while True:
    m[0]+=1
    m[1]-=1
    m[2]+=1
    m[3]-=1
    _try+=1
    for i in range(4):
        if m[i]==mm[i]:
            print(_try)
            exit()
