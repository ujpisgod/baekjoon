# 1. 제곱수들을 '집합(set)'으로 만듭니다. (검색 속도 0.0001초!)
b = set(x**2 for x in range(1, 224))

# 2. 2개의 제곱수 합도 '집합'으로 묶어서 중복을 확 없애줍니다.
b2 = set(i + j for i in b for j in b)

# 입력받는 숫자를 대문자 N으로 바꿉니다. (위에 223을 n으로 썼으니까요!)
N = int(input())

if N in b:
    print(1)
elif N in b2:
    print(2)
else:
    # 3. 3개짜리(b3)를 1100만 개나 무식하게 만들 필요가 없습니다!
    # N이 3개의 제곱수 합(N = x + y + z)이라면, N에서 제곱수 하나(x)를 뺐을 때 남은 값(y + z)이 b2 안에 무조건 있겠죠?
    is_three = False
    for square in b:
        if (N - square) in b2:
            print(3)
            is_three = True
            break
            
    # 1, 2, 3 다 아니면 무조건 4!
    if not is_three:
        print(4)