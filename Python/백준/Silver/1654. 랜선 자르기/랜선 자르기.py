x, y = map(int, input().split())
a1 = [int(input()) for _ in range(x)]
start = 1
end = sum(a1) // y 
while start <= end:
    mid=(start + end) // 2     
    b=0
    for i in a1:
        b+=i//mid
    if b >= y:
        start = mid + 1
    else:
        end = mid - 1
print(end)