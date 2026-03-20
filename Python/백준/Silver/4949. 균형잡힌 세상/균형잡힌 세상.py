import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == ".": break
    
    stack = [] # 이게 바로 우리들의 '프링글스 통'!
    ans = "yes"
    
    for char in line:
        if char == "(" or char == "[":
            stack.append(char) # 여는 괄호는 일단 통에 담아!
            
        elif char == ")":
            # 통이 비었거나, 맨 위가 '('가 아니면 짝이 안 맞는 거야!
            if not stack or stack[-1] != "(":
                ans = "no"
                break
            stack.pop() # 짝이 맞으면 통에서 빼버려!
            
        elif char == "]":
            if not stack or stack[-1] != "[":
                ans = "no"
                break
            stack.pop()
            
    # 문장을 다 읽었는데 통에 괄호가 남아있으면? 그것도 'no' (짝이 안 맞음)
    if stack: ans = "no"
    
    print(ans)