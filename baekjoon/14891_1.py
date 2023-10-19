# 톱니바퀴가 4개가 아닌 N개라면???
# 회전시킬 때마다 arr 붙였다 떼었다 할 수 없잖아?
# 12시 방향 하나를 잡고 해보자
"""
top 방향 arr 하나 만든다
회전시킬 후보를 표시 (idx, 오른쪽 쭉 왼쪽 쭉, 회전)
=> (번호, 회전 방향

1. idx 회전후보 추가 tlst = [(idx, 0)]
2. 오른쪽 방향 톱니 처리(극성이 같으면 break)
    for i in (idx+1, N):
        # 왼쪽 +2위치 != 오른쪽 +6위치(%8 처리 필요)
        if arr[i-1][(top[i-1]+2)%8] != arr[i][(top[i]+6)%8]
        tlst.append((i, (i-idx) % 2))
3. 왼쪽 방향 톱니 처리
"""

N = 4
arr = [[0] * 8] + [list(map(int, input())) for _ in range(N)]
K = int(input())
top = [0] * (N+1)

for _ in range(K):
    idx, dr = map(int, input().split())

    # 1. idx 톱니를 회전
    tlst = [(idx, 0)]
    # 2. idx 우측 방향 처리
    for i in range(idx+1, N+1):
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 => 회전 후보 추가
        if arr[i-1][(top[i-1]+2)%8] != arr[i][(top[i]+6)%8]:
            tlst.append((i, (i-idx)%2))
        else:
            break # 같은 극성이면 더 전달되지 않음

    # 3. idx 좌측 방향 처리
    for i in range(idx-1, 0, -1):
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 => 회전 후보 추가
        if arr[i][(top[i]+2)%8] != arr[i+1][(top[i+1]+6)%8]:
            tlst.append((i, (idx-i)%2))
        else:
            break

    # 4. 실제 회전 처리(cw이면 top값을 -1
    for i, rot in tlst:
        if rot == 0: # dr과 같은 방향
            top[i] = (top[i] - dr + 8) % 8
        else:
            top[i] = (top[i] + dr + 8) % 8

# 점수 계산
ans = 0
for i in range(1, N+1):
    ans += (arr[i][top[i]] * (2 ** (i-1)))

print(ans)