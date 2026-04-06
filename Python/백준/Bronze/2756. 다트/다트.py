import math
n1=int(input())
def where(x):
    if x<=3:
        return 100
    elif 3<x<=6:
        return 80
    elif 6<x<=9:
        return 60
    elif 9<x<=12:
        return 40
    elif 12<x<=15:
        return 20
    else:
        return 0
for i in range(n1):
    n=0
    m=0
    k=list(map(float,input().split()))
    l=[(0,1),(2,3),(4,5)]
    ll=[(6,7),(8,9),(10,11)]
    for j,p in l:
           n+=where(math.sqrt(k[j]**2+k[p]**2))
    for j,p in ll:
           m+=where(math.sqrt(k[j]**2+k[p]**2))
    if n==m:
        kl='TIE'
        p=''
    elif n>m:
        kl='WINS'
        p=' PLAYER 1'
    elif n<m:
        kl='WINS'
        p=' PLAYER 2'
    print(f'SCORE: {n} to {m},{p} {kl}.')