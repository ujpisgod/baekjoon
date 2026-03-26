import sys
import heapq

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    
    # 딕셔너리 대신 속도가 더 빠른 크기 k짜리 생사부 배열 생성
    # True면 살아있음, False면 지워짐(유령)
    visited = [False] * k 

    for i in range(k):
        cmd = input().split()
        if not cmd: continue
        oper, num = cmd[0], int(cmd[1])

        if oper == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i)) # 최대 힙은 부호 반대
            visited[i] = True # i번째 데이터는 살아있다고 기록
            
        elif oper == 'D':
            if num == 1:
                # 최대 힙에서 유령들 걷어내기 (질문자님의 decdown 로직)
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                # 진짜가 나오면 빼고 생사부에 사망(False) 신고
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                # 최소 힙에서 유령들 걷어내기 (질문자님의 ascdown 로직)
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                # 진짜가 나오면 빼고 사망 신고
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # === 모든 턴이 끝나고 마지막 정답 출력 전 최종 유령 청소 ===
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # 출력
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        # 최대 힙은 부호를 다시 뒤집어서 출력!
        print(f"{-max_heap[0][0]} {min_heap[0][0]}")