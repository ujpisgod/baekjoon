n=int(input())
l=list(map(int,input().split()))
ans=[]
k=0
s=0
def solve():
    global k, s
    if len(ans)==n-2:
        k=max(k,s)
        return
    for i,t in enumerate(l):
        if i in ans:
            continue
        elif i==0:
            continue
        elif i==(n-1):
            continue
        else:
            ans.append(i)
            left=i-1
            right=i+1
            while left in ans:
                left-=1
            while right in ans:
                right+=1
            s+=l[left]*l[right]
            solve()
            ans.pop()
            s-=l[left]*l[right]
solve()
print(k)