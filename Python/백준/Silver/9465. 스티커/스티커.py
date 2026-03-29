n=int(input())
nn=[(0,1,1,0),(1,0,0,1)]
for i in range(n):
    l=int(input())
    s=[list(map(int,input().split())) for _ in range(2)]
    if l==1:
        print(max(s[0][0],s[1][0]))
    elif l==2:
        print(max(s[0][1]+s[1][0],s[0][0]+s[1][1]))
    elif l>2:
        s[0][1]+=s[1][0]
        s[1][1]+=s[0][0]
        for j in range(l-2):
            for k in nn:
                s[k[0]][j+2]=max([s[k[1]][j],s[k[2]][j+1]])+s[k[3]][j+2]
        print(max(s[0][l-1],s[1][l-1]))