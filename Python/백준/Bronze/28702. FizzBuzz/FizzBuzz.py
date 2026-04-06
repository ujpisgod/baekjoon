# 세 줄을 입력받으면서 숫자를 찾아보자
s1 = input()
s2 = input()
s3 = input()

# 리스트에 넣어서 관리하면 편해
arr = [s1, s2, s3]

for i in range(3):
    # 만약 글자가 숫자로만 이루어져 있다면?
    if arr[i].isdigit():
        # 그 숫자를 기준으로 '다음에 올 숫자'를 계산해
        # i가 0이면(첫번째 줄) +3, i가 1이면 +2, i가 2면(세번째 줄) +1
        target_num = int(arr[i]) + (3 - i)
        break

# 이제 target_num이 Fizz인지 Buzz인지 숫자인지만 판별하면 끝!
if target_num % 3 == 0 and target_num % 5 == 0:
    print("FizzBuzz")
elif target_num % 3 == 0:
    print("Fizz")
elif target_num % 5 == 0:
    print("Buzz")
else:
    print(target_num)