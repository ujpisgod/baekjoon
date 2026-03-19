a = input()
k = 1  # 처음 알파벳 세트 1번은 무조건 쳐야 하니까 1부터 시작!

for i in range(1, len(a)):
    # 뒤의 알파벳이 앞의 알파벳보다 순서가 앞이거나 '같으면'
    if a[i] <= a[i-1]: 
        k += 1

print(k)