N = int(input())
per = list(map(int, input().split()))
per = sorted(per, reverse=False)
times = 0

for n in range(N):
    times += per[n] * (N - n)

print(times)