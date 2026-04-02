import sys
def solve(k):
    if k == 0:
        return '-'
    prev = solve(k-1)
    return prev + ' ' * (3**(k-1)) + prev
while True:
    line = sys.stdin.readline()
    if not line:
        break
    try:
        n = int(line.strip())
        print(solve(n))
    except ValueError:
        break