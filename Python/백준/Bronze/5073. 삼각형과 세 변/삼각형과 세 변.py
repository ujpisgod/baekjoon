while True:
    b=[]
    a1,a2,a3=map(int,input().split())
    if (a1+a2+a3)==0:
        break
    b.append(a1)
    b.append(a2)
    b.append(a3)
    a=set(b)
    if max(b)<(sum(b)-max(b)):
        if len(a)==3:
            print("Scalene")
        if len(a)==2:
            print("Isosceles")
        if len(a)==1:
            print("Equilateral")
    else:
        print("Invalid")