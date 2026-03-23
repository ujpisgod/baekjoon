n=int(input())
a=list(map(int,input().split()))
d={}
i=0
j=0
max_len=0
for i in range(n):
    d[a[i]] = d.get(a[i], 0) + 1
    while len(d) > 2:
        d[a[j]] -= 1         
        if d[a[j]] == 0:
            d.pop(a[j])
        j += 1
    max_len = max(max_len, i - j + 1)
print(max_len)