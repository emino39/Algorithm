T = int(input())

for t in range(T):
    N = int(input())
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for n in range(4, N+1):
        dp[n] = dp[n-3] + dp[n-2] + dp[n-1]

    print(dp[N])