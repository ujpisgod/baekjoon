n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    n1=c%a
    n2=c//a+1
    if n1 == 0: 
        n1 = a       
        n2 = c // a
    if n2<10:        
        print(f"{n1}0{n2}")
    else:
        print(f"{n1}{n2}")