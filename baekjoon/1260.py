def DFS(v):
    global v_dfs
    print(v, end=" ")
    v_dfs[v] = 1
    for u in range(1, N+1):
        if arr[v][u] and not v_dfs[u]:
            v_dfs[u] = 1
            DFS(u)

N, M, V = list(map(int, input().split()))

arr = [[0] * (N+1) for _ in range(N+1)]
v_dfs = [0] * (N+1)
v_bfs = [0] * (N+1)

# bfs queue
queue = []

# 노드 연결
for m in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

# dfs
DFS(V)
print()

queue.append(V)

while queue:
    s = queue.pop(0)
    v_bfs[s] = 1
    print(s, end=" ")

    for t in range(N+1):
        if arr[s][t] and not v_bfs[t]:
            v_bfs[t] = 1
            queue.append(t)