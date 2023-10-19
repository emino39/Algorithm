N = int(input())
arr = list(map(int, input().split()))
arr.sort()

total = 0

for i in range(N):
    total += (arr[i] * (N-i))

print(total)