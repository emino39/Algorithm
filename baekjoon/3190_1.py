# 정답 https://www.youtube.com/watch?v=6lD3GPJp69U

N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
dlst = [input().split() for _ in range(L)]

dtbl = [0] * (10001) # command 읽기 위한 것
for sec, turn in dlst:
    dtbl[int(sec)] = turn

# 시계방향으로 방향 정의
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dr = 2 # direction 초기값 오른쪽 값
snake = [(1, 1)]
ans = 0

while True:
    ans += 1 # 1초 경과
    # 처음에 머리가 늘어남
    x, y = snake[0] # 현재 머리 좌표
    nx = x + dx[dr]
    ny = y + dy[dr] # 진행 방향으로 한 칸 이동

    # 벽에 부딪히거나 뱀 몸에 부딪힌 경우 종료
    if 1 <= nx <= N and 1 <= ny <= N and (nx, ny) not in snake:
        snake.insert(0, (nx, ny)) # 머리 위치에 이동 좌표 넣기

        # 사과 먹은 경우
        if (nx, ny) in apples:
            apples.remove((nx, ny))
        else:
            # 사과 먹은 경우가 아니면 꼬리 제거
            snake.remove(snake[-1])

        # 방향 전환
        if dtbl[ans] == 'D':
            dr = (dr + 1) % 4
        elif dtbl[ans] == 'L':
            dr = (dr + 3) % 4

    else:
        break

print(ans)