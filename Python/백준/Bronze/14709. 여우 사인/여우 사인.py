n1=int(input())
a=[]
for i in range(n1):
    m,n=map(int,input().split())
    a.append([min(m,n),max(m,n)])
a.sort()
if a==[[1,3],[1,4],[3,4]]:
    print('Wa-pa-pa-pa-pa-pa-pow!')
else:
    print('Woof-meow-tweet-squeek')