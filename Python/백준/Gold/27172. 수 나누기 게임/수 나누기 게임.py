import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int, input().split()))
exist=[False]*1000001
for i in l:
    exist[i]=True
sc=[0]*1000001
for i in l:
    for j in range(i*2,1000001,i):
        if exist[j]:
            sc[i]+=1
            sc[j]-=1 
for x in l:
    print(sc[x],end=' ')