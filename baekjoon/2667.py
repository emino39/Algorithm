def is_arr(s, t):
    if 0 <= s < N and 0 <= t < N:
        return True
    return False

def DFS(u, v):
    global visited, num, arr

    for k in range(4):
        nx = u + dx[k]
        ny = v + dy[k]
        # print(nx, ny)
        if is_arr(nx, ny) and arr[nx][ny] == 1:
            # if not visited[nx][ny]:
            arr[nx][ny] = 0
            # visited[nx][ny] = 1
            num += 1
            DFS(nx, ny)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# visited = [[0] * N for _ in range(N)]

cnt = 0 # 단지의 수
num = 0
apt = []

for i in range(N):
    for j in range(N):
        if is_arr(i, j) and arr[i][j] == 1:
            # if not visited[i][j]:
            arr[i][j] = 0
            cnt += 1
            num = 1
            # visited[i][j] = 1
            DFS(i, j)
            apt.append(num)

print(cnt)
for a in apt:
    print(a)
