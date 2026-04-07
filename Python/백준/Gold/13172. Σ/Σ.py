import sys

def solve():
    input = sys.stdin.readline
    MOD = 1000000007
    m = int(input())
    ans = 0
    for _ in range(m):
        n, s = map(int, input().split())
        expected_value = s * pow(n, MOD - 2, MOD)
        ans = (ans + expected_value) % MOD
    print(ans)
if __name__ == '__main__':
    solve()