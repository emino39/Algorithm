N = int(input())

# 2차원
dp = [[0] * 10 for _ in range(N+1)]

# 한자리수일때
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        # 가장 뒤에 오는 숫자가 0일 땐 앞에 1만 올 수 있음
        if j == 0:
            dp[i][j] = dp[i-1][1]
        # 가장 뒤에 오는 숫자가 1~8일 땐 앞에 +- 1이 옴
        elif 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        # 가장 뒤에 오는 숫자가 9일 땐 앞에 8만 올 수 있음
        else:
            dp[i][j] = dp[i-1][8]

print(sum(dp[N]) % 1000000000)