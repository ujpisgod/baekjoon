import sys
n = int(sys.stdin.readline())
check_col = [False] * n
check_diag1 = [False] * (2 * n)
check_diag2 = [False] * (2 * n)
ans = 0
def solve(row):
    global ans
    if row == n:
        ans += 1
        return
    for col in range(n):
        if not (check_col[col] or check_diag1[row + col] or check_diag2[row - col + n]):
            check_col[col] = check_diag1[row + col] = check_diag2[row - col + n] = True
            solve(row + 1)
            check_col[col] = check_diag1[row + col] = check_diag2[row - col + n] = False

solve(0)
print(ans)