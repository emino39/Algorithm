def is_arr(p, q):
    if 0 <= p < N and 0 <= q < M:
        return True
    return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    for k in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1

    visited = [[0] * M for _ in range(N)]
    # BFS
    queue = []
    num = 0 # number of bug

    for n in range(N):
        for m in range(M):
            if arr[n][m] == 1 and not visited[n][m]:
                num += 1
                queue.append([n, m, num])

                while queue:
                    i, j, c = queue.pop(0)

                    for l in range(4):
                        nx = i + dx[l]
                        ny = j + dy[l]

                        if is_arr(nx, ny) and arr[nx][ny] == 1:
                            if not visited[nx][ny]:
                                visited[nx][ny] = 1
                                queue.append([nx, ny, c])

    print(num)