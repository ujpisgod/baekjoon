d={0:0,1:3,2:6,3:9,4:2,5:5,6:8,7:1,8:4,9:7}
n=input()
c=0
k=False
for i in range(12):
    if i%2==1:
        if n[i]=='*':
            k=True
            continue
        c+=d[int(n[i])]
    elif i%2==0:
        if n[i]=='*':
            continue
        c+=int(n[i])
h=0
if k:
    target=(10-(c+int(n[12]))%10)%10
    for key, value in d.items():
        if value == target:
            h=key
else:
    h= (10 - (c + int(n[12])) % 10) % 10
print(h)