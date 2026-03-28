def mul(A,B):
    c = [[0, 0], [0, 0]]
    for i in range(2):          # A의 행(가로)
        for j in range(2):      # B의 열(세로)
            for k in range(2):  # 곱해지는 원소들
                c[i][j] += A[i][k] * B[k][j]
                c[i][j] %= 1000000007
    return c
n=int(input())
if n==0:
    print(0)
    exit()
def power(a,n):
    if n>2:
        half=power(a,n//2)
        if n%2==0:
            return mul(half,half)
        else:
            return mul(a,mul(half,half))
    elif n==2:
        return mul(a,a)
    elif n==1:
        return a
base=[[1,1],[1,0]]
print(power(base,n)[0][1])