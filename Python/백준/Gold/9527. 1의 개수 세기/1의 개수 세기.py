import sys
input = sys.stdin.readline
a,b = map(int, input().split())
def count_ones(x: int) -> int:
    if x < 0:
        return 0
    total = 0
    bit = 1
    while bit <= x:
        cycle = bit << 1
        full_cycles = (x + 1) // cycle
        remainder = (x + 1) % cycle
        total += full_cycles * bit
        total += max(0, remainder - bit)
        bit <<= 1
    return total
print(count_ones(b) - count_ones(a - 1))