dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    max_cnt = 0
    queue = []

    for i in range(N):
        for j in range(N):
            queue.append([i, j, arr[i][j], arr[i][j], 1])

            while queue:
                x, y, first, cur, cnt = queue.pop()

                # 최댓값 체크
                if max_cnt < cnt:
                    max_cnt = cnt
                    max_num = first
                elif max_cnt == cnt:
                    if max_num > first:
                        max_num = first

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == cur + 1:
                            queue.append([nx, ny, first, arr[nx][ny], cnt + 1])

    print(f'#{t+1} {max_num} {max_cnt}')

