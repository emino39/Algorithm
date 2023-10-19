def backtracking(n, arr):
    global ans

    if n > N:
        if len(arr) == M:
            ans.append(arr)
        return

    backtracking(n + 1, arr + [n])  # 포함
    backtracking(n + 1, arr)  # 미포함


N, M = map(int, input().split())
ans = []

backtracking(1, [])

for a in ans:
    print(*a)