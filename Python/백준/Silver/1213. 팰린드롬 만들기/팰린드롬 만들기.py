import sys
from collections import Counter
s = sys.stdin.readline().rstrip()
count = Counter(s)
sorted_keys = sorted(count.keys())
odd_char = ""
half = ""
for char in sorted_keys:
    if count[char] % 2 == 1:
        if odd_char:
            print("I'm Sorry Hansoo")
            sys.exit()
        odd_char = char
    half += char * (count[char] // 2)
print(half + odd_char + half[::-1])