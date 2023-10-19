# 치킨집 M개 남기는 모든 경우
# 치킨집을 남길지 안 남길지는 이진트리의 형태
# 가능한 모든 경우를 처리해 정답을 찾는데, 치킨집을 남긴다 남기지 않는다 2가지 경우,,,, 2^13
def cal(tlst):
    # 모든 집과 tlst의 치킨집 거리 중 최솟값의 누적값 구하기
    sm = 0
    for hi, hj in houses: # 집 좌표 하나씩 처리
        mn = 2 * N # 가장 먼 치킨거리
        for ci, cj in tlst:
            mn = min(mn, abs(hi-ci) + abs(hj-cj))
        sm += mn

    return sm
def dfs(n, tlst):
    global ans
    if n == CNT: # 종료 조건: 모든 치킨집의 폐업 여부 결정 시
        if len(tlst) == M: # M개 유지 결정 시 최솟값 갱신
            ans = min(ans, cal(tlst))
        return

    # 유지하는 경우
    dfs(n+1, tlst + [chickens[n]])
    # 폐업하는 경우
    dfs(n+1, tlst)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 집, 치킨집 좌표를 house, chicken에 저장
houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

CNT = len(chickens) # 전체 치킨집 수

ans = 2* N * 2 * N

# dfs(n, tlst)
dfs(0, [])
print(ans)