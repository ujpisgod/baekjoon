import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
inorder=list(map(int, input().split()))
postorder=list(map(int, input().split()))
pos=[0]*(n+1)
for i in range(n):
    pos[inorder[i]]=i
def build(in_l,in_r,post_l,post_r):
    if in_l > in_r:
        return
    root=postorder[post_r]
    print(root,end=' ')
    idx=pos[root]
    left_size=idx-in_l
    build(in_l,idx-1,post_l,post_l+left_size-1)
    build(idx+1,in_r,post_l+left_size,post_r-1)
build(0,n-1,0,n-1)