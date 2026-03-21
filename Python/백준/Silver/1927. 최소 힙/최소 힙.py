import sys
input=sys.stdin.readline
n=int(input())
a=[0]
def up(a,n):
    if n>1 and a[n]<a[n//2]:
        a[n],a[n//2]=a[n//2],a[n]
        n=n//2
        up(a,n)
    else:
        return
def refill(a, start):
    left = start * 2
    right = start * 2 + 1
    smallest = start 
    if left < len(a) and a[left] < a[smallest]:
        smallest = left 
    if right < len(a) and a[right] < a[smallest]:
        smallest = right
    if smallest != start:
        a[start], a[smallest] = a[smallest], a[start]
        refill(a, smallest)
for i in range(n):
    new=int(input())
    if new!=0:
        a.append(new)
        n=len(a)-1
        up(a,n)
    else:
        if len(a)==1:
            print(0)
            continue
        a[1],a[-1]=a[-1],a[1]
        print(a.pop(-1))
        start=1
        refill(a,start)