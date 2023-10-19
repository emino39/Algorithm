def DFS(v):
    global virus

    virus[v] = 1
    for n in range(1, N+1):
        if arr[v][n] == 1 and not virus[n]:
            virus[n] = 1
            DFS(n)


N = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
virus = [0] * (N+1)
M = int(input())

for m in range(M):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1

DFS(1)
print(sum(virus)-1)