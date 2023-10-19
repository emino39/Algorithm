N = int(input())
days = [0] * N
costs = [0] * N

dp = [0] * (N+1)

for n in range(N):
    day, cost = map(int, input().split())
    days[n] = day
    costs[n] = cost

# bottom up 방식 / i번째 일까지 일했을 때 얻을 수 있는 최대 수익
for i in range(N):
    for j in range(i+days[i], N+1): # j는 i번째 날에 상담을 진행했을 때 상담이 가능한 모든 날짜
        if dp[j] < dp[i] + costs[i]:
            dp[j] = dp[i] + costs[i]
print(dp[-1])

"""
# top-down 방식 / 
for i in range(N-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담하지 않음
    if i + days[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], costs[i], dp[i + days[i]])
print(dp)

"""
