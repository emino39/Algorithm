# 동 1, 서 2, 북 3, 남 4
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 전개도 별 숫자
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
# top, east, front
direction = [1, 3, 5] 

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 첫 주사위 위치는 x, y이니까 (x, y)에 주사위 두고 지도 숫자 또는 주사위 숫자 복사하기
if arr[x][y] == 0:
    arr[x][y] = dice[1]
else:
    dice[1] = arr[x][y]
    arr[x][y] = 0

for k in range(K):
    top, east, front = direction
    # 1 동쪽 굴리기
    # top -> east, east -> bottom, front 그대로
    if commands[k] == 1:
        nx = x + dx[0]
        ny = y + dy[0]

        if 0 <= nx < N and 0 <= ny < M:
            direction = [(7 - east), top, front]
            if arr[nx][ny] == 0:
                arr[nx][ny] = dice[east]
            else:
                dice[east] = arr[nx][ny]
                arr[nx][ny] = 0
            # 현재 좌표 갱신
            x, y = nx, ny
            # 상단 숫자 출력
            print(dice[(7-east)])
    # 2 서쪽 굴리기
    # east -> top, (7 - top) -> east, front 그대로
    if commands[k] == 2:
        nx = x + dx[1]
        ny = y + dy[1]

        if 0 <= nx < N and 0 <= ny < M:
            direction = [east, (7 - top), front]
            if arr[nx][ny] == 0:
                arr[nx][ny] = dice[(7-east)]
            else:
                dice[(7-east)] = arr[nx][ny]
                arr[nx][ny] = 0
            # 현재 좌표 갱신
            x, y = nx, ny
            # 상단 숫자 출력
            print(dice[east])
    # 3 북쪽 굴리기
    # front -> top, east 그대로, (7 - top) -> front
    if commands[k] == 3:
        nx = x + dx[2]
        ny = y + dy[2]

        if 0 <= nx < N and 0 <= ny < M:
            direction = [front, east, (7 - top)]
            if arr[nx][ny] == 0:
                arr[nx][ny] = dice[(7-front)]
            else:
                dice[(7-front)] = arr[nx][ny]
                arr[nx][ny] = 0
            # 현재 좌표 갱신
            x, y = nx, ny
            # 상단 숫자 출력
            print(dice[front])
    # 4 남쪽 굴리기
    # top -> front, east 그대로, (7 - front) -> top
    if commands[k] == 4:
        nx = x + dx[3]
        ny = y + dy[3]

        if 0 <= nx < N and 0 <= ny < M:
            direction = [(7-front), east, top]
            if arr[nx][ny] == 0:
                arr[nx][ny] = dice[front]
            else:
                dice[front] = arr[nx][ny]
                arr[nx][ny] = 0
            # 현재 좌표 갱신
            x, y = nx, ny
            # 상단 숫자 출력
            print(dice[(7-front)])