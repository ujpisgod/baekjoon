import sys

# 입력값 전체를 한 번에 읽어서 리스트로 변환
data = sys.stdin.read().split()

if not data:
    exit()

N = int(data[0])
M = int(data[1])
A = int(data[2])

half = (M // 2) + 1  # 기준점이 되는 중앙값

# 4번째 입력값(인덱스 3)부터 차례대로 호출된 번호(X) 확인
for i in range(3, len(data)):
    X = int(data[i])
    
    if X == half:  # 기준점과 같은 번호를 불렀다면 종료 조건
        print(0)
        break
        
    diff = X - half  # 이동해야 할 칸 수
    
    # 원형 배열에서의 다음 사람 위치 계산
    A = (A - 1 + diff) % N + 1
    print(A)