from collections import deque

def is_arr(p, q):
    if 0 <= p < N and 0 <= q < M:
        return True
    else:
        return False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
queue = deque()
queue.append([0, 0, 1])

while queue:
    i, j, cnt = queue.popleft()
    # check[i][j] = 1 => 여기에 입력하면 메모리 초과????

    if i == N-1 and j == M-1:
        print(cnt)
        break
    else:
        for l in range(4):
            nx = i + dx[l]
            ny = j + dy[l]

            if is_arr(nx, ny) and arr[nx][ny]:
                if not check[nx][ny]:
                    check[nx][ny] = 1
                    queue.append([nx, ny, cnt+1])
