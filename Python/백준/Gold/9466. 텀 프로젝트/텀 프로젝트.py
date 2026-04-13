import sys
input = sys.stdin.readline
testcase = int(input())

for _ in range(testcase):
    ans = 0
    n = int(input())
    l = list(map(int, input().split()))
    p = len(l)
    pr = {}
    visit = [False] * (p + 1)
    for who, want in enumerate(l, start=1):
        pr[who] = [want, 0]
        if who == want:
            visit[who] = True
    st = 1
    for i in range(1, p + 1):
        if not visit[i]:
            k = i
            stemp = st
            while True:
                visit[k] = True
                pr[k][1] = st
                start = pr[k][0]
                if pr[start][1] == 0:
                    k=start
                    st+=1
                elif pr[start][1]<stemp:
                    ans+=(st-stemp+1)
                    st+=1
                    break
                else:
                    ans+=(pr[start][1]-stemp)
                    st+=1
                    break
    print(ans)