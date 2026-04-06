a=list(input())
b=list(input())
k=[]
for i in a:
    k.append(i)
    if len(k)>=len(b) and k[-len(b)::1]==b:
        del k[-len(b):]
if not k:
    print('FRULA')
else:
    print(''.join(k))
