import sys
sys.setrecursionlimit(10**6)
n,y,x=map(int,input().split())
l=2**n
half=l//2
num=0
def a(half):
    if half==0:
        return
    global x
    global y
    q4=[0,0]
    global num
    if half<=x:
        q4[1]=1
    if half<=y:
        q4[0]=1
    if q4==[1,1]:
        num+=3*(half**2)
        x-=half
        y-=half
        a(half//2)
    elif q4==[0,1]:
        num+=1*(half**2)
        x-=half
        a(half//2)
    elif q4==[1,0]:
        num+=2*(half**2)
        y-=half
        a(half//2)
    elif q4==[0,0]:
        a(half//2)
a(half)
print(num)