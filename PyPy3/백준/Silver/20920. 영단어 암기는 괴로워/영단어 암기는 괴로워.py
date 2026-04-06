import sys
input = sys.stdin.readline
n, m = map(int, input().split())

d = {}
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        d[word] = d.get(word, 0) + 1
voca = list(d.keys())
voca.sort(key=lambda x: (-d[x], -len(x), x))
for word in voca:
    print(word)