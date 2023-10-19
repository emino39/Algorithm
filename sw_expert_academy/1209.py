for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    tmp_sum = 0
    # 각 행의 합
    for i in range(100):
        tmp_sum = sum(arr[i])
        if max_sum < tmp_sum:
            max_sum = tmp_sum

    # 각 열의 합
    for i in range(100):
        tmp_sum = 0
        for j in range(100):
            tmp_sum += arr[j][i]
        if max_sum < tmp_sum:
            max_sum = tmp_sum

    # 좌상우하 대각선 합
    tmp_sum = 0
    for i in range(100):
        tmp_sum += arr[i][i]
    if max_sum < tmp_sum:
        max_sum = tmp_sum

    # 우상좌하 대각선 합
    tmp_sum = 0
    for i in range(100):
        tmp_sum += arr[i][99 - i]
    if max_sum < tmp_sum:
        max_sum = tmp_sum

    print(f'#{t} {max_sum}')