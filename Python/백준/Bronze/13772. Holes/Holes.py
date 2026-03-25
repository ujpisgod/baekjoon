n=int(input())
for i in range(n):
    r=0
    a=input()
    r+=a.count("A")
    r+=2*a.count("B")
    r+=a.count("D")
    r+=a.count("O")
    r+=a.count("P")
    r+=a.count("Q")
    r+=a.count("R")
    print(r)