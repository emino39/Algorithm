# 회전은 시계방향이니까 맨 끝 배열값을 맨 앞으로 가져옴
# 로봇 위치도 함께 회전.. 로봇은 (현재위치 + 1) % 2N?
from collections import deque
def rotate(lst, rob):
    num = lst.pop()
    lst.appendleft(num)

    new_rob = deque()

    while rob:
        r = rob.popleft()
        r += 1

        if r != (N - 1):
            new_rob.append(r)

    return lst, new_rob

def move(lst, rob):
    new_rob = deque()

    while rob:
        r = rob.popleft()
        if (r + 1) != (N - 1):
            if (r + 1) not in rob and (r + 1) not in new_rob:
                if lst[r + 1] > 0:
                    lst[r + 1] -= 1
                    new_rob.append(r + 1)
            else:
                new_rob.append(r)
        # else:
        #     lst[N-1] -= 1

    return lst, new_rob


N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr = deque(arr)
robots = deque() # 로봇 위치 저장
cnt = 0

if arr.count(0) == K:
    print(1)
else:
    while True:
        # 단계 올리기
        cnt += 1

        # 1. 컨베이어벨트, 로봇 회전
        arr, robots = rotate(arr, robots)

        # 2. 로봇 이동
        arr, robots = move(arr, robots)

        # 3. 올리는 위치에 로봇 올리기
        if arr[0] > 0:
            arr[0] -= 1
            robots.append(0)

        # 4. 내구도 확인
        if arr.count(0) >= K:
            break

    print(cnt)