def backtracking(n, i, arr):
    if n == M:
        ans.append(arr)
        return

    for j in range(i, N+1):
        backtracking(n+1, j, arr + [j])

N, M = map(int, input().split())
ans = []
backtracking(0, 1, [])

for a in ans:
    print(*a)