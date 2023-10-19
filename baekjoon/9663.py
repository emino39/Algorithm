def backtracking(n):
    global ans
    if n == N: #N행까지 진행한 경우
        ans += 1
        return

    for j in range(N):
        if v1[j] == 0 and v2[n+j] == 0 and v3[n-j] == 0: # 위 열, 대각선에 queen이 없는 경우
            v1[j], v2[n + j], v3[n - j] = 1, 1, 1
            backtracking(n+1)
            v1[j], v2[n + j], v3[n - j] = 0, 0, 0


N = int(input())
ans = 0
v1 = [0] * N # 열 visited 체크
v2 = [0] * (2 * N) # 우상향 대각 visited 체크
v3 = [0] * (2 * N) # 우하향 대각 visited 체크
backtracking(0)
print(ans)