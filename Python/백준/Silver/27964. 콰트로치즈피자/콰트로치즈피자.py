n=int(input())
a=set()
b=input().split()
for i in b:
    if i.endswith('Cheese'):
        a.add(i)
if len(a)>=4:
    print('yummy')
else:
    print('sad')