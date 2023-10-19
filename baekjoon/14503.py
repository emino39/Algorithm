# 0 북 1 동 2 남 3 서 / 반시계방향 회전
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # x, y, direction
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0 # 청소한 칸의 수
flag = 0

while True:
    if flag: # 갈 수 없을 때
        break

    # 현재 칸이 청소되지 않았을 때
    if arr[r][c] == 0:
        cnt += 1
        arr[r][c] = -1 # 청소 된 상태 -1

    # 청소 가능한지 4 방향으로 탐색
    able = 0
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]

        if arr[nr][nc] == 0:
            able = 1
            break

    # 청소할 수 없을 때
    if not able:
        tmp_d = (d + 2) % 4
        if arr[r+dx[tmp_d]][c+dy[tmp_d]] != 1: # 벽 아니고 갈 수 있을 때
            r = r + dx[tmp_d]
            c = c + dy[tmp_d]
        else:
            # 벽이라면 작동 멈춤
            flag = 1
    else: # 청소 할 수 있을 때
        d = (d + 3) % 4 # 반시계 방향으로 회전
        if arr[r+dx[d]][c+dy[d]] == 0:
            r = r + dx[d]
            c = c + dy[d]

print(cnt)