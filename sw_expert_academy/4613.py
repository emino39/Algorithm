import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    mx = 0 # max

    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for s in range(i+1): 
                cnt += arr[s].count('W')
            for s in range(i+1, j+1):
                cnt += arr[s].count('B')
            for s in range(j+1, N):
                cnt += arr[s].count('R')
            mx = max(mx, cnt)

    print(f'#{t+1} {N*M - mx}')