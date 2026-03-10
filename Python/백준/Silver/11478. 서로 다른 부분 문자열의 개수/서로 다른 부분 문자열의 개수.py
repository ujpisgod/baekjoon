a=input()
a1=set()
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        a1.add(a[i:j])
print(len(a1))