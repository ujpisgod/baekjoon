from collections import deque
n=int(input())
a=deque(range(1,n+1))
while len(a)>1:
    a.popleft()#버리기
    d=a.popleft()
    a.append(d)#맨뒤
print(a[0])