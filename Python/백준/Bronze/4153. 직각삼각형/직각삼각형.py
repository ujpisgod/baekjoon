while True:
    u=list(map(int,input().split()))
    u.sort()
    a=u[0]
    b=u[1]
    c=u[2]
    if a==0 and b==0 and c==0:
        break
    elif a**2+b**2==c**2:
        print('right')
    else:
        print('wrong')    
