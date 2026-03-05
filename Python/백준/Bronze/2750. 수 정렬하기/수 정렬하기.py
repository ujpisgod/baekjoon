n=int(input())
a=[]
t=0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            
for i in a:
    print(i)