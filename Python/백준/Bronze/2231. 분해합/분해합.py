n = int(input())
for i in range(n):
    d = sum(map(int, str(i)))+i
    if d==n:
        print(i)
        exit()
print(0)