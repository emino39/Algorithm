# 다리를 지을 수 있는 경우의 수
# 다리의 개수는 강 서쪽에 있는 다리의 수(N)
# 이게 어떻게 다이나믹프로그래밍???
# M개 중에서 순서 없이 N개를 뽑는 코드인데
from math import factorial

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    total = factorial(M) / (factorial(N) * factorial(M-N))
    print(int(total))
    # print(combinations(M, N))
