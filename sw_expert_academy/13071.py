TC = int(input())

for tc in range(TC):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = sorted(arr, key=lambda x: (x[1], x[0]))

    # dp = [0] * N
    # dp[0] = 1
    end_time = 0
    ans = 0

    for i in range(N):
        if arr[i][0] >= end_time:
            end_time = arr[i][1]
            ans += 1

    # for i in range(1, N):
    #     dp[i] = 1
    #     for j in range(i):
    #         # 앞선 화물차의 끝나는 시간이 현재 화물차의 시작 시간 이하이면
    #         if arr[j][1] <= arr[i][0]:
    #             dp[i] = max(dp[i], dp[j]+1)

    print(f'#{tc+1} {ans}')