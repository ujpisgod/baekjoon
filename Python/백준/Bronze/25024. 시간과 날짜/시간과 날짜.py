n=int(input())
a31=[1,3,5,7,8,10,12]
for i in range(n):
    a='No'
    b='No'
    x,y=map(int,input().split())
    if x<24 and y<60:
        a='Yes'
    if 0<x<13:
        if x==2 and 0<y<30:
            b='Yes'
        elif (x in a31) and 0<y<32:
            b='Yes'
        elif(x not in a31) and 0<y<31 and x!=2:
            b='Yes'
    print(f'{a} {b}')