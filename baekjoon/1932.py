import sys
read = sys.stdin.readline

N = int(input())
arr = [list(map(int, read().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = arr[0][0]

for n in range(1, N):
    for m in range(len(arr[n])):
        if m == 0:
            dp[n][m] = dp[n-1][m] + arr[n][m]
        elif m == len(arr[n]) - 1:
            dp[n][m] = dp[n-1][m-1] + arr[n][m]
        else:
            dp[n][m] = max(dp[n-1][m-1], dp[n-1][m]) + arr[n][m]

print(max(dp[N-1]))

"""
7
10 15
18 16 15
20 23 20 19
24 30 25 26 24
"""
