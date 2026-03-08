import sys
input=sys.stdin.readline    
n=int(input())
s=set()
for i in range(n):
    k=input().strip()
    if k=='all':
        s=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        continue
    elif k=='empty':
        s=set()
        continue
    a,b=k.split()
    b=int(b)
    if a=='add':
        s.add(b)
    elif a=='remove':
        s.discard(b)
    elif a=='check':
        if b in s:
            print(1)
        else:
            print(0)
    elif a=='toggle':
        if b in s:
            s.remove(b)
        else:
            s.add(b)