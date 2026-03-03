a=int(input())
b=set()
for n in range(a):
    x,y=map(int,input().split())
    for i in range(10):
        for j in range(10):
            b.add((x+1+i,y+1+j))
print(len(b))