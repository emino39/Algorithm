from collections import deque

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]
clouds = deque(clouds)
for m in range(M):
    visited = [[0] * N for _ in range(N)]
    d, s = map(int, input().split())
    s = s % N

    # 구름 이동 및 물 양 증가
    while clouds:
        x, y = clouds.popleft()

        nx = (x + (dx[d-1] * s) + N) % N
        ny = (y + (dy[d-1] * s) + N) % N
        visited[nx][ny] = 1

        arr[nx][ny] += 1

    # 물 복사
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                cnt = 0
                for u, v in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                    nu = i + u
                    nv = j + v

                    if 0 <= nu < N and 0 <= nv < N and arr[nu][nv] > 0:
                        cnt += 1

                arr[i][j] += cnt

    # 구름 생성
    before = len(clouds)
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2:
                if not visited[i][j]:
                    clouds.append((i, j))
                    arr[i][j] -= 2


total = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            total += arr[i][j]

print(total)