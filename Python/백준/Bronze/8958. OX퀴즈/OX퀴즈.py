n=int(input())
for i in range(n):
    strikes=0
    m=input()
    num=0
    for i in m:
        if i=='O':
            strikes+=1
            num+=strikes
        elif i=='X':
            strikes=0
    print(num)