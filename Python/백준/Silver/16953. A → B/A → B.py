a,b=map(int,input().split())
w=0
while b>a:
    k=[(2,0),(10,1)]
    moved=False
    for i in k:
        if b%i[0]==i[1]:
            b=b//i[0]
            w+=1
            moved=True
            break
    if not moved:
        break
if b==a:
    print(w+1)
else:
    print(-1)