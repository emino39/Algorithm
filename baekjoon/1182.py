# 가능한 모든 경우

# 이 문제에서 종료조건은?
def backtracking(n, sm, cnt):
    global ans

    if n == N:
        if sm == S and cnt != 0:
            ans += 1
        return

    backtracking(n+1, sm+arr[n], cnt+1)  # 포함
    backtracking(n+1, sm, cnt) # 미포함

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
backtracking(0, 0, 0) # n: index, sm: sum, cnt: 더한 숫자 개수
print(ans)