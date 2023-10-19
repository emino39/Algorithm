"""
top-down
완료가 있을 때는 역방향이 낫다
p[i] : i번째 상담 결정 시 최대수익(N-1부터 내려가기)

아래 두 값 중 최댓값
dp[n+T[n]] + P[n] # 가능 시 상담
dp[n+1] # n번째 상담 안 했을 때

for n (N-1, -1, -1)
if n + T[n] <= N
dp[n]
else
dp[n] <- dp[n+1]
ans <- dp[0]
"""

N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0] * (N+1)

for n in range(N-1, -1, -1):
    if n+T[n] <= N:
        dp[n] = max(dp[n+1], dp[n+T[n]] + P[n])
    else:
        dp[n] = dp[n+1]

print(dp[0])