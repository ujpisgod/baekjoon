n=int(input())
mid=(n+1)//2
print((n+1)//2,end=" ")
for i in range(1,(n+1)//2):
    print((n+1)//2+i,end=" ")
    print((n+1)//2-i,end="")
    if i < (n+2)/2-1:
        print(" ", end="")
if 0==n%2:
    print(" ",n)