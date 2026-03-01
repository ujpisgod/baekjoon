n=int(input())
for i in range(n):
    a,b=input().split()
    print("".join([int(a)*j for j in b]))