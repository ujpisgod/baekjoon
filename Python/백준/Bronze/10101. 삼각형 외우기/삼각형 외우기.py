a=set()
a1=int(input())
a2=int(input())
a3=int(input())
if a1+a2+a3==180:
    a.add(a1)
    a.add(a2)
    a.add(a3)
    if len(a)==3:
        print("Scalene")
    if len(a)==2:
        print("Isosceles")
    if len(a)==1:
        print("Equilateral")
else:
    print("Error")