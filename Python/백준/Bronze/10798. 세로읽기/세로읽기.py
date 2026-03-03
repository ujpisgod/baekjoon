a=[list(input()) for i in range(5)]
b=[]
for i in range(15):
    for j in range(5):
        try:
            b.append(a[j][i])
        except IndexError:
            pass
print("".join(b))    