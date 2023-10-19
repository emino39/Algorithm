# 2 x n 타일링
N = int(input())

arr = [0] * (N + 3)

arr[1] = 1
arr[2] = 2
arr[3] = 3

for n in range(4, N+1):
    arr[n] = arr[n-1] + arr[n-2]

print(arr[N] % 10007)