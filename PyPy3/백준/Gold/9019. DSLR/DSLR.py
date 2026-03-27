from collections import deque as dq
n=int(input())
def d(x):
    x=(x*2)%10000
    return x
def s(x):
    if x==0:
        return 9999
    else:
        return x-1
def l(x):
    x=(x%1000)*10+(x//1000)    
    return x
def r(x):
    x=(x%10)*1000+(x//10)    
    return x
f=[d,s,l,r]
for i in range(n):
    w=['']*10000
    q=dq([])
    a,b=map(int,input().split())
    visit=[False]*10000
    q.append(a)
    visit[a]=True
    is_found=False
    while q:
        cc=4
        num=q.popleft()
        if num==0:
            cc=2
        for _ in range(cc):
            neww=f[_](num)
            if visit[neww]==False:
                visit[neww]=True
                w[neww]=w[num]+["D", "S", "L", "R"][_]
                if neww==b:
                    print(w[neww])
                    is_found=True
                    break
                q.append(neww)
        if is_found==True:
            break