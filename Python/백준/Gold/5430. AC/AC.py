from collections import deque as dq
n=int(input())
def check():
    global r
    if r==True:
        r=False
    else:
        r=True

for _ in range(n):
    r=False
    i=False
    kk=[]
    a=input()
    b=int(input())
    arr_str = input()
    if b == 0:
        c = dq()
    else:
        c = dq(arr_str[1:-1].split(','))
    for j in a:
        if j=="R":
            check()
        if j=='D':
            if len(c)==0:
                i=True
                break
            if r==True:
                c.pop()
            else:
                c.popleft()
    if i==True:
        print('error')
    else:   
        if r==True:
            c.reverse()
        print(f"[{','.join(c)}]")