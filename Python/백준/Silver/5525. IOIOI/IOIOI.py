n = int(input())
m = int(input())
s = input()

ans = 0
count = 0
i = 0

# 인덱스 i가 문자열 끝에 닿기 전까지 돈다
while i < (m - 1):
    # 'IOI' 패턴이 3칸 딱 맞게 나오는지 확인 (길이 3짜리 짧은 슬라이싱은 시간 안 잡아먹어)
    if s[i:i+3] == 'IOI':
        count += 1
        i += 2  # 'O'를 건너뛰고 다음 'I'부터 다시 검사하기 위해 2칸 점프!
        
        # 우리가 찾는 Pn 패턴 길이만큼 'IOI'가 연속으로 나왔다면?
        if count == n:
            ans += 1
            count -= 1  # 패턴이 계속 이어질 수 있으니 카운트만 1 깎고 계속 탐색
    else:
        # 패턴이 끊겼으면 카운트 초기화하고 1칸만 전진
        i += 1
        count = 0

print(ans)