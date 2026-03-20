import sys
# input을 sys의 빠른 버전으로 교체!
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    # 이제부터는 10만 개를 읽어도 눈 깜짝할 새에 끝남
    b = int(input())
    if b == 0:
        a.pop()
    else:
        a.append(b)

print(sum(a))