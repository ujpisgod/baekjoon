a,b,c=map(int,input().split())
print(min(c*(b+1)*(100-a)//100,c*b))