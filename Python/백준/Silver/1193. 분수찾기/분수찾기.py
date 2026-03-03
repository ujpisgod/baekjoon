a=int(input())
n=1
while (n*(n+1)//2)<a:
    n+=1
if n%2==1:
    a1=n-(a-((n-1)*n)//2)+1
    a2=a-((n-1)*n)//2
elif n%2==0:
    a1=a-((n-1)*n)//2
    a2=n-(a-((n-1)*n)//2)+1
    
print(f"{a1}/{a2}")