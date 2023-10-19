def change_stone(stone):
    if stone == 2:
        return 1
    else:
        return 2

def is_arr(p, q):
    if 1 <= p <= N and 1 <= q <= N:
        return True
    return False

def count_stones(arr):
    black, white = 0, 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    return black, white

# 8방향
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    stones = [[0] * (N+1) for _ in range(N+1)]
    a = N // 2
    stones[a][a], stones[a+1][a+1] = 2, 2
    stones[a][a+1], stones[a+1][a] = 1, 1

    for m in range(M):
        x, y, stone = map(int, input().split())
        stones[x][y] = stone

        queue = [[] for _ in range(8)]

        for i in range(8):
            nx = x
            ny = y

            while True:
                if not is_arr(nx+dx[i], ny+dy[i]):
                    queue[i] = []
                    break
                else:
                    if stones[nx+dx[i]][ny+dy[i]] == 0:
                        queue[i] = []
                        break
                    else:
                        if stones[nx+dx[i]][ny+dy[i]] == stone:
                            break
                        else:
                            queue[i].append([nx+dx[i], ny+dy[i], stones[nx+dx[i]][ny+dy[i]]])
                            nx += dx[i]
                            ny += dy[i]

        for q in queue:
            for qq in q:
                u, v, s = qq
                stones[u][v] = change_stone(s)

    black, white = count_stones(stones)
    print(f'#{t+1} {black} {white}')