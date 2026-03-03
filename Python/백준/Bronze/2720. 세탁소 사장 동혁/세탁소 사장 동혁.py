a=int(input())
for i in range(a):
    c=int(input())
    a1=c//25
    c=c%25
    a2=c//10
    c=c%10
    a3=c//5
    a4=c%5
    print(a1,a2,a3,a4)