import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
ans = []
while True:
    common = set(A) & set(B)
    if not common:
        break
    max_val = max(common)
    ans.append(max_val)
    idx_a = A.index(max_val)
    idx_b = B.index(max_val)
    A = A[idx_a + 1:]
    B = B[idx_b + 1:]
print(len(ans))
if ans:
    print(*ans)