n=int(input())
d={}
for i in range(n):
    a,b=input().split()
    d.update({a:b})
a1=[x for x, i in d.items() if i=="enter"]
a1.sort(reverse=1)
for i in a1:
    print(i)
