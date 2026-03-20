import sys
input = sys.stdin.readline

n = int(input())
stack = [] # 리스트 이름을 알아보기 쉽게 stack으로 지었어

for _ in range(n):
    command = input().split() # 리스트로 받으면 숫자가 있든 없든 안전해
    
    op = command[0] # 명령어 (push, pop 등)
    
    if op == 'push':
        stack.append(int(command[1]))
        
    elif op == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
            
    elif op == 'size':
        print(len(stack))
        
    elif op == 'empty':
        # 스택이 비어있으면 1, 아니면 0
        print(1 if not stack else 0)
        
    elif op == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1]) # 맨 뒤에 있는 놈이 스택의 맨 위!