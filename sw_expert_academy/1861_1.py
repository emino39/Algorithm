dx = [-1, 0, 1, 0] # 상하
dy = [0, -1, 0, 1] # 좌우

def isarr(p, q):
    if 0 <= p < N and 0 <= q < N: return True
    else: return False

TC = int(input())

for tc in range(TC):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    min_num = []

    for i in range(N):
        for j in range(N):
            queue = []
            queue.append([i, j, 0])

            while queue:
                x, y, c = queue.pop(0)
                time = c

                c += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if isarr(nx, ny) and arr[nx][ny] - arr[x][y] == 1:
                        queue.append([nx, ny, c])

            if max_cnt <= c:
                max_cnt = c
                min_num.append([arr[i][j], c])

    num = N * N + 1
    for ii in range(len(min_num)-1, -1, -1):
        if min_num[ii][1] != max_cnt:
            break
        if min_num[ii][1] == max_cnt:
            if min_num[ii][0] < num:
                num = min_num[ii][0]

    print("#{} {} {}".format(tc+1, num, max_cnt))