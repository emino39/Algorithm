def backtracking(cnt, score, cal):
    global max_score

    if cnt == N:
        if cal <= L:
            max_score = max(max_score, score)
        return

    # 선택하는 경우
    backtracking(cnt+1, score+foods[cnt][0], cal+foods[cnt][1])
    # 선택하지 않는 경우
    backtracking(cnt+1, score, cal)

TC = int(input())

for tc in range(TC):
    N, L = map(int, input().split())
    foods = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0

    backtracking(0, 0, 0) # index, score, cal

    print(f'#{tc+1} {max_score}')