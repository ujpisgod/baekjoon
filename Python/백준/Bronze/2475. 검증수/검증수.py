d={0:0,1:1,2:4,3:9,4:6,5:5,6:6,7:9,8:4,9:1}
a=map(int,input().split())
c=0
for i in a:
    c+=d[i]
print(c%10)