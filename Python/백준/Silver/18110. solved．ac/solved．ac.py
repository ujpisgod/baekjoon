import sys
input=sys.stdin.readline
n=int(input())
if n==0:
    print(0)
    exit()
tail=(n*3+10)//20#반올림
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
m=a[tail : n-tail]   
print((2*sum(m)+len(m))//(2*len(m)))#반올림
    