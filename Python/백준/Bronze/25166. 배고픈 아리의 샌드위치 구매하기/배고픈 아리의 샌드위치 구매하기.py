S, M = map(int, input().split())

if S < 1024:
    # 아리 돈으로 해결 가능
    print("No thanks")
else:
    # 부족한 돈 계산
    need = S - 1023
    
    # 부족한 돈(need)이 쿠폰(M)의 비트 안에 다 들어있는가?
    if (need & M) == need:
        print("Thanks")
    else:
        print("Impossible")