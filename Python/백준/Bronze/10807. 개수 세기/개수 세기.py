n=int(input())
a=list(input().split())
b=input()
c=0
for i in range(n):
    if a[i]==b:
        c+=1
print(c)