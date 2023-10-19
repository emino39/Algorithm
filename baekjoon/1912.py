import sys
read = sys.stdin.readline

N = int(read())
arr = list(map(int, read().split()))

for n in range(1, N):
    arr[n] = max(arr[n], arr[n-1] + arr[n])

print(max(arr))

