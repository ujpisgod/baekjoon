import sys
input=sys.stdin.readline
l1=[0]+list(input().strip())
l2=[0]+list(input().strip())
dp=[[0]*len(l1) for i in range(len(l2))]
for i in range(1,len(l2)):
    for j in range(1,len(l1)):
        if l1[j]==l2[i]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(max(dp[-1]))
ans = []
i=len(l2) - 1
j=len(l1) - 1
while i>0 and j>0:
    if dp[i-1][j] == dp[i][j]:
        i-=1
    elif dp[i][j-1] == dp[i][j]:
        j-=1
    else:
        ans.append(l1[j])
        i-=1
        j-=1
if ans:
    print(''.join(ans[::-1]))
