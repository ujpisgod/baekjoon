from collections import deque as dq
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
sada = []
bem = []
visit = [False] * 101

for i in range(a):
    p, q = map(int, input().split())
    sada.append((p, q))
for i in range(b):
    p, q = map(int, input().split())
    bem.append((p, q))

count = [0] * 101
count[1] = 0
q = dq()
q.append(1)
visit[1] = True

while q:
    t = q.popleft()
    if t == 100:
        print(count[100])
        break
        
    for i in range(1, 7):
        nx = t + i # 일단 주사위 굴린 위치
        
        if nx < 101:
            # 1. 큐에 넣기 전에! 사다리나 뱀이 있는지 싹 다 검사해서 최종 위치(nx)를 바꿉니다.
            for c in range(a):
                if nx == sada[c][0]:
                    nx = sada[c][1]
                    break
            for cc in range(b):
                if nx == bem[cc][0]:
                    nx = bem[cc][1]
                    break
            
            # 2. 최종 위치가 확정된 상태에서, 방문 안 한 곳일 때만 큐에 딱 한 번 넣습니다.
            if visit[nx] == False:
                visit[nx] = True
                q.append(nx)
                count[nx] = count[t] + 1