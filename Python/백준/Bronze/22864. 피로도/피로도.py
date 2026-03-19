a,b,n,m=map(int,input().split())
ct=0
tired=0
work=0
while ct<24:
    ct+=1
    if tired+a<=m:
        work+=b
        tired+=a
    elif tired+a>m:
        tired-=n
        if tired<0:
            tired=0
print(work)