def dfs(n, sm):
    global ans
    # [1] 종료 조건: 가능한 n(종료)에 관련된 정의!
    if n >= N:
        ans = max(ans, sm)
        return

    # [2] 하부 호출: 화살표 개수만큼 호출
    # 상담하는 경우(가능한 경우)
    if n + T[n] <= N:
        dfs(n+T[n], sm + P[n])
    # 상담하지 않는 경우(항상 가능)
    dfs(n+1, sm)


N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())


ans = 0
dfs(0, 0)
print()