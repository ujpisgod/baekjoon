a,b=map(int,input().split())
ls=list(range(a+1))
for i in range(b):
    c,d=map(int,input().split())
    ls[c:d+1]=ls[c:d+1][::-1]
print(*ls[1:])