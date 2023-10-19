import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * N

for n in range(1, N):
    for k in range(n):
        if arr[k] < arr[n]:
            dp[n] = max(dp[n], dp[k] + 1)

print(max(dp))
