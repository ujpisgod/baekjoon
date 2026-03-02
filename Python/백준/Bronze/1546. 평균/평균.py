n=input()
a=list(map(int,input().split()))
m=max(a)
print((sum(a)/len(a))*(100/m))