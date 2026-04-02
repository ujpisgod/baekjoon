n=int(input())
def solve(x):
    if x>1:
        return x*solve(x-1)
    else:
        return 1
print(solve(n))