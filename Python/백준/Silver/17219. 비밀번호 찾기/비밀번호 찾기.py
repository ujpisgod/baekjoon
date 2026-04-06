import sys
input=sys.stdin.readline
m,n=map(int,input().split())
dic={}
for i in range(m):
    a,b=input().split()
    dic[a]=b
for i in range(n):
    c=input().rstrip()
    print(dic[c])
    