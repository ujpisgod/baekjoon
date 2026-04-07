while True:
    try:
        n=int(input())
        dp=[1]*(n+1)
        if n<2:
            print(1)
            continue
        dp[2]=3
        if n==2:
            print(dp[2])
            continue
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+2*dp[i-2])
        print(dp[n])
    except EOFError:
        exit()