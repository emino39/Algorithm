N = int(input())

if N % 5 == 0:
    print(N // 5)
else:
    cnt = 0

    while N > 0:
        N -= 3
        cnt += 1

        if N % 5 == 0:
            cnt += (N // 5)
            print(cnt)
            break
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N == 0:
            print(cnt)
            break




"""
INF = int(1e9)
dp = [INF] * (N + 1)

if N == 4:
    print(-1)
elif N == 3 or N == 5:
    print(1)
else:
    dp[3] = 1
    dp[5] = 1

    for i in range(6, N+1):
        dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
    
    if dp[N] >= INF:
        print(-1)
    else:
        print(dp[N])
"""