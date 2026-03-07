sg=int(input())
sgl=set(map(int,input().split()))
rec=int(input())
recl=list(map(int,input().split()))
for i in range(rec):
    if recl[i] in sgl:
        recl[i]="1"
    else:
        recl[i]="0"
print(" ".join(recl))
        