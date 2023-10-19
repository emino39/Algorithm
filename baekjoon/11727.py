"""
n == 1 => 1
n == 2 => 3
n == 3 => 5
n == 4 => 11
n == 5 => 21


n == 8 => 171
그림 그려서 풀기

"""
N = int(input())
dp = [0] * 1001
dp[0] = 1
dp[1] = 1

for n in range(2, N+1):
    dp[n] = dp[n-1] + 2 * dp[n-2]

print(dp[N] % 10007)