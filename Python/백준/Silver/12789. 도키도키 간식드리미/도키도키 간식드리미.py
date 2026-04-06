from collections import deque as dq
q=dq()
n=int(input())
l=list(map(int,input().split()))
s=dq([0])
for i in l:
    q.append(i)
target=1
while True:
    if q and q[0]==target:
        q.popleft()
        target+=1
        if not q and len(s)==1:
            break
    elif s and s[-1]==target:
        s.pop()
        target+=1
        if len(s)==1 and not q:
            break
    elif q and target!=s[-1]:
        s.append(q.popleft())
    elif not q and target!=s[-1]:
        print('Sad')
        exit()
print('Nice')