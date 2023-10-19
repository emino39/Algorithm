"""
백트래킹: 가능한 모든 경우
종료조건 n: 사람 번호
dfs...
모두 팀 선택 후 정답 처리
"""

def cal(a_list, b_list):
    a_sum, b_sum = 0, 0

    for i in range(M):
        for j in range(M):
            a_sum += arr[a_list[i]][a_list[j]]
            b_sum += arr[b_list[i]][b_list[j]]

    return abs(a_sum - b_sum)

def dfs(n, a_list, b_list):
    global ans
    print('a_list', a_list)
    print('b_list', b_list)

    if n == N:
        if len(a_list) == len(b_list): # 반반 나눔
            ans = min(ans, cal(a_list, b_list))
        return

    dfs(n+1, a_list + [n], b_list) # A팀 선택
    dfs(n+1, a_list, b_list + [n]) # B팀 선택

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

M = N // 2

ans = 100 * M * M

dfs(0, [], [])
print(ans)