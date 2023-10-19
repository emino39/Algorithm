dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
arr = [[0] * N for _ in range(N)] # 빈 교실
students = dict()

for n in range(N*N):
    stu = list(map(int, input().split()))
    students[stu[0]] = stu[1:]

visited = [[0] * N for _ in range(N)]

for student, likes in students.items():
    max_like = 0
    positions = []
    # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: # (i, j)가 빈 칸(앉을 수 있는 칸)
                tmp_like = 0
                tmp_empty = 0

                for l in range(4):
                    ni = i + dx[l]
                    nj = j + dy[l]

                    if 0 <= ni < N and 0 <= nj < N:
                        if visited[ni][nj] != 0:
                            if arr[ni][nj] in likes:
                                tmp_like += 1
                        elif visited[ni][nj] == 0:
                            tmp_empty += 1


                if max_like < tmp_like:
                    max_like = tmp_like
                    positions = [(i, j, tmp_empty)]
                elif max_like == tmp_like:
                    positions.append((i, j, tmp_empty))

    positions = sorted(positions, key=lambda x: (-x[2], x[0], x[1]))
    x, y, _ = positions[0]

    arr[x][y] = student
    visited[x][y] = 1

    # print(arr)

score = 0
for i in range(N):
    for j in range(N):
        tmp_score = 0
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in students[arr[i][j]]:
                    tmp_score += 1

        if tmp_score > 0:
            score += 10 ** (tmp_score - 1)

print(score)