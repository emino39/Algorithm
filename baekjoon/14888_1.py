# backtracking

def dfs(n, sm, add, sub, mul, div):
    global mn, mx
    # 결과값, 중간값 범위
    if sm < int(-1e9) or sm > int(1e9):
        return

    # 종료 조건
    if n == N:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return

    # 하부 호출 (단, 연산자 개수 남았을 경우만 호출 가능)
    if add > 0:
        dfs(n+1, sm+lst[n], add-1, sub, mul, div)
    if sub > 0:
        dfs(n+1, sm-lst[n], add, sub-1, mul, div)
    if mul > 0:
        dfs(n+1, sm*lst[n], add, sub, mul-1, div)
    if div > 0:
        dfs(n+1, int(sm/lst[n]), add, sub, mul, div-1)

N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mn, mx = int(1e9), int(-1e9)

dfs(1, lst[0], add, sub, mul, div)
print(mx, mn, sep='\n')