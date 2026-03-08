a=[]
for i in range(15):
    a.append(list(input().split()))
for i in range(15):
    for j in range(15):
        if a[i][j]=='w':
            print('chunbae')
            exit()
        elif a[i][j]=='b':
            print('nabi')
            exit()
        elif a[i][j]=='g':
            print('yeongcheol')
            exit()