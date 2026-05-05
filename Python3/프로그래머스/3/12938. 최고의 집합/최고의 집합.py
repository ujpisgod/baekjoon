def solution(n, s):
    answer = []
    if n>s:
        answer=[-1]
        return answer
    if n==s:
        answer=[1]
        return answer
    k=s//n
    t=s%n
    for i in range(n-t):
        answer.append(k)
    for i in range(t):
        answer.append(k+1)
    return answer