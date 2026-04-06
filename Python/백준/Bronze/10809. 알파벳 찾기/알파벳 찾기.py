s = input().strip()
print(*[s.find(chr(i)) for i in range(97, 123)])