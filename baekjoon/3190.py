from collections import deque
# 좌, 상, 우, 하 (0, 1, 2, 3)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N = int(input())
arr = [[-1] * (N+1) for _ in range(N+1)]

apples = int(input())
for a in range(apples):
    u, v = map(int, input().split())
    arr[u][v] = 'a'

snake = deque()
snake.append([1, 1]) # [start_x, start_y, 꼬리 체크]
arr[1][1] = 2 # 오른쪽 방향
head = [1, 1]

M = int(input())
second = 0
flag = 0

commands = [list(map(str, input().split())) for _ in range(M)]

for command in commands:
    s, c = command
    s = int(s)

    while True:
        if second > s:
            if second >= int(commands[-1][0]):
                pass
            else:
                break

        x, y = snake[0][0], snake[0][1]
        direction = arr[x][y]

        if second == s: # 헤드의 방향 바꾸기
            if c == 'L':
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4

            arr[x][y] = direction

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= N and 1 <= ny <= N:
            # 사과 먹었을 때
            if arr[nx][ny] == 'a':
                arr[nx][ny] = direction # 사과는 지우고 새로운 뱀의 머리
                snake.appendleft([nx, ny])
                head[0], head[1] = nx, ny

            elif arr[nx][ny] in [0, 1, 2, 3]:
                # 몸에 닿아 죽는 경우
                flag = 1
                break
            else: # head가 몸통 안 만나고 그냥 진행할 때
                arr[nx][ny] = direction
                snake_len = len(snake)
                for l in range(snake_len):
                    i, j = snake[l]
                    d = arr[i][j]

                    snake[l][0] += dx[d]
                    snake[l][1] += dy[d]
                    if l == snake_len - 1:
                        arr[i][j] = -1

        else:
            # 영역 밖으로 나갔을 때
            flag = 1
            break

        second += 1

    if flag:
        break

print(second+1)