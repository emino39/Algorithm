import sys

read = sys.stdin.readline

N = int(read())
# 색칠하는 비용을 2차원 배열로 만듦
arr = [list(map(int, read().split())) for _ in range(N)]

for n in range(1, N):
    arr[n][0] += min(arr[n-1][1], arr[n-1][2])
    arr[n][1] += min(arr[n-1][0], arr[n-1][2])
    arr[n][2] += min(arr[n-1][0], arr[n-1][1])

print(min(arr[-1]))
