import sys
# 백준 시간초과 방지용 (이거 없으면 로직이 맞아도 시간초과 납니다)
input = sys.stdin.readline 

n = int(input())

def ascup(x, i):
    q1.append((x, i))
    l = len(q1) - 1
    while l > 1:
        if q1[l][0] < q1[l // 2][0]:
            q1[l], q1[l // 2] = q1[l // 2], q1[l]
            l = l // 2
        else:
            break

def decup(x, i):
    q2.append((x, i))
    l = len(q2) - 1
    while l > 1:
        if q2[l][0] > q2[l // 2][0]:
            q2[l], q2[l // 2] = q2[l // 2], q2[l]
            l = l // 2
        else:
            break

def ascdown():
    while True:
        if len(q1) - 1 == 0:
            return None
        elif len(q1) - 1 == 1:
            r = q1.pop()
            if r[1] in lll: # 유령이면 버림
                return None
            return r
        else:
            q1[1], q1[len(q1) - 1] = q1[len(q1) - 1], q1[1]
            r = q1.pop()
            idx = 1
            while idx * 2 <= len(q1) - 1:
                left = idx * 2
                right = idx * 2 + 1
                mi = left
                if right <= len(q1) - 1 and q1[right][0] < q1[left][0]:
                    mi = right
                if q1[idx][0] <= q1[mi][0]:
                    break
                q1[idx], q1[mi] = q1[mi], q1[idx]
                idx = mi
            if r[1] not in lll: # 살아있는 값이면 반환
                return r

def decdown():
    while True:
        if len(q2) - 1 == 0:
            return None
        elif len(q2) - 1 == 1:
            r = q2.pop()
            if r[1] in lll:
                return None
            return r
        else:
            q2[1], q2[len(q2) - 1] = q2[len(q2) - 1], q2[1]
            idx = 1
            r = q2.pop()
            while idx * 2 <= len(q2) - 1:
                left = idx * 2
                right = idx * 2 + 1
                ma = left
                if right <= len(q2) - 1 and q2[right][0] > q2[left][0]:
                    ma = right
                if q2[idx][0] >= q2[ma][0]:
                    break
                q2[idx], q2[ma] = q2[ma], q2[idx]
                idx = ma
            if r[1] not in lll:
                return r

for _ in range(n):
    lll = {}
    q1 = [0]
    q2 = [0]
    n1 = int(input())
    
    for i in range(n1):
        # 파이썬 입력 공백 처리
        cmd = input().split()
        if not cmd: continue
        a, b = cmd[0], int(cmd[1])
        
        if a == 'I':
            decup(b, i)
            ascup(b, i)
        elif a == 'D':
            if b == 1:
                k = decdown()
                if k is not None:
                    lll[k[1]] = k[0]
            elif b == -1:
                k = ascdown()
                if k is not None:
                    lll[k[1]] = k[0]

    # === 마지막 정답 출력 ===
    k_min = ascdown()
    if k_min is None:
        print("EMPTY")
    else:
        k_max = decdown()
        if k_max is None:
            # 1개만 남았을 경우 최댓값과 최솟값이 동일함
            print(f'{k_min[0]} {k_min[0]}')
        else:
            print(f'{k_max[0]} {k_min[0]}')