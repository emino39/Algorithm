# 활성상태, 비활성상태를 옆에 알파벳으로 같이 해야하나
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    exists = {} # 세포 위치와 값 확인
    queue = []

    # 우선 exists에 세포 넣기
    for n in range(N):
        for m in range(M):
            if arr[n][m]:
                queue.append([n, m, arr[n][m], arr[n][m], 0])
                exists[(n, m)] = 1

    queue = sorted(queue, key=lambda x: x[2], reverse=True)
    print(queue)

    time = 0
    while True:
        time += 1
        if time == K+1:
            break

        for i in range(len(queue)):
            x, y, life, lefttime, t = queue[i]

            if lefttime == 0:
