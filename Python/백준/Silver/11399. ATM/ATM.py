a=int(input())
b=list(map(int,input().split()))
b.sort()
c=0
for i in range(a):
    c+=b[i]*(a-i)
print(c)