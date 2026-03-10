def isp(a):
    t=2
    if a<2:
        return 1
    while True:
        if t**2<=a:
            if a%t==0:
                return 1
            else:
                t+=1
        else:
            return 0
n=int(input())
for i in range(n):
    k=0
    r=int(input())
    while True:
        if isp(r+k)==0:
            print (r+k)
            break
        else:
            k+=1