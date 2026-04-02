n=int(input())
def h(n,start,obj,hel):
    if n==1:
        print(start,obj)
    else:
        h(n-1,start,hel,obj)
        print(start,obj)
        h(n-1,hel,obj,start)
print(2**n-1)
h(n,1,3,2)
