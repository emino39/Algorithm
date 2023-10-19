from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(si, sj):
    global visited
    queue = deque()
    queue.append([si, sj]) # 큐에 초기 데이터 삽입
    visited[si][sj] = 1 # 방문 표시
    alst = [[si, sj]] # 연합에 추가(정답 리스트)
    sm = arr[si][sj] # 연합 인구 합계

    while queue:
        ci, cj = queue.popleft()

        for n in range(4):
            ni = ci + dx[n]
            nj = cj + dy[n]

            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj]:
                    if L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                        queue.append([ni, nj])
                        alst.append([ni, nj])
                        sm += arr[ni][nj]
                        visited[ni][nj] = 1

    if len(alst) > 1: # 연합인 경우 평균값으로 인구 변경
        for ti, tj in alst:
            arr[ti][tj] = sm // len(alst)
        return 1 # 연합이 있었던
    return 0


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
day = 0

while True:
    visited = [[0] * N for _ in range(N)]
    flag = 0
    # 전체를 순회하면서 미방문 => 연합 처리
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: # 미방문
                flag = max(flag, bfs(i, j))

    if not flag: # 이동이 없었음
        break

    day += 1 # 연합이 있어서 인구 이동

print(day)