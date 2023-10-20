"""
dp[1] = price[1]
dp[2] = dp[1] + price[1] or dp[0] + price[2]
dp[3] = dp[2] + price[1] or dp[1] + price[2] or dp[0] + price[3]
dp[4] = dp[3] + price[1] or dp[2] + price[2] or dp[1] + price[3] + dp[0] + price[4]
...
"""
N = int(input())
prices = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + prices[j])

print(dp[N])