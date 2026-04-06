import sys

# 입력과 출력 양쪽 모두 극한의 속도로 세팅
input = sys.stdin.readline
print_out = sys.stdout.write

n = int(input())
l = [0]

def up(a):
    l.append(a)
    c = len(l) - 1
    while c != 1:
        parent = c // 2
        
        # abs() 함수 호출을 변수에 캐싱하여 중복 연산 제거
        abs_c = abs(l[c])
        abs_p = abs(l[parent])
        
        if abs_c < abs_p:
            l[c], l[parent] = l[parent], l[c]
            c = parent
        elif abs_c == abs_p:
            if l[c] < l[parent]:
                l[c], l[parent] = l[parent], l[c]
                c = parent
            else:
                break
        else:
            break

def down():
    if len(l) == 1:
        print_out("0\n")
        return
        
    n = 1
    l[n], l[-1] = l[-1], l[n]
    
    # print() 대신 sys.stdout.write()로 한 줄씩 초고속 출력
    print_out(str(l.pop()) + "\n")
    
    length = len(l)
    while True:
        minn = n
        left = n * 2
        right = n * 2 + 1
        
        # abs_minn을 층마다 한 번만 계산해서 깎아먹는 시간 방어
        if length > left:
            abs_minn = abs(l[minn])
            abs_left = abs(l[left])
            if abs_minn > abs_left:
                minn = left
            elif abs_minn == abs_left and l[minn] > l[left]:
                minn = left
                
        if length > right:
            # 왼쪽 자식과 비교하며 minn이 바뀌었을 수 있으니 다시 한 번 갱신
            abs_minn = abs(l[minn]) 
            abs_right = abs(l[right])
            if abs_minn > abs_right:
                minn = right
            elif abs_minn == abs_right and l[minn] > l[right]:
                minn = right
                
        if minn != n:
            l[n], l[minn] = l[minn], l[n]
            n = minn
        else:
            break

for _ in range(n):
    k = int(input())
    if k != 0:
        up(k)
    else:
        down()