n=int(input())
nn=set()
ans=0
for i in range(n):
    m=input()
    if m=='ENTER':
        ans+=len(nn)
        nn.clear()
    else:
        nn.add(m)
ans+=len(nn)
print(ans)