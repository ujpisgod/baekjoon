import sys
input=sys.stdin.readline
def solve():
    n=int(input().rstrip())
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    dd={}
    ans=0
    for i in range(n):
        a,b,c,d=map(int,input().split())
        a1.append(a)
        a2.append(b)
        a3.append(c)
        a4.append(d)
    for i in a1:
        for j in a2:
            dd[i+j]=dd.get(i+j,0)+1
    for i in a3:
        for j in a4:
            ans+=dd.get(-1*(i+j),0)
    return ans
print(solve())