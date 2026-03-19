a,b=map(int,input().split())
c=list(map(int,input().split()))
if sum(c)<b:
    print(-1)
    exit()
attack=0
for i in range(a):
    attack+=c[i]
    if attack>=b:
        print(i+1)
        exit()