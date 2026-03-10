while True:
    a=int(input())
    if a==0:
        exit()
    m=[True]*(2*a+1)
    m[0]=False
    m[1]=False
    for i in range(2,2*a+1):
        if m[i]==False:
            continue
        else:
            for j in range(2*i,2*a+1,i):
                m[j]=False
    p=m[:a+1].count(True)
    q=m.count(True)
    print(q-p)