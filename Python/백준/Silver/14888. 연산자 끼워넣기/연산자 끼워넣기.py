n=int(input())
l=list(map(int,input().split()))
op=list(map(int,input().split()))
ans=[]
def a1(a,b):
    return a+b

def a2(a,b):
    return a-b

def a3(a,b):
    return a*b

def a4(a,b):
    return int(a / b)
f=[a1,a2,a3,a4]
def solve(now,num):
    if now==n:
        ans.append(num)
        return
    for i in range(4):
        if op[i]==0:
            continue
        else:
            op[i]-=1
            solve(now+1,f[i](num,l[now]))
            op[i]+=1
solve(1,l[0])
print(max(ans))
print(min(ans))
