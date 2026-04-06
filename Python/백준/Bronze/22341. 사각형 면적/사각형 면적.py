n,c=map(int,input().split())
n1=n
n2=n
for i in range(c):
    a,b=map(int,input().split())
    if a<n1 and b<n2 and n1*b>n2*a:
        n2=b
    elif a<n1 and b<n2 and n1*b<=n2*a:
        n1=a
print(n1*n2)