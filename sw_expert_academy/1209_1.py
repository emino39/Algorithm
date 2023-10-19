def my_max(a):
    max_x = 0
    for x in a:
        if x >= max_x:
            max_x = x
    return max_x


for n in range(10):
    row_sums = []
    col_sums = []
    d_sums = []

    a, b, c = 0, 0, 0
    tc = int(input())

    arr = [[x for x in list(map(int, input().split()))] for y in range(100)]

    for i in range(100):
        row_sum = 0
        for j in range(len(arr[i])):
            row_sum += arr[i][j]
        row_sums.append(row_sum)

    for j in range(len(arr[0])):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        col_sums.append(col_sum)

    d_sum1 = 0
    d_sum2 = 0
    for i in range(100):
        d_sum1 += arr[i][i]
        d_sum2 += arr[i][99 - i]
    d_sums.append(d_sum1)
    d_sums.append(d_sum2)

    a = my_max(row_sums)
    b = my_max(col_sums)
    c = my_max(d_sums)
    sum_max = my_max([a, b, c])
    print(f'#{tc} {sum_max}')