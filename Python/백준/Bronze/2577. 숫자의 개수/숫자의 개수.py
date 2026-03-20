from collections import deque

a = int(input())
b = int(input())
c = int(input())
d = str(a * b * c) # 곱한 결과를 문자열로!

# 1. 아예 처음부터 글자를 정수로 바꿔서 큐에 싹 다 집어넣기!
queue = deque()
for char in d:
    queue.append(int(char)) # '1', '7', '0', '0' 을 정수 1, 7, 0, 0으로 넣음

k = [0] * 10 # 0부터 9까지 개수를 저장할 창고

# 2. 큐가 빌 때까지 하나씩 뽑아서 카운트! (while문이 훨씬 깔끔해)
while queue:
    num = queue.popleft()
    k[num] += 1

# 3. 정답 출력
for i in range(10):
    print(k[i])