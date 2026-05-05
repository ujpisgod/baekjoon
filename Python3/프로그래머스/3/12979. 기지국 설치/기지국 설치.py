def solution(n, stations, w):
    answer = 0
    start=1
    for i in stations:
        end=i-w-1
        if end>=start:
            answer+=(end-start+2*w+1)//(2*w+1)
        start=i+w+1
    if start <= n:
        answer += (n-start+2*w+1)//(2*w+1)
    return answer