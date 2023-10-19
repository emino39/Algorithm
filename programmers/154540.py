from collections import deque

def solution(maps):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    W = len(maps[0])
    H = len(maps)
    visited = [[0] * W for _ in range(H)]

    queue = deque()
    
    for h in range(H):
        for w in range(W):
            total = 0
            if maps[h][w] != 'X' and not visited[h][w]:
                total += int(maps[h][w])
                queue.append([h, w])
                visited[h][w] = 1
    
            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < H and 0 <= ny < W:
                        if maps[nx][ny] != 'X' and not visited[nx][ny]:
                            total += int(maps[nx][ny])
                            queue.append([nx, ny])
                            visited[nx][ny] = 1

            if total != 0:
                answer.append(total)
                total = 0

    if answer == []:
        return [-1]
    else:
        answer = sorted(answer, reverse=False)
    
    return answer

if __name__ == "__main__":
    maps = ["X591X","X1X5X","X231X", "1XXX1"]
    # maps = ["XXX", "XXX", "XXX"]
    answer = solution(maps)
    print(answer)