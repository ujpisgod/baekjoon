a,b=map(int,input().split())
a1=set()
b1=[]
for i in range(a):
    a1.add(input())
for i in range(b):
    k=input()
    if k in a1:
        b1.append(k)
b1.sort()
print(len(b1))
for i in range(len(b1)):
    print(b1[i])