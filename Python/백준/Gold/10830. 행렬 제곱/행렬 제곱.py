n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
def vm(mat1, mat2):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res[i][j] %= 1000
    return res
def solve(x, matrix):
    if x == 1:
        return [[matrix[i][j] % 1000 for j in range(n)] for i in range(n)]
    half = solve(x // 2, matrix)
    squared = vm(half, half)
    if x % 2 == 0:
        return squared
    else:
        return vm(matrix, squared)
p=solve(m, l)
for i in p:
    print(*i)