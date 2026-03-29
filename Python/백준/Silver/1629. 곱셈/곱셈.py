a,b,c=map(int,input().split())
def sa(a,b,c):
    if b%2==0 and b>2:
        n=b//2
        k=sa(a,n,c)
        return k*k%c
    elif b%2==1 and b>2:
        n=b//2
        k=sa(a,n,c)
        return k*k*a%c
    elif b==1:
        return a%c
    elif b==2:
        return (a**2)%c
print(sa(a,b,c))
