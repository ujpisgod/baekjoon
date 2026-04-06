k=input()
if k.find('A')!=-1:
    k=k.replace('B', 'A')
    k=k.replace('C', 'A')
    k=k.replace('D', 'A')
    k=k.replace('F', 'A')
elif k.find('A')==-1 and k.find('B')!=-1:
    k=k.replace('C', 'B')
    k=k.replace('D', 'B')
    k=k.replace('F', 'B')
elif k.find('A')==-1 and k.find('B')==-1 and k.find('C')!=-1:
    k=k.replace('D', 'C')
    k=k.replace('F', 'C')
else:
    print('A'*len(k))
    exit()
print(k)