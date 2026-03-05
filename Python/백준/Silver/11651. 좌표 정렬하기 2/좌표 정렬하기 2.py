n=int(input())
t=[]
for i in range(n):
    a,b=map(int,input().split())
    t.append((b,a))
t.sort()
for i in range(n):
    print(t[i][1],t[i][0])