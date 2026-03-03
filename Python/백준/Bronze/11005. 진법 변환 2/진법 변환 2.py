a,b=map(int,input().split())
num=[]
def change(n):
    if n>9:
        x= chr(n+55)
        return x
    else:
        return str(n)
while a>0:
    num.append(change(a%b))
    a=a//b
num.reverse()
print("".join(num))