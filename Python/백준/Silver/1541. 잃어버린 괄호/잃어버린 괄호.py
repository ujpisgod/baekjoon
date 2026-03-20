n=input().split('-')
d=[]
for i in range(len(n)):
    k=list(map(int,n[i].split('+')))
    d.append(sum(k))
for i in range(1,len(d)):
    d[0]=d[0]-d[i]
print(d[0])