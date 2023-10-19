N = int(input())

arr = [int(input()) for _ in range(N)]
dp = [0] * N

if N <= 2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]

    for n in range(2, N):
        dp[n] = max(dp[n-3] + arr[n-1] + arr[n], dp[n-2] + arr[n])

    print(dp[-1])
