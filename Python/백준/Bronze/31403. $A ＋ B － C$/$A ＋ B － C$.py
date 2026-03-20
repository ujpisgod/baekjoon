a = input()
b = input()
c = input()

# 1. 수로 생각했을 때: 처음부터 다 숫자로 바꿔서 계산!
print(int(a) + int(b) - int(c))

# 2. 문자열로 생각했을 때: a랑 b는 글자 상태로 먼저 이어 붙이고("1"+"2"="12"), 
# 그 합쳐진 글자를 숫자로 바꾼 뒤에 c(숫자)를 빼준다!
print(int(a + b) - int(c))