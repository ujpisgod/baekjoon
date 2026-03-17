n=input()
a=n.count('6')
b=n.count('9')
n1=[]
for i in range(10):
    if i==6 or i==9:
        continue
    n1.append(n.count(str(i)))
c=(a+b+1)//2
d=max(max(n1),c)
print(d)