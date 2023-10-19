N = int(input())
cnt = 0
dp = [5001] * 5001
dp[3], dp[5] = 1, 1

for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[N] if dp[N] > 0 else -1)