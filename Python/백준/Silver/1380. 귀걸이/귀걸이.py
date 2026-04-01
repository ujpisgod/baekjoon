tc=1
while True:
    try:
        d={}
        name=[]
        n=int(input())
        for i in range(n):
            k=input()
            name.append(k)
            d[k]=0
        for i in range(2*n-1):
            a,b=input().split()
            d[name[int(a)-1]]+=1
        for h, v in d.items():
            if v == 1:
                print(tc,h)
                tc+=1
    except EOFError:
        exit()
        