a,b=input().split()
c=0
def num(char):
    if '0' <= char <= '9':
        return int(char)
    else:
        x=ord(char)-55
        return x
for i in range(len(a)):
    c+=num(a[-(1+i)])*(int(b)**i)
print(c)