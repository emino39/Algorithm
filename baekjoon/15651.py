def backtracking(n, arr):
    global ans

    if n == M:
        ans.append(arr)
        return

    for i in range(1, N+1):
        backtracking(n+1, arr + [i])

N, M = map(int, input().split())
ans = []
backtracking(0, [])

for a in ans:
    print(*a)