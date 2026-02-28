a=int(input())
t=0
for _ in range(a):
    b=input()
    for i in set(b):
        if i*b.count(i) not in b:
            t+=1
            break
print(a-t)
    