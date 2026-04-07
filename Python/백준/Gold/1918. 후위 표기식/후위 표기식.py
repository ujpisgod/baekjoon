import sys
expression = sys.stdin.readline().rstrip()
stack = []
ans = ""
for char in expression:
    if char.isalpha():
        ans += char
    elif char == '(':
        stack.append(char)
    elif char == '*' or char == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(char)
    elif char == '+' or char == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
while stack:
    ans += stack.pop()

print(ans)