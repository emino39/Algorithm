def backtracking(cnt, arr):
    global visited, ans
    # 종료 조건(cnt에 관련된 것), 정답 처리
    if cnt == M: # M개의 수열을 완성
        ans.append(arr)
        return

    # 하부 단계(함수) 호출
    for j in range(1, N+1):
        if not visited[j]:
            visited[j] = 1
            backtracking(cnt+1, arr + [j])
            visited[j] = 0

N, M = map(int, input().split())
ans = [] # 정답을 저장할 리스트
visited = [0] * (N+1) # 중복 확인을 위한 visited

backtracking(0, [])

for a in ans:
    print(*a)