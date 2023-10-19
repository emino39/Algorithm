from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 각 공 위치 찾기
for n in range(N):
    for m in range(M):
        if arr[n][m] == 'R':
            red = [n, m]
            arr[n][m] = '.'
        elif arr[n][m] == 'B':
            blue = [n, m]
            arr[n][m] = '.'
            
cnt = 0 # 움직이는 횟수
flag = 0
queue = [[red[0], red[1], blue[0], blue[1], 0]]


while queue:
    if flag:
        break

    rx, ry, bx, by, c = queue.pop(0)

    # 이동 횟수가 10보다 클 때
    if c > 10:
        flag = -1
        break

    for i in range(4):
        go = 0

        nrx = rx
        nry = ry
        nbx = bx
        nby = by

        while True:
            if (nrx + dx[i]) == nbx and (nry + dy[i]) == nby:
                if arr[nbx+dx[i]][nby+dy[i]] == '.':
                    go = 1
                    nrx += dx[i]
                    nry += dy[i]
                    nbx += dx[i]
                    nby += dy[i]
                else:
                    break

            else:
                if arr[nrx+dx[i]][nry+dy[i]] == '.': # 레드가 갈 수 있는 상황
                    if arr[nbx+dx[i]][nby+dy[i]] == 'O': # 블루가 구멍에 들어간다면
                        go = 0
                        break
                    elif arr[nbx+dx[i]][nby+dy[i]] == '#': # 블루는 안 움직이고 레드만 움직임
                        go = 1
                        nrx += dx[i]
                        nry += dy[i]
                    elif arr[nbx+dx[i]][nby+dy[i]] == '.': # 블루 레드 모두 움직일 수 있는 상황
                        go = 1
                        nrx += dx[i]
                        nry += dy[i]
                        nbx += dx[i]
                        nby += dy[i]
                elif arr[nrx+dx[i]][nry+dy[i]] == 'O':
                    flag = 1
                    cnt = c+1
                    break
                elif arr[nrx+dx[i]][nry+dy[i]] == '#':
                    break

        if go:
            queue.append([nrx, nry, nbx, nby, c + 1])

        if flag:
            break

if flag > 0:
    print(cnt)
else:
    print(-1)