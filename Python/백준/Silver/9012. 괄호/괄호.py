import sys
n=int(input())
for i in range(n):
    k=0
    m=input()
    stack=[]
    for j in m:
        if j=='(':
            stack.append(1)
        else:
            if not stack:
                print('NO')
                k=1
                break
            else:
                stack.pop()
    if stack and k==0:
        print('NO')
    elif not stack and k==0:
        print('YES')