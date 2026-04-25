import sys
import copy
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
def compress(line):
    nums = [x for x in line if x != 0]
    merged = []
    i = 0
    while i < len(nums):
        if i + 1 < len(nums) and nums[i] == nums[i + 1]:
            merged.append(nums[i] * 2)
            i += 2
        else:
            merged.append(nums[i])
            i += 1
    merged += [0] * (n - len(merged))
    return merged
def move(b, d):
    new_b = copy.deepcopy(b)
    if d == 0:  # up
        for c in range(n):
            line = [new_b[r][c] for r in range(n)]
            line = compress(line)
            for r in range(n):
                new_b[r][c] = line[r]
    elif d == 1:  # down
        for c in range(n):
            line = [new_b[r][c] for r in range(n - 1, -1, -1)]
            line = compress(line)
            for idx, r in enumerate(range(n - 1, -1, -1)):
                new_b[r][c] = line[idx]
    elif d == 2:  # left
        for r in range(n):
            line = new_b[r][:]
            line = compress(line)
            new_b[r] = line
    else:  # right
        for r in range(n):
            line = new_b[r][::-1]
            line = compress(line)
            new_b[r] = line[::-1]
    return new_b
ans = 0
def backtrack(depth, b):
    global ans
    for row in b:
        ans = max(ans, max(row))
    if depth == 5:
        return
    for d in range(4):
        backtrack(depth + 1, move(b, d))
backtrack(0, board)
print(ans)