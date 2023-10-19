from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))
robots = [0] * N
# arr = deque(arr)
# robots = deque(robots) # 로봇 위치 저장

cnt = 0

while True:
    cnt += 1
    # rotate
    # arr = [arr[-1]] + arr[:-1]
    arr.insert(0, arr.pop())

    # robots = [0] + robots[:-1] # 어차피 맨 오른쪽은 없어지니까 맨 앞에 [0] 더함
    robots.pop()
    robots.insert(0, 0)
    robots[N-1] = 0


    # move
    for i in range(N-2, 0, -1):
        if robots[i] == 1 and robots[i+1] == 0 and arr[i+1] > 0:
            robots[i+1] = 1
            robots[i] = 0
            arr[i+1] -= 1

    # 올리기
    if arr[0] > 0:
        arr[0] -= 1
        robots[0] = 1

    # 0인 개수가 K개 이상이면 탈출
    if arr.count(0) >= K:
        break

print(cnt)