import math as m
a,b=map(int,input().split())
c=sum(list(map(int,input().split())))
if (c//a)<b:
    print(m.ceil((c-a*b)/(b-100)))
else:
    print(0)