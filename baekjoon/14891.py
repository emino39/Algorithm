def rotate(arr, d):
    if d == 1: # 시계 방향
        arr = [arr[-1]] + arr[:7]
    else:
        arr = arr[1:] + [arr[0]]
    return arr

# N극은 0, S극은 1
wheels = [list(input()) for _ in range(4)]
total = 0
K = int(input())
for k in range(K):
    # 회전시킬 톱니 번호, 회전방향(1 시계 -1 반시계)
    num, direction = map(int, input().split())
    check = [0, 0, 0] # 1-2, 2-3, 3-4
    # 회전하기 전에 체크하기
    if wheels[0][2] != wheels[1][6]:
        check[0] = 1
    if wheels[1][2] != wheels[2][6]:
        check[1] = 1
    if wheels[2][2] != wheels[3][6]:
        check[2] = 1

    if num == 1:
        wheels[0] = rotate(wheels[0], direction)
        if check[0] == 1:
            wheels[1] = rotate(wheels[1], direction * (-1))
            if check[1] == 1:
                wheels[2] = rotate(wheels[2], direction)
                if check[2] == 1:
                    wheels[3] = rotate(wheels[3], direction * (-1))
    elif num == 2:
        wheels[1] = rotate(wheels[1], direction)
        if check[0] == 1:
            wheels[0] = rotate(wheels[0], direction * (-1))
        if check[1] == 1:
            wheels[2] = rotate(wheels[2], direction * (-1))
            if check[2] == 1:
                wheels[3] = rotate(wheels[3], direction)
    elif num == 3:
        wheels[2] = rotate(wheels[2], direction)
        if check[1] == 1:
            wheels[1] = rotate(wheels[1], direction * (-1))
            if check[0] == 1:
                wheels[0] = rotate(wheels[0], direction)
        if check[2] == 1:
            wheels[3] = rotate(wheels[3], direction * (-1))
    else:
        wheels[3] = rotate(wheels[3], direction)
        if check[2] == 1:
            wheels[2] = rotate(wheels[2], direction * (-1))
            if check[1] == 1:
                wheels[1] = rotate(wheels[1], direction)
                if check[0] == 1:
                    wheels[0] = rotate(wheels[0], direction * (-1))

total = int(wheels[0][0]) + int(wheels[1][0]) * 2 + int(wheels[2][0]) * 4 + int(wheels[3][0]) * 8

print(total)